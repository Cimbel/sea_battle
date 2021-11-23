import class_field
import exceptions_and_errors as err


class FourDeck(class_field.BuildFiled):
    count_deck = 0
    four_deck_pos1 = None
    four_deck_pos2 = None
    four_deck_pos3 = None
    four_deck_pos4 = None
    prop_field = None
    tmp_pos_four_deck_computer = []

    def clear(self):
        self.four_deck_pos1, self.four_deck_pos2, self.four_deck_pos3, self.four_deck_pos4 = None, None, None, None
        self.prop_field, self.count_deck = None, 0

    # lp - list_pos[1..]
    def is_deck_pos_valid(self, lp1, lp2, lp3, lp4):
        """
        :param lp1: list type, list of two integers
        :param lp2: list type, list of two integers
        :param lp3: list type, list of two integers
        :param lp4: list type, list of two integers
        :return: None
        """
        if self.play_field[lp1[0]][lp1[1]] == "-" \
                or self.play_field[lp2[0]][lp2[1]] == "-" \
                or self.play_field[lp3[0]][lp3[1]] == "-" \
                or self.play_field[lp4[0]][lp4[1]] == "-":

            self.clear()
            raise err.WrongPosFourDeck

        elif self.play_field[lp1[0]][lp1[1]] == "#" \
                or self.play_field[lp2[0]][lp2[1]] == "#" \
                or self.play_field[lp3[0]][lp3[1]] == "#" \
                or self.play_field[lp4[0]][lp4[1]] == "#":

            self.clear()
            raise err.PosIsBusy

        # pos in row
        elif lp1[0] == lp2[0] and lp1[0] == lp3[0] and lp1[0] == lp4[0] and lp2[0] == lp3[0] and lp2[0] == lp4[0] \
                and lp3[0] == lp4[0]:
            self.prop_field = "row"

        # pos in column
        elif lp1[1] == lp2[1] and lp1[1] == lp3[1] and lp1[1] == lp4[1] and lp2[1] == lp3[1] and lp2[1] == lp4[1] \
                and lp3[1] == lp4[1]:
            self.prop_field = "column"

        # temporary list of pos - tmp_l
        tmp_l = [lp1[0], lp2[0], lp3[0], lp4[0]] if self.prop_field == "column" else [lp1[1], lp2[1], lp3[1], lp4[1]]

        max_pos_num = tmp_l.pop(tmp_l.index(max(tmp_l)))
        min_pos_num = tmp_l.pop(tmp_l.index(min(tmp_l)))
        tmp_l.sort()

        if not ((max_pos_num - 1 == tmp_l[1]) and (min_pos_num + 1 == tmp_l[0])):
            self.clear()
            raise err.WrongPosFourDeck

    def set_four_deck(self, pos):
        """

        :param pos: string type, position of four deck ship
                    must be like "h1:h2:h3:h4"
        :return: None
        """
        for num in range(11):
            for char in self.letters_small:
                new_pos = pos.split(":")

                # set ships and space around them
                if new_pos[0].lower() == f"{num}{char}" or new_pos[0].lower() == f"{char}{num}" \
                        or new_pos[1].lower() == f"{char}{num}" or new_pos[1].lower() == f"{num}{char}" \
                        or new_pos[2].lower() == f"{char}{num}" or new_pos[2].lower() == f"{num}{char}" \
                        or new_pos[3].lower() == f"{char}{num}" or new_pos[3].lower() == f"{num}{char}":

                    # set second deck
                    if self.count_deck == 1:
                        self.four_deck_pos2 = f"{num}:{self.letters_small.find(char)}"
                        self.count_deck += 1

                    # set third deck
                    elif self.count_deck == 2:
                        self.four_deck_pos3 = f"{num}:{self.letters_small.find(char)}"
                        self.count_deck += 1

                    # set ford deck
                    elif self.count_deck == 3:
                        self.four_deck_pos4 = f"{num}:{self.letters_small.find(char)}"

                        # fdp_l1 - four_deck_pos_list1 ...
                        fdp_l1 = list(map(int, self.four_deck_pos1.split(":")))
                        fdp_l2 = list(map(int, self.four_deck_pos2.split(":")))
                        fdp_l3 = list(map(int, self.four_deck_pos3.split(":")))
                        fdp_l4 = list(map(int, self.four_deck_pos4.split(":")))

                        self.is_deck_pos_valid(fdp_l1, fdp_l2, fdp_l3, fdp_l4)

                        # set decks
                        self.play_field[fdp_l1[0]][fdp_l1[1]] = "#"
                        self.play_field[fdp_l2[0]][fdp_l2[1]] = "#"
                        self.play_field[fdp_l3[0]][fdp_l3[1]] = "#"
                        self.play_field[fdp_l4[0]][fdp_l4[1]] = "#"

                        # set '-' around deck
                        self.set_space_around_deck(fdp_l1)
                        self.set_space_around_deck(fdp_l2)
                        self.set_space_around_deck(fdp_l3)
                        self.set_space_around_deck(fdp_l4)

                        # set position in dict
                        self.position_of_ships["four_deck_ship"] = [self.four_deck_pos1, self.four_deck_pos2,
                                                                    self.four_deck_pos3, self.four_deck_pos4]
                        self.clear()
                        return

                    # set first deck
                    else:
                        self.four_deck_pos1 = f"{num}:{self.letters_small.find(char)}"
                        self.count_deck += 1

    # set all possible pos for computer's four deck ship
    def set_possible_pos_computer(self):
        """
        Set possible position for computer's four deck ship

        :return: None
        """
        for i in range(11):
            for j in range(len(self.letters_small)):
                try:
                    if self.play_field[i][j] == "@" and self.play_field[i][j + 1] == "@" \
                            and self.play_field[i][j + 2] == "@" and self.play_field[i][j + 3] == "@":
                        self.tmp_pos_four_deck_computer.append(f"{i}{self.letters_small[j]}:"
                                                               f"{i}{self.letters_small[j + 1]}:"
                                                               f"{i}{self.letters_small[j + 2]}:"
                                                               f"{i}{self.letters_small[j + 3]}")

                    if self.play_field[i][j] == "@" and self.play_field[i + 1][j] == "@" \
                            and self.play_field[i + 2][j] == "@" and self.play_field[i + 3][j] == "@":
                        self.tmp_pos_four_deck_computer.append(f"{i}{self.letters_small[j]}:"
                                                               f"{i + 1}{self.letters_small[j]}:"
                                                               f"{i + 2}{self.letters_small[j]}:"
                                                               f"{i + 3}{self.letters_small[j]}")
                except IndexError:
                    continue

    # get the list of all possible position for four deck ship
    def get_tmp_list(self):
        """
        :return: list, list of possible position for
                 computer's four deck ship
        """
        return self.tmp_pos_four_deck_computer
