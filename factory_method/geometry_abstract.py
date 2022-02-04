from abc import abstractmethod, ABCMeta


class IGeometry(metaclass=ABCMeta):

    @abstractmethod
    def draw(self):
        pass
