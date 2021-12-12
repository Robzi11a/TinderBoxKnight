import pygame

KIND_OF_TILES = ["DarkTile", "LightTile", "KnightDarkBackground"]
KIND_OF_TILES += ["KnightLightBackground", "HiddenTorch", "HiddenSpider"]
KIND_OF_TILES += ["HiddenClueUp", "HiddenClueDiagonal", "VisibleUnlitTorch"]
KIND_OF_TILES += ["VisibleLitTorch", "KnightScanBackground", "ScanTile"]
KIND_OF_TILES += ["MovementUp", "MovementRight", "MovementDown"]
KIND_OF_TILES += ["MovementLeft", "MatchButton", "ScanButton"]
KIND_OF_TILES += ["QuitButton", "Controls"]
KIND_OF_TILES += ["QuitButton"]
KIND_OF_TILES += ["LitSpider"]
KIND_OF_TILES += ["LightClosedGate", "LightPressurePlate"]
KIND_OF_TILES += ["Lives1", "Lives2","Lives3"]

DARK_PURPLE = (3.5, 3.9, 7.8)

# Wall 

WALL = "Wall.png"

# Dark tile = ["d"]

DARK_TILE_EMPTY = "DarkTile.png"

# Light tile = ["l"]

LIGHT_TILE_EMPTY = "LightTile.png"

# Knight dark tile = ["kd"]

KNIGHT_DARK_BACKGROUND = "KnightDarkBackground.png"

# Knight Light tile = ["kl"]

KNIGHT_LIGHT_BACKGROUND = "KnightLightBackground.png"

# Lit Closed Gate ["lcg"]

LIT_CLOSED_GATE = "LightClosedGate.png"

# Lit Opened Gate ["log"]
LIT_OPENED_GATE = "LightTile.png"

# Broken Lamp ["bl"]

BROKEN_LAMP = "BrokenLamp.png"

# Lit Skeleton ["lss, lsr, lsa"]

LIT_SKELETON_SKULL = "SkullBones.png"

LIT_SKELETON_RIBS = "RibBones.png"

LIT_SKELETON_ARMS = "ArmBones.png"

LIT_WEB_SKELETON_RIBS = "VisibleWebRibBones.png"

LIT_WEB_SKELETON_ARMS = "VisibleWebArmBones.png"

LIT_S_TILE = "STILE.png"

LIT_F_TILE = "FTILE.png"

# Ranged Enemy ["lre, dre, drea"]

LIT_RANGED_ENEMY = "LightShadow.png"

DARK_RANGED_ENEMY = "DarkShadow.png"

DARK_RANGED_ENEMY_ANGRY = "DarkShadowAngry.png"

# Poison tiles 

POISON_TILE_EMPTY = "PoisonTile.png"

POISON_KNIGHT_BACKGROUND = "PoisonKnightBackground.png"

POISON_SHADOW = "PoisonShadow.png"

POISON_SKELETON_SKULL = "PoisonSkullBones.png"

POISON_SKELETON_RIBS = "PoisonRibBones.png"

POISON_SKELETON_ARMS = "PoisonArmBones.png"

# Lit Bookshelf ["lb"]

LIT_BOOKSHELF = "LitBookshelf.png"

# Lit Book [lj]

LIT_JOURNAL = "LightBook.png"

# Lit Pressure Plate [lpp]

LIT_PRESSURE_PLATE = "LightPressurePlate.png"

# Lit Clues [lcd, lcu, lcr, lsc]

LIT_CLUE_DIAGONAL = "ClueDiagonal.png"

LIT_CLUE_UP = "ClueUp.png"

LIT_CLUE_RIGHT = "ClueRight.png"

LIT_SPIDER_CLUE = "SpiderClue.png"

LIT_RIGHT_ROOM_CLUE = "VisibleRightRoomClue.png"

LIT_LEFT_ROOM_CLUE = "VisibleLeftRoomClue.png"

LIT_MATCH_CLUE = "SpiderClue.png"

# Hidden object dark tiles = ["ht, hs, hcu, hcd, hcr, hcs, hb, dpp,dog,hcg"]

HIDDEN_TORCH = "DarkTile.png"

HIDDEN_SPIDER = "DarkTile.png"

HIDDEN_CLUE_UP = "DarkTile.png"

HIDDEN_CLUE_DIAGONAL = "DarkTile.png"

HIDDEN_CLUE_RIGHT = "DarkTile.png"

HIDDEN_CLUE_SPIDER = "DarkTile.png"

HIDDEN_BOOKSHELF = "DarkTile.png"

HIDDEN_PRESSUREPLATE = "DarkTile.png"

HIDDEN_CLOSED_GATE = "DarkTile.png"

HIDDEN_OPENED_GATE = "DarkTile.png"

HIDDEN_WALL = "DarkTile.png"

HIDDEN_RIGHT_ROOM_CLUE = "DarkTile.png"

HIDDEN_LEFT_ROOM_CLUE = "DarkTile.png"

# Torch tiles in the light = ["vut, vlt"]

VISIBLE_UNLIT_TORCH = "UnlitLightTorch.png"

VISIBLE_LIT_TORCH = "LitLightTorch.png"

# Scan tiles = ["sk, st"]

SCAN_KNIGHT = "KnightScanBackground.png"

SCAN_TILE = "ScanTile.png"

# Button tiles = ["mu, mr, md, ml, mb, sb"]
 
MOVEMENT_UP = "MovementUp.png"

MOVEMENT_RIGHT = "MovementRight.png"

MOVEMENT_DOWN = "MovementDown.png"

MOVEMENT_LEFT = "MovementLeft.png"

MATCH_BUTTON = "MatchButton.png"

SCAN_BUTTON = "ScanButton.png"

# Info Tiles = ["qc"] 

QUIT_CONTROL = "QuitButton.png"

CONTROLS = "Controls.png"

# Lit spider monster tiles = ["ls"]

LIT_SPIDER = "LitSpider.png"


#Lives number showed =["ml1, ml2, ml3"]
LIVES_1 = "Lives1.png"
LIVES_2 = "Lives2.png"
LIVES_3 = "Lives3.png"

# Game states
MAIN_MENU = 1

LEVEL = 2

END_SCREEN = 3

QUIT = 4

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WINDOW_WIDTH = screen.get_rect().width
WINDOW_HEIGHT = screen.get_rect().height
# WINDOW_WIDTH = 700
# WINDOW_HEIGHT = 600

