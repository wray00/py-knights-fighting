class Knight:
    def __init__(self, knight_config: dict) -> None:
        self.knight_config = knight_config

    def apply_hp_and_potion(self) -> int:
        return self.knight_config["hp"] + self.apply_potion("hp")

    def apply_armour_and_potion(self) -> int:
        protection = 0
        for armour in self.knight_config["armour"]:
            protection += armour["protection"]
        return protection + self.apply_potion("protection")

    def apply_weapon_and_potion(self) -> int:
        return (self.knight_config["power"]
                + self.knight_config["weapon"]["power"]
                + self.apply_potion("power"))

    def apply_potion(self, type_of_effect: str) -> int:
        if (self.knight_config["potion"] is not None
                and type_of_effect in self.knight_config["potion"]["effect"]):
            return self.knight_config["potion"]["effect"][type_of_effect]

        return 0
