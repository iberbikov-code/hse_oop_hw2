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
        return f"{self.name}: {self.quantity} {self.unit}"

    def __repr__(self)->str:
        return f"Ingredient('{self.name}',{self.quantity},'{self.unit}')"

    def __eq__(self, other)->bool:
        if not isinstance(other,Ingredient):
            return False
        return self.name==other.name and self.unit==other.unit
class Recipe:
    def __init__(self,title:str,ingredients:list=None):
        self.title =title
        self.ingredients=ingredients if ingredients is not None else []
    def add_ingredient(self,ingredient:'Ingredient'):
        for existing in self.ingredients:
            if existing==ingredient:
                existing.quantity+=ingredient.quantity
        self.ingredients.append(ingredient)
    @staticmethod
    def is_valid_ratio(ratio):
        return isinstance(ratio,(int,float))and ratio>0
    def scale(self,ratio:float)->'Recipe':
        new_ingredients=[
            Ingredient(ing.name,ing.quantity*ratio,ing.unit) 
            for ing in self.ingredients
        ]
        return Recipe(self.title,new_ingredients)
    def __len__(self):
        return len(self.ingredients)
    def __str__(self):
        ing_strs="\n".join([f" -{ing}" for ing in self.ingredients])
        return f"Рецепт:{self.title}\nИнгредиенты:\n{ing_strs}"
class ShoppingList:
    def __init__(self):
        self._items=[]
    def add_recipe(self, recipe:'Recipe',portions:float):
        if portions<=0:
            raise ValueError("Количество порций должно быть положительным")
        scaled_recipe=recipe.scale(portions)
        for ingredient in scaled_recipe.ingredients:
            self._items.append((ingredient,recipe.title))
    def remove_recipe(self,title:str):
        self._items=[(ing,rec_title)for ing, rec_title in self._items if rec_title!=title]
    def get_list(self)->list:
        summary ={}
        for ingredient,_ in self._items:
            key= (ingredient.name,ingredient.unit)
            if key in summary:
                summary[key]+=ingredient.quantity
            else:
                summary[key]=ingredient.quantity
        result=[
            Ingredient(name,quantity,unit) 
            for (name,unit),quantity in summary.items()
        ]
        result.sort(key=lambda x:x.name)
        return result
    def __add__(self,other:'ShoppingList')->'ShoppingList':
        new_list=ShoppingList()
        new_list._items=self._items+other._items
        return new_list
class DietaryRecipe(Recipe):
    def __init__(self,title:str,diet_type:str,ingredients:list=None):
        super().__init__(title,ingredients)
        self.diet_type=diet_type
    def scale(self,ratio:float)->'DietaryRecipe':
        scaled_parent=super().scale(ratio)
        return DietaryRecipe(scaled_parent.title,self.diet_type,scaled_parent.ingredients)
    def __str__(self):
        parent_str=super().__str__()
        return f"[{self.diet_type}]{parent_str}"