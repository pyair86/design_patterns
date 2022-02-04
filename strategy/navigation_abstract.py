from abc import ABC, abstractmethod


# could be INavigation as well
class NavigationAbstract(ABC):

    @abstractmethod
    def navigate(self):
        pass
