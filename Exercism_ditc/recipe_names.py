def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: dict - dictionary with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """

    # for name in ideas:
    #     if name in recipe_updates:
    #         ideas[name].update(recipe_updates[name])
      # or 
    for name, updates in recipe_updates.items(): 
      if name in ideas: 
        ideas[name].update(updates)
      else:
        ideas[name] = updates 
    print(ideas)

    return ideas
  
ideas = {'Banana Bread' : {'Banana': 1, 'Apple': 1, 'Walnuts': 1, 'Flour': 1, 'Eggs': 2, 'Butter': 1},
                  'Raspberry Pie' : {'Raspberry': 1, 'Orange': 1, 'Pie Crust': 1, 'Cream Custard': 1}}
recipe_updates = {'Banana Bread' : {'Banana': 2, 'Apple': 1, 'Walnuts': 1, 'Flour': 1, 'Eggs': 2, 'Butter': 1}}

update_recipes(ideas, recipe_updates)