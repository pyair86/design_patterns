from geom_factory import GeomFactory

if __name__ == "__main__":

    geom1 = GeomFactory.build_geom("point")
    geom1.draw()
    geom2 = GeomFactory.build_geom("polygon")
    geom2.draw()
