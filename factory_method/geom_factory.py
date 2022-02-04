from polygon import Polygon
from point import Point


class GeomFactory:

    @staticmethod
    def build_geom(geom_type):
        if geom_type == "point":
            return Point()
        elif geom_type == "polygon":
            return Polygon()
        else:
            print("no valid geom")

