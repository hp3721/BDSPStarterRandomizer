from Enums.GameRevision import GameRevision
from Enums.GameType import GameType
from GameOffsets.BD.BDGameOffsets100 import BDGameOffsets100
from GameOffsets.BD.BDGameOffsets110 import BDGameOffsets110
from GameOffsets.BD.BDGameOffsets111 import BDGameOffsets111
from GameOffsets.BD.BDGameOffsets112 import BDGameOffsets112
from GameOffsets.BD.BDGameOffsets113 import BDGameOffsets113
from GameOffsets.SP.SPGameOffsets100 import SPGameOffsets100
from GameOffsets.SP.SPGameOffsets110 import SPGameOffsets110
from GameOffsets.SP.SPGameOffsets111 import SPGameOffsets111
from GameOffsets.SP.SPGameOffsets112 import SPGameOffsets112
from GameOffsets.SP.SPGameOffsets113 import SPGameOffsets113


class GameOffsets:
    def __init__(self, gameType: GameType, gameRevision: GameRevision):
        match gameType:
            case GameType.BD:
                match gameRevision:
                    case GameRevision.REV_100:
                        offsets = BDGameOffsets100()
                    case GameRevision.REV_110:
                        offsets = BDGameOffsets110()
                    case GameRevision.REV_111:
                        offsets = BDGameOffsets111()
                    case GameRevision.REV_112:
                        offsets = BDGameOffsets112()
                    case GameRevision.REV_113:
                        offsets = BDGameOffsets113()
            case GameType.SP:
                match gameRevision:
                    case GameRevision.REV_100:
                        offsets = SPGameOffsets100()
                    case GameRevision.REV_110:
                        offsets = SPGameOffsets110()
                    case GameRevision.REV_111:
                        offsets = SPGameOffsets111()
                    case GameRevision.REV_112:
                        offsets = SPGameOffsets112()
                    case GameRevision.REV_113:
                        offsets = SPGameOffsets113()
        
        self.buildID = offsets.buildID

        self.starterGrassOffset = offsets.starterGrassOffset
        self.starterFireOffset = offsets.starterFireOffset
        self.starterWaterOffset = offsets.starterWaterOffset
        
        self.rivalGrassOffset = offsets.rivalGrassOffset
        self.rivalFireOffset = offsets.rivalFireOffset
        self.rivalWaterOffset = offsets.rivalWaterOffset
