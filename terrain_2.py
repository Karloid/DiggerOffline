class Terrain(object):
    hp = 100
    pass

    def isAccessible(self):
        return self.hp == 0

    @staticmethod
    def color():
        pass


class EmptySpace(Terrain):
    hp = 0

    @staticmethod
    def color():
        return "#2196F3"


class Humus(Terrain):
    @staticmethod
    def color():
        return "#795548"


class Sand(Terrain):
    @staticmethod
    def color():
        return "#FFC107"


class Diorite(Terrain):
    @staticmethod
    def color():
        return "#9E9E9E"


class Tree(Terrain):
    @staticmethod
    def color():
        return "#4CAF50"
