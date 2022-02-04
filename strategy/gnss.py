from navigation_abstract import NavigationAbstract


class GNSS(NavigationAbstract):

    def navigate(self):
        print("using GPS, GLONASS...")
