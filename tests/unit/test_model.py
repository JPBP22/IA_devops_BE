from api.models import Recipe
import pytest

def test_create_recipe():
    """
    GIVEN a Recipe model
    WHEN a new Recipe is created
    THEN check the name, ingredients, steps, rating and favorite fields are defined correctly
    """
    recipe = Recipe('Pop tart', 'Large Eggs, Salt, Butter', 'C, serve', 5, True)
    assert recipe.name == 'Pop tart'
    assert recipe.ingredients == 'Large Eggs, Salt, Butter, Cinammon, Flour'
    assert recipe.steps == 'Crack eggs, pour eggs,mix with flower, put into oven at 250, bake 10 minutes, bring out, put cinamon, cool down'
    assert recipe.rating == 3
    assert recipe.favorite == True
