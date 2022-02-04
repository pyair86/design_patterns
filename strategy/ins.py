from navigation_abstract import NavigationAbstract


class INS(NavigationAbstract):

    def navigate(self):
        print("using Inertial Measurement Unit")
