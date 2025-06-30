# Ingredients Checker

# 1: Define ingredients
recipe_ingredients = {"flour", "sugar", "butter", "eggs", "milk"}

# 2: Get user input 
user_input = input("Enter the ingredients you have (separat by comma): ")
user_ingredients = set(user_input.split(", "))

# 3: Compare 
ingredients_missing = recipe_ingredients - user_ingredients
extra_ingredients = user_ingredients - recipe_ingredients

# 4: Display Results
print("\n RESULT")
if ingredients_missing:
    print(f"You are missing the these ingredients: {', '.join(ingredients_missing)}")
else:
    print("You have all the ingredients needed.")

if extra_ingredients:
    print(f"You have extra ingredients: {', '.join(extra_ingredients)}")
else:
    print("You have all the ingredients needed.")