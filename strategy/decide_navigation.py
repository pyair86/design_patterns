from navigation_abstract import NavigationAbstract


class DecideNavigation:

    def __init__(self, navigation_strategy: NavigationAbstract) -> None:
        self.navigation_strategy = navigation_strategy

    @property
    def strategy(self) -> NavigationAbstract:
        return self.navigation_strategy

    @strategy.setter
    def strategy(self, strategy: NavigationAbstract) -> None:
        self.navigation_strategy = strategy

    def navigate(self) -> None:
        self.navigation_strategy.navigate()
