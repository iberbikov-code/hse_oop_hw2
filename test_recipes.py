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


def test_recipe_creation():
    """Проверка инициализации рецепта"""
    ing=Ingredient("Мука",500,"г")
    recipe=Recipe("Пицца",[ing])
    assert recipe.title=="Пицца"
    assert len(recipe.ingredients)==1
def test_add_ingredient():
    """Проверка добавления и суммирования ингредиентов"""
    recipe=Recipe("Пицца")
    recipe.add_ingredient(Ingredient("Мука",500,"г"))
    recipe.add_ingredient(Ingredient("Мука",200,"г"))
    recipe.add_ingredient(Ingredient("Сыр",100,"г"))
    
    assert len(recipe.ingredients)==2 
    assert recipe.ingredients[0].quantity==700.0
def test_scale():
    """Проверка масштабирования рецепта"""
    recipe=Recipe("Пицца",[Ingredient("Мука",100,"г")])
    scaled =recipe.scale(2)
    
    assert scaled is not recipe
    assert scaled.ingredients[0].quantity==200.0
    assert recipe.ingredients[0].quantity==100.0 
def test_scale_invalid_ratio():
    """Проверка выброса исключения при неверном коэффициенте"""
    recipe= Recipe("Пицца",[Ingredient("Мука",100,"г")])
    with pytest.raises(ValueError):
        recipe.scale(0)
    with pytest.raises(ValueError):
        recipe.scale(-1)
def test_recipe_len():
    """Проверка метода __len__"""
    recipe =Recipe("Пицца",[
        Ingredient("Мука",100,"г"),
        Ingredient("Сыр",50,"г")
    ])
    assert len(recipe)==2



def test_add_recipe():
    """Проверка добавления рецепта в список покупок"""
    recipe=Recipe("Пицца",[Ingredient("Мука",100,"г")])
    sl=ShoppingList()
    sl.add_recipe(recipe,2)
    items=sl.get_list()
    assert len(items)== 1
    assert items[0].quantity ==200.0

def test_add_recipe_invalid_portions():
    """Проверка выброса исключения при порциях <= 0"""
    recipe=Recipe("Пицца",[Ingredient("Мука",100,"г")])
    sl=ShoppingList()
    with pytest.raises(ValueError):
        sl.add_recipe(recipe,0)
    with pytest.raises(ValueError):
        sl.add_recipe(recipe,-1)

def test_remove_recipe():
    """Проверка удаления рецепта из списка"""
    recipe=Recipe("Пицца",[Ingredient("Мука",100,"г")])
    sl=ShoppingList()
    sl.add_recipe(recipe,1)
    sl.remove_recipe("Пицца")
    assert len(sl.get_list())==0
    sl.remove_recipe("Борщ")

def test_get_list():
    """Проверка суммирования и сортировки итогового списка"""
    r1=Recipe("Пицца",[Ingredient("Мука",100,"г")])
    r2=Recipe("Хлеб",[Ingredient("Мука",200,"г"),Ingredient("Дрожжи",1,"шт")])
    sl=ShoppingList()
    sl.add_recipe(r1,1)
    sl.add_recipe(r2,1)
    items =sl.get_list()
    flour =next(i for i in items if i.name=="Мука")
    assert flour.quantity==300.0
    assert items[0].name=="Дрожжи"
    assert items[1].name=="Мука"

def test_add_operator():
    """Проверка объединения двух списков покупок через +"""
    sl1=ShoppingList()
    sl1.add_recipe(Recipe("A",[Ingredient("X",1,"шт")]),1)
    sl2=ShoppingList()
    sl2.add_recipe(Recipe("B",[Ingredient("Y",2,"шт")]),1)
    combined=sl1+sl2
    assert len(combined.get_list())==2
    assert len(sl1.get_list())==1
    assert len(sl2.get_list())==1