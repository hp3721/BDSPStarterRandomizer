class SPGameOffsets100:
    def __init__(self):
        self.buildID = '1284AB14C1477243AE2A3550EF828709'
        
        # Starter Pokémon Offsets
        get_DefaultPokeNoAddress = 0x1BBBBE0

        self.starterGrassOffset = get_DefaultPokeNoAddress + 0xC8
        self.starterFireOffset = self.starterGrassOffset + 0x8C
        self.starterWaterOffset = self.starterFireOffset + 0x4
        
        # Rival Pokémon Offsets
        get_RivalPokeNoAddress = 0x1BBBF60
        
        self.rivalGrassOffset = get_RivalPokeNoAddress + 0xC8
        self.rivalFireOffset = self.rivalGrassOffset + 0x8C
        self.rivalWaterOffset = self.rivalFireOffset + 0x4
