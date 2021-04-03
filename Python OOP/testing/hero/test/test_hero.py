import unittest
from hero.project.hero import Hero


class HeroTests(unittest.TestCase):
    username = 'Assia'
    level = 2
    health = 20
    damage = 20

    def test_hero_init__expect_to_create_it(self):
        self.assertEqual('Assia', self.username)
        self.assertEqual(2, self.level)
        self.assertEqual(20, self.health)
        self.assertEqual(20, self.damage)

    def test_hero_battle__when_enemy_username_is_equal_to_hero_username__expect_exception(self):
        hero = Hero(self.username, self.level, self.health, self.damage)
        enemy_hero = Hero(self.username, self.level, self.health, self.damage)
        with self.assertRaises(Exception) as context:
            hero.battle(enemy_hero)

        self.assertEqual("You cannot fight yourself", str(context.exception))

    def test_hero_battle__when_hero_health_is_0__expect_exception(self):
        hero = Hero(self.username, self.level, 0, self.damage)
        enemy_hero = Hero('Raya', self.level, self.health, self.damage)
        with self.assertRaises(Exception) as context:
            hero.battle(enemy_hero)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(context.exception))

    def test_hero_battle__when_hero_health_is_negative__expect_exception(self):
        hero = Hero(self.username, self.level, -5, self.damage)
        enemy_hero = Hero('Raya', self.level, self.health, self.damage)
        with self.assertRaises(Exception) as context:
            hero.battle(enemy_hero)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(context.exception))

    def test_hero_battle__when_enemy_health_is_0__expect_exception(self):
        hero = Hero(self.username, self.level, self.health, self.damage)
        enemy_hero = Hero('Raya', self.level, 0, self.damage)
        with self.assertRaises(Exception) as context:
            hero.battle(enemy_hero)

        self.assertEqual(f"You cannot fight {enemy_hero.username}. He needs to rest", str(context.exception))

    def test_hero_battle__when_enemy_health_is_negative__expect_exception(self):
        hero = Hero(self.username, self.level, self.health, self.damage)
        enemy_hero = Hero('Raya', self.level, -2, self.damage)
        with self.assertRaises(Exception) as context:
            hero.battle(enemy_hero)

        self.assertEqual(f"You cannot fight {enemy_hero.username}. He needs to rest", str(context.exception))

    def test_hero_battle__when_both_health_is_positive_when_both_health_is_negative_after_battle_expect_to_return_draw(self):
        hero = Hero(self.username, self.level, self.health, self.damage)
        enemy_hero = Hero('Raya', 3, 6, 30)
        result = hero.battle(enemy_hero)

        self.assertEqual("Draw", result)

    def test_hero_battle__when_both_health_is_positive_when_enemy_health_is_negative_after_battle_expect_to_increase_hero_health_level_damage(self):
        hero = Hero(self.username, self.level, self.health, self.damage)
        enemy_hero = Hero('Raya', 1, 6, 10)
        result = hero.battle(enemy_hero)

        self.assertEqual("You win", result)
        self.assertEqual(3, hero.level)
        self.assertEqual(15, hero.health)
        self.assertEqual(25, hero.damage)

    def test_hero_battle__when_both_health_is_positive_when_hero_health_is_negative_after_battle_expect_to_increase_enemy_health_level_damage(self):
        hero = Hero(self.username, self.level, self.health, self.damage)
        enemy_hero = Hero('Raya', 3, 50, 10)
        result = hero.battle(enemy_hero)

        self.assertEqual("You lose", result)
        self.assertEqual(4, enemy_hero.level)
        self.assertEqual(15, enemy_hero.health)
        self.assertEqual(15, enemy_hero.damage)

    def test_hero_str__expect_to_return_it(self):
        hero = Hero(self.username, self.level, self.health, self.damage)
        result = f"Hero {self.username}: {self.level} lvl\n" \
               f"Health: {self.health}\n" \
               f"Damage: {self.damage}\n"

        self.assertEqual(result, str(hero))


if __name__ == '__main__':
    unittest.main()