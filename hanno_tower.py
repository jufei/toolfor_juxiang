import copy
import sys

step_count = 1


class c_tower(object):
    def __init__(self, name, plates_count):
        self.plates_count = plates_count
        self.name = name
        if plates_count > 0:
            self.plates_list = range(1, plates_count + 1)
        else:
            self.plates_list = []

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

    def move_out(self):
        if self.plates_list:
            plate = self.plates_list[0]
            self.plates_list = self.plates_list[1:]
            self.plates_count -= 1
            return plate
        else:
            return -1

    def move_in(self, plate):
        self.plates_list = [plate] + self.plates_list
        self.plates_count += 1


def move_plate(from_tower, to_tower):
    global step_count
    to_tower.move_in(from_tower.move_out())
    print('Step: {}  {} -> {}'.format(step_count, from_tower, to_tower))
    step_count += 1


def move_2_plate(from_tower, to_tower, buffer_tower):
    move_plate(from_tower, buffer_tower)
    move_plate(from_tower, to_tower)
    move_plate(buffer_tower, to_tower)


def move_n_plate(from_tower, to_tower, buffer_tower, n):
    if n == 1:
        move_plate(from_tower, to_tower)
    elif n == 2:
        move_2_plate(from_tower, to_tower, buffer_tower)
    else:
        move_n_plate(from_tower, buffer_tower, to_tower, n - 1)
        move_plate(from_tower, to_tower)
        move_n_plate(buffer_tower, to_tower, from_tower, n - 1)


if __name__ == '__main__':
    total = int(sys.argv[1])
    ta = c_tower('A', total)
    tb = c_tower('B', 0)
    tc = c_tower('C', 0)

    move_n_plate(ta, tc, tb, total)
    # print(ta.plates_list)
    # print(tb.plates_list)
    # print(tc.plates_list)
