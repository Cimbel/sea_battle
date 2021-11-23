import one_deck
import two_deck
import three_deck
import four_deck
import exceptions_and_errors as err
import sys
from war import War
import random
import time
from colors import Colors
import colorama
from guide import guide

NAVIGATOR = "[Navigator]: "
LETTERS_SEA_FIELD = "abcdefghij"
DUPLICATION_ERR_MSG = f"\n{Colors.RED}[Error]: Duplication positions{Colors.END}\n" \
                      f"[Hint]: See 'guide' or set not duplication positions"
NOT_EXISTS_POS_ERR_MSG = f"\n{Colors.RED}[Error]: Not existing position{Colors.END}\n[Hint]: Choose another position"
P_BUSY_MSG = f"\n{Colors.RED}[Error]: One of the position you've tried to set up is busy!{Colors.END}" \
             f"\n[Hint]: Choose position with '@' char\n"
ALREADY_SHOT_MSG = f"\n{Colors.RED}[Error]: The pos you trying attack has already shot!{Colors.END}" \
                   f"\n[Hint]: Try another one with \"@\" char"
play_field_p = one_deck.OneDeck()
play_field_p.fill_pos()
play_field_p.fill_field()
play_field2_p, play_field3_p, play_field4_p = None, None, None
max1_p, max2_p, max3_p, max4_p = 0, 0, 0, 0
exit_set_up_ships_loop = None
from_choosing_type = None
exit_choose_type_loop_bool = False
is_printed_intro_bool = False
exit_main_loop = False
exit_battle_mode = False


def set_colors(field):
    """
    Set colorful chars on play field

    :param field: list type (matrix 11x11), play field
    :return: list type, changed play field
    """
    for num in range(11):
        for char in range(11):
            if field[num][char] == "@":
                field[num][char] = f"{Colors.GREEN}@{Colors.END}"
            elif field[num][char] == "#" or field[num][char] == "-" or field[num][char] == "X":
                field[num][char] = f"{Colors.RED}{field[num][char]}{Colors.END}"
            elif field[num][char] not in ["@", " ", "", "#", "-"]:
                field[num][char] = f"{Colors.BOLD}{field[num][char]}{Colors.END}"

    return field


def delete_colors(field):
    """
    Delete colorful chars on play field

    :param field: list type (matrix 11x11), play field
    :return: list type, changed play field
    """
    for num in range(11):
        for char in range(11):
            if field[num][char] == f"{Colors.GREEN}@{Colors.END}":
                field[num][char] = f"@"
            elif field[num][char] == f"{Colors.RED}#{Colors.END}":
                field[num][char] = "#"
            elif field[num][char] == f"{Colors.RED}-{Colors.END}":
                field[num][char] = "-"
            elif field[num][char] == f"{Colors.RED}X{Colors.END}":
                field[num][char] = "X"

    return field


def do_color_field(obj_field):
    """
    Paint color, print play field, delete color

    :param obj_field: object type
    :return: None
    """
    set_colors(obj_field.play_field)
    obj_field.print_field()
    delete_colors(obj_field.play_field)


def create_shoot_field():
    """
    Create instance of OneDeck class

    :return: object type
    """
    shooting_field = one_deck.OneDeck()
    shooting_field.fill_field()
    shooting_field.fill_pos()

    return shooting_field


def clear_minus(field):
    """
    Delete '-' chars

    :param field: object type,
    :return: object type, changed object
    """
    for row in range(11):
        for column in range(11):
            if field[row][column] == "-":
                field[row][column] = "@"

    return field


def battle(computer_obj, player_obj):
    """
    The game's battle logic

    :param computer_obj: object type
    :param player_obj: object type
    :return: None
    """
    shooting_field_player = create_shoot_field()
    shooting_field_computer = create_shoot_field()
    clear_minus(player_obj.play_field)
    clear_minus(computer_obj.play_field)

    battle_object = War(computer_obj, player_obj, shooting_field_computer, shooting_field_player)
    who_is_shooting = "player"
    keep_shooting_computer = False

    set_colors(battle_object.p_obj.play_field)
    battle_object.p_obj.print_field()
    delete_colors(battle_object.p_obj.play_field)
    print("\n\n")
    set_colors(battle_object.shoot_field_p.play_field)
    battle_object.shoot_field_p.print_field()
    delete_colors(battle_object.shoot_field_p.play_field)

    while True:
        result_check_game_over = battle_object.check_game_over()

        try:
            if who_is_shooting == "player":
                if result_check_game_over:
                    print(result_check_game_over)
                    time.sleep(3)
                    break

                shooting_pos = input("\n[shooting pos]: ").lower().strip()

                if shooting_pos.strip().lower() == "guide":
                    guide()
                    do_color_field(battle_object.p_obj)
                    print("")
                    do_color_field(battle_object.shoot_field_p)
                    continue

                elif shooting_pos.strip().lower() == "help":
                    show_help()
                    continue

                elif shooting_pos.strip().lower() == "exit":
                    exit_program()
                    time.sleep(2)
                    do_color_field(battle_object.p_obj)
                    print("")
                    do_color_field(battle_object.shoot_field_p)
                    continue

                elif shooting_pos == "menu":
                    if exit_to_menu(battle_mode=True):
                        break
                    time.sleep(1)
                    do_color_field(battle_object.p_obj)
                    print("")
                    do_color_field(battle_object.shoot_field_p)

                msg_response_player = battle_object.attack(shooting_pos, who_is_shooting)
                print("")
                do_color_field(battle_object.p_obj)
                print("")
                do_color_field(battle_object.shoot_field_p)
                print(msg_response_player)

                if "missed" in msg_response_player:
                    who_is_shooting = "computer"
                else:
                    who_is_shooting = "player"

            elif who_is_shooting == "computer":
                if result_check_game_over:
                    print(result_check_game_over)
                    time.sleep(3)
                    break

                shooting_pos = battle_object.get_random_pos_computer(keep_shooting_computer)
                msg_response_computer = battle_object.attack(shooting_pos, who_is_shooting)
                print(f"\n{NAVIGATOR}Computer is thinking where to shoot...\n")
                time.sleep(6)
                do_color_field(battle_object.p_obj)
                print("")
                do_color_field(battle_object.shoot_field_p)

                print(f"\n{NAVIGATOR}Computer shot in \"{shooting_pos}\" position")

                if "missed" in msg_response_computer:
                    print(msg_response_computer)
                    who_is_shooting = "player"

                elif "killed" in msg_response_computer:
                    print(msg_response_computer)
                    who_is_shooting = "computer"
                    battle_object.count_shot_suborder_computer = 0
                    keep_shooting_computer = False

                else:
                    print(msg_response_computer)
                    who_is_shooting = "computer"
                    keep_shooting_computer = True

        except err.NotExistingPos:
            print(NOT_EXISTS_POS_ERR_MSG)
            continue
        except err.AlreadyShot:
            print(ALREADY_SHOT_MSG)
            continue


def is_pos_valid(available_pos, pos, type_ship):
    """
    :param available_pos: list type, list of available position
    :param pos: string type, position of ship
    :param type_ship: string type
    :return: None
    """
    new_pos_list = pos.split(":")

    if len(new_pos_list) != 1 and type_ship == "one_deck":
        raise err.WrongPosOneDeck
    elif len(new_pos_list) != 2 and type_ship == "two_deck":
        raise err.WrongPosTwoDeck
    elif len(new_pos_list) != 3 and type_ship == "three_deck":
        raise err.WrongPosThreeDeck
    elif len(new_pos_list) != 4 and type_ship == "four_deck":
        raise err.WrongPosFourDeck

    for pos in new_pos_list:
        if pos not in available_pos:
            raise err.NotExistingPos
        elif new_pos_list.count(pos) > 1:
            raise err.DuplicationPos


def choose_option_from_menu(opt, print_out=False):
    """
    Execute function by given command

    :param opt: string type
    :param print_out: bool type
    :return: bool type
    """
    if opt.strip().lower() == "exit":
        return True if not print_out else exit_program()
    elif opt.strip().lower() == "guide":
        return True if not print_out else guide()
    elif opt.strip().lower() == "help":
        return True if not print_out else show_help()
    elif opt.strip().lower() == "reset":
        return True if not print_out else reset_ships()
    elif opt.strip().lower() == "menu":
        return True if not print_out else exit_to_menu()
    else:
        return False


def show_help():
    print("""
    start    ---   Start a new round of battle
    exit     ---   Exit from the game
    help     ---   Show the help page one more time
    guide    ---   Get an instructions about how to play
    reset    ---   Delete all ships and start to set upping again
    menu     ---   Back to menu and you lose all ships which you set upped

    -- [!NOTE!] 'reset' only works while you set upping your ships in 'manually mode'

    -- [!NOTE!] in battle mode works the next options 'guide', 'exit', 'help', 'menu'
        """)


def exit_program():
    while True:
        print("\n[Navigator]: Do you really wanna leave us?\n")
        ans = input("[yes(y)|no(n)]: ").lower().strip()
        if ans == "yes" or ans == "y":
            print(f"\n{NAVIGATOR}It is so sad that you leave us.")
            time.sleep(2)
            print(f"{NAVIGATOR}I hope you will visit us one more time.")
            time.sleep(2)
            print(f"{NAVIGATOR}Bye!\n")
            time.sleep(2)
            sys.exit(0)
        elif ans == "no" or ans == "n":
            print(f"\n{NAVIGATOR}Right choice! \n{NAVIGATOR}Keep going the game.\n")
            break
        else:
            print(f"\n{Colors.RED}[Error]: Unknown answer!{Colors.END}"
                  f"\n[Hint]: Try the next ones ('yes', 'y') or ('no, 'n')\n")


def reset_ships(prompt=True):
    """
    Reset global variables

    :param prompt: bool type
    :return: None
    """
    if prompt:
        print(f"\n{NAVIGATOR}Do you really want to reset all ships?\n")
        while True:
            ans = input("[yes(y) | no(no)]: ")
            if ans == "yes" or ans == "y":
                print(f"\n{NAVIGATOR}Okay, let's do it!")
                time.sleep(2)
                break
            elif ans == "no" or ans == "n":
                print(f"\n{NAVIGATOR}Keep going!\n")
                time.sleep(1)
                global play_field_p
                set_colors(play_field_p.play_field)
                play_field_p.print_field()
                delete_colors(play_field_p.play_field)
                return
            else:
                print(f"\n{Colors.RED}[Error]: Unknown answer!{Colors.END}"
                      f"\n[Hint]: Try the next ones ('yes', 'y') or ('no, 'n')\n")

    play_field_p = one_deck.OneDeck()
    play_field_p.fill_pos()
    play_field_p.fill_field()
    global play_field2_p, play_field3_p, play_field4_p
    play_field2_p, play_field3_p, play_field4_p = None, None, None
    global max1_p, max2_p, max3_p, max4_p
    max1_p, max2_p, max3_p, max4_p = 0, 0, 0, 0
    print("")

    if prompt:
        set_colors(play_field_p.play_field)
        play_field_p.print_field()
        delete_colors(play_field_p.play_field)


def set_ships_random():
    """
    Wrapper for 'set_ships_computer' function

    :return: object type, field with set upped ships
    """
    while True:
        try:
            return set_ships_computer()
        except err.NotAvailablePosLeft:
            continue


def set_ships_computer():
    """
    Set randomly ships on field

    :return: object type
    """
    max1, max2, max3, max4 = 0, 0, 0, 0
    pitch2, pitch3, pitch4 = None, None, None
    pitch1 = one_deck.OneDeck()
    pitch1.fill_pos()
    pitch1.fill_field()
    count_max4_c = 0

    while True:
        if max1 != 4:
            try:

                rand_pos_one_deck = f"{random.randint(1, 10)}{LETTERS_SEA_FIELD[random.randint(0, 9)]}"
                is_pos_valid(pitch1.accessible_position, rand_pos_one_deck, "one_deck")
                pitch1.set_one_deck(rand_pos_one_deck)
                max1 += 1

            except err.WrongPosOneDeck:
                continue
            except err.NotExistingPos:
                continue
            except err.PosIsBusy:
                continue
            except IndexError:
                continue
            except err.DuplicationPos:
                continue

            if max1 == 4:
                pitch2 = two_deck.TwoDeck()
                pitch2.fill_pos()
                pitch2.play_field = pitch1.play_field.copy()
                pitch2.position_of_ships = pitch1.position_of_ships.copy()

        elif max2 != 3:
            try:

                rand_char_two_deck = random.randint(0, 9)
                rand_num_two_deck = random.randint(1, 10)
                possible_next_positions = [f"{rand_num_two_deck + 1}{LETTERS_SEA_FIELD[rand_char_two_deck]}",
                                           f"{rand_num_two_deck - 1}{LETTERS_SEA_FIELD[rand_char_two_deck]}",
                                           f"{rand_num_two_deck}{LETTERS_SEA_FIELD[rand_char_two_deck + 1]}",
                                           f"{rand_num_two_deck}{LETTERS_SEA_FIELD[rand_char_two_deck - 1]}"]
                rand_pos_two_deck = f"{rand_num_two_deck}{LETTERS_SEA_FIELD[rand_char_two_deck]}:" \
                                    f"{possible_next_positions[random.randint(0, 3)]}"

                is_pos_valid(pitch2.accessible_position, rand_pos_two_deck, "two_deck")
                pitch2.set_two_deck(rand_pos_two_deck)
                max2 += 1

            except err.WrongPosTwoDeck:
                continue
            except err.NotExistingPos:
                continue
            except err.PosIsBusy:
                continue
            except IndexError:
                continue
            except err.DuplicationPos:
                continue

            if max2 == 3:
                pitch3 = three_deck.ThreeDeck()
                pitch3.fill_pos()
                pitch3.play_field = pitch2.play_field.copy()
                pitch3.position_of_ships = pitch2.position_of_ships.copy()

        elif max3 != 2:
            try:

                rand_char_three_deck = random.randint(0, 9)
                rand_num_three_deck = random.randint(1, 10)
                possible_next_positions = [f":{rand_num_three_deck - 1}{LETTERS_SEA_FIELD[rand_char_three_deck]}:"
                                           f"{rand_num_three_deck + 1}{LETTERS_SEA_FIELD[rand_char_three_deck]}",
                                           f":{rand_num_three_deck}{LETTERS_SEA_FIELD[rand_char_three_deck - 1]}:"
                                           f"{rand_num_three_deck}{LETTERS_SEA_FIELD[rand_char_three_deck + 1]}"]
                rand_pos_three_deck = f"{rand_num_three_deck}{LETTERS_SEA_FIELD[rand_char_three_deck]}" \
                                      f"{possible_next_positions[random.randint(0, 1)]}"

                is_pos_valid(pitch3.accessible_position, rand_pos_three_deck, "three_deck")
                pitch3.set_three_deck(rand_pos_three_deck)
                max3 += 1

            except err.WrongPosThreeDeck:
                continue
            except err.NotExistingPos:
                continue
            except err.PosIsBusy:
                continue
            except IndexError:
                continue
            except err.DuplicationPos:
                continue

            if max3 == 2:
                pitch4 = four_deck.FourDeck()
                pitch4.fill_pos()
                pitch4.play_field = pitch3.play_field.copy()
                pitch4.position_of_ships = pitch3.position_of_ships.copy()

        elif max4 != 1:

            count_max4_c += 1

            if count_max4_c == 2:
                raise err.NotAvailablePosLeft

            try:
                pitch4.set_possible_pos_computer()
                possible_pos_four_deck = pitch4.get_tmp_list()
                rand_pos_four_deck = possible_pos_four_deck[random.randint(0, len(possible_pos_four_deck) - 1)]
                is_pos_valid(pitch4.accessible_position, rand_pos_four_deck, "four_deck")
                pitch4.set_four_deck(rand_pos_four_deck)
                return pitch4

            except err.WrongPosFourDeck:
                continue
            except err.NotExistingPos:
                continue
            except err.PosIsBusy:
                continue
            except IndexError:
                continue
            except err.DuplicationPos:
                continue
            except ValueError:
                continue


def exit_to_menu(choose_type_mode=False, battle_mode=False):
    """
    Loop for exit to menu

    :param choose_type_mode: bool type
    :param battle_mode: bool
    :return: bool type
    """
    if battle_mode:
        global exit_battle_mode
        while True:
            print(f"\n{NAVIGATOR}Do you wanna exit to menu?\n")
            ans = input("[yes(y) | no(n)]: ").strip().lower()
            if ans == "yes" or ans == "y":
                global exit_set_up_ships_loop
                exit_battle_mode = True
                return True
            elif ans == "no" or ans == "n":
                print(f"\n{NAVIGATOR}Keep going!\n")
                time.sleep(1)
                return
            else:
                print(f"\n{Colors.RED}[Error]: Unknown answer!{Colors.END}\n")
    else:
        global play_field_p
        while True:
            print(f"\n{NAVIGATOR}Do you wanna exit to menu?\n")
            ans = input("[yes(y) | no(n)]: ").strip().lower()
            if ans == "yes" or ans == "y":
                global exit_set_up_ships_loop
                exit_set_up_ships_loop = True
                print(f"\n\n{NAVIGATOR}Welcome back to menu!")
                print(f"{NAVIGATOR}Type \"help\" for all available commands")
                return True
            elif ans == "no" or ans == "n":
                print(f"\n{NAVIGATOR}Keep going!\n")
                return False if choose_type_mode else play_field_p.print_field()
            else:
                print(f"\n{Colors.RED}[Error]: Unknown answer!{Colors.END}\n")


def type_set_up_ships():
    """
    Choose type of set upping ships

    :return: bool type
    """
    global play_field4_p, exit_set_up_ships_loop, from_choosing_type, exit_choose_type_loop_bool

    while True:
        play_field4_p = set_ships_random()
        print("")
        do_color_field(play_field4_p)
        print(f"\n{NAVIGATOR}Does it okay?\n")
        print(f"{NAVIGATOR}You can choose another type of set upping ships")
        print(f"{NAVIGATOR}Just type 'at' in answer below\n")

        while True:
            ans = input("[yes(y) | no(n) | another type(at)]: ")
            if ans.strip().lower() == "y" or ans.strip().lower() == "yes":
                exit_set_up_ships_loop = True
                from_choosing_type = True
                return True
            elif ans.strip().lower() == "no" or ans.strip().lower() == "n":
                break
            elif ans.strip().lower() == "at":
                play_field4_p = None
                print("")
                return False
            elif ans.lower().strip() == "menu":
                if exit_to_menu(choose_type_mode=True):
                    exit_choose_type_loop_bool = True
                    exit_set_up_ships_loop = True
                    return False
            elif ans.lower().strip() == "guide":
                guide()
                do_color_field(play_field4_p)
                print(f"\n{NAVIGATOR}Does it okay?\n")
            elif ans.lower().strip() == "exit":
                exit_program()
                time.sleep(2)
                do_color_field(play_field4_p)
                print(f"\n{NAVIGATOR}Does it okay?\n")
            elif ans.lower().strip() == "help":
                show_help()
                time.sleep(4)
                do_color_field(play_field4_p)
                print(f"\n{NAVIGATOR}Does it okay?\n")
            else:
                print(f"\n{Colors.RED}[Error]: Unknown answer!{Colors.END}"
                      f"\n[Hint]: Try the next ones ('yes', 'y') or ('no, 'n')\n")
                do_color_field(play_field4_p)
                print(f"\n{NAVIGATOR}Does it okay?\n")


def main():
    """
    Main function of the game

    :return: None
    """
    global play_field_p, from_choosing_type, is_printed_intro_bool
    global play_field2_p, play_field3_p, play_field4_p, exit_main_loop
    global max1_p, max2_p, max3_p, max4_p, exit_battle_mode

    if not is_printed_intro_bool:
        print(
            """
            Hey bro, I am glad to see you in our game.
            If you ready for a sea battle you welcome.
            Type "help" for all available commands.
            """
        )
        is_printed_intro_bool = True
    elif exit_battle_mode:
        print(
            """
            Welcome back to menu!
            You have interrupted the battle!
            Hope you did the right choice.
            """
        )
        reset_ships(prompt=False)
        exit_battle_mode = False
    else:
        print(
            """
            Welcome back to menu fighter!
            Hope you have enjoyed your battle!
            If you wanna exit, just type "exit".
            If you wanna get information about
            commands then type "help".
            """
        )
        reset_ships(prompt=False)

    # main loop
    while True:
        if exit_main_loop:
            exit_main_loop = False
            break

        choose_option = input("[menu]: ").strip().lower()

        # instruction about the game
        if choose_option == "guide":
            guide()

        # logic of game
        elif choose_option == "start":

            global exit_set_up_ships_loop
            exit_set_up_ships_loop = False
            global exit_choose_type_loop_bool
            exit_choose_type_loop_bool = False

            print(f"\n\n{NAVIGATOR}Welcome on board, fighter!")
            print(f"{NAVIGATOR}It's time for you to set your ships")
            print(f"{NAVIGATOR}What type of set upping ships do you wanna choose?\n\n")

            # choose type of set upping ships
            while True:
                if exit_choose_type_loop_bool:
                    exit_choose_type_loop_bool = False
                    break

                print("\nmanually - you set up all ships by your own")
                print("random   - we will set up ships instead of you randomly\n")
                type_set_up = input("[manually(m) | random(r)]: ").strip().lower()

                if type_set_up == "m" or type_set_up == "manually":
                    print(f"\n{NAVIGATOR}The template for one deck ship is 'position'")
                    print(f"{NAVIGATOR}For example 'j8'\n")
                    do_color_field(play_field_p)
                    break
                elif type_set_up == "r" or type_set_up == "random":
                    if type_set_up_ships():
                        break
                    else:
                        continue
                elif type_set_up == "menu":
                    if exit_to_menu(choose_type_mode=True):
                        break
                elif type_set_up == "guide":
                    guide()
                    print("")
                    continue
                elif type_set_up == "exit":
                    exit_program()
                elif type_set_up == "help":
                    show_help()
                else:
                    print("\n[Error]: Unknown answer!\n")

            # set upping ships manually loop
            while True:

                if exit_set_up_ships_loop and from_choosing_type:
                    exit_main_loop = True
                    exit_set_up_ships_loop = False
                    from_choosing_type = False
                    break
                elif exit_set_up_ships_loop:
                    reset_ships(prompt=False)
                    exit_set_up_ships_loop = False
                    break

                # set up one deck ships
                if max1_p != 4:

                    one_deck_ship_pos = input("\n[one-deck]: ").strip().lower()

                    try:

                        if choose_option_from_menu(one_deck_ship_pos):
                            choose_option_from_menu(one_deck_ship_pos, print_out=True)
                            continue

                        is_pos_valid(play_field_p.accessible_position, one_deck_ship_pos, "one_deck")

                        play_field_p.set_one_deck(one_deck_ship_pos)
                        print("")
                        do_color_field(play_field_p)
                        max1_p += 1

                    except err.WrongPosOneDeck:
                        print(f"\n{Colors.RED}[Error]: Wrong position for one deck ship!{Colors.END}")
                        print("[Hint]: Try position with \"@\" char")
                        continue
                    except err.NotExistingPos:
                        print(NOT_EXISTS_POS_ERR_MSG)
                        continue
                    except err.PosIsBusy:
                        print(P_BUSY_MSG)
                        continue

                    if max1_p == 4:
                        play_field2_p = two_deck.TwoDeck()
                        play_field2_p.fill_pos()
                        play_field2_p.play_field = play_field_p.play_field
                        play_field2_p.position_of_ships = play_field_p.position_of_ships
                        print(f"\n{NAVIGATOR}You have set up all 'one deck ships'!")
                        print(f"{NAVIGATOR}Now it's time for set up 'two deck ships'")
                        print(f"{NAVIGATOR}The template is following 'position:position'")
                        print(f"{NAVIGATOR}For example '10c:10d'")

                # set up two deck ships
                elif max2_p != 3:
                    two_deck_ship_pos = input("\n[two_deck]: ").strip().lower()

                    try:

                        if choose_option_from_menu(two_deck_ship_pos):
                            choose_option_from_menu(two_deck_ship_pos, print_out=True)
                            continue

                        is_pos_valid(play_field2_p.accessible_position, two_deck_ship_pos, "two_deck")

                        play_field2_p.set_two_deck(two_deck_ship_pos)
                        print("")
                        do_color_field(play_field2_p)
                        max2_p += 1
                    except err.WrongPosTwoDeck:
                        print(f"{Colors.RED}\n[Error]: Wrong position for two deck ship{Colors.END}")
                        print("[Hint]: See 'guide' how to set up two deck ship")
                        continue
                    except err.PosIsBusy:
                        print(P_BUSY_MSG)
                        continue
                    except err.NotExistingPos:
                        print(NOT_EXISTS_POS_ERR_MSG)
                        continue
                    except err.DuplicationPos:
                        print(DUPLICATION_ERR_MSG)
                        continue

                    if max2_p == 3:
                        play_field3_p = three_deck.ThreeDeck()
                        play_field3_p.fill_pos()
                        play_field3_p.play_field = play_field2_p.play_field
                        play_field3_p.position_of_ships = play_field2_p.position_of_ships
                        print(f"\n{NAVIGATOR}Good job!")
                        print(f"{NAVIGATOR}You have set up all the 'two deck ships'")
                        print(f"{NAVIGATOR}Now, it's time for 'three deck ships'")
                        print(f"{NAVIGATOR}The template is 'position:position:position'")
                        print(f"{NAVIGATOR}For example '3j:4j:5j'")

                # set up three deck ships
                elif max3_p != 2:

                    three_deck_ship_pos = input("\n[three-deck]: ").strip().lower()

                    try:

                        if choose_option_from_menu(three_deck_ship_pos):
                            choose_option_from_menu(three_deck_ship_pos, print_out=True)
                            continue

                        is_pos_valid(play_field3_p.accessible_position, three_deck_ship_pos, "three_deck")

                        play_field3_p.set_three_deck(three_deck_ship_pos)
                        print("")
                        do_color_field(play_field3_p)
                        max3_p += 1

                    except err.WrongPosThreeDeck:
                        print(f"\n{Colors.RED}[Error]: Wrong position for three deck ship{Colors.END}")
                        print("[Hint]: Try another one, or see 'guide'")
                        continue
                    except err.NotExistingPos:
                        print(NOT_EXISTS_POS_ERR_MSG)
                        continue
                    except err.PosIsBusy:
                        print(P_BUSY_MSG)
                        continue
                    except err.DuplicationPos:
                        print(DUPLICATION_ERR_MSG)
                        continue

                    if max3_p == 2:
                        play_field4_p = four_deck.FourDeck()
                        play_field4_p.fill_pos()
                        play_field4_p.position_of_ships = play_field3_p.position_of_ships
                        play_field4_p.play_field = play_field3_p.play_field
                        print(f"\n{NAVIGATOR}Perfect!")
                        print(f"{NAVIGATOR}You have set up all 'three deck' ships")
                        print(f"{NAVIGATOR}Time has come for set up 'four deck' ship")
                        print(f"{NAVIGATOR}The template is 'position:position:position:position'")
                        print(f"{NAVIGATOR}For example 'h1:h2:h3:h4'")

                # set up four deck ship
                elif max4_p != 1:
                    four_deck_ship_pos = input("\n[four-deck]: ").strip().lower()

                    try:
                        if choose_option_from_menu(four_deck_ship_pos):
                            choose_option_from_menu(four_deck_ship_pos, print_out=True)
                            continue

                        is_pos_valid(play_field4_p.accessible_position, four_deck_ship_pos, "four_deck")

                        play_field4_p.set_four_deck(four_deck_ship_pos)
                        print("\n")
                        do_color_field(play_field4_p)
                    except err.WrongPosFourDeck:
                        print(f"\n{Colors.RED}[Error]: Wrong position for four deck ship{Colors.END}")
                        print("[Hint]: Try another one, or see 'guide'")
                        continue
                    except err.NotExistingPos:
                        print(NOT_EXISTS_POS_ERR_MSG)
                        continue
                    except err.PosIsBusy:
                        print(P_BUSY_MSG)
                        continue
                    except err.DuplicationPos:
                        print(DUPLICATION_ERR_MSG)
                        continue

                    max4_p += 1

                    exit_main_loop = True
                    break

        # when exit
        elif choose_option == "exit":
            exit_program()

        # just type a space
        elif choose_option == "":
            continue

        # help
        elif choose_option == "help":
            show_help()

        # menu
        elif choose_option == "menu":
            print("\nYou are in menu =)\n")

        # unknown command
        else:
            print(f"\n{Colors.RED}[Error]: Unknown command!{Colors.END}")
            print("[Hint]: Type 'help' for all available commands!\n")

    print(f"\n{NAVIGATOR}Awesome!")
    time.sleep(1)
    print(f"{NAVIGATOR}You successfully placed all ships")
    time.sleep(3)
    print(f"{NAVIGATOR}Now, it's time for battle with your opponent!\n")
    time.sleep(4)
    print(f"{NAVIGATOR}Waiting while computer is placing all ships\n\n")
    time.sleep(3)

    # start battle
    c_obj = set_ships_random()
    battle(c_obj, play_field4_p)


# run game
if __name__ == "__main__":

    # needs for work colors in console
    colorama.init()

    while True:
        main()
