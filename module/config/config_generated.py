import datetime

# This file was automatically generated by module/config/config_updater.py.
# Don't modify it manually.


class GeneratedConfig:
    """
    Auto generated configuration
    """

    # Group `Scheduler`
    Scheduler_Enable = False  # True, False
    Scheduler_NextRun = datetime.datetime(2020, 1, 1, 0, 0)
    Scheduler_Command = 'Alas'
    Scheduler_ServerUpdate = '04:00'

    # Group `Emulator`
    Emulator_Serial = 'auto'
    Emulator_PackageName = 'auto'  # auto, JP-Official, OVERSEA-TWHKMO, OVERSEA-Korea, OVERSEA-Asia, OVERSEA-America, OVERSEA-Global
    Emulator_GameLanguage = 'auto'  # auto, jp, en
    Emulator_ScreenshotMethod = 'auto'  # auto, ADB, ADB_nc, uiautomator2, aScreenCap, aScreenCap_nc, DroidCast, DroidCast_raw, scrcpy
    Emulator_ControlMethod = 'MaaTouch'  # minitouch, MaaTouch
    Emulator_AdbRestart = False

    # Group `EmulatorInfo`
    EmulatorInfo_Emulator = 'auto'  # auto, NoxPlayer, NoxPlayer64, BlueStacks4, BlueStacks5, BlueStacks4HyperV, BlueStacks5HyperV, LDPlayer3, LDPlayer4, LDPlayer9, MuMuPlayer, MuMuPlayerX, MuMuPlayer12, MEmuPlayer
    EmulatorInfo_name = None
    EmulatorInfo_path = None

    # Group `Error`
    Error_Restart = 'game'  # game, game_emulator
    Error_SaveError = True
    Error_ScreenshotLength = 1
    Error_OnePushConfig = 'provider: null'

    # Group `Optimization`
    Optimization_ScreenshotInterval = 0.3
    Optimization_CombatScreenshotInterval = 1.0
    Optimization_WhenTaskQueueEmpty = 'goto_main'  # stay_there, goto_main, close_game

    # Group `Cafe`
    Cafe_Reward = True
    Cafe_Touch = True
    Cafe_AutoAdjust = True
    Cafe_SecondCafe = True

    # Group `Bounty`
    Bounty_OnError = 'skip'  # stop, skip

    # Group `Highway`
    Highway_Stage = 1  # 1, 2, 3, 4, 5, 6, 7, 8, 9
    Highway_Count = 2

    # Group `DesertRailroad`
    DesertRailroad_Stage = 1  # 1, 2, 3, 4, 5, 6, 7, 8, 9
    DesertRailroad_Count = 2

    # Group `Schoolhouse`
    Schoolhouse_Stage = 1  # 1, 2, 3, 4, 5, 6, 7, 8, 9
    Schoolhouse_Count = 2

    # Group `Scrimmage`
    Scrimmage_OnError = 'skip'  # stop, skip

    # Group `Trinity`
    Trinity_Stage = 1  # 1, 2, 3, 4
    Trinity_Count = 2

    # Group `Gehenna`
    Gehenna_Stage = 1  # 1, 2, 3, 4
    Gehenna_Count = 2

    # Group `Millennium`
    Millennium_Stage = 1  # 1, 2, 3, 4
    Millennium_Count = 2

    # Group `TacticalChallenge`
    TacticalChallenge_PlayerSelect = 0  # 0, 1, 2, 3

    # Group `ItemStorage`
    ItemStorage_AP = {}
    ItemStorage_Credit = {}
    ItemStorage_Pyroxene = {}
    ItemStorage_BountyTicket = {}
    ItemStorage_ScrimmageTicket = {}
    ItemStorage_TacticalChallengeTicket = {}
