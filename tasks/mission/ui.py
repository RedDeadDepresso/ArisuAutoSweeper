from module.base.timer import Timer
from module.logger import logger
from module.ocr.ocr import Digit
from module.ui.switch import Switch
from tasks.base.assets.assets_base_page import BACK, MISSION_CHECK, EVENT_CHECK, WORK_GO_TO_EVENT
from tasks.base.page import page_mission, page_commissions, page_work  # ,page_event
from tasks.base.ui import UI
from tasks.mission.assets.assets_mission import *
from tasks.stage.mission_list import StageList
from tasks.stage.sweep import StageSweep

SHARED_LIST = StageList('SharedList')
EVENT_LIST = StageList('EventList', EVENT_LIST, EVENT_INDEX, EVENT_ITEM, button_stars=EVENT_STARS)
SHARED_SWEEP = StageSweep('MissionSweep', 99)
SHARED_SWEEP.set_button(button_check=CHECK_MISSION_SWEEP)  # Check sweep is different for mission, event
COMMISSIONS_SWEEP = StageSweep('CommissionsSweep', 99)

SWITCH_NORMAL = Switch("Normal_switch")
SWITCH_NORMAL.add_state("on", NORMAL_ON)
SWITCH_NORMAL.add_state("off", NORMAL_OFF)

SWITCH_HARD = Switch("HARD_switch")
SWITCH_HARD.add_state("on", HARD_ON)
SWITCH_HARD.add_state("off", HARD_OFF)

SWITCH_STORY = Switch("QUEST_switch")
SWITCH_STORY.add_state("on", STORY_ON)
SWITCH_STORY.add_state("off", STORY_OFF)

SWITCH_QUEST = Switch("QUEST_switch")
SWITCH_QUEST.add_state("on", QUEST_ON)
SWITCH_QUEST.add_state("off", QUEST_OFF)

"""
A dictionary that maps the mode to a tuple where 
the first element is an argument to go_back and second is for ui_ensure
Missing for "E" because there are no event in Global and no page_event
"""
MODE_TO_PAGE = {
    "N": (MISSION_CHECK, page_mission),
    "H": (MISSION_CHECK, page_mission),
    "XP": (CHECK_XP, page_commissions),
    "CR": (CHECK_CR, page_commissions),
    "E": (EVENT_CHECK, None)  # page_event
}

MODE_TO_SWITCH = {
    "N": SWITCH_NORMAL,
    "H": SWITCH_HARD,
    "E": SWITCH_QUEST,
    "ES": SWITCH_STORY
}

class MissionUI(UI):
    def select_mission(self, mode, stage):
        area = int(stage.split("-")[0])
        if self.select_area(area) and self.select_mode(mode):
            return True
        return False

    def select_area(self, num):
        """"
        May require further error handling for these cases. 
        1. Fails to ocr area number
        2. May trigger too many click exception when clicking left or right too many times
        3. Area not unlocked. Simplest way if left or right button are still present 
        but problem is it is expensive to check every time and they always keep moving.
        """
        tries = 0
        ocr_area = Digit(OCR_AREA)
        while 1:
            try:
                self.device.screenshot()
                current_area = int(ocr_area.ocr_single_line(self.device.image))
                if current_area == num:
                    return True
                elif current_area > num:
                    [self.click_with_interval(LEFT, interval=1) for x in range(abs(current_area - num))]
                elif current_area < num:
                    [self.click_with_interval(RIGHT, interval=1) for x in range(abs(current_area - num))]
            except:
                tries += 1
                if tries > 3:
                    logger.warning(f"Area {num} not found")
                    return False

    def select_mode(self, mode):
        """
        Set switch to on. 
        Returns:
            True if switch is set, False if switch not found
        """
        switch = MODE_TO_SWITCH[mode]
        if not switch.appear(main=self):
            logger.info(f'{switch.name} not found')
            return False
        switch.set('on', main=self)
        return True

    def enter_stage(self, mode, index: int) -> bool:
        list = EVENT_LIST if mode == "E" else SHARED_LIST
        if list.select_index_enter(self, index):
            return True
        return False

    def do_sweep(self, mode, num: int) -> bool:
        if mode in ["XP", "CR"]:
            return COMMISSIONS_SWEEP.do_sweep(self, num=num)
        else:
            return SHARED_SWEEP.do_sweep(self, num=num)

    def navigate(self, prev, next):
        """
        go_back is called when the previous stage and next stage are in
        the same game mode. 
        For example, "N" and "H" are in Mission so we call go_back.
        If different, ui_ensure is called for example, "N" and "IR".
        """
        if prev == next or (prev in ["N", "H"] and next in ["N", "H"]):
            self.go_back(MODE_TO_PAGE[next][0])
        elif prev in ["XP", "CR"] and next in ["XP", "CR"]:
            self.go_back(CHECK_COMMISSIONS)
        else:
            self.goto_event() if next == "E" else self.ui_ensure(MODE_TO_PAGE[next][1])

    def go_back(self, check):
        while 1:
            self.device.screenshot()
            if self.match_color(check) and self.appear(check):
                return True
            self.click_with_interval(BACK, interval=2)

    def goto_event(self):
        """
        Should be removed after implementing ui_ensure(page_event)
        """
        self.ui_ensure(page_work)
        timer = Timer(1).start()
        while 1:
            self.device.screenshot()
            if self.appear(EVENT_CHECK):
                break
            self.appear_then_click(WORK_GO_TO_EVENT)
            self.device.swipe((40, 160), (260, 40))
            while not timer.reached_and_reset():
                pass


class CommissionsUI(UI):
    """Works the same way as select_bounty"""

    def select_commission(self, mode):
        if mode == "CR":
            dest_enter, dest_check = SELECT_CR, CHECK_CR
        else:
            dest_enter, dest_check = SELECT_XP, CHECK_XP
        timer = Timer(5, 10).start()
        while 1:
            self.device.screenshot()
            self.appear_then_click(dest_enter, interval=1)
            if self.appear(dest_check):
                return True
            if timer.reached():
                return False
