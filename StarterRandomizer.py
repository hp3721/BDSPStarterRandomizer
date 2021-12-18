from Enums.GameRevision import GameRevision
from Enums.GameType import GameType
from GameOffsets.GameOffsets import GameOffsets
from Patch import Patch
import random

gameOffsets = GameOffsets(GameType.BD, GameRevision.REV_112)
patch = Patch(shift=0x100)

patch.addPatch(gameOffsets.starterGrassOffset, f'mov w0, #{hex(random.randint(1, 493))}')
patch.addPatch(gameOffsets.starterFireOffset, f'mov w8, #{hex(random.randint(1, 493))}')
patch.addPatch(gameOffsets.starterWaterOffset, f'mov w9, #{hex(random.randint(1, 493))}')

patch.addPatch(gameOffsets.rivalGrassOffset, f'mov w0, #{hex(random.randint(1, 493))}')
patch.addPatch(gameOffsets.rivalFireOffset, f'mov w8, #{hex(random.randint(1, 493))}')
patch.addPatch(gameOffsets.rivalWaterOffset, f'mov w8, #{hex(random.randint(1, 493))}')

with open(f'{gameOffsets.buildID}.ips', 'wb') as ipsFile:
    ipsFile.write(patch.generateIPS32Patch())