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
    Emulator_GameLanguage = 'auto'  # auto, jp, en, zht
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
    Optimization_WhenTaskQueueEmpty = 'goto_main'  # stay_there, goto_main, close_game, exit_aas, exit_emulator, exit_aas_emulator, shutdown

    # Group `Cafe`
    Cafe_Reward = True
    Cafe_Touch = True
    Cafe_AutoAdjust = True
    Cafe_SecondCafe = True

    # Group `Invitation`
    Invitation_Enable = True
    Invitation_WaitingHour = 0  # 0, 3, 6, 9
    Invitation_Choice = 'list_top'  # list_top, by_name
    Invitation_Name = None
    Invitation_Substitute = False

    # Group `Schedule`
    Schedule_OnError = 'skip'  # stop, skip

    # Group `Choice1`
    Choice1_Location = 'None'  # None, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    Choice1_Classrooms = None

    # Group `Choice2`
    Choice2_Location = 'None'  # None, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    Choice2_Classrooms = None

    # Group `Choice3`
    Choice3_Location = 'None'  # None, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    Choice3_Classrooms = None

    # Group `Choice4`
    Choice4_Location = 'None'  # None, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    Choice4_Classrooms = None

    # Group `Choice5`
    Choice5_Location = 'None'  # None, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    Choice5_Classrooms = None

    # Group `Choice6`
    Choice6_Location = 'None'  # None, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    Choice6_Classrooms = None

    # Group `Choice7`
    Choice7_Location = 'None'  # None, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    Choice7_Classrooms = None

    # Group `Bounty`
    Bounty_OnError = 'skip'  # stop, skip

    # Group `Highway`
    Highway_Stage = 0  # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    Highway_Count = 2

    # Group `DesertRailroad`
    DesertRailroad_Stage = 0  # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    DesertRailroad_Count = 2

    # Group `Schoolhouse`
    Schoolhouse_Stage = 0  # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    Schoolhouse_Count = 2

    # Group `Scrimmage`
    Scrimmage_OnError = 'skip'  # stop, skip

    # Group `Trinity`
    Trinity_Stage = 0  # 0, 1, 2, 3, 4
    Trinity_Count = 2

    # Group `Gehenna`
    Gehenna_Stage = 0  # 0, 1, 2, 3, 4
    Gehenna_Count = 2

    # Group `Millennium`
    Millennium_Stage = 0  # 0, 1, 2, 3, 4
    Millennium_Count = 2

    # Group `TacticalChallenge`
    TacticalChallenge_PlayerSelect = 0  # 0, 1, 2, 3

    # Group `NormalShop`
    NormalShop_Enable = False
    NormalShop_Purchases = 1  # 1, 2, 3, 4
    NormalShop_1 = False
    NormalShop_2 = False
    NormalShop_3 = False
    NormalShop_4 = False
    NormalShop_5 = False
    NormalShop_6 = False
    NormalShop_7 = False
    NormalShop_8 = False
    NormalShop_9 = False
    NormalShop_10 = False
    NormalShop_11 = False
    NormalShop_12 = False
    NormalShop_13 = False
    NormalShop_14 = False
    NormalShop_15 = False
    NormalShop_16 = False
    NormalShop_17 = False
    NormalShop_18 = False
    NormalShop_19 = False
    NormalShop_20 = False

    # Group `TacticalChallengeShop`
    TacticalChallengeShop_Enable = False
    TacticalChallengeShop_Purchases = 1  # 1, 2, 3, 4
    TacticalChallengeShop_1 = False
    TacticalChallengeShop_2 = False
    TacticalChallengeShop_3 = False
    TacticalChallengeShop_4 = False
    TacticalChallengeShop_5 = False
    TacticalChallengeShop_6 = False
    TacticalChallengeShop_7 = False
    TacticalChallengeShop_8 = False
    TacticalChallengeShop_9 = False
    TacticalChallengeShop_10 = False
    TacticalChallengeShop_11 = False
    TacticalChallengeShop_12 = False
    TacticalChallengeShop_13 = False
    TacticalChallengeShop_14 = False
    TacticalChallengeShop_15 = False

    # Group `Formation`
    Formation_burst1 = 1  # 1, 2, 3, 4
    Formation_burst2 = 4  # 1, 2, 3, 4
    Formation_pierce1 = 2  # 1, 2, 3, 4
    Formation_pierce2 = 4  # 1, 2, 3, 4
    Formation_mystic1 = 3  # 1, 2, 3, 4
    Formation_mystic2 = 4  # 1, 2, 3, 4

    # Group `ManualBoss`
    ManualBoss_Enable = False

    # Group `Normal`
    Normal_Enable = False
    Normal_Area = 4
    Normal_Completion = 'clear'  # clear, three_stars

    # Group `Hard`
    Hard_Enable = False
    Hard_Area = 6
    Hard_Completion = 'clear'  # clear, three_stars, three_stars_chest

    # Group `ItemStorage`
    ItemStorage_AP = {}
    ItemStorage_Credit = {}
    ItemStorage_Pyroxene = {}
    ItemStorage_BountyTicket = {}
    ItemStorage_ScrimmageTicket = {}
    ItemStorage_TacticalChallengeTicket = {}
