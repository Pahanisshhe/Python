class Triangle(object):

    def __init__(self, v1, v2, v3):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3

    def move(self, x, y):
        self.v1[0] += x
        self.v2[0] += x
        self.v3[0] += x
        self.v1[1] += y
        self.v2[1] += y
        self.v3[1] += y

    def info(self):
        print(self.v1, self.v2, self.v3)


class Tetragon(object):

    def __init__(self, v1, v3):
        self.v1 = v1
        self.v3 = v3

    def move(self, x, y):
        self.v1[0] += x
        self.v3[0] += x
        self.v1[1] += y
        self.v3[1] += y

    def info(self):
        print(self.v1, self.v3)


def is_intersect(triangle: Triangle, tetragon: Tetragon):
    f_in = f_out = False
    for i in triangle.__dict__.values():
        if tetragon.v1[0] < i[0] < tetragon.v3[0] and tetragon.v1[1] < i[1] < tetragon.v3[1]:
            f_in = True
        if (tetragon.v1[0] > i[0] or i[0] > tetragon.v3[0]) or (tetragon.v1[1] > i[1] or i[1] > tetragon.v3[1]):
            f_out = True
    if f_in and f_out:
        return True
    else:
        return False


triangle = Triangle([1, 1], [2, 7], [6, 3])
tetragon = Tetragon([0, 0], [5, 4])
triangle.info()
tetragon.info()

print(is_intersect(triangle, tetragon))
