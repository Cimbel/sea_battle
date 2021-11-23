class BuildFiled:
    _char = "@"
    play_field = []
    _letters = "ABCDEFGHIJ "
    letters_small = " abcdefghij"
    accessible_position = []
    position_of_ships = {
        "one_deck_ships": {},
        "two_deck_ships": {},
        "three_deck_ships": {},
        "four_deck_ship": {}
    }

    def set_space_around_deck(self, list_pos):
        """
        Set '-' chars around deck

        :param list_pos: list type, list of two integers
        :return: None
        """
        deck_pos_list = [f"{list_pos[0] + 1}:{list_pos[1]}", f"{list_pos[0] - 1}:{list_pos[1]}",
                         f"{list_pos[0]}:{list_pos[1] - 1}", f"{list_pos[0]}:{list_pos[1] + 1}",
                         f"{list_pos[0] + 1}:{list_pos[1] + 1}", f"{list_pos[0] - 1}:{list_pos[1] - 1}",
                         f"{list_pos[0] + 1}:{list_pos[1] - 1}", f"{list_pos[0] - 1}:{list_pos[1] + 1}"]

        # dp - deck position
        for dp in range(len(deck_pos_list)):
            # temporary list of position
            tmp_l = list(map(int, deck_pos_list[dp].split(":")))
            try:

                if self.play_field[tmp_l[0]][tmp_l[1]] == "@":
                    self.play_field[tmp_l[0]][tmp_l[1]] = "-"

            # when position is out of map
            except IndexError:
                continue

    def fill_field(self):
        """
        Create play field(matrix 11x11)

        :return: None
        """
        for i in range(11):
            self.play_field.append([])
            for j in range(11):
                if i == 0 and j == 0:
                    self.play_field[i].append(" ")

                if i > 0 and j == 0:
                    self.play_field[i].append(i)

                if i == 0:
                    self.play_field[i].append(self._letters[j])
                else:
                    self.play_field[i].append(self._char)

    def print_field(self):
        for i in range(11):
            for j in range(11):
                if j == 10:
                    print(self.play_field[i][j], end=" ")
                else:
                    if i == 10 and j == 0:
                        print(self.play_field[i][j], end=" ")
                    else:
                        print(self.play_field[i][j], end="  ")
            print("")

    # fill available positions(ships)
    def fill_pos(self):
        """
        Fill all possible position in upper and lower
        case, also in reverse sequence (6H, 6h, h6, H6)

        :return: None
        """
        for i in range(11):
            if i == 0:
                pass
            else:
                for j in self.letters_small:
                    if j != " ":
                        self.accessible_position.append(f"{j.lower()}{i}")
                        self.accessible_position.append(f"{j.upper()}{i}")
                        self.accessible_position.append(f"{i}{j.lower()}")
                        self.accessible_position.append(f"{i}{j.upper()}")
