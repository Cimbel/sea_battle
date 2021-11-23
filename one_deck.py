import class_field
import exceptions_and_errors as err


class OneDeck(class_field.BuildFiled):
    max_one_deck = 0

    def __init__(self):
        self.play_field = []
        self.accessible_position = []
        self.position_of_ships = {
            "one_deck_ships": {},
            "two_deck_ships": {},
            "three_deck_ships": {},
            "four_deck_ship": {}
        }

    # set position of one deck ship to dict
    def set_pos(self, num, char):
        """
        Set position of one deck ship in dictionary

        :param num: int type
        :param char: int type
        :return: None
        """
        if self.max_one_deck == 1:
            self.position_of_ships["one_deck_ships"]["first_one_deck"] = f"{num}:{char}"
        elif self.max_one_deck == 2:
            self.position_of_ships["one_deck_ships"]["second_one_deck"] = f"{num}:{char}"
        elif self.max_one_deck == 3:
            self.position_of_ships["one_deck_ships"]["third_one_deck"] = f"{num}:{char}"
        elif self.max_one_deck == 4:
            self.position_of_ships["one_deck_ships"]["fourth_one_deck"] = f"{num}:{char}"

    def is_deck_pos_valid(self, deck_pos_l):
        """
        :param deck_pos_l: list type, list of two integer
        :return: None
        """
        if self.play_field[deck_pos_l[0]][deck_pos_l[1]] == "-":
            raise err.WrongPosOneDeck
        elif self.play_field[deck_pos_l[0]][deck_pos_l[1]] == "#":
            raise err.PosIsBusy

    def set_one_deck(self, pos):
        """
        Set '#' on play field (matrix 11x11)

        :param pos: string type, position of one deck ship
                    must be like "h1:h1"
        :return: None
        """
        for num in range(11):
            for char in self.letters_small:
                # set ships and space around them
                if pos.lower() == f"{num}{char}" or pos.lower() == f"{char}{num}":
                    one_deck_pos_l = [num, self.letters_small.find(char)]
                    self.is_deck_pos_valid(one_deck_pos_l)
                    self.play_field[num][self.letters_small.find(char)] = "#"
                    self.set_space_around_deck(one_deck_pos_l)
                    self.max_one_deck += 1
                    self.set_pos(num, self.letters_small.find(char))
                    return
