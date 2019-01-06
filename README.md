# household-inventory
Household inventory system

## pantry
The "pantry" superclass lets you add things, consume things, consolidate things (i.e., two half-used boxes of crackers means you have the equivalent of one full box of crackers), build a shopping list, and then clear the shopping list.

There are currently two pantry types - a FoodPantry and a SupplyCloset.

## thing
The "thing" superclass is used to define items. For the FoodPantry, a Grocery class is used, whereas for the SupplyCloset a Supply class is used. Each class defines its own categories (dry goods, produce, cleaning supplies, etc.) and units (box, jar, tub, can, etc.)

## To-Do
- [ ]Add GUI interface via Flask app<br>
- [ ]Add additional "pantry" and "thing" types
- [ ]Add some sort of backend storage, either a database or flat files
