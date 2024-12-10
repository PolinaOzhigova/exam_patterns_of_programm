from abc import ABC, abstractmethod

class BaseModel(ABC):
    @abstractmethod
    def create(self):
        pass