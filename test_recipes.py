import pytest
from recipes import Ingredient,Recipe,ShoppingList,DietaryRecipe
def test_ingredient_creation():
    """Проверка, что атрибуты правильно инициализируются"""
    ing= Ingredient("Мука",500,"г")
    assert ing.name=="Мука"
    assert ing.quantity==500.0
    assert ing.unit=="г"
def test_ingredient_str():
    """Проверка метода __str__"""
    ing =Ingredient("Мука",500,"г")
    assert str(ing)== "Мука: 500.0 г"
def test_ingredient_eq():
    """Проверка метода __eq__"""
    ing1=Ingredient("Мука",500,"г")
    ing2=Ingredient("Мука",200,"г") 
    ing3=Ingredient("Сахар",500,"г")
    ing4=Ingredient("Мука",500,"кг")

    assert ing1==ing2 
    assert ing1!=ing3 
    assert ing1!=ing4 