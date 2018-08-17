def test_recipe (food_1, food_2):
  return food_1 + " a la " + food_2

food_1 = "pasta"
food_2 = "carbonara"
recipe = test_recipe(food_1, food_2)
print("Eat " + recipe + "!")


def test_dog (dog_1, dog_2):
    return dog_1 + " korsad med " + dog_2

dog_1="cocker spaniel"
dog_2="pudel"
blandras=test_dog(dog_1, dog_2)
print("En "+ blandras + " kallas för cockapoo.")