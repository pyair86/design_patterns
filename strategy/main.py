from decide_navigation import DecideNavigation
from gnss import GNSS
from ins import INS

if __name__ == "__main__":

    navigation_system = DecideNavigation(GNSS())
    navigation_system.navigate()

    navigation_system.strategy = INS()
    navigation_system.navigate()