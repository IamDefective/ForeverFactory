
class Menu:

    # List of all menus
    menus = []

    def __init__(self, display_name, options=None, info=None, isIndexed=False):

        '''
        The init function sets up the menu object and its
        attributes.

        Display name is the string that is shown in menus
        where this menu is an option. A type error is raised
        if anything other than a string is passed.

        Both the options and info parameters should be given
        as lists. If no lists are given, no options or info 
        are assigned upon initialization. A type error is
        raised if anything other than a list is passed.

        The isIndexed parameter indicates whether or not the
        options in the menu should be assigned indexes, which
        can be used in place of a name when selecting menu
        options. A type error is raised if anything other
        than a boolean is passed.

        Info and options are stored as dictionaries.
        Reference the add_info and add_options methods for an
        explanation of how options and info are checked for
        invalid items and how the dictionaries are created.

        The linked_in attribute is a list containing all
        menus in which this menu is displayed as an option.
        Menus are added when they add this menu to
        their options.

        Each menu is appended to the class-wide list of all
        menus.
        '''

        # Assign display name
        if isinstance(display_name, str):
            self.display_name = display_name

        else:
            raise TypeError(f'{display_name} is not a valid display name')

        # Create dictionary of option indexes
        if isinstance(isIndexed, bool):

            self.isIndexed = isIndexed
        
            if isIndexed:
                self.indexes = {}

        else:
            raise TypeError(f'{isIndexed} is not a boolean')

        # Create dictionary of options
        self.options = {}

        # Create dictionary of info
        self.info = {}

        # Create list of menus that display this menu in their options
        self.linked_in = []

        # Add any provided options to options dictionary
        if options is None:
            pass

        elif isinstance(options, list):

            # Add any invalid options to this list
            invalid_options = [option
                for option in options
                if not
                (isinstance(option, Menu)
                or (isinstance(option, tuple) and len(option) == 2 and isinstance(option[0], str)
                    and (isinstance(option[1], str) or callable(option[1]))
                    )
                )
                ]
            
            # If there are any invalid options in the list
            # A type error is raised
            if len(invalid_options) > 0:
                raise TypeError(f'{invalid_options[0]} is not a valid option')

            # Add each option to dictionary of options
            for option in options:

                # Value is a menu object
                if isinstance(option, Menu):
                    self.options[option.display_name.lower()] = option
                    option.linked_in.append(self)

                # Value is a tuple
                elif isinstance(option, tuple):
                    self.options[option[0].lower()] = option

        else:
            raise TypeError(
                f'Options must be in the form of a list or None, not {type(options)}'
            )

        # Information to be displayed in the menu
        if info is None:
            pass

        elif isinstance(info, list):

            # Add any invalid info items to this list
            invalid_info_items = [item
                for item in info
                if not
                (isinstance(item, tuple) and len(item) == 2 and isinstance(item[0], str))
                ]

            # Raise a type error if any info items are invalid
            if len(invalid_info_items) > 0:
                raise TypeError(
                    f'Info items must be a tuple with a string for its label and one other item, not {invalid_info_items[0]}'
                    )

            # Add info to self.info if no invalid items were found
            self.info.update({pair[0].lower():pair for pair in info})

        else:
            raise TypeError(f'Info must be in the form of a list or None, not {type(info)}')

        # Add self to list of all menus
        Menu.menus.append(self)

    # Method for adding options to the menu
    def add_options(self, options):

        '''
        This method takes a list of options to be appended to
        the menu's dictionary of options. It raises a type
        error if anything other than a list is passed.

        First it iterates through each option to verify they
        are all valid. 

        For each option in the list, the method checks if it
        is a Menu object or a valid tuple.

        Valid tuples all start with a string to be used as a
        display name inside menus. The second item in the
        tuple must be either a string, making it an info
        option, or a function, making it a command option.

        If these conditions are not met, the method raises a
        type error saying the given option is invalid.

        If these conditions are met, each option is added to
        the menu's options dictionary.

        Each option has its lowercase display name as its
        dictionary key. Menu options have the Menu object as
        their dictionary value, and tuple options have their
        entire tuple, (display_name, string/function), as
        their value.
        '''

        # Verify options argument is a list
        if isinstance(options, list):

            # Add any invalid options to this list
            invalid_options = [option
                for option in options
                if not
                (isinstance(option, Menu)
                or (isinstance(option, tuple) and len(option) == 2 and isinstance(option[0], str)
                    and (isinstance(option[1], str) or callable(option[1]))
                    )
                )
                ]
            
            # If there are any invalid options in the list
            # A type error is raised
            if len(invalid_options) > 0:
                raise TypeError(f'{invalid_options[0]} is not a valid option')

            # Add each option to dictionary of options
            for option in options:

                # Value is a menu object
                if isinstance(option, Menu):
                    self.options[option.display_name.lower()] = option
                    option.linked_in.append(self)

                # Value is a tuple
                elif isinstance(option, tuple):
                    self.options[option[0].lower()] = option

        else:
            raise TypeError(
                f'Options must be in the form of a list or None, not {type(options)}'
            )

    # Method for adding info to the menu
    def add_info(self, info):
        
        '''
        This method takes a list of info to be appended to
        the menu's dictionary of info. It raises a type
        error if anything other than a list is passed.

        First it iterates through each info item to verify 
        they are all valid. 

        The method verifies that each item in the list is a
        tuple with two items in it, with first being a
        string, the display name.

        If these conditions are not met, the method raises a
        type error saying the given info item is invalid.

        If these conditions are met, each info item is added
        to the menu's info dictionary.

        Each info item has its lowercase display name as its
        dictionary key, and the entire tuple as its
        dictionary value.
        '''

        if isinstance(info, list):
                
            # Add any invalid info items to this list
            invalid_info_items = [item
                for item in info
                if not
                (isinstance(item, tuple) and len(item) == 2 and isinstance(item[0], str))
                ]

            # Raise a type error if any info items are invalid
            if len(invalid_info_items) > 0:
                raise TypeError(
                        f'Info items must be a tuple with a string for its label and one other item, not {invalid_info_items[0]}'
                    )

            # Add info to self.info if no invalid items were found
            self.info.update({pair[0].lower():pair for pair in info})

        else:
            raise TypeError(f'Info must be in the form of a list, not {type(info)}')

    # Method for updating info
    def update_info(self, info_key, new_value):
        self.info[info_key.lower()] = new_value


class System:

    '''
    This class handles all system variables (menu history,
    command definitions, current menu) and runs the system.

    display_width is an integer that determines how many
    characters wide the menu-separation bars will be. If
    anything other than an integer is given, a type error
    will be raised

    The commands dictionary links all commands (which should
    be lowercase strings) to their functions.

    current_menu stores the menu the user is currently
    operating in. It is set to None by default.

    isRunning is used in the run method to determine whether
    the inner while loop is running. It is set to false by
    default, but is set to true once run is called.

    The history list is a list of menus that were previously
    displayed. When a new menu is selected, the old current
    menu is appended to history, and current_menu is set to
    the new menu. If the back option is selected, the current
    menu is popped from the end of the list, removing it from
    the menu history, and the previous menu becomes the
    current menu.
    '''

    display_width = 120

    commands = {}

    current_menu = None

    isRunning = False
    notClosed = False

    history = []

    @classmethod
    def set_display_width(cls, width):

        '''
        The set_display_width method is the proper way of
        modifying the display width. If anything other than an
        integer is passed into the method, it raises a type
        error. If display_width is modified directly and set to
        anything other than an integer, no error will be
        immediately raised, but once display_width is referenced
        (like in the display method), most likely an error will
        occur, but it may not be as specific or helpful as the
        error in set_display_width.
        '''

        if isinstance(width, int):
            cls.display_width = width

        else:
            raise TypeError(
                f'Display width must be an integer, not {width}'
            )

    @classmethod
    def set_current_menu(cls, menu, record=False):

        '''
        The set_current_menu method is the proper way of
        assigning a new menu. If anything other than a Menu
        object is passed, a type error is raised. Otherwise, the
        current_menu is set to the new menu. If the record
        parameter is set to true, the new menu is appended to the
        history list.
        '''

        if isinstance(menu, Menu):

            cls.current_menu = menu

            if record:
                cls.history.append(menu)

        else:
            raise TypeError(f'Menu must be of type Menu, not {type(menu)}')

    @classmethod
    def display(cls):

        '''
        The display method displays current_menu, taking no
        arguments. For items in the info dictionary, it displays
        each item's display name/label, which is the first thing
        in the item's tuple, next to a tilda. It then displays
        the second thing in the tuple, which can be anything, as
        long as it is compatible with the print function. The
        method then, next to a '>' symbol, displays each option,
        found in the options dictionary, using the display name
        for menu options, or the first thing in tuple options
        (functions and info options).
        '''

        print()
        print('-' * cls.display_width)
        print('=' * cls.display_width)
        print(f'{cls.current_menu.display_name}:')

        # Display menu info
        if len(cls.current_menu.info) != 0:

            print()

            for name, info in cls.current_menu.info.values():
                print(f'~ {name}: {info}')

        # Display menu options
        if len(cls.current_menu.options) != 0:

            print()

            for item in cls.current_menu.options.items():

                index = ''
                option = item[1]

                if cls.current_menu.isIndexed:
                    index = list(cls.current_menu.options.items()).index(item) + 1

                if isinstance(option, Menu):
                    print(f'{index}> {option.display_name}')

                elif isinstance(option, tuple):
                    print(f'{index}> {option[0]}')

        print('\n' + '=' * cls.display_width)
        print('-' * cls.display_width)

    @classmethod
    def display_info(cls, info):

        '''
        The display_info method is used to display info options
        when selected using the select command. It takes a tuple,
        called info, and unpacks it into display_name and
        contents. It uses display_name as the title of the info
        card, and then prints the contents where info and options
        would be found in menus.
        '''

        display_name, contents = info

        print()
        print('-' * cls.display_width)
        print('=' * cls.display_width)
        print(f'{display_name}:')
        print(f'\n{contents}')
        print('\n' + '=' * cls.display_width)
        print('-' * cls.display_width)

    @staticmethod
    def go_back(*noargs):

        '''
        The go_back method calls System.set_current_menu and
        passes the second to last item in System.history, which
        is the previous menu. The method then removes the
        exitted menu from System.history.

        go_back is not currently called by any existing
        functions, but can be linked in menus using
        System.go_back to create a back button in each menu.
        
        The method currently takes an unused argument, noargs,
        for compatibility with the select_option command, which
        currently always passes the users input to any function
        selected by the user.
        '''

        if len(System.history) > 1:
            System.set_current_menu(System.history[-2])
            System.history.pop()

        else:
            print('\nYou cannot go back any further')

    @classmethod
    def check_command(cls, passed):

        '''
        The check_command method takes input from the user, which
        is given by the run method after giving the prompt "Enter
        a Command:". The method reformats the input by calling
        the split method, creating a list of the individual words
        entered by the user. A variable called command is
        assigned the value of the first word in the list, which
        should be a command if the user knows what they are
        doing, and the command is made to be lowercase. The
        method makes sure to add an empty string to the passed
        list if the user hit enter without giving any text. The
        method then searches for the command in System.commands.
        If the command is found, the method calls the
        corresponding method and passes the user input as an
        argument. If the command is not found, the method tells
        the user it was not found.
        '''

        # Input is split into individual words
        # First word is tried as a command
        passed = passed.split()

        if len(passed) == 0:
            passed.append('')

        command = passed[0].lower()

        # Executes commands
        if command in cls.commands:
            cls.commands[command](passed)

        else:
            print('\nThat is not a supported command')

    @staticmethod
    def select_option(phrase):

        '''
        The select_option method is called when the user gives
        the select or index command (aliases s and i). It takes
        one argument, phrase, which is the user's command in the
        form of a list containing each individual word.

        The method verifies the user gave something to select,
        letting them know they made a mistake if no selection
        was given.

        The method then determines how the user wants to select
        an option, either by using the option's name or by using
        the option's index.

        If the user wants to normal select, the method assigns
        a variable called selection the value of the second word
        in the user's command, which should be the name of the
        option, in lowercase. The method then searches through
        the current menu's options dictionary for the selected
        option. If the selection is of type Menu, the method
        calls System.set_current_menu and passes the selected
        menu. If the selection is a tuple option, the method
        assigns a variable called target the value of the tuple.
        If the second item in the tuple is a string, it is an
        info option and is displayed using System.display_info.
        Otherwise, if the second item in the tuple is a
        function, the function is called with the phrase list as
        an argument. If the selection is not found in the
        current menu's options dictionary, the method tells the
        user it was not found.

        INDEX SELECTION EXPLANATION
        '''

        # Checks if the user gave an option to select
        if len(phrase) > 1:

            # Set selection to second word in phrase if command was normal select
            if phrase[0].lower() == 'select' or phrase[0].lower() == 's':
                selection = phrase[1].lower()

            # User gave index select and current_menu is indexed
            elif System.current_menu.isIndexed and (
                phrase[0].lower() == 'index' or phrase[0].lower() == 'i'):

                # Make sure user gave an index
                if phrase[1].isdigit():

                    selection = int(phrase[1])

                    # User gave out of range index
                    if selection > len(System.current_menu.options):
                        print('\nYou gave an out-of-range index')
                        return
                    
                    # User gave valid index
                    else:
                        # Set selection to option with given index
                        selection = list(System.current_menu.options.keys())[selection - 1]

                # User didn't give an index
                else:
                    print('\nYou must give a number you want to index')
                    return
            
            # User gave index select and current_menu is not indexed
            elif not System.current_menu.isIndexed and (
                phrase[0].lower() == 'index' or phrase[0].lower() == 'i'):
                print('\nThis menu is not indexed')
                return

            # Handle menu options
            if selection in System.current_menu.options and isinstance(
                    System.current_menu.options[selection],
                    Menu):
                System.set_current_menu(System.current_menu.options[selection], record=True)

            # Handle tuple options (information or functions)
            elif selection in System.current_menu.options and isinstance(
                    System.current_menu.options[selection],
                    tuple):

                # Target is the tuple
                target = System.current_menu.options[selection]

                # Handle info tuples
                if isinstance(target[1], str):
                    System.display_info(target)
                    input('Press enter when you are done:\n> ')

                # Handle function tuples
                elif callable(target[1]):
                    target[1](phrase)

            # Selection wasnt found
            elif selection not in System.current_menu.options:
                print('\nThat is not something you can select')

        else:
            print('\nYou must give an option to select')

    # Add select command to dictionary of commands
    # "s" can be used as an alias of "select"
    # "i" can be used as an alias of "index"
    commands['select'] = select_option.__func__
    commands['s'] = select_option.__func__
    commands['index'] = select_option.__func__
    commands['i'] = select_option.__func__

    # Method to run the system
    @classmethod
    def run(cls):

        '''
        The run method contains the main loop where things
        happen. There is an outer loop, which runs as long as
        System.notClosed is set to true, and an inner loop,
        which runs as long as System.isRunning is set to true.
        The inner loop displays menus and takes input.
        '''

        # The system pauses when this is set to false
        cls.isRunning = True

        # The system loop ends when this is set to false
        cls.notClosed = True

        # Whole loop, when this closes, the program shuts down
        while cls.notClosed:

            # Inner loop, this pauses when isRunning is set to false
            while cls.isRunning:



                # Display the current menu
                cls.display()

                # Take a command
                cls.check_command(input('\nEnter a Command:\n- '))

