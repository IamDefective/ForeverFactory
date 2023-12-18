# Menu Class
# Options can link to other menus or display text
# Eventually will need to be able to do things through menus
# Example: option to quit
# When quit is selected, program is ended
#


class Menu:

    # List of all menus
    menus = []

    def __init__(self, display_name, options=None, info=None):

        # Name shown when referring to the menu in the terminal
        self.display_name = display_name

        # Create a dictionary to store all menu options
        self.options = {}
        
        # Create a dictionary to store all information
        self.info = {}

        # Selectable options displayed when menu is selected
        # Options can be menus or tuples of (display_name, message to be displayed when option is selected)
        if options is None:
            pass

        elif type(options) == list:

            # Verify every option is a valid type (Menu object or string)
            for option in options:

                # Pass if option is a Menu object
                if type(option) == Menu:
                    pass

                # Verify a valid tuple of strings was passed
                elif type(option) == tuple:

                    if len(option) == 2 and type(option[0]) == str and type(option[1]) == str:
                        pass

                    else:
                        raise TypeError(f'Message options must be a tuple of 2 strings, gave {option}')

                # Switch "passes" boolean to false if an option is not a valid type
                else:
                    raise TypeError(
                        f'Menu options must be of type Menu or string tuple, not {type(option)}'
                    )

            # "if passes" Adds provided options to the options dictionary
            # Uses menu display names for the keys of menu options
            # Uses the first of the two strings for the keys of message options (string tuples)

            # Dictionary keys (display names) are lowercase to simplify the process of
            # searching through dictionaries (case insensitive)
            # But display names should be capitalized when displayed, because it looks better

            for option in options:

                # Value is a menu object
                if type(option) == Menu:
                    self.options[option.display_name.lower()] = option

                # Value is a tuple of two strings
                elif type(option) == tuple and len(option) == 2 and type(option[0]) == str and type(option[1]) == str:
                    self.options[option[0].lower()] = option

        else:
            raise TypeError(f'Options must be in the form of a list or None, not {type(options)}')
        
        # Information to be displayed in the menu
        if info is None:
            pass

        else:

            # Set to false if an invalid item is found in "info"

            for item in info:

                if type(item) == tuple and len(item) == 2 and type(item[0]) == str:
                    pass

                else:
                    raise TypeError(f'Info items must be a tuple with a string for its label and one other item, not {item}')

            for item in info:
                self.info[item[0].lower()] = item

        # Add self to list of all menus
        Menu.menus.append(self)

    # Method to add an option to the menu
    def add_options(self, options):

        if type(options) == list:

            # Verify every option is a valid type (Menu object or string)
            for option in options:

                # Pass if option is a Menu object
                if type(option) == Menu:
                    pass

                # Verify a valid tuple of strings was passed
                elif type(option) == tuple:

                    if len(option) == 2 and type(option[0]) == str and type(
                            option[1]) == str:
                        pass

                    else:
                        raise TypeError(
                            f'Message options must be a tuple of 2 strings, gave {option}'
                        )

                # Switch "passes" boolean to false if an option is not a valid type
                else:
                    raise TypeError(
                        f'Menu options must be of type Menu or string tuple, not {type(option)}'
                    )

            # Adds provided options to the options dictionary
            # Uses menu display names for the keys of menu options
            # Uses the first of the two strings for the keys of message options (string tuples)

            # Dictionary keys (display names) are lowercase to simplify the process of
            # searching through dictionaries (case insensitive)
            # But display names should be capitalized when displayed, because it looks better

            for option in options:

                # Value is a menu object
                if type(option) == Menu:
                    self.options[option.display_name.lower()] = option

                # Value is a tuple of two strings
                elif type(option) == tuple:
                    self.options[option[0].lower()] = option

        else:
            raise TypeError(
                f'Options must be in the form of a list or None, not {type(options)}'
            )


# "Master" class, holds the run function (static method)
# Holds all system variables like menu history and command definitions
class System:

    # Number of characters wide the display is
    # Not neccesarily the same as the terminal width
    # Mostly just determines width of bars used to seperate menus
    # Default is 120 characters
    display_width = 120

    # Dictionary linking commands to their functions
    commands = {}

    # Current menu
    current_menu = None

    # Boolean that determines whether or not the system is running
    isRunning = False

    # List of previous menus
    # Used to support back button feature
    history = []

    # Method to change the display width
    @staticmethod
    def set_display_width(width):
        System.display_width = width

    # Method to change the current menu
    @staticmethod
    def set_current_menu(menu):

        if type(menu) == Menu:
            System.current_menu = menu

        else:
            raise TypeError(f'Menu must be of type Menu, not {type(menu)}')

    # Method to set the initial menu (main menu)
    @staticmethod
    def set_initial_menu(initial_menu):
        System.set_current_menu(initial_menu)
        System.history.append(initial_menu)

    # Method used to display the current menu
    @staticmethod
    def display():

        print()
        print('-' * System.display_width)
        print('=' * System.display_width)
        print(f'{System.current_menu.display_name}:')

        if len(System.current_menu.info) != 0:

            print()

            for item in System.current_menu.info.values():
                print(f'~ {item[0]}: {item[1]}')

        if len(System.current_menu.options) != 0:

            print()

            for option in System.current_menu.options.values():

                if type(option) == Menu:
                    print(f'> {option.display_name}')

                elif type(option) == tuple:
                    print(f'> {option[0]}')

        print('\n' + '=' * System.display_width)
        print('-' * System.display_width)

    # Method to check if passed command is valid
    @staticmethod
    def check_command(passed):

        passed = passed.lower().split()

        if len(passed) == 0:
            passed.append('')

        # Executes commands
        if passed[0] in System.commands:
            System.commands[passed[0]](passed)

        else:
            print('\nThat is not a supported command')

    # Command to select an option
    @staticmethod
    def select_option(selection):

        if len(selection) > 1:

            selection = selection[1]

            if selection in System.current_menu.options and type(System.current_menu.options[selection]) == Menu:
                System.set_current_menu(System.current_menu.options[selection])
                System.history.append(System.current_menu)

            elif selection in System.current_menu.options and type(
                    System.current_menu.options[selection]) == tuple:
                pass  #NEED TO FIGURE OUT HOW MESSAGES SHOULD BE DISPLAYED

            elif selection not in System.current_menu.options:
                print('\nThat is not something you can select')

        else:
            print('\nYou must give an option to select')

    # Add select command to dictionary of commands
    # "sel" can be used as an alias of "select"
    commands['select'] = select_option.__func__
    commands['sel'] = select_option.__func__

    # Command to go back to the previous menu
    @staticmethod
    def go_back(noargs):

        if len(System.history) > 1:
            System.set_current_menu(System.history[-2])
            System.history.pop()

        else:
            print('\nYou cannot go back any further')

    # Add back command to dictionary of commands
    commands['back'] = go_back.__func__

    # Method to run the system
    @staticmethod
    def run():

        # The system pauses when this is set to false
        System.isRunning = True

        # Whole loop, when this closes, the program shuts down
        while True:

            # Inner loop, this pauses when isRunning is set to false
            while System.isRunning:

                # Display the current menu
                System.display()

                # Take a command
                System.check_command(input('\nEnter a Command:\n- '))


############################################################################################################
############################################################################################################
############################################################################################################

class Monster:

    def __init__(self, name, health, attack):

        self.name = name
        self.health = health
        self.attack = attack



settings_menu = Menu('Settings')
example_menu = Menu('Example')
other_menu = Menu('Other')
stat_page = Menu('Stats')

main_menu_options = [
    stat_page, settings_menu, example_menu, other_menu,
    ('Info', 'This is information')
]

main_menu = Menu('Main Menu')
main_menu.add_options(main_menu_options)

goblin = Monster('Goblin', 20, 5)

goblin_menu = Menu('Goblin', info=[('Health', goblin.health), ('Attack', goblin.attack)], options=[settings_menu])

main_menu.add_options([goblin_menu])

System.set_display_width(67)
System.set_initial_menu(main_menu)
System.run()
