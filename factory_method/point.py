from geometry_abstract import IGeometry


class Point(IGeometry):

    def __init__(self):
        self.shape = "point"

    def draw(self):
        print(f"drawing {self.shape}")
