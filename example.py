import menu_system as men


class Info:

    def __init__(self, label, data, menu):

        self.label = label
        self.data = data
        self.menu = menu

    def formatted(self):
        return (self.label, self.data)

    def change(self, phrase):

        if len(phrase) > 2 and phrase[2].isdigit():
            self.data -= int(phrase[2])
            self.menu.update_info('health', self.formatted())

        elif len(phrase) > 2 and not phrase[2].isdigit():
            print('\nThe amount you give must a number')

        else:
            self.data -= 1
            self.menu.update_info('health', self.formatted())


main_menu = men.Menu('Main Menu')
play_menu = men.Menu('Play', isIndexed=True)
main_info = 'This is an example use of a menu system engine.\nIt\'s not done.'
settings_menu = men.Menu('Settings')

infExample = Info('Health', 23, play_menu)

play_options = [
    ('Back', men.System.go_back),
    ('Info',
     'This is an example use of a menu system engine.\nIt\'s not done.'),
    ('Hurt', infExample.change)
]

main_menu.add_options([play_menu, ('Info', main_info), settings_menu])

play_menu.add_options(play_options)
play_menu.add_info([infExample.formatted()])

settings_options = [('Back', men.System.go_back)]
settings_menu.add_options(settings_options)

men.System.set_display_width(50)
men.System.set_current_menu(main_menu, record=True)
men.System.run()

# ADD INDEXED MENU OPTIONS
# Use if statement inside System.run instead of two loops, so a variable is false, the loop skips all logic, but the loop stays open
