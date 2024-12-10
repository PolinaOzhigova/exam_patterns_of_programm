from base_model import BaseModel

class WarehouseModel(BaseModel):
    __address:str = ""

    """
    Наименование
    """
    @property
    def address(self) -> str:
        return self.__address
    
    @address.setter
    def address(self, value:str):
        self.__address = value.strip()


    """
    Фабричный метод
    """
    @staticmethod
    def create(address:str):
        item = WarehouseModel()
        item.address = address
        return item
