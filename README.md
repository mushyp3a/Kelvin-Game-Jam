# please do not comprehend this code.

## json structure :3

* Ingredients
  * Ingredient1
    * Heater
      * (null / ingredient produced)
    * Extractor
      * (null / ingredient produced)
    * Grinder
      * (null / ingredient produced)
* Recipes
  * Item1
    * [ingredient1, ingredient2]

### Ingredients Example
dictionary["Ingredients"]["Ingredient1"]["Heater"] == "Ingredient2"

dictionary["Ingredients"]["Ingredient1"]["Grinder"] == null

### Recipes Example

dictionary["Recipes"]["Item1"] = ["Item1", "Item2"]

dictionary["Recipes"]["Item1"][0] == "Item1"
