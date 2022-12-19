from api.models import Recipe
import pytest

def test_create_recipe():
    """
    GIVEN a Recipe model
    WHEN a new Recipe is created
    THEN check the name, ingredients, steps, rating and favorite fields are defined correctly
    """
    recipe = Recipe('Pop tart', 'Large Eggs, Salt, Butter, Cinammon, Flour', 'Crack eggs, pour eggs, mix with flower, put into oven, bake ten minutes, bring out, put cinamon, cool down', 3, True)
    assert recipe.name == 'Pop tart'
    assert recipe.ingredients == 'Large Eggs, Salt, Butter, Cinammon, Flour'
    assert recipe.steps == 'Crack eggs, pour eggs, mix with flower, put into oven, bake ten minutes, bring out, put cinamon, cool down'
    assert recipe.rating == 3
    assert recipe.favorite == True
