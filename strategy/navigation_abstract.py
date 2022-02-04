from abc import ABC, abstractmethod


class NavigationAbstract(ABC):

    @abstractmethod
    def navigate(self):
        pass
