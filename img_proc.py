import cv2
import codecs

CN_layout = ['elder_titan', 'undying', 'abaddon', 'shredder', 'omniknight', 'beastmaster', 'legion_commander',
             'skeleton_king', 'phoenix', 'centaur', 'rattletrap', 'huskar', 'life_stealer', 'earth_spirit',
             'abyssal_underlord', 'tiny', 'tusk', 'pudge', 'earthshaker', 'axe', 'slardar', 'sven', 'kunkka',
             'night_stalker', 'doom_bringer', 'treant', 'sand_king', 'chaos_knight', 'tidehunter', 'alchemist',
             'lycan', 'wisp', 'spirit_breaker', 'brewmaster', 'bristleback', 'magnataur', 'dragon_knight',
             'juggernaut', 'clinkz', 'viper', 'razor', 'venomancer', 'riki', 'drow_ranger', 'morphling',
             'nyx_assassin', 'bloodseeker', 'templar_assassin', 'vengefulspirit', 'arc_warden', 'naga_siren',
             'troll_warlord', 'phantom_assassin', 'phantom_lancer', 'spectre', 'nevermore', 'lone_druid', 'terrorblade',
             'antimage', 'slark', 'ember_spirit', 'ursa', 'sniper', 'gyrocopter', 'pangolier', 'mirana', 'meepo',
             'weaver', 'medusa', 'broodmother', 'faceless_void', 'bounty_hunter', 'luna', 'monkey_king', 'tinker',
             'furion', 'keeper_of_the_light', 'skywrath_mage', 'zuus', 'winter_wyvern', 'techies', 'witch_doctor',
             'lich', 'puck', 'pugna', 'disruptor', 'dazzle', 'leshrac', 'rubick', 'shadow_demon', 'shadow_shaman',
             'warlock', 'jakiro', 'death_prophet', 'obsidian_destroyer', 'crystal_maiden', 'silencer', 'queenofpain',
             'necrolyte', 'invoker', 'oracle', 'bane', 'visage', 'lina', 'lion', 'batrider', 'enigma',
             'ancient_apparition', 'dark_willow', 'chen', 'storm_spirit', 'windrunner', 'ogre_magi', 'enchantress',
             'dark_seer']


def crop_hero_template_img():
    # 221,189,46,72
    # 273,189,46,72
    # 221,269,46,72
    # 221,373,46,72
    x, y, w, h = 169, 189, 46, 72
    d_col, d_row, d_class = 52, 80, 184
    hero_num = [[21, 16], [21, 16], [21, 20]]
    img = cv2.imread('interface.png')
    for c, rows in enumerate(hero_num):
        for row, col in enumerate(rows):
            for _col in range(col):
                _x = x + _col * d_col
                _y = y + row * d_row + c * d_class
                crop_img = img[_y:_y + h, _x:_x + w]
                # crop_img = img[_y + h - 26:_y + h,
                #            int(_x + w / 2 - 13):int(_x + w / 2 + 13)]
                cv2.imshow("cropped", crop_img)
                cv2.waitKey(0)


def generate_hero_index_py(lang=None):
    lines = ['class HeroIndex(object):\n']
    x, y, w, h = 169, 189, 46, 72
    d_col, d_row, d_class = 52, 80, 184
    hero_num = [[21, 16], [21, 16], [21, 20]]
    counter = 0
    for c, rows in enumerate(hero_num):
        for row, col in enumerate(rows):
            for _col in range(col):
                _x = x + _col * d_col
                _y = y + row * d_row + c * d_class
                lines.append('    {} = {}\n'.format(CN_layout[counter], (_x, _y)))
                counter += 1

    with codecs.open('hero_index.py', 'w', encoding='utf-8') as f:
        f.writelines(lines)


def main():
    # crop_hero_template_img()
    generate_hero_index_py()


if __name__ == '__main__':
    main()
