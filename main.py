

class Vacuum:

    def __init__(self, movements=[], obstacles = []):
        self.max_coordiate= (0, 0)
        # current direction can be N:(0,1), E:(1,0),S:(0,-1), W:(-1,0),
        self.current_direction = (0         ,1)
        self.movements = movements
        self.obstacles = obstacles

    def elucidian_distance(self):
        return self.max_coordiate[0]**2 + self.max_coordiate[1] ** 2

    def vacuum_movements(self):

        for movement in self.movements:

            if movement = -1:
                if self.current_direction = 1:


            if movement = -2:
                pass

            if movement <= 9 and movement >= 1:
                pass




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    vacuum_movements()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
