from app.knight import Knight


def perform_battle(knight1: Knight,
                   knight2: Knight) -> dict:
    knight1_hp = (knight1.apply_hp_and_potion()
                  - (knight2.apply_weapon_and_potion()
                     - knight1.apply_armour_and_potion()))
    knight2_hp = (knight2.apply_hp_and_potion()
                  - (knight1.apply_weapon_and_potion()
                     - knight2.apply_armour_and_potion()))

    return {
        knight1.knight_config["name"]: 0 if knight1_hp < 0 else knight1_hp,
        knight2.knight_config["name"]: 0 if knight2_hp < 0 else knight2_hp,
    }
