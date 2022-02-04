from geometry_abstract import IGeometry


class Polygon(IGeometry):

    def __init__(self):
        self.shape = "polygon"

    def draw(self):
        print(f"drawing {self.shape}")
