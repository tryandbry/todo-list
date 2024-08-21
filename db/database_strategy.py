from abc import ABC, abstractmethod


class DatabaseStrategy(ABC):
    @abstractmethod
    def database_uri(self):
        pass

    @abstractmethod
    def test_database_uri(self):
        pass
