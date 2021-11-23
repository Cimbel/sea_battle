import exceptions_and_errors as err
import random
from colors import Colors


class War:
    letters_small = " abcdefghij"
    dead_ships_count_player = 0
    dead_ships_count_computer = 0
    already_shot_pos_computer = []
    count_shot_suborder_computer = 0
    count_try_shoot_computer = 0

    def __init__(self, c_obj, p_obj, shoot_field_computer, shoot_field_player):
        self.c_obj = c_obj
        self.p_obj = p_obj
        self.shoot_field_c = shoot_field_computer
        self.shoot_field_p = shoot_field_player

    def check_game_over(self):
        """
        :return: string type -- when some of the opponents win
                 bool -- false if don't know who win
        """
        if self.dead_ships_count_player == 10:
            return f"\n\n{Colors.GREEN}[Navigator]: Congrats! You killed all ships and won the battle!{Colors.END}"
        elif self.dead_ships_count_computer == 10:
            return f"\n\n{Colors.RED}[Navigator]: You lose, computer beat you!{Colors.END}"

        return False

    def who_killed_ship(self, opponent_name):
        """
        +1 if some of opponents killed ship

        :param opponent_name: string type
        :return: None
        """
        if opponent_name == "computer":
            self.dead_ships_count_computer += 1
        elif opponent_name == "player":
            self.dead_ships_count_player += 1

    def who_shooting(self, opponent_name):
        """
        Set list of two objects

        :param opponent_name: string type
        :return: list type, list of two objects
        """
        list_who_shooting = [opponent_name]

        if opponent_name == "player":
            list_who_shooting.append(self.c_obj)
            list_who_shooting.append(self.shoot_field_p)
        elif opponent_name == "computer":
            list_who_shooting.append(self.p_obj)
            list_who_shooting.append(self.shoot_field_c)

        return list_who_shooting

    def get_next_pos_computer(self, pos):
        """
        Set list of available positions for computer,
        when computer trying to shoot two deck ship.

        :param pos: list type, list of two integers
        :return: list type, random positions
        """
        rand_deck_pos = []
        list_pos = [f"{pos[0] + 1}:{pos[1]}", f"{pos[0] - 1}:{pos[1]}",
                    f"{pos[0]}:{pos[1] + 1}", f"{pos[0]}:{pos[1] - 1}"]

        for deck_pos in range(len(list_pos)):
            tmp_list = list(map(int, list_pos[deck_pos].split(":")))
            try:
                if self.shoot_field_c.play_field[tmp_list[0]][tmp_list[1]] == "@":
                    rand_deck_pos.append(f"{tmp_list[0]}{self.letters_small[tmp_list[1]]}")
            except IndexError:
                continue

        return rand_deck_pos

    def get_list_pos(self, pos):
        """
        Find indexes of position in play field

        :param pos: string type, shooting position
        :return: list type, list of two integers
        """
        for num in range(11):
            for char in self.letters_small:
                if pos.lower() == f"{num}{char}" or pos.lower() == f"{char}{num}":
                    return [num, self.letters_small.find(char)]

    def random_next_tf_pos(self, type_line: str, *args):
        """
        Set next possible position if computer shooting
        three deck ship or four deck ship

        :param type_line: string type, 'column' or 'row'
        :param args: list types, list of two integers
        :return: list type, possible position list
        """

        random_pos_list = None
        list_pos = []

        if type_line == "row":
            max_num = max([arg[1] for arg in args])
            min_num = min([arg[1] for arg in args])
            random_pos_list = [f"{args[0][0]}:{max_num + 1}", f"{args[0][0]}:{min_num - 1}"]
        elif type_line == "column":
            max_num = max([arg[0] for arg in args])
            min_num = min([arg[0] for arg in args])
            random_pos_list = [f"{max_num + 1}:{args[0][1]}", f"{min_num - 1}:{args[0][1]}"]

        for new_pos in range(len(random_pos_list)):
            tmp_list = list(map(int, random_pos_list[new_pos].split(":")))

            try:
                if self.shoot_field_c.play_field[tmp_list[0]][tmp_list[1]] == "@":
                    list_pos.append(f"{tmp_list[0]}{self.letters_small[tmp_list[1]]}")
            except IndexError:
                continue

        return list_pos

    def get_random_pos_computer(self, keep_shooting_computer=False):
        """
        Find next computer's shooting position

        :param keep_shooting_computer: bool type, 'True' when computer
                                       trying kill two deck ship or higher
        :return: list type, list of all random possible positions for shooting
        """

        list_pos = []

        # shooting four deck ship
        if keep_shooting_computer and self.count_shot_suborder_computer == 3:
            last_pos1 = self.get_list_pos(self.already_shot_pos_computer[-1].lower())
            last_pos2 = self.get_list_pos(self.already_shot_pos_computer[-2].lower())
            last_pos3 = self.get_list_pos(self.already_shot_pos_computer[-3].lower())

            # row
            if last_pos1[0] == last_pos2[0] and last_pos3[0] == last_pos2[0] and last_pos1[0] == last_pos3[0]:
                list_pos = self.random_next_tf_pos("row", last_pos1, last_pos2, last_pos3)

            # column
            elif last_pos1[1] == last_pos2[1] and last_pos3[1] == last_pos2[1] and last_pos1[1] == last_pos3[1]:
                list_pos = self.random_next_tf_pos("column", last_pos1, last_pos2, last_pos3)

        # shooting three deck or higher
        elif keep_shooting_computer and self.count_shot_suborder_computer == 2:
            last_pos1 = self.get_list_pos(self.already_shot_pos_computer[-1].lower())
            last_pos2 = self.get_list_pos(self.already_shot_pos_computer[-2].lower())

            # row
            if last_pos1[0] == last_pos2[0]:
                list_pos = self.random_next_tf_pos("row", last_pos1, last_pos2)

            # column
            elif last_pos1[1] == last_pos2[1]:
                list_pos = self.random_next_tf_pos("column", last_pos1, last_pos2)

        # shooting two deck or higher
        elif keep_shooting_computer:
            last_shot_pos = self.already_shot_pos_computer[-1].lower()
            list_pos = self.get_next_pos_computer(self.get_list_pos(last_shot_pos))

        # shooting one deck or higher
        else:
            for num in range(11):
                for char in self.letters_small:
                    pos = self.shoot_field_c.play_field[num][self.letters_small.find(char)]
                    if pos == "@":
                        list_pos.append(f"{num}{char}")

        return list_pos[random.randint(0, len(list_pos) - 1)]

    def attack(self, pos, who_shoot):
        """
        Check if one of an opponent is hit target or not

        :param pos: string type, position for shooting
        :param who_shoot: string type, 'computer' or 'player'
        :return: string type, message of result shooting
        """
        who_shoot_list = self.who_shooting(who_shoot)
        opponent_name, who_shoot, who_field = who_shoot_list
        self.is_shooting_pos_valid(self.p_obj.accessible_position, pos.lower(), who_field)
        list_pos = self.get_list_pos(pos.lower())
        shoot_pos = who_shoot.play_field[list_pos[0]][list_pos[1]]

        # hit the target
        if shoot_pos == "#":
            who_field.play_field[list_pos[0]][list_pos[1]] = "X"
            who_shoot.play_field[list_pos[0]][list_pos[1]] = "X"

            if opponent_name == "computer":
                self.already_shot_pos_computer.append(pos)
                self.count_shot_suborder_computer += 1

            return self.change_pos_ships_computer(f"{list_pos[0]}:{list_pos[1]}", who_shoot_list)

        # missed the target
        elif shoot_pos == "@":
            who_field.play_field[list_pos[0]][list_pos[1]] = "-"
            who_shoot.play_field[list_pos[0]][list_pos[1]] = "-"

            return f"\n{Colors.RED}[Navigator]: You missed!{Colors.END}" if opponent_name == "player" \
                else "\n[Navigator]: Computer missed!"

    @staticmethod
    def get_shot_msg(opponent_name, type_shot, type_ship=None):
        """
        Set message, depends on event

        :param opponent_name: string type, 'computer' or 'player'
        :param type_shot: string type, 'killed' or 'hit'
        :param type_ship: by default 'None', string type when equal to 'killed'
        :return: string type, message hit the target or killed
        """
        if opponent_name == "computer" and type_shot == "hit":
            return "\n[Navigator]: Computer hit the target!\n[Navigator]: Computer keep going shooting"
        elif opponent_name == "computer" and type_shot == "killed":
            return f"\n[Navigator]: Computer killed {type_ship} ship!\n[Navigator]: Computer keep going shooting"
        elif opponent_name == "player" and type_shot == "hit":
            return f"\n{Colors.CYAN}[Navigator]: Good job! You hit the target" \
                   f"\n[Navigator]: Keep going shooting{Colors.END}"
        elif opponent_name == "player" and type_shot == "killed":
            return f"\n{Colors.CYAN}[Navigator]: You killed {type_ship} ship!" \
                   f"\n[Navigator]: Keep going shooting{Colors.END}"

    def which_msg(self, opponent_name, list_pos, who_shoot, who_field, count_deck, ship_type):
        """
        Relate to event, choose which msg send to user

        :param opponent_name: string type, "computer" or "player"
        :param list_pos: list type, list all particular ship positions
        :param who_shoot: object type, "computer's" or "player's" play field
        :param who_field: object type, "computer's" or "player's" shooting field
        :param count_deck: int type, how many decks in the particular ship
        :param ship_type: string type, kind of ship "two deck", "three deck" or "four deck"
        :return: string type, msg depends on event
        """
        if list_pos.count("X") == count_deck:
            self.set_space_around_dead_ship(list_pos, who_shoot, who_field)
            self.who_killed_ship(opponent_name)
            return self.get_shot_msg(opponent_name, "killed", type_ship=ship_type)
        else:
            return self.get_shot_msg(opponent_name, "hit")

    def change_pos_ships_computer(self, pos, who_shoot_list):
        """
        Check if player's shoot pos exists in all available
        pos in computer's dict

        :param pos: string type, position of shooting
        :param who_shoot_list: list type, list of two objects and one string type
        :return: string type, message 'hit' or 'killed' a ship
        """

        opponent_name, who_shoot, who_field = who_shoot_list

        for key in who_shoot.position_of_ships.keys():
            if key == "one_deck_ships":

                for key_one_deck in who_shoot.position_of_ships[key]:
                    one_pos = who_shoot.position_of_ships[key][key_one_deck]
                    if pos == one_pos:

                        # set space around one deck ship
                        who_field.set_space_around_deck(list(map(int, one_pos.split(":"))))
                        who_shoot.set_space_around_deck(list(map(int, one_pos.split(":"))))

                        # set pos as dead
                        who_shoot.position_of_ships[key][key_one_deck] = "X"

                        self.who_killed_ship(opponent_name)

                        return self.get_shot_msg(opponent_name, "killed", type_ship="one deck")

            elif key == "two_deck_ships":

                for key_two_deck in who_shoot.position_of_ships[key]:
                    list_pos = who_shoot.position_of_ships[key][key_two_deck]
                    if pos in list_pos:
                        list_pos.append("X")
                        return self.which_msg(opponent_name, list_pos, who_shoot, who_field, 2, "two deck")

            elif key == "three_deck_ships":

                for key_three_deck in who_shoot.position_of_ships[key]:
                    list_pos = who_shoot.position_of_ships[key][key_three_deck]
                    if pos in list_pos:
                        list_pos.append("X")
                        return self.which_msg(opponent_name, list_pos, who_shoot, who_field, 3, "three deck")

            elif key == "four_deck_ship":
                list_pos = who_shoot.position_of_ships[key]
                if pos in list_pos:
                    list_pos.append("X")
                    return self.which_msg(opponent_name, list_pos, who_shoot, who_field, 4, "four deck")

    def is_shooting_pos_valid(self, available_pos, pos, who_field):
        """
        :param available_pos: list type, all available position on play field
        :param pos: string type, shooting position
        :param who_field: object type, which field to check
        :return: None
        """
        if pos not in available_pos:
            raise err.NotExistingPos

        list_pos = self.get_list_pos(pos.lower())
        shooting_pos = who_field.play_field[list_pos[0]][list_pos[1]]

        if shooting_pos == "-" or shooting_pos == "X":
            raise err.AlreadyShot

    @staticmethod
    def set_space_around_dead_ship(list_dead_pos, who_shoot, who_field):
        """
        Set '-' around dead ship

        :param list_dead_pos: list type, list of string with 'X' and ships' positions
        :param who_shoot: object type, on which shooting field set '-'
        :param who_field: object type, on which play field set '-'
        :return: None
        """
        for item in range(len(list_dead_pos)):
            if list_dead_pos[item] != "X":
                dead_pos = list(map(int, list_dead_pos[item].split(":")))
                who_field.set_space_around_deck(dead_pos)
                who_shoot.set_space_around_deck(dead_pos)
