from base_model import BaseModel

class OrganizationModel(BaseModel):
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
        item = OrganizationModel()
        item.name = name
        return item