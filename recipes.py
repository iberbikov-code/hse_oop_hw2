class Ingredient:
    def __init__(self,name:str,quantity: float,unit:str):
        self.name=name
        self.unit=unit
        self.quantity=quantity  
    @property
    def quantity(self)->float:
        return self._quantity
    @quantity.setter
    def quantity(self,value):
        if not isinstance(value,(int,float)) or value<=0:
            raise ValueError("Количество должно быть положительным")
        self._quantity=float(value)
    def __str__(self)->str:
        return f"{self.name}:{self.quantity}{self.unit}"

    def __repr__(self)->str:
        return f"Ingredient('{self.name}',{self.quantity},'{self.unit}')"

    def __eq__(self, other)->bool:
        if not isinstance(other,Ingredient):
            return False
        return self.name==other.name and self.unit==other.unit