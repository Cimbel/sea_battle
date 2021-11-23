import class_field
import exceptions_and_errors as err


class TwoDeck(class_field.BuildFiled):
    count_deck, max_two_deck = 0, 0
    two_deck_pos1, two_deck_pos2 = None, None

    def is_ship_pos_valid(self, deck_list_pos1, deck_list_pos2):
        """
        :param deck_list_pos1: list type, list of two integers
        :param deck_list_pos2: list type, list of two integers
        :return: None
        """
        if self.play_field[deck_list_pos1[0]][deck_list_pos1[1]] == "-" \
                or self.play_field[deck_list_pos2[0]][deck_list_pos2[1]] == "-":
            self.two_deck_pos1, self.two_deck_pos2, self.count_deck = None, None, 0
            raise err.WrongPosTwoDeck
        elif self.play_field[deck_list_pos1[0]][deck_list_pos1[1]] == "#" \
                or self.play_field[deck_list_pos2[0]][deck_list_pos2[1]] == "#":
            self.two_deck_pos1, self.two_deck_pos2, self.count_deck = None, None, 0
            raise err.PosIsBusy

        list_pos = [f"{deck_list_pos1[0] + 1}:{deck_list_pos1[1]}",
                    f"{deck_list_pos1[0] - 1}:{deck_list_pos1[1]}",
                    f"{deck_list_pos1[0]}:{deck_list_pos1[1] - 1}",
                    f"{deck_list_pos1[0]}:{deck_list_pos1[1] + 1}"]

        if self.two_deck_pos2 not in list_pos:
            self.two_deck_pos1, self.two_deck_pos2, self.count_deck = None, None, 0
            raise err.WrongPosTwoDeck

    def set_pos(self, pos1, pos2):
        """
        Set position of deck to dictionary

        :param pos1: string type, position of deck
        :param pos2: string type, position of deck
        :return: None
        """
        if self.max_two_deck == 1:
            self.position_of_ships["two_deck_ships"]["first_two_deck"] = [pos1, pos2]
        elif self.max_two_deck == 2:
            self.position_of_ships["two_deck_ships"]["second_two_deck"] = [pos1, pos2]
        elif self.max_two_deck == 3:
            self.position_of_ships["two_deck_ships"]["third_two_deck"] = [pos1, pos2]

    def set_two_deck(self, pos):
        """
        Set '#' on play field for two deck ship

        :param pos: string type, position of two deck ship
                    must be like 'h1:h2'
        :return: None
        """
        for i in range(11):
            for j in self.letters_small:

                # skip row where letters and numbers
                if i == 0:
                    pass

                # set ships and space around them
                else:
                    new_pos = pos.split(":")

                    if new_pos[0].lower() == f"{i}{j}" or new_pos[0].lower() == f"{j}{i}" \
                            or new_pos[1].lower() == f"{j}{i}" or new_pos[1].lower() == f"{i}{j}":

                        if self.count_deck == 1:
                            self.two_deck_pos2 = f"{i}:{self.letters_small.find(j)}"

                            # two_deck_pos1_list is short for tdp1_l
                            # two_deck_pos2_list is short for tdp1_l
                            tdp1_l = list(map(int, self.two_deck_pos1.split(":")))
                            tdp2_l = list(map(int, self.two_deck_pos2.split(":")))

                            self.is_ship_pos_valid(tdp1_l, tdp2_l)
                            self.play_field[tdp1_l[0]][tdp1_l[1]] = "#"
                            self.play_field[tdp2_l[0]][tdp2_l[1]] = "#"

                            self.set_space_around_deck(tdp1_l)
                            self.set_space_around_deck(tdp2_l)

                            self.max_two_deck += 1
                            self.set_pos(self.two_deck_pos1, self.two_deck_pos2)

                            self.two_deck_pos1, self.two_deck_pos2, self.count_deck = None, None, 0
                            return

                        else:
                            self.count_deck += 1
                            self.two_deck_pos1 = f"{i}:{self.letters_small.find(j)}"
