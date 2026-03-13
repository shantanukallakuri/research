import json

# ══════════════════════════════════════════════════════════════════════════════
# foods.py — Nutrition database for the interactive chart
# All values are per 100g of the food as commonly consumed.
# Structure per entry:
#   "grams"    → macronutrients in grams (Protein, Carbs, Fat, Fiber)
#   "minerals" → vitamins & minerals in mg or mcg
#   "calories" → energy in kcal
#   "category" → used by JS to group foods in the selector grid
# Sources: USDA FoodData Central, NIH nutritional references
# ══════════════════════════════════════════════════════════════════════════════

FOODS = {

  # ── FRUITS ──────────────────────────────────────────────────────────────────
  "Apple":          {"category":"Fruit",     "grams":{"Protein (g)":0.3,  "Carbs (g)":14.0, "Fat (g)":0.2,  "Fiber (g)":2.4},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":0.1,  "Calcium (mg)":6.0,   "Vit C (mg)":4.6,  "Potassium (mg)":107.0},  "calories":52.0},
  "Apricot":        {"category":"Fruit",     "grams":{"Protein (g)":1.4,  "Carbs (g)":11.1, "Fat (g)":0.4,  "Fiber (g)":2.0},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":0.4,  "Calcium (mg)":13.0,  "Vit C (mg)":10.0, "Potassium (mg)":259.0},  "calories":48.0},
  "Avocado":        {"category":"Fruit",     "grams":{"Protein (g)":2.0,  "Carbs (g)":9.0,  "Fat (g)":15.0, "Fiber (g)":6.7},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":0.6,  "Calcium (mg)":12.0,  "Vit C (mg)":10.0, "Potassium (mg)":485.0},  "calories":160.0},
  "Banana":         {"category":"Fruit",     "grams":{"Protein (g)":1.1,  "Carbs (g)":23.0, "Fat (g)":0.3,  "Fiber (g)":2.6},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":0.3,  "Calcium (mg)":5.0,   "Vit C (mg)":8.7,  "Potassium (mg)":358.0},  "calories":89.0},
  "Blackberry":     {"category":"Fruit",     "grams":{"Protein (g)":1.4,  "Carbs (g)":10.2, "Fat (g)":0.5,  "Fiber (g)":5.3},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":0.6,  "Calcium (mg)":29.0,  "Vit C (mg)":21.0, "Potassium (mg)":162.0},  "calories":43.0},
  "Blueberry":      {"category":"Fruit",     "grams":{"Protein (g)":0.7,  "Carbs (g)":14.0, "Fat (g)":0.3,  "Fiber (g)":2.4},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":0.3,  "Calcium (mg)":6.0,   "Vit C (mg)":9.7,  "Potassium (mg)":77.0},   "calories":57.0},
  "Cherry":         {"category":"Fruit",     "grams":{"Protein (g)":1.1,  "Carbs (g)":16.0, "Fat (g)":0.3,  "Fiber (g)":2.1},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":0.4,  "Calcium (mg)":13.0,  "Vit C (mg)":7.0,  "Potassium (mg)":222.0},  "calories":63.0},
  "Coconut":        {"category":"Fruit",     "grams":{"Protein (g)":3.3,  "Carbs (g)":15.2, "Fat (g)":33.5, "Fiber (g)":9.0},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":2.4,  "Calcium (mg)":14.0,  "Vit C (mg)":3.3,  "Potassium (mg)":356.0},  "calories":354.0},
  "Cranberry":      {"category":"Fruit",     "grams":{"Protein (g)":0.4,  "Carbs (g)":12.2, "Fat (g)":0.1,  "Fiber (g)":4.6},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":0.3,  "Calcium (mg)":8.0,   "Vit C (mg)":13.3, "Potassium (mg)":85.0},   "calories":46.0},
  "Date":           {"category":"Fruit",     "grams":{"Protein (g)":1.8,  "Carbs (g)":75.0, "Fat (g)":0.2,  "Fiber (g)":6.7},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":1.0,  "Calcium (mg)":39.0,  "Vit C (mg)":0.4,  "Potassium (mg)":696.0},  "calories":277.0},
  "Fig":            {"category":"Fruit",     "grams":{"Protein (g)":0.8,  "Carbs (g)":19.2, "Fat (g)":0.3,  "Fiber (g)":2.9},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":0.4,  "Calcium (mg)":35.0,  "Vit C (mg)":2.0,  "Potassium (mg)":232.0},  "calories":74.0},
  "Grape":          {"category":"Fruit",     "grams":{"Protein (g)":0.7,  "Carbs (g)":18.0, "Fat (g)":0.2,  "Fiber (g)":0.9},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":0.4,  "Calcium (mg)":10.0,  "Vit C (mg)":3.2,  "Potassium (mg)":191.0},  "calories":69.0},
  "Grapefruit":     {"category":"Fruit",     "grams":{"Protein (g)":0.8,  "Carbs (g)":11.0, "Fat (g)":0.1,  "Fiber (g)":1.6},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":0.1,  "Calcium (mg)":22.0,  "Vit C (mg)":31.2, "Potassium (mg)":135.0},  "calories":42.0},
  "Guava":          {"category":"Fruit",     "grams":{"Protein (g)":2.6,  "Carbs (g)":14.3, "Fat (g)":1.0,  "Fiber (g)":5.4},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":0.3,  "Calcium (mg)":18.0,  "Vit C (mg)":228.3,"Potassium (mg)":417.0},  "calories":68.0},
  "Kiwi":           {"category":"Fruit",     "grams":{"Protein (g)":1.1,  "Carbs (g)":15.0, "Fat (g)":0.5,  "Fiber (g)":3.0},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":0.3,  "Calcium (mg)":34.0,  "Vit C (mg)":92.7, "Potassium (mg)":312.0},  "calories":61.0},
  "Lemon":          {"category":"Fruit",     "grams":{"Protein (g)":1.1,  "Carbs (g)":9.3,  "Fat (g)":0.3,  "Fiber (g)":2.8},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":0.6,  "Calcium (mg)":26.0,  "Vit C (mg)":53.0, "Potassium (mg)":138.0},  "calories":29.0},
  "Lychee":         {"category":"Fruit",     "grams":{"Protein (g)":0.8,  "Carbs (g)":16.5, "Fat (g)":0.4,  "Fiber (g)":1.3},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":0.3,  "Calcium (mg)":5.0,   "Vit C (mg)":71.5, "Potassium (mg)":171.0},  "calories":66.0},
  "Mango":          {"category":"Fruit",     "grams":{"Protein (g)":0.8,  "Carbs (g)":15.0, "Fat (g)":0.4,  "Fiber (g)":1.6},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":0.2,  "Calcium (mg)":11.0,  "Vit C (mg)":36.4, "Potassium (mg)":168.0},  "calories":60.0},
  "Melon":          {"category":"Fruit",     "grams":{"Protein (g)":0.8,  "Carbs (g)":8.2,  "Fat (g)":0.2,  "Fiber (g)":0.9},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":0.2,  "Calcium (mg)":9.0,   "Vit C (mg)":36.7, "Potassium (mg)":267.0},  "calories":34.0},
  "Orange":         {"category":"Fruit",     "grams":{"Protein (g)":0.9,  "Carbs (g)":12.0, "Fat (g)":0.1,  "Fiber (g)":2.4},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":0.1,  "Calcium (mg)":40.0,  "Vit C (mg)":53.2, "Potassium (mg)":181.0},  "calories":47.0},
  "Papaya":         {"category":"Fruit",     "grams":{"Protein (g)":0.5,  "Carbs (g)":11.0, "Fat (g)":0.3,  "Fiber (g)":1.7},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":0.3,  "Calcium (mg)":20.0,  "Vit C (mg)":60.9, "Potassium (mg)":182.0},  "calories":43.0},
  "Passion Fruit":  {"category":"Fruit",     "grams":{"Protein (g)":2.2,  "Carbs (g)":23.4, "Fat (g)":0.7,  "Fiber (g)":10.4}, "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":1.6,  "Calcium (mg)":12.0,  "Vit C (mg)":30.0, "Potassium (mg)":348.0},  "calories":97.0},
  "Peach":          {"category":"Fruit",     "grams":{"Protein (g)":0.9,  "Carbs (g)":10.0, "Fat (g)":0.3,  "Fiber (g)":1.5},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":0.3,  "Calcium (mg)":6.0,   "Vit C (mg)":6.6,  "Potassium (mg)":190.0},  "calories":39.0},
  "Pear":           {"category":"Fruit",     "grams":{"Protein (g)":0.4,  "Carbs (g)":15.0, "Fat (g)":0.1,  "Fiber (g)":3.1},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":0.2,  "Calcium (mg)":9.0,   "Vit C (mg)":4.3,  "Potassium (mg)":116.0},  "calories":57.0},
  "Pineapple":      {"category":"Fruit",     "grams":{"Protein (g)":0.5,  "Carbs (g)":13.0, "Fat (g)":0.1,  "Fiber (g)":1.4},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":0.3,  "Calcium (mg)":13.0,  "Vit C (mg)":47.8, "Potassium (mg)":109.0},  "calories":50.0},
  "Plum":           {"category":"Fruit",     "grams":{"Protein (g)":0.7,  "Carbs (g)":11.4, "Fat (g)":0.3,  "Fiber (g)":1.4},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":0.2,  "Calcium (mg)":6.0,   "Vit C (mg)":9.5,  "Potassium (mg)":157.0},  "calories":46.0},
  "Pomegranate":    {"category":"Fruit",     "grams":{"Protein (g)":1.7,  "Carbs (g)":19.0, "Fat (g)":1.2,  "Fiber (g)":4.0},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":0.3,  "Calcium (mg)":10.0,  "Vit C (mg)":10.2, "Potassium (mg)":236.0},  "calories":83.0},
  "Raspberry":      {"category":"Fruit",     "grams":{"Protein (g)":1.2,  "Carbs (g)":12.0, "Fat (g)":0.7,  "Fiber (g)":6.5},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":0.7,  "Calcium (mg)":25.0,  "Vit C (mg)":26.2, "Potassium (mg)":151.0},  "calories":52.0},
  "Strawberry":     {"category":"Fruit",     "grams":{"Protein (g)":0.7,  "Carbs (g)":8.0,  "Fat (g)":0.3,  "Fiber (g)":2.0},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":0.4,  "Calcium (mg)":16.0,  "Vit C (mg)":58.8, "Potassium (mg)":153.0},  "calories":32.0},
  "Tangerine":      {"category":"Fruit",     "grams":{"Protein (g)":0.8,  "Carbs (g)":13.3, "Fat (g)":0.3,  "Fiber (g)":1.8},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":0.1,  "Calcium (mg)":37.0,  "Vit C (mg)":26.7, "Potassium (mg)":166.0},  "calories":53.0},
  "Watermelon":     {"category":"Fruit",     "grams":{"Protein (g)":0.6,  "Carbs (g)":8.0,  "Fat (g)":0.2,  "Fiber (g)":0.4},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":0.2,  "Calcium (mg)":7.0,   "Vit C (mg)":8.1,  "Potassium (mg)":112.0},  "calories":30.0},

  # ── VEGETABLES ──────────────────────────────────────────────────────────────
  "Artichoke":      {"category":"Vegetable", "grams":{"Protein (g)":3.3,  "Carbs (g)":11.4, "Fat (g)":0.2,  "Fiber (g)":5.4},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":1.3,  "Calcium (mg)":44.0,  "Vit C (mg)":11.7, "Potassium (mg)":370.0},  "calories":47.0},
  "Asparagus":      {"category":"Vegetable", "grams":{"Protein (g)":2.2,  "Carbs (g)":3.9,  "Fat (g)":0.1,  "Fiber (g)":2.1},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":2.1,  "Calcium (mg)":24.0,  "Vit C (mg)":5.6,  "Potassium (mg)":202.0},  "calories":20.0},
  "Beetroot":       {"category":"Vegetable", "grams":{"Protein (g)":1.6,  "Carbs (g)":10.0, "Fat (g)":0.2,  "Fiber (g)":2.8},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":0.8,  "Calcium (mg)":16.0,  "Vit C (mg)":4.9,  "Potassium (mg)":325.0},  "calories":43.0},
  "Bell Pepper":    {"category":"Vegetable", "grams":{"Protein (g)":1.0,  "Carbs (g)":6.0,  "Fat (g)":0.3,  "Fiber (g)":2.1},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":0.4,  "Calcium (mg)":7.0,   "Vit C (mg)":127.7,"Potassium (mg)":211.0},  "calories":31.0},
  "Broccoli":       {"category":"Vegetable", "grams":{"Protein (g)":2.8,  "Carbs (g)":7.0,  "Fat (g)":0.4,  "Fiber (g)":2.6},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":0.7,  "Calcium (mg)":47.0,  "Vit C (mg)":89.2, "Potassium (mg)":316.0},  "calories":34.0},
  "Brussels Sprout":{"category":"Vegetable", "grams":{"Protein (g)":3.4,  "Carbs (g)":9.0,  "Fat (g)":0.3,  "Fiber (g)":3.8},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":1.4,  "Calcium (mg)":42.0,  "Vit C (mg)":85.0, "Potassium (mg)":389.0},  "calories":43.0},
  "Carrot":         {"category":"Vegetable", "grams":{"Protein (g)":0.9,  "Carbs (g)":10.0, "Fat (g)":0.2,  "Fiber (g)":2.8},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":0.3,  "Calcium (mg)":33.0,  "Vit C (mg)":5.9,  "Potassium (mg)":320.0},  "calories":41.0},
  "Cauliflower":    {"category":"Vegetable", "grams":{"Protein (g)":1.9,  "Carbs (g)":5.0,  "Fat (g)":0.3,  "Fiber (g)":2.0},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":0.4,  "Calcium (mg)":22.0,  "Vit C (mg)":48.2, "Potassium (mg)":299.0},  "calories":25.0},
  "Celery":         {"category":"Vegetable", "grams":{"Protein (g)":0.7,  "Carbs (g)":3.0,  "Fat (g)":0.2,  "Fiber (g)":1.6},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":0.2,  "Calcium (mg)":40.0,  "Vit C (mg)":3.1,  "Potassium (mg)":260.0},  "calories":16.0},
  "Cucumber":       {"category":"Vegetable", "grams":{"Protein (g)":0.7,  "Carbs (g)":3.6,  "Fat (g)":0.1,  "Fiber (g)":0.5},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":0.3,  "Calcium (mg)":16.0,  "Vit C (mg)":2.8,  "Potassium (mg)":147.0},  "calories":15.0},
  "Edamame":        {"category":"Vegetable", "grams":{"Protein (g)":11.9, "Carbs (g)":8.9,  "Fat (g)":5.2,  "Fiber (g)":5.2},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":2.3,  "Calcium (mg)":63.0,  "Vit C (mg)":6.1,  "Potassium (mg)":436.0},  "calories":122.0},
  "Garlic":         {"category":"Vegetable", "grams":{"Protein (g)":6.4,  "Carbs (g)":33.0, "Fat (g)":0.5,  "Fiber (g)":2.1},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":1.7,  "Calcium (mg)":181.0, "Vit C (mg)":31.2, "Potassium (mg)":401.0},  "calories":149.0},
  "Kale":           {"category":"Vegetable", "grams":{"Protein (g)":4.3,  "Carbs (g)":9.0,  "Fat (g)":1.5,  "Fiber (g)":3.6},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":1.5,  "Calcium (mg)":150.0, "Vit C (mg)":120.0,"Potassium (mg)":491.0},  "calories":49.0},
  "Leek":           {"category":"Vegetable", "grams":{"Protein (g)":1.5,  "Carbs (g)":14.0, "Fat (g)":0.3,  "Fiber (g)":1.8},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":2.1,  "Calcium (mg)":59.0,  "Vit C (mg)":12.0, "Potassium (mg)":180.0},  "calories":61.0},
  "Lettuce":        {"category":"Vegetable", "grams":{"Protein (g)":1.4,  "Carbs (g)":2.9,  "Fat (g)":0.2,  "Fiber (g)":1.3},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":1.2,  "Calcium (mg)":36.0,  "Vit C (mg)":9.2,  "Potassium (mg)":238.0},  "calories":15.0},
  "Mushroom":       {"category":"Vegetable", "grams":{"Protein (g)":3.1,  "Carbs (g)":3.3,  "Fat (g)":0.3,  "Fiber (g)":1.0},  "minerals":{"Vit B12 (mcg)":0.04, "Iron (mg)":0.5,  "Calcium (mg)":3.0,   "Vit C (mg)":2.1,  "Potassium (mg)":318.0},  "calories":22.0},
  "Onion":          {"category":"Vegetable", "grams":{"Protein (g)":1.1,  "Carbs (g)":9.3,  "Fat (g)":0.1,  "Fiber (g)":1.7},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":0.2,  "Calcium (mg)":23.0,  "Vit C (mg)":7.4,  "Potassium (mg)":146.0},  "calories":40.0},
  "Peas":           {"category":"Vegetable", "grams":{"Protein (g)":5.4,  "Carbs (g)":14.0, "Fat (g)":0.4,  "Fiber (g)":5.1},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":1.5,  "Calcium (mg)":25.0,  "Vit C (mg)":40.0, "Potassium (mg)":244.0},  "calories":81.0},
  "Potato":         {"category":"Vegetable", "grams":{"Protein (g)":2.0,  "Carbs (g)":17.0, "Fat (g)":0.1,  "Fiber (g)":2.2},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":0.8,  "Calcium (mg)":12.0,  "Vit C (mg)":19.7, "Potassium (mg)":425.0},  "calories":77.0},
  "Pumpkin":        {"category":"Vegetable", "grams":{"Protein (g)":1.0,  "Carbs (g)":6.5,  "Fat (g)":0.1,  "Fiber (g)":0.5},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":0.8,  "Calcium (mg)":21.0,  "Vit C (mg)":9.0,  "Potassium (mg)":340.0},  "calories":26.0},
  "Spinach":        {"category":"Vegetable", "grams":{"Protein (g)":2.9,  "Carbs (g)":3.6,  "Fat (g)":0.4,  "Fiber (g)":2.2},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":2.7,  "Calcium (mg)":99.0,  "Vit C (mg)":28.1, "Potassium (mg)":558.0},  "calories":23.0},
  "Sweet Corn":     {"category":"Vegetable", "grams":{"Protein (g)":3.2,  "Carbs (g)":19.0, "Fat (g)":1.2,  "Fiber (g)":2.7},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":0.5,  "Calcium (mg)":2.0,   "Vit C (mg)":6.8,  "Potassium (mg)":270.0},  "calories":86.0},
  "Sweet Potato":   {"category":"Vegetable", "grams":{"Protein (g)":1.6,  "Carbs (g)":20.0, "Fat (g)":0.1,  "Fiber (g)":3.0},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":0.6,  "Calcium (mg)":30.0,  "Vit C (mg)":2.4,  "Potassium (mg)":337.0},  "calories":86.0},
  "Tomato":         {"category":"Vegetable", "grams":{"Protein (g)":0.9,  "Carbs (g)":3.9,  "Fat (g)":0.2,  "Fiber (g)":1.2},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":0.3,  "Calcium (mg)":10.0,  "Vit C (mg)":13.7, "Potassium (mg)":237.0},  "calories":18.0},
  "Turnip":         {"category":"Vegetable", "grams":{"Protein (g)":0.9,  "Carbs (g)":6.4,  "Fat (g)":0.1,  "Fiber (g)":1.8},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":0.3,  "Calcium (mg)":30.0,  "Vit C (mg)":21.0, "Potassium (mg)":191.0},  "calories":28.0},
  "Zucchini":       {"category":"Vegetable", "grams":{"Protein (g)":1.2,  "Carbs (g)":3.1,  "Fat (g)":0.3,  "Fiber (g)":1.0},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":0.4,  "Calcium (mg)":16.0,  "Vit C (mg)":17.9, "Potassium (mg)":261.0},  "calories":17.0},

  # ── NUTS ────────────────────────────────────────────────────────────────────
  "Almonds":        {"category":"Nut",       "grams":{"Protein (g)":21.2, "Carbs (g)":21.7, "Fat (g)":49.4, "Fiber (g)":12.5}, "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":3.7,  "Calcium (mg)":264.0, "Vit C (mg)":0.0,  "Potassium (mg)":733.0},  "calories":579.0},
  "Brazil Nuts":    {"category":"Nut",       "grams":{"Protein (g)":14.3, "Carbs (g)":12.3, "Fat (g)":66.4, "Fiber (g)":7.5},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":2.4,  "Calcium (mg)":160.0, "Vit C (mg)":0.7,  "Potassium (mg)":659.0},  "calories":659.0},
  "Cashews":        {"category":"Nut",       "grams":{"Protein (g)":18.2, "Carbs (g)":30.2, "Fat (g)":43.8, "Fiber (g)":3.3},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":6.7,  "Calcium (mg)":37.0,  "Vit C (mg)":0.5,  "Potassium (mg)":660.0},  "calories":553.0},
  "Hazelnuts":      {"category":"Nut",       "grams":{"Protein (g)":15.0, "Carbs (g)":17.0, "Fat (g)":60.8, "Fiber (g)":9.7},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":4.7,  "Calcium (mg)":114.0, "Vit C (mg)":6.3,  "Potassium (mg)":680.0},  "calories":628.0},
  "Macadamia":      {"category":"Nut",       "grams":{"Protein (g)":7.9,  "Carbs (g)":13.8, "Fat (g)":75.8, "Fiber (g)":8.6},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":3.7,  "Calcium (mg)":85.0,  "Vit C (mg)":1.2,  "Potassium (mg)":368.0},  "calories":718.0},
  "Peanuts":        {"category":"Nut",       "grams":{"Protein (g)":25.8, "Carbs (g)":16.1, "Fat (g)":49.2, "Fiber (g)":8.5},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":4.6,  "Calcium (mg)":92.0,  "Vit C (mg)":0.0,  "Potassium (mg)":705.0},  "calories":567.0},
  "Pecans":         {"category":"Nut",       "grams":{"Protein (g)":9.2,  "Carbs (g)":13.9, "Fat (g)":72.0, "Fiber (g)":9.6},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":2.5,  "Calcium (mg)":70.0,  "Vit C (mg)":1.1,  "Potassium (mg)":410.0},  "calories":691.0},
  "Pine Nuts":      {"category":"Nut",       "grams":{"Protein (g)":13.7, "Carbs (g)":13.1, "Fat (g)":68.4, "Fiber (g)":3.7},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":5.5,  "Calcium (mg)":16.0,  "Vit C (mg)":0.8,  "Potassium (mg)":597.0},  "calories":673.0},
  "Pistachios":     {"category":"Nut",       "grams":{"Protein (g)":20.6, "Carbs (g)":27.7, "Fat (g)":45.4, "Fiber (g)":10.3}, "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":3.9,  "Calcium (mg)":105.0, "Vit C (mg)":5.6,  "Potassium (mg)":1025.0}, "calories":562.0},
  "Walnuts":        {"category":"Nut",       "grams":{"Protein (g)":15.2, "Carbs (g)":13.7, "Fat (g)":65.2, "Fiber (g)":6.7},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":2.9,  "Calcium (mg)":98.0,  "Vit C (mg)":1.3,  "Potassium (mg)":441.0},  "calories":654.0},

  # ── SEEDS ────────────────────────────────────────────────────────────────────
  "Chia Seeds":     {"category":"Seed",      "grams":{"Protein (g)":16.5, "Carbs (g)":42.1, "Fat (g)":30.7, "Fiber (g)":34.4}, "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":7.7,  "Calcium (mg)":631.0, "Vit C (mg)":1.6,  "Potassium (mg)":407.0},  "calories":486.0},
  "Flaxseeds":      {"category":"Seed",      "grams":{"Protein (g)":18.3, "Carbs (g)":28.9, "Fat (g)":42.2, "Fiber (g)":27.3}, "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":5.7,  "Calcium (mg)":255.0, "Vit C (mg)":0.6,  "Potassium (mg)":813.0},  "calories":534.0},
  "Hemp Seeds":     {"category":"Seed",      "grams":{"Protein (g)":31.6, "Carbs (g)":8.7,  "Fat (g)":48.8, "Fiber (g)":4.0},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":7.95, "Calcium (mg)":70.0,  "Vit C (mg)":0.5,  "Potassium (mg)":1200.0}, "calories":553.0},
  "Poppy Seeds":    {"category":"Seed",      "grams":{"Protein (g)":17.99,"Carbs (g)":28.1, "Fat (g)":41.6, "Fiber (g)":19.5}, "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":9.76, "Calcium (mg)":1438.0,"Vit C (mg)":1.0,  "Potassium (mg)":719.0},  "calories":525.0},
  "Pumpkin Seeds":  {"category":"Seed",      "grams":{"Protein (g)":30.2, "Carbs (g)":10.7, "Fat (g)":49.1, "Fiber (g)":6.0},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":8.8,  "Calcium (mg)":46.0,  "Vit C (mg)":1.9,  "Potassium (mg)":919.0},  "calories":559.0},
  "Sesame Seeds":   {"category":"Seed",      "grams":{"Protein (g)":17.7, "Carbs (g)":23.5, "Fat (g)":49.7, "Fiber (g)":11.8}, "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":14.6, "Calcium (mg)":975.0, "Vit C (mg)":0.0,  "Potassium (mg)":468.0},  "calories":573.0},
  "Sunflower Seeds":{"category":"Seed",      "grams":{"Protein (g)":20.8, "Carbs (g)":20.0, "Fat (g)":51.5, "Fiber (g)":8.6},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":5.3,  "Calcium (mg)":78.0,  "Vit C (mg)":1.4,  "Potassium (mg)":645.0},  "calories":584.0},

  # ── LEGUMES ──────────────────────────────────────────────────────────────────
  "Black Beans":    {"category":"Legume",    "grams":{"Protein (g)":8.9,  "Carbs (g)":23.7, "Fat (g)":0.5,  "Fiber (g)":8.7},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":2.1,  "Calcium (mg)":27.0,  "Vit C (mg)":0.0,  "Potassium (mg)":355.0},  "calories":132.0},
  "Chickpeas":      {"category":"Legume",    "grams":{"Protein (g)":8.9,  "Carbs (g)":27.4, "Fat (g)":2.6,  "Fiber (g)":7.6},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":2.9,  "Calcium (mg)":49.0,  "Vit C (mg)":1.3,  "Potassium (mg)":291.0},  "calories":164.0},
  "Kidney Beans":   {"category":"Legume",    "grams":{"Protein (g)":8.7,  "Carbs (g)":22.8, "Fat (g)":0.5,  "Fiber (g)":6.4},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":2.9,  "Calcium (mg)":28.0,  "Vit C (mg)":1.2,  "Potassium (mg)":403.0},  "calories":127.0},
  "Lima Beans":     {"category":"Legume",    "grams":{"Protein (g)":6.8,  "Carbs (g)":20.9, "Fat (g)":0.4,  "Fiber (g)":7.0},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":2.4,  "Calcium (mg)":17.0,  "Vit C (mg)":0.0,  "Potassium (mg)":508.0},  "calories":115.0},
  "Mung Beans":     {"category":"Legume",    "grams":{"Protein (g)":7.0,  "Carbs (g)":19.2, "Fat (g)":0.4,  "Fiber (g)":7.6},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":1.8,  "Calcium (mg)":27.0,  "Vit C (mg)":1.0,  "Potassium (mg)":266.0},  "calories":105.0},
  "Navy Beans":     {"category":"Legume",    "grams":{"Protein (g)":8.2,  "Carbs (g)":26.1, "Fat (g)":0.6,  "Fiber (g)":10.5}, "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":2.4,  "Calcium (mg)":69.0,  "Vit C (mg)":1.5,  "Potassium (mg)":354.0},  "calories":140.0},
  "Pinto Beans":    {"category":"Legume",    "grams":{"Protein (g)":9.0,  "Carbs (g)":26.2, "Fat (g)":0.7,  "Fiber (g)":9.0},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":2.2,  "Calcium (mg)":46.0,  "Vit C (mg)":1.4,  "Potassium (mg)":436.0},  "calories":143.0},
  "Soybeans":       {"category":"Legume",    "grams":{"Protein (g)":16.6, "Carbs (g)":9.9,  "Fat (g)":9.0,  "Fiber (g)":6.0},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":5.1,  "Calcium (mg)":102.0, "Vit C (mg)":6.0,  "Potassium (mg)":515.0},  "calories":173.0},

  # ── LENTILS ──────────────────────────────────────────────────────────────────
  "Black Lentils":  {"category":"Lentil",    "grams":{"Protein (g)":9.0,  "Carbs (g)":20.0, "Fat (g)":0.4,  "Fiber (g)":8.0},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":3.3,  "Calcium (mg)":19.0,  "Vit C (mg)":1.5,  "Potassium (mg)":369.0},  "calories":116.0},
  "Green Lentils":  {"category":"Lentil",    "grams":{"Protein (g)":9.0,  "Carbs (g)":20.1, "Fat (g)":0.4,  "Fiber (g)":7.9},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":3.3,  "Calcium (mg)":19.0,  "Vit C (mg)":1.5,  "Potassium (mg)":369.0},  "calories":116.0},
  "Red Lentils":    {"category":"Lentil",    "grams":{"Protein (g)":9.0,  "Carbs (g)":20.1, "Fat (g)":0.4,  "Fiber (g)":7.9},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":3.3,  "Calcium (mg)":19.0,  "Vit C (mg)":1.5,  "Potassium (mg)":369.0},  "calories":116.0},
  "Yellow Lentils": {"category":"Lentil",    "grams":{"Protein (g)":8.8,  "Carbs (g)":20.2, "Fat (g)":0.4,  "Fiber (g)":7.9},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":3.2,  "Calcium (mg)":16.0,  "Vit C (mg)":1.5,  "Potassium (mg)":358.0},  "calories":114.0},

  # ── GRAINS ───────────────────────────────────────────────────────────────────
  "Amaranth":       {"category":"Grain",     "grams":{"Protein (g)":3.8,  "Carbs (g)":19.0, "Fat (g)":1.6,  "Fiber (g)":2.1},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":2.1,  "Calcium (mg)":47.0,  "Vit C (mg)":2.0,  "Potassium (mg)":135.0},  "calories":102.0},
  "Barley":         {"category":"Grain",     "grams":{"Protein (g)":2.3,  "Carbs (g)":28.2, "Fat (g)":0.4,  "Fiber (g)":3.8},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":1.3,  "Calcium (mg)":11.0,  "Vit C (mg)":0.0,  "Potassium (mg)":93.0},   "calories":123.0},
  "Brown Rice":     {"category":"Grain",     "grams":{"Protein (g)":2.6,  "Carbs (g)":23.0, "Fat (g)":0.9,  "Fiber (g)":1.8},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":0.5,  "Calcium (mg)":10.0,  "Vit C (mg)":0.0,  "Potassium (mg)":79.0},   "calories":112.0},
  "Buckwheat":      {"category":"Grain",     "grams":{"Protein (g)":3.4,  "Carbs (g)":19.9, "Fat (g)":0.6,  "Fiber (g)":2.7},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":0.8,  "Calcium (mg)":7.0,   "Vit C (mg)":0.0,  "Potassium (mg)":88.0},   "calories":92.0},
  "Bulgur Wheat":   {"category":"Grain",     "grams":{"Protein (g)":3.1,  "Carbs (g)":18.6, "Fat (g)":0.2,  "Fiber (g)":4.5},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":1.0,  "Calcium (mg)":10.0,  "Vit C (mg)":0.0,  "Potassium (mg)":68.0},   "calories":83.0},
  "Millet":         {"category":"Grain",     "grams":{"Protein (g)":3.5,  "Carbs (g)":23.7, "Fat (g)":1.0,  "Fiber (g)":1.3},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":0.6,  "Calcium (mg)":3.0,   "Vit C (mg)":0.0,  "Potassium (mg)":62.0},   "calories":119.0},
  "Oats":           {"category":"Grain",     "grams":{"Protein (g)":2.4,  "Carbs (g)":12.0, "Fat (g)":1.4,  "Fiber (g)":1.7},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":0.7,  "Calcium (mg)":8.0,   "Vit C (mg)":0.0,  "Potassium (mg)":61.0},   "calories":68.0},
  "Quinoa":         {"category":"Grain",     "grams":{"Protein (g)":4.4,  "Carbs (g)":21.3, "Fat (g)":1.9,  "Fiber (g)":2.8},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":1.5,  "Calcium (mg)":17.0,  "Vit C (mg)":0.0,  "Potassium (mg)":172.0},  "calories":120.0},
  "Rye":            {"category":"Grain",     "grams":{"Protein (g)":3.1,  "Carbs (g)":23.4, "Fat (g)":0.6,  "Fiber (g)":3.9},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":1.1,  "Calcium (mg)":6.0,   "Vit C (mg)":0.0,  "Potassium (mg)":61.0},   "calories":113.0},
  "Sorghum":        {"category":"Grain",     "grams":{"Protein (g)":3.3,  "Carbs (g)":24.6, "Fat (g)":0.9,  "Fiber (g)":1.4},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":0.9,  "Calcium (mg)":13.0,  "Vit C (mg)":0.0,  "Potassium (mg)":109.0},  "calories":112.0},
  "Spelt":          {"category":"Grain",     "grams":{"Protein (g)":5.5,  "Carbs (g)":26.0, "Fat (g)":0.8,  "Fiber (g)":3.9},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":1.7,  "Calcium (mg)":19.0,  "Vit C (mg)":0.0,  "Potassium (mg)":136.0},  "calories":127.0},
  "White Rice":     {"category":"Grain",     "grams":{"Protein (g)":2.7,  "Carbs (g)":28.2, "Fat (g)":0.3,  "Fiber (g)":0.4},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":0.2,  "Calcium (mg)":10.0,  "Vit C (mg)":0.0,  "Potassium (mg)":35.0},   "calories":130.0},
  "Wild Rice":      {"category":"Grain",     "grams":{"Protein (g)":4.0,  "Carbs (g)":21.3, "Fat (g)":0.3,  "Fiber (g)":1.8},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":0.6,  "Calcium (mg)":3.0,   "Vit C (mg)":0.0,  "Potassium (mg)":101.0},  "calories":101.0},

  # ── CEREALS (cooked / as-consumed unless noted) ──────────────────────────────
  "Bran Flakes":    {"category":"Cereal",    "grams":{"Protein (g)":7.5,  "Carbs (g)":68.0, "Fat (g)":1.9,  "Fiber (g)":15.0}, "minerals":{"Vit B12 (mcg)":1.5,  "Iron (mg)":13.0, "Calcium (mg)":40.0,  "Vit C (mg)":0.0,  "Potassium (mg)":550.0},  "calories":319.0},
  "Cornflakes":     {"category":"Cereal",    "grams":{"Protein (g)":6.7,  "Carbs (g)":84.0, "Fat (g)":0.4,  "Fiber (g)":1.2},  "minerals":{"Vit B12 (mcg)":1.5,  "Iron (mg)":8.0,  "Calcium (mg)":3.0,   "Vit C (mg)":0.0,  "Potassium (mg)":95.0},   "calories":357.0},
  "Granola":        {"category":"Cereal",    "grams":{"Protein (g)":7.8,  "Carbs (g)":60.0, "Fat (g)":18.0, "Fiber (g)":5.2},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":3.0,  "Calcium (mg)":50.0,  "Vit C (mg)":0.0,  "Potassium (mg)":280.0},  "calories":471.0},
  "Muesli":         {"category":"Cereal",    "grams":{"Protein (g)":8.8,  "Carbs (g)":66.0, "Fat (g)":5.4,  "Fiber (g)":7.5},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":4.6,  "Calcium (mg)":70.0,  "Vit C (mg)":0.0,  "Potassium (mg)":390.0},  "calories":363.0},
  "Porridge Oats":  {"category":"Cereal",    "grams":{"Protein (g)":2.4,  "Carbs (g)":12.0, "Fat (g)":1.4,  "Fiber (g)":1.7},  "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":0.7,  "Calcium (mg)":8.0,   "Vit C (mg)":0.0,  "Potassium (mg)":61.0},   "calories":68.0},
  "Shredded Wheat": {"category":"Cereal",    "grams":{"Protein (g)":9.9,  "Carbs (g)":75.0, "Fat (g)":1.7,  "Fiber (g)":11.0}, "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":5.0,  "Calcium (mg)":43.0,  "Vit C (mg)":0.0,  "Potassium (mg)":340.0},  "calories":340.0},
  "Wheat Germ":     {"category":"Cereal",    "grams":{"Protein (g)":23.2, "Carbs (g)":51.8, "Fat (g)":9.7,  "Fiber (g)":13.2}, "minerals":{"Vit B12 (mcg)":0.0,  "Iron (mg)":6.3,  "Calcium (mg)":39.0,  "Vit C (mg)":0.0,  "Potassium (mg)":892.0},  "calories":360.0},
}

def get_chart_data(selected_foods):
    """Return JSON with grams, minerals, and calories for all selected foods,
    sorted alphabetically by food name within the selection."""
    # Filter to valid foods and sort alphabetically
    foods = sorted([f for f in selected_foods if f in FOODS])
    # Pull nutrient key lists from the first food entry
    first = list(FOODS.values())[0]
    gram_keys    = list(first["grams"].keys())
    mineral_keys = list(first["minerals"].keys())
    result = {
        "foods":        foods,
        "gram_keys":    gram_keys,
        "mineral_keys": mineral_keys,
        # Build nutrient -> [value per selected food] mappings
        "grams":    {n: [FOODS[f]["grams"][n]    for f in foods] for n in gram_keys},
        "minerals": {n: [FOODS[f]["minerals"][n]  for f in foods] for n in mineral_keys},
        "calories": [FOODS[f]["calories"] for f in foods],
    }
    return json.dumps(result)
