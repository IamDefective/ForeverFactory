
class Menu:

    menus = {}

    def __init__(self, name):

        self.name = name
        self.options = {}

        Menu.menus[name] = self

    
    # Method for adding a menu option
    # Example: menu.add_option(settings_menu)
    # Example Display: 
    #       
    #       ====================================================================================
    #       
    #       SETTINGS: 
    #       > Controls
    #       > Graphics
    #       > Sound
    #     

    def add_option(self, *options):

        for option in options:
            if option.name in Menu.menus.keys() : self.options[option.name.lower()] = option


class Game:

    current_menu = None

    commands = {}


    # Method for changing the current_menu
    @staticmethod
    def set_menu(menu):

        if type(menu) == Menu : Game.current_menu = menu
        else : raise TypeError(f'{menu} is not a menu')


    # Method for getting the current_menu
    @staticmethod
    def get_menu() : return Game.current_menu
    

    # Method for Displaying the current_menu
    @staticmethod
    def display_menu():

        print(f'\n--------------------------------------------------------------------------------------------------------------\n==============================================================================================================\n{Game.current_menu.name}:\n')
        for option in Game.current_menu.options.keys() : print(f'> {Game.current_menu.options[option].name}')
        print('\n==============================================================================================================\n--------------------------------------------------------------------------------------------------------------')

    
    # Method for getting user input inside a command
    @staticmethod
    def get_input(message):

        print('\n' + message)

        return input('- ')

    

    # Command for selecting a menu option
    @staticmethod
    def select_option():

        response = Game.get_input('What do you want to select:').lower()

        if response in Game.current_menu.options.keys() and type(Game.current_menu.options[response]) == Menu:
            Game.set_menu(Game.current_menu.options[response])

    commands['select'] = select_option.__func__
    
    ########################################################################################################################
    # RUNS THE GAME
    ########################################################################################################################
    @staticmethod
    def run():
        
        while True:

            Game.display_menu()

            # Request command
            command = input('\nEnter Command:\n- ').lower()

            if command in Game.commands.keys():
                selected_command = Game.commands[command]
                selected_command()

            else : print('\nThat is not a valid command')
            



main_menu = Menu('Main Menu')
info_menu = Menu('Info')
settings_menu = Menu('Settings')
credits_menu = Menu('Credits')
more_menu = Menu('More')

main_menu.add_option(info_menu, settings_menu, credits_menu, more_menu)

Game.set_menu(main_menu)

Game.run()