import class_field
import exceptions_and_errors as err


class ThreeDeck(class_field.BuildFiled):
    count_deck, max_three_deck = 0, 0
    three_deck_pos1, three_deck_pos2, three_deck_pos3, property_field = None, None, None, None

    def clear(self):
        self.count_deck = 0
        self.property_field, self.three_deck_pos1, self.three_deck_pos2, self.three_deck_pos3, = None, None, None, None

    def set_pos(self, pos1, pos2, pos3):
        """
        Set position to dictionary

        :param pos1: string type, position of deck
        :param pos2: string type, position of deck
        :param pos3: string type, position of deck
        :return: None
        """
        if self.max_three_deck == 1:
            self.position_of_ships["three_deck_ships"]["first_three_deck"] = [pos1, pos2, pos3]
        elif self.max_three_deck == 2:
            self.position_of_ships["three_deck_ships"]["second_three_deck"] = [pos1, pos2, pos3]

    def is_deck_pos_valid(self, deck_pos1, deck_pos2, deck_pos3):
        """
        :param deck_pos1: list type, list of two integers
        :param deck_pos2: list type, list of two integers
        :param deck_pos3: list type, list of two integers
        :return: None
        """
        if self.play_field[deck_pos1[0]][deck_pos1[1]] == "-" \
                or self.play_field[deck_pos2[0]][deck_pos2[1]] == "-" \
                or self.play_field[deck_pos3[0]][deck_pos3[1]] == "-":

            self.clear()
            raise err.WrongPosThreeDeck

        elif self.play_field[deck_pos1[0]][deck_pos1[1]] == "#" \
                or self.play_field[deck_pos2[0]][deck_pos2[1]] == "#" \
                or self.play_field[deck_pos3[0]][deck_pos3[1]] == "#":

            self.clear()
            raise err.PosIsBusy

        # all decks in one row
        elif deck_pos1[0] == deck_pos2[0] and deck_pos1[0] == deck_pos3[0] and deck_pos2[0] == deck_pos3[0]:
            self.property_field = "row"

        # all decks in one column
        elif deck_pos1[1] == deck_pos2[1] and deck_pos1[1] == deck_pos3[1] and deck_pos2[1] == deck_pos3[1]:
            self.property_field = "column"

        tmp_list_pos = [deck_pos1[1], deck_pos2[1], deck_pos3[1]] if self.property_field == "row" \
            else [deck_pos1[0], deck_pos2[0], deck_pos3[0]]

        max_pos_num = tmp_list_pos.pop(tmp_list_pos.index(max(tmp_list_pos)))
        min_pos_num = tmp_list_pos.pop(tmp_list_pos.index(min(tmp_list_pos)))

        if not ((tmp_list_pos[0] + 1) == max_pos_num and (tmp_list_pos[0] - 1) == min_pos_num):
            self.clear()
            raise err.WrongPosThreeDeck

    def set_three_deck(self, pos):
        """
        Set '#' on play field

        :param pos: string type, position of three deck ships
                    must be like "h1:h2:h3"
        :return: None
        """
        for num in range(11):
            for char in self.letters_small:
                new_pos = pos.split(":")

                if new_pos[0].lower() == f"{num}{char}" or new_pos[0].lower() == f"{char}{num}" \
                        or new_pos[1].lower() == f"{char}{num}" or new_pos[1].lower() == f"{num}{char}" \
                        or new_pos[2].lower() == f"{char}{num}" or new_pos[2].lower() == f"{num}{char}":

                    # set second deck
                    if self.count_deck == 1:
                        self.three_deck_pos2 = f"{num}:{self.letters_small.find(char)}"
                        self.count_deck += 1

                    # set third deck
                    elif self.count_deck == 2:
                        self.three_deck_pos3 = f"{num}:{self.letters_small.find(char)}"

                        tdp_l1 = list(map(int, self.three_deck_pos1.split(":")))
                        tdp_l2 = list(map(int, self.three_deck_pos2.split(":")))
                        tdp_l3 = list(map(int, self.three_deck_pos3.split(":")))

                        self.is_deck_pos_valid(tdp_l1, tdp_l2, tdp_l3)
                        self.play_field[tdp_l1[0]][tdp_l1[1]] = "#"
                        self.play_field[tdp_l2[0]][tdp_l2[1]] = "#"
                        self.play_field[tdp_l3[0]][tdp_l3[1]] = "#"

                        # set '-' around deck
                        self.set_space_around_deck(tdp_l1)
                        self.set_space_around_deck(tdp_l2)
                        self.set_space_around_deck(tdp_l3)

                        self.max_three_deck += 1
                        self.set_pos(self.three_deck_pos1, self.three_deck_pos2, self.three_deck_pos3)

                        return

                    # set first deck
                    else:
                        self.three_deck_pos1 = f"{num}:{self.letters_small.find(char)}"
                        self.count_deck += 1
