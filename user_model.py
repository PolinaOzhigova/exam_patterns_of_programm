from base_model import BaseModel

class UserModel(BaseModel):
    __name:str = ""

    """
    Наименование
    """
    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, value:str):
        self.__name = value.strip()


    """
    Фабричный метод
    """
    @staticmethod
    def create(name:str):
        item = UserModel()
        item.name = name
        return item