# foods.py — Nutrition database
# All values per 100g. Sources: USDA FoodData Central, IFCT 2017 (Indian Foods).
#
# Nutrient schema per food:
#   macro     : classic macros in grams
#   vitamins  : fat- and water-soluble vitamins in mg or mcg
#   minerals  : dietary minerals in mg
#   amino     : essential + conditionally essential amino acids in mg
#   fats      : fatty acid breakdown in grams
#   calories  : kcal
#   category  : display group string

import json

FOODS = {

  # ════════════════════════════════════════════════════════════════════════════
  # FRUITS
  # ════════════════════════════════════════════════════════════════════════════
  "Apple":         {"category":"Fruit","calories":52,
    "macro":   {"Protein (g)":0.3,"Carbs (g)":14.0,"Fat (g)":0.2,"Fiber (g)":2.4,"Sugar (g)":10.4},
    "vitamins":{"Vit A (mcg)":3,"Vit C (mg)":4.6,"Vit D (mcg)":0,"Vit E (mg)":0.18,"Vit K (mcg)":2.2,"Vit B1 (mg)":0.017,"Vit B2 (mg)":0.026,"Vit B3 (mg)":0.09,"Vit B5 (mg)":0.06,"Vit B6 (mg)":0.04,"Vit B9 (mcg)":3,"Vit B12 (mcg)":0},
    "minerals":{"Calcium (mg)":6,"Iron (mg)":0.1,"Magnesium (mg)":5,"Phosphorus (mg)":11,"Potassium (mg)":107,"Sodium (mg)":1,"Zinc (mg)":0.04,"Selenium (mcg)":0},
    "amino":   {"Tryptophan (mg)":1,"Threonine (mg)":6,"Isoleucine (mg)":6,"Leucine (mg)":13,"Lysine (mg)":12,"Methionine (mg)":1,"Phenylalanine (mg)":6,"Valine (mg)":12,"Histidine (mg)":5},
    "fats":    {"Saturated (g)":0.03,"Monounsat (g)":0.01,"Polyunsat (g)":0.05,"Omega-3 (g)":0.009,"Omega-6 (g)":0.043}},

  "Avocado":       {"category":"Fruit","calories":160,
    "macro":   {"Protein (g)":2.0,"Carbs (g)":9.0,"Fat (g)":15.0,"Fiber (g)":6.7,"Sugar (g)":0.7},
    "vitamins":{"Vit A (mcg)":7,"Vit C (mg)":10.0,"Vit D (mcg)":0,"Vit E (mg)":2.07,"Vit K (mcg)":21,"Vit B1 (mg)":0.07,"Vit B2 (mg)":0.13,"Vit B3 (mg)":1.74,"Vit B5 (mg)":1.39,"Vit B6 (mg)":0.26,"Vit B9 (mcg)":81,"Vit B12 (mcg)":0},
    "minerals":{"Calcium (mg)":12,"Iron (mg)":0.6,"Magnesium (mg)":29,"Phosphorus (mg)":52,"Potassium (mg)":485,"Sodium (mg)":7,"Zinc (mg)":0.64,"Selenium (mcg)":0.4},
    "amino":   {"Tryptophan (mg)":25,"Threonine (mg)":73,"Isoleucine (mg)":84,"Leucine (mg)":143,"Lysine (mg)":132,"Methionine (mg)":36,"Phenylalanine (mg)":107,"Valine (mg)":107,"Histidine (mg)":49},
    "fats":    {"Saturated (g)":2.13,"Monounsat (g)":9.80,"Polyunsat (g)":1.82,"Omega-3 (g)":0.11,"Omega-6 (g)":1.69}},

  "Banana":        {"category":"Fruit","calories":89,
    "macro":   {"Protein (g)":1.1,"Carbs (g)":23.0,"Fat (g)":0.3,"Fiber (g)":2.6,"Sugar (g)":12.2},
    "vitamins":{"Vit A (mcg)":3,"Vit C (mg)":8.7,"Vit D (mcg)":0,"Vit E (mg)":0.1,"Vit K (mcg)":0.5,"Vit B1 (mg)":0.03,"Vit B2 (mg)":0.07,"Vit B3 (mg)":0.67,"Vit B5 (mg)":0.33,"Vit B6 (mg)":0.37,"Vit B9 (mcg)":20,"Vit B12 (mcg)":0},
    "minerals":{"Calcium (mg)":5,"Iron (mg)":0.3,"Magnesium (mg)":27,"Phosphorus (mg)":22,"Potassium (mg)":358,"Sodium (mg)":1,"Zinc (mg)":0.15,"Selenium (mcg)":1},
    "amino":   {"Tryptophan (mg)":9,"Threonine (mg)":28,"Isoleucine (mg)":28,"Leucine (mg)":68,"Lysine (mg)":50,"Methionine (mg)":8,"Phenylalanine (mg)":49,"Valine (mg)":47,"Histidine (mg)":77},
    "fats":    {"Saturated (g)":0.11,"Monounsat (g)":0.03,"Polyunsat (g)":0.07,"Omega-3 (g)":0.027,"Omega-6 (g)":0.046}},

  "Blueberry":     {"category":"Fruit","calories":57,
    "macro":   {"Protein (g)":0.7,"Carbs (g)":14.0,"Fat (g)":0.3,"Fiber (g)":2.4,"Sugar (g)":10.0},
    "vitamins":{"Vit A (mcg)":3,"Vit C (mg)":9.7,"Vit D (mcg)":0,"Vit E (mg)":0.57,"Vit K (mcg)":19.3,"Vit B1 (mg)":0.04,"Vit B2 (mg)":0.04,"Vit B3 (mg)":0.42,"Vit B5 (mg)":0.12,"Vit B6 (mg)":0.05,"Vit B9 (mcg)":6,"Vit B12 (mcg)":0},
    "minerals":{"Calcium (mg)":6,"Iron (mg)":0.3,"Magnesium (mg)":6,"Phosphorus (mg)":12,"Potassium (mg)":77,"Sodium (mg)":1,"Zinc (mg)":0.16,"Selenium (mcg)":0.1},
    "amino":   {"Tryptophan (mg)":5,"Threonine (mg)":18,"Isoleucine (mg)":17,"Leucine (mg)":41,"Lysine (mg)":13,"Methionine (mg)":8,"Phenylalanine (mg)":26,"Valine (mg)":30,"Histidine (mg)":9},
    "fats":    {"Saturated (g)":0.03,"Monounsat (g)":0.05,"Polyunsat (g)":0.15,"Omega-3 (g)":0.06,"Omega-6 (g)":0.09}},

  "Mango":         {"category":"Fruit","calories":60,
    "macro":   {"Protein (g)":0.8,"Carbs (g)":15.0,"Fat (g)":0.4,"Fiber (g)":1.6,"Sugar (g)":13.7},
    "vitamins":{"Vit A (mcg)":54,"Vit C (mg)":36.4,"Vit D (mcg)":0,"Vit E (mg)":0.9,"Vit K (mcg)":4.2,"Vit B1 (mg)":0.06,"Vit B2 (mg)":0.06,"Vit B3 (mg)":0.67,"Vit B5 (mg)":0.2,"Vit B6 (mg)":0.13,"Vit B9 (mcg)":43,"Vit B12 (mcg)":0},
    "minerals":{"Calcium (mg)":11,"Iron (mg)":0.2,"Magnesium (mg)":10,"Phosphorus (mg)":14,"Potassium (mg)":168,"Sodium (mg)":1,"Zinc (mg)":0.09,"Selenium (mcg)":0.6},
    "amino":   {"Tryptophan (mg)":7,"Threonine (mg)":31,"Isoleucine (mg)":25,"Leucine (mg)":50,"Lysine (mg)":66,"Methionine (mg)":8,"Phenylalanine (mg)":27,"Valine (mg)":38,"Histidine (mg)":19},
    "fats":    {"Saturated (g)":0.09,"Monounsat (g)":0.14,"Polyunsat (g)":0.07,"Omega-3 (g)":0.051,"Omega-6 (g)":0.018}},

  "Orange":        {"category":"Fruit","calories":47,
    "macro":   {"Protein (g)":0.9,"Carbs (g)":12.0,"Fat (g)":0.1,"Fiber (g)":2.4,"Sugar (g)":9.4},
    "vitamins":{"Vit A (mcg)":11,"Vit C (mg)":53.2,"Vit D (mcg)":0,"Vit E (mg)":0.18,"Vit K (mcg)":0,"Vit B1 (mg)":0.09,"Vit B2 (mg)":0.04,"Vit B3 (mg)":0.28,"Vit B5 (mg)":0.25,"Vit B6 (mg)":0.06,"Vit B9 (mcg)":30,"Vit B12 (mcg)":0},
    "minerals":{"Calcium (mg)":40,"Iron (mg)":0.1,"Magnesium (mg)":10,"Phosphorus (mg)":14,"Potassium (mg)":181,"Sodium (mg)":0,"Zinc (mg)":0.07,"Selenium (mcg)":0.5},
    "amino":   {"Tryptophan (mg)":9,"Threonine (mg)":15,"Isoleucine (mg)":25,"Leucine (mg)":23,"Lysine (mg)":47,"Methionine (mg)":8,"Phenylalanine (mg)":21,"Valine (mg)":46,"Histidine (mg)":18},
    "fats":    {"Saturated (g)":0.02,"Monounsat (g)":0.02,"Polyunsat (g)":0.02,"Omega-3 (g)":0.007,"Omega-6 (g)":0.013}},

  "Papaya":        {"category":"Fruit","calories":43,
    "macro":   {"Protein (g)":0.5,"Carbs (g)":11.0,"Fat (g)":0.3,"Fiber (g)":1.7,"Sugar (g)":7.8},
    "vitamins":{"Vit A (mcg)":47,"Vit C (mg)":60.9,"Vit D (mcg)":0,"Vit E (mg)":0.3,"Vit K (mcg)":2.6,"Vit B1 (mg)":0.02,"Vit B2 (mg)":0.03,"Vit B3 (mg)":0.36,"Vit B5 (mg)":0.2,"Vit B6 (mg)":0.04,"Vit B9 (mcg)":37,"Vit B12 (mcg)":0},
    "minerals":{"Calcium (mg)":20,"Iron (mg)":0.3,"Magnesium (mg)":21,"Phosphorus (mg)":10,"Potassium (mg)":182,"Sodium (mg)":8,"Zinc (mg)":0.08,"Selenium (mcg)":0.6},
    "amino":   {"Tryptophan (mg)":8,"Threonine (mg)":11,"Isoleucine (mg)":12,"Leucine (mg)":28,"Lysine (mg)":25,"Methionine (mg)":2,"Phenylalanine (mg)":16,"Valine (mg)":17,"Histidine (mg)":5},
    "fats":    {"Saturated (g)":0.09,"Monounsat (g)":0.08,"Polyunsat (g)":0.06,"Omega-3 (g)":0.016,"Omega-6 (g)":0.044}},

  "Pomegranate":   {"category":"Fruit","calories":83,
    "macro":   {"Protein (g)":1.7,"Carbs (g)":19.0,"Fat (g)":1.2,"Fiber (g)":4.0,"Sugar (g)":13.7},
    "vitamins":{"Vit A (mcg)":0,"Vit C (mg)":10.2,"Vit D (mcg)":0,"Vit E (mg)":0.6,"Vit K (mcg)":16.4,"Vit B1 (mg)":0.07,"Vit B2 (mg)":0.05,"Vit B3 (mg)":0.29,"Vit B5 (mg)":0.38,"Vit B6 (mg)":0.08,"Vit B9 (mcg)":38,"Vit B12 (mcg)":0},
    "minerals":{"Calcium (mg)":10,"Iron (mg)":0.3,"Magnesium (mg)":12,"Phosphorus (mg)":36,"Potassium (mg)":236,"Sodium (mg)":3,"Zinc (mg)":0.35,"Selenium (mcg)":0.5},
    "amino":   {"Tryptophan (mg)":17,"Threonine (mg)":38,"Isoleucine (mg)":43,"Leucine (mg)":68,"Lysine (mg)":54,"Methionine (mg)":13,"Phenylalanine (mg)":50,"Valine (mg)":57,"Histidine (mg)":29},
    "fats":    {"Saturated (g)":0.12,"Monounsat (g)":0.09,"Polyunsat (g)":0.08,"Omega-3 (g)":0.033,"Omega-6 (g)":0.047}},

  "Strawberry":    {"category":"Fruit","calories":32,
    "macro":   {"Protein (g)":0.7,"Carbs (g)":8.0,"Fat (g)":0.3,"Fiber (g)":2.0,"Sugar (g)":4.9},
    "vitamins":{"Vit A (mcg)":1,"Vit C (mg)":58.8,"Vit D (mcg)":0,"Vit E (mg)":0.29,"Vit K (mcg)":2.2,"Vit B1 (mg)":0.02,"Vit B2 (mg)":0.02,"Vit B3 (mg)":0.39,"Vit B5 (mg)":0.12,"Vit B6 (mg)":0.05,"Vit B9 (mcg)":24,"Vit B12 (mcg)":0},
    "minerals":{"Calcium (mg)":16,"Iron (mg)":0.4,"Magnesium (mg)":13,"Phosphorus (mg)":24,"Potassium (mg)":153,"Sodium (mg)":1,"Zinc (mg)":0.14,"Selenium (mcg)":0.4},
    "amino":   {"Tryptophan (mg)":8,"Threonine (mg)":19,"Isoleucine (mg)":18,"Leucine (mg)":41,"Lysine (mg)":30,"Methionine (mg)":2,"Phenylalanine (mg)":20,"Valine (mg)":23,"Histidine (mg)":12},
    "fats":    {"Saturated (g)":0.02,"Monounsat (g)":0.04,"Polyunsat (g)":0.16,"Omega-3 (g)":0.065,"Omega-6 (g)":0.09}},

  # ── Indian fruits ──
  "Amla (Gooseberry)": {"category":"Fruit","calories":44,
    "macro":   {"Protein (g)":0.9,"Carbs (g)":10.2,"Fat (g)":0.6,"Fiber (g)":4.3,"Sugar (g)":0.0},
    "vitamins":{"Vit A (mcg)":15,"Vit C (mg)":600.0,"Vit D (mcg)":0,"Vit E (mg)":0.37,"Vit K (mcg)":0,"Vit B1 (mg)":0.03,"Vit B2 (mg)":0.01,"Vit B3 (mg)":0.3,"Vit B5 (mg)":0.06,"Vit B6 (mg)":0.08,"Vit B9 (mcg)":6,"Vit B12 (mcg)":0},
    "minerals":{"Calcium (mg)":50,"Iron (mg)":1.2,"Magnesium (mg)":10,"Phosphorus (mg)":27,"Potassium (mg)":198,"Sodium (mg)":1,"Zinc (mg)":0.12,"Selenium (mcg)":0},
    "amino":   {"Tryptophan (mg)":7,"Threonine (mg)":16,"Isoleucine (mg)":23,"Leucine (mg)":33,"Lysine (mg)":24,"Methionine (mg)":9,"Phenylalanine (mg)":22,"Valine (mg)":30,"Histidine (mg)":12},
    "fats":    {"Saturated (g)":0.1,"Monounsat (g)":0.06,"Polyunsat (g)":0.3,"Omega-3 (g)":0.06,"Omega-6 (g)":0.24}},

  "Guava":         {"category":"Fruit","calories":68,
    "macro":   {"Protein (g)":2.6,"Carbs (g)":14.3,"Fat (g)":1.0,"Fiber (g)":5.4,"Sugar (g)":8.9},
    "vitamins":{"Vit A (mcg)":31,"Vit C (mg)":228.3,"Vit D (mcg)":0,"Vit E (mg)":0.73,"Vit K (mcg)":2.6,"Vit B1 (mg)":0.07,"Vit B2 (mg)":0.04,"Vit B3 (mg)":1.08,"Vit B5 (mg)":0.45,"Vit B6 (mg)":0.11,"Vit B9 (mcg)":49,"Vit B12 (mcg)":0},
    "minerals":{"Calcium (mg)":18,"Iron (mg)":0.3,"Magnesium (mg)":22,"Phosphorus (mg)":40,"Potassium (mg)":417,"Sodium (mg)":2,"Zinc (mg)":0.23,"Selenium (mcg)":0.6},
    "amino":   {"Tryptophan (mg)":26,"Threonine (mg)":60,"Isoleucine (mg)":67,"Leucine (mg)":107,"Lysine (mg)":102,"Methionine (mg)":22,"Phenylalanine (mg)":66,"Valine (mg)":78,"Histidine (mg)":35},
    "fats":    {"Saturated (g)":0.28,"Monounsat (g)":0.09,"Polyunsat (g)":0.4,"Omega-3 (g)":0.1,"Omega-6 (g)":0.3}},

  "Jackfruit":     {"category":"Fruit","calories":95,
    "macro":   {"Protein (g)":1.7,"Carbs (g)":23.3,"Fat (g)":0.6,"Fiber (g)":1.5,"Sugar (g)":19.1},
    "vitamins":{"Vit A (mcg)":5,"Vit C (mg)":13.8,"Vit D (mcg)":0,"Vit E (mg)":0.34,"Vit K (mcg)":0,"Vit B1 (mg)":0.1,"Vit B2 (mg)":0.06,"Vit B3 (mg)":0.92,"Vit B5 (mg)":0.24,"Vit B6 (mg)":0.1,"Vit B9 (mcg)":24,"Vit B12 (mcg)":0},
    "minerals":{"Calcium (mg)":24,"Iron (mg)":0.6,"Magnesium (mg)":29,"Phosphorus (mg)":21,"Potassium (mg)":303,"Sodium (mg)":3,"Zinc (mg)":0.42,"Selenium (mcg)":0},
    "amino":   {"Tryptophan (mg)":21,"Threonine (mg)":71,"Isoleucine (mg)":55,"Leucine (mg)":99,"Lysine (mg)":68,"Methionine (mg)":15,"Phenylalanine (mg)":54,"Valine (mg)":68,"Histidine (mg)":30},
    "fats":    {"Saturated (g)":0.14,"Monounsat (g)":0.16,"Polyunsat (g)":0.19,"Omega-3 (g)":0.05,"Omega-6 (g)":0.14}},

  "Tamarind":      {"category":"Fruit","calories":239,
    "macro":   {"Protein (g)":2.8,"Carbs (g)":62.5,"Fat (g)":0.6,"Fiber (g)":5.1,"Sugar (g)":38.0},
    "vitamins":{"Vit A (mcg)":2,"Vit C (mg)":3.5,"Vit D (mcg)":0,"Vit E (mg)":0.1,"Vit K (mcg)":0,"Vit B1 (mg)":0.43,"Vit B2 (mg)":0.15,"Vit B3 (mg)":1.94,"Vit B5 (mg)":0.14,"Vit B6 (mg)":0.07,"Vit B9 (mcg)":14,"Vit B12 (mcg)":0},
    "minerals":{"Calcium (mg)":74,"Iron (mg)":2.8,"Magnesium (mg)":92,"Phosphorus (mg)":113,"Potassium (mg)":628,"Sodium (mg)":28,"Zinc (mg)":0.1,"Selenium (mcg)":1.3},
    "amino":   {"Tryptophan (mg)":19,"Threonine (mg)":90,"Isoleucine (mg)":97,"Leucine (mg)":167,"Lysine (mg)":135,"Methionine (mg)":13,"Phenylalanine (mg)":113,"Valine (mg)":128,"Histidine (mg)":60},
    "fats":    {"Saturated (g)":0.27,"Monounsat (g)":0.18,"Polyunsat (g)":0.06,"Omega-3 (g)":0.02,"Omega-6 (g)":0.04}},

  # ════════════════════════════════════════════════════════════════════════════
  # VEGETABLES
  # ════════════════════════════════════════════════════════════════════════════
  "Broccoli":      {"category":"Vegetable","calories":34,
    "macro":   {"Protein (g)":2.8,"Carbs (g)":7.0,"Fat (g)":0.4,"Fiber (g)":2.6,"Sugar (g)":1.7},
    "vitamins":{"Vit A (mcg)":31,"Vit C (mg)":89.2,"Vit D (mcg)":0,"Vit E (mg)":0.78,"Vit K (mcg)":102,"Vit B1 (mg)":0.07,"Vit B2 (mg)":0.12,"Vit B3 (mg)":0.64,"Vit B5 (mg)":0.57,"Vit B6 (mg)":0.18,"Vit B9 (mcg)":63,"Vit B12 (mcg)":0},
    "minerals":{"Calcium (mg)":47,"Iron (mg)":0.7,"Magnesium (mg)":21,"Phosphorus (mg)":66,"Potassium (mg)":316,"Sodium (mg)":33,"Zinc (mg)":0.41,"Selenium (mcg)":2.5},
    "amino":   {"Tryptophan (mg)":33,"Threonine (mg)":88,"Isoleucine (mg)":76,"Leucine (mg)":129,"Lysine (mg)":135,"Methionine (mg)":27,"Phenylalanine (mg)":86,"Valine (mg)":113,"Histidine (mg)":49},
    "fats":    {"Saturated (g)":0.04,"Monounsat (g)":0.01,"Polyunsat (g)":0.04,"Omega-3 (g)":0.099,"Omega-6 (g)":0.04}},

  "Carrot":        {"category":"Vegetable","calories":41,
    "macro":   {"Protein (g)":0.9,"Carbs (g)":10.0,"Fat (g)":0.2,"Fiber (g)":2.8,"Sugar (g)":4.7},
    "vitamins":{"Vit A (mcg)":835,"Vit C (mg)":5.9,"Vit D (mcg)":0,"Vit E (mg)":0.66,"Vit K (mcg)":13.2,"Vit B1 (mg)":0.07,"Vit B2 (mg)":0.06,"Vit B3 (mg)":0.98,"Vit B5 (mg)":0.27,"Vit B6 (mg)":0.14,"Vit B9 (mcg)":19,"Vit B12 (mcg)":0},
    "minerals":{"Calcium (mg)":33,"Iron (mg)":0.3,"Magnesium (mg)":12,"Phosphorus (mg)":35,"Potassium (mg)":320,"Sodium (mg)":69,"Zinc (mg)":0.24,"Selenium (mcg)":0.1},
    "amino":   {"Tryptophan (mg)":12,"Threonine (mg)":28,"Isoleucine (mg)":27,"Leucine (mg)":45,"Lysine (mg)":40,"Methionine (mg)":10,"Phenylalanine (mg)":30,"Valine (mg)":39,"Histidine (mg)":15},
    "fats":    {"Saturated (g)":0.04,"Monounsat (g)":0.01,"Polyunsat (g)":0.1,"Omega-3 (g)":0.002,"Omega-6 (g)":0.098}},

  "Spinach":       {"category":"Vegetable","calories":23,
    "macro":   {"Protein (g)":2.9,"Carbs (g)":3.6,"Fat (g)":0.4,"Fiber (g)":2.2,"Sugar (g)":0.4},
    "vitamins":{"Vit A (mcg)":469,"Vit C (mg)":28.1,"Vit D (mcg)":0,"Vit E (mg)":2.03,"Vit K (mcg)":483,"Vit B1 (mg)":0.08,"Vit B2 (mg)":0.19,"Vit B3 (mg)":0.72,"Vit B5 (mg)":0.07,"Vit B6 (mg)":0.2,"Vit B9 (mcg)":194,"Vit B12 (mcg)":0},
    "minerals":{"Calcium (mg)":99,"Iron (mg)":2.7,"Magnesium (mg)":79,"Phosphorus (mg)":49,"Potassium (mg)":558,"Sodium (mg)":79,"Zinc (mg)":0.53,"Selenium (mcg)":1},
    "amino":   {"Tryptophan (mg)":39,"Threonine (mg)":122,"Isoleucine (mg)":147,"Leucine (mg)":223,"Lysine (mg)":174,"Methionine (mg)":53,"Phenylalanine (mg)":129,"Valine (mg)":161,"Histidine (mg)":64},
    "fats":    {"Saturated (g)":0.06,"Monounsat (g)":0.01,"Polyunsat (g)":0.17,"Omega-3 (g)":0.138,"Omega-6 (g)":0.026}},

  "Kale":          {"category":"Vegetable","calories":49,
    "macro":   {"Protein (g)":4.3,"Carbs (g)":9.0,"Fat (g)":1.5,"Fiber (g)":3.6,"Sugar (g)":2.3},
    "vitamins":{"Vit A (mcg)":500,"Vit C (mg)":120.0,"Vit D (mcg)":0,"Vit E (mg)":1.54,"Vit K (mcg)":817,"Vit B1 (mg)":0.11,"Vit B2 (mg)":0.13,"Vit B3 (mg)":1.02,"Vit B5 (mg)":0.09,"Vit B6 (mg)":0.27,"Vit B9 (mcg)":141,"Vit B12 (mcg)":0},
    "minerals":{"Calcium (mg)":150,"Iron (mg)":1.5,"Magnesium (mg)":47,"Phosphorus (mg)":92,"Potassium (mg)":491,"Sodium (mg)":38,"Zinc (mg)":0.56,"Selenium (mcg)":0.9},
    "amino":   {"Tryptophan (mg)":50,"Threonine (mg)":136,"Isoleucine (mg)":139,"Leucine (mg)":199,"Lysine (mg)":212,"Methionine (mg)":34,"Phenylalanine (mg)":130,"Valine (mg)":172,"Histidine (mg)":67},
    "fats":    {"Saturated (g)":0.19,"Monounsat (g)":0.1,"Polyunsat (g)":0.34,"Omega-3 (g)":0.18,"Omega-6 (g)":0.16}},

  "Sweet Potato":  {"category":"Vegetable","calories":86,
    "macro":   {"Protein (g)":1.6,"Carbs (g)":20.0,"Fat (g)":0.1,"Fiber (g)":3.0,"Sugar (g)":4.2},
    "vitamins":{"Vit A (mcg)":961,"Vit C (mg)":2.4,"Vit D (mcg)":0,"Vit E (mg)":0.26,"Vit K (mcg)":1.8,"Vit B1 (mg)":0.08,"Vit B2 (mg)":0.06,"Vit B3 (mg)":0.56,"Vit B5 (mg)":0.8,"Vit B6 (mg)":0.29,"Vit B9 (mcg)":11,"Vit B12 (mcg)":0},
    "minerals":{"Calcium (mg)":30,"Iron (mg)":0.6,"Magnesium (mg)":25,"Phosphorus (mg)":47,"Potassium (mg)":337,"Sodium (mg)":55,"Zinc (mg)":0.3,"Selenium (mcg)":0.6},
    "amino":   {"Tryptophan (mg)":30,"Threonine (mg)":75,"Isoleucine (mg)":73,"Leucine (mg)":109,"Lysine (mg)":66,"Methionine (mg)":28,"Phenylalanine (mg)":93,"Valine (mg)":96,"Histidine (mg)":36},
    "fats":    {"Saturated (g)":0.02,"Monounsat (g)":0.0,"Polyunsat (g)":0.01,"Omega-3 (g)":0.007,"Omega-6 (g)":0.003}},

  "Tomato":        {"category":"Vegetable","calories":18,
    "macro":   {"Protein (g)":0.9,"Carbs (g)":3.9,"Fat (g)":0.2,"Fiber (g)":1.2,"Sugar (g)":2.6},
    "vitamins":{"Vit A (mcg)":42,"Vit C (mg)":13.7,"Vit D (mcg)":0,"Vit E (mg)":0.54,"Vit K (mcg)":7.9,"Vit B1 (mg)":0.04,"Vit B2 (mg)":0.02,"Vit B3 (mg)":0.59,"Vit B5 (mg)":0.09,"Vit B6 (mg)":0.08,"Vit B9 (mcg)":15,"Vit B12 (mcg)":0},
    "minerals":{"Calcium (mg)":10,"Iron (mg)":0.3,"Magnesium (mg)":11,"Phosphorus (mg)":24,"Potassium (mg)":237,"Sodium (mg)":5,"Zinc (mg)":0.17,"Selenium (mcg)":0},
    "amino":   {"Tryptophan (mg)":6,"Threonine (mg)":27,"Isoleucine (mg)":18,"Leucine (mg)":30,"Lysine (mg)":27,"Methionine (mg)":6,"Phenylalanine (mg)":27,"Valine (mg)":24,"Histidine (mg)":14},
    "fats":    {"Saturated (g)":0.03,"Monounsat (g)":0.03,"Polyunsat (g)":0.08,"Omega-3 (g)":0.003,"Omega-6 (g)":0.08}},

  # ── Indian vegetables ──
  "Bitter Melon":  {"category":"Vegetable","calories":17,
    "macro":   {"Protein (g)":1.0,"Carbs (g)":3.7,"Fat (g)":0.2,"Fiber (g)":2.8,"Sugar (g)":0.0},
    "vitamins":{"Vit A (mcg)":24,"Vit C (mg)":84.0,"Vit D (mcg)":0,"Vit E (mg)":0.14,"Vit K (mcg)":4.8,"Vit B1 (mg)":0.04,"Vit B2 (mg)":0.04,"Vit B3 (mg)":0.4,"Vit B5 (mg)":0.21,"Vit B6 (mg)":0.04,"Vit B9 (mcg)":72,"Vit B12 (mcg)":0},
    "minerals":{"Calcium (mg)":19,"Iron (mg)":0.4,"Magnesium (mg)":17,"Phosphorus (mg)":31,"Potassium (mg)":296,"Sodium (mg)":5,"Zinc (mg)":0.8,"Selenium (mcg)":0},
    "amino":   {"Tryptophan (mg)":9,"Threonine (mg)":28,"Isoleucine (mg)":27,"Leucine (mg)":47,"Lysine (mg)":41,"Methionine (mg)":9,"Phenylalanine (mg)":29,"Valine (mg)":36,"Histidine (mg)":16},
    "fats":    {"Saturated (g)":0.02,"Monounsat (g)":0.01,"Polyunsat (g)":0.09,"Omega-3 (g)":0.04,"Omega-6 (g)":0.05}},

  "Bottle Gourd":  {"category":"Vegetable","calories":14,
    "macro":   {"Protein (g)":0.6,"Carbs (g)":3.4,"Fat (g)":0.02,"Fiber (g)":0.5,"Sugar (g)":0.0},
    "vitamins":{"Vit A (mcg)":0,"Vit C (mg)":10.1,"Vit D (mcg)":0,"Vit E (mg)":0.0,"Vit K (mcg)":0,"Vit B1 (mg)":0.03,"Vit B2 (mg)":0.02,"Vit B3 (mg)":0.32,"Vit B5 (mg)":0.18,"Vit B6 (mg)":0.04,"Vit B9 (mcg)":6,"Vit B12 (mcg)":0},
    "minerals":{"Calcium (mg)":26,"Iron (mg)":0.2,"Magnesium (mg)":11,"Phosphorus (mg)":13,"Potassium (mg)":150,"Sodium (mg)":2,"Zinc (mg)":0.7,"Selenium (mcg)":0},
    "amino":   {"Tryptophan (mg)":6,"Threonine (mg)":20,"Isoleucine (mg)":24,"Leucine (mg)":32,"Lysine (mg)":25,"Methionine (mg)":6,"Phenylalanine (mg)":18,"Valine (mg)":26,"Histidine (mg)":10},
    "fats":    {"Saturated (g)":0.0,"Monounsat (g)":0.0,"Polyunsat (g)":0.01,"Omega-3 (g)":0.0,"Omega-6 (g)":0.01}},

  "Drumstick (Moringa)": {"category":"Vegetable","calories":37,
    "macro":   {"Protein (g)":2.1,"Carbs (g)":8.5,"Fat (g)":0.2,"Fiber (g)":3.2,"Sugar (g)":0.0},
    "vitamins":{"Vit A (mcg)":4,"Vit C (mg)":141.0,"Vit D (mcg)":0,"Vit E (mg)":0.0,"Vit K (mcg)":0,"Vit B1 (mg)":0.05,"Vit B2 (mg)":0.06,"Vit B3 (mg)":0.62,"Vit B5 (mg)":0.0,"Vit B6 (mg)":0.12,"Vit B9 (mcg)":44,"Vit B12 (mcg)":0},
    "minerals":{"Calcium (mg)":30,"Iron (mg)":0.4,"Magnesium (mg)":45,"Phosphorus (mg)":50,"Potassium (mg)":461,"Sodium (mg)":42,"Zinc (mg)":0.45,"Selenium (mcg)":0},
    "amino":   {"Tryptophan (mg)":18,"Threonine (mg)":76,"Isoleucine (mg)":76,"Leucine (mg)":129,"Lysine (mg)":88,"Methionine (mg)":22,"Phenylalanine (mg)":87,"Valine (mg)":95,"Histidine (mg)":40},
    "fats":    {"Saturated (g)":0.04,"Monounsat (g)":0.02,"Polyunsat (g)":0.1,"Omega-3 (g)":0.02,"Omega-6 (g)":0.08}},

  "Fenugreek Leaves": {"category":"Vegetable","calories":49,
    "macro":   {"Protein (g)":4.4,"Carbs (g)":6.0,"Fat (g)":0.9,"Fiber (g)":1.1,"Sugar (g)":0.0},
    "vitamins":{"Vit A (mcg)":395,"Vit C (mg)":220.0,"Vit D (mcg)":0,"Vit E (mg)":0.0,"Vit K (mcg)":0,"Vit B1 (mg)":0.04,"Vit B2 (mg)":0.31,"Vit B3 (mg)":0.9,"Vit B5 (mg)":0.0,"Vit B6 (mg)":0.0,"Vit B9 (mcg)":0,"Vit B12 (mcg)":0},
    "minerals":{"Calcium (mg)":395,"Iron (mg)":16.5,"Magnesium (mg)":0,"Phosphorus (mg)":51,"Potassium (mg)":31,"Sodium (mg)":76,"Zinc (mg)":0.0,"Selenium (mcg)":0},
    "amino":   {"Tryptophan (mg)":47,"Threonine (mg)":120,"Isoleucine (mg)":130,"Leucine (mg)":210,"Lysine (mg)":180,"Methionine (mg)":36,"Phenylalanine (mg)":140,"Valine (mg)":150,"Histidine (mg)":60},
    "fats":    {"Saturated (g)":0.18,"Monounsat (g)":0.1,"Polyunsat (g)":0.4,"Omega-3 (g)":0.1,"Omega-6 (g)":0.3}},

  "Lotus Root":    {"category":"Vegetable","calories":74,
    "macro":   {"Protein (g)":2.6,"Carbs (g)":17.2,"Fat (g)":0.1,"Fiber (g)":4.9,"Sugar (g)":0.5},
    "vitamins":{"Vit A (mcg)":0,"Vit C (mg)":44.0,"Vit D (mcg)":0,"Vit E (mg)":0.18,"Vit K (mcg)":0.3,"Vit B1 (mg)":0.16,"Vit B2 (mg)":0.22,"Vit B3 (mg)":0.39,"Vit B5 (mg)":0.37,"Vit B6 (mg)":0.26,"Vit B9 (mcg)":13,"Vit B12 (mcg)":0},
    "minerals":{"Calcium (mg)":45,"Iron (mg)":1.2,"Magnesium (mg)":23,"Phosphorus (mg)":100,"Potassium (mg)":556,"Sodium (mg)":45,"Zinc (mg)":0.39,"Selenium (mcg)":0.7},
    "amino":   {"Tryptophan (mg)":24,"Threonine (mg)":79,"Isoleucine (mg)":75,"Leucine (mg)":120,"Lysine (mg)":95,"Methionine (mg)":22,"Phenylalanine (mg)":80,"Valine (mg)":105,"Histidine (mg)":45},
    "fats":    {"Saturated (g)":0.02,"Monounsat (g)":0.0,"Polyunsat (g)":0.04,"Omega-3 (g)":0.01,"Omega-6 (g)":0.03}},

  "Taro Root":     {"category":"Vegetable","calories":112,
    "macro":   {"Protein (g)":1.5,"Carbs (g)":26.5,"Fat (g)":0.2,"Fiber (g)":4.1,"Sugar (g)":0.4},
    "vitamins":{"Vit A (mcg)":4,"Vit C (mg)":4.5,"Vit D (mcg)":0,"Vit E (mg)":2.38,"Vit K (mcg)":1.0,"Vit B1 (mg)":0.1,"Vit B2 (mg)":0.03,"Vit B3 (mg)":0.6,"Vit B5 (mg)":0.3,"Vit B6 (mg)":0.28,"Vit B9 (mcg)":22,"Vit B12 (mcg)":0},
    "minerals":{"Calcium (mg)":43,"Iron (mg)":0.6,"Magnesium (mg)":33,"Phosphorus (mg)":84,"Potassium (mg)":591,"Sodium (mg)":11,"Zinc (mg)":0.23,"Selenium (mcg)":0.7},
    "amino":   {"Tryptophan (mg)":18,"Threonine (mg)":51,"Isoleucine (mg)":57,"Leucine (mg)":97,"Lysine (mg)":73,"Methionine (mg)":21,"Phenylalanine (mg)":62,"Valine (mg)":73,"Histidine (mg)":32},
    "fats":    {"Saturated (g)":0.04,"Monounsat (g)":0.01,"Polyunsat (g)":0.08,"Omega-3 (g)":0.03,"Omega-6 (g)":0.05}},

  # ════════════════════════════════════════════════════════════════════════════
  # NUTS
  # ════════════════════════════════════════════════════════════════════════════
  "Almonds":       {"category":"Nut","calories":579,
    "macro":   {"Protein (g)":21.2,"Carbs (g)":21.7,"Fat (g)":49.4,"Fiber (g)":12.5,"Sugar (g)":4.4},
    "vitamins":{"Vit A (mcg)":0,"Vit C (mg)":0.0,"Vit D (mcg)":0,"Vit E (mg)":25.63,"Vit K (mcg)":0,"Vit B1 (mg)":0.21,"Vit B2 (mg)":1.14,"Vit B3 (mg)":3.62,"Vit B5 (mg)":0.47,"Vit B6 (mg)":0.14,"Vit B9 (mcg)":44,"Vit B12 (mcg)":0},
    "minerals":{"Calcium (mg)":264,"Iron (mg)":3.7,"Magnesium (mg)":270,"Phosphorus (mg)":481,"Potassium (mg)":733,"Sodium (mg)":1,"Zinc (mg)":3.12,"Selenium (mcg)":4.1},
    "amino":   {"Tryptophan (mg)":214,"Threonine (mg)":601,"Isoleucine (mg)":755,"Leucine (mg)":1492,"Lysine (mg)":580,"Methionine (mg)":151,"Phenylalanine (mg)":1120,"Valine (mg)":1025,"Histidine (mg)":522},
    "fats":    {"Saturated (g)":3.73,"Monounsat (g)":31.55,"Polyunsat (g)":12.33,"Omega-3 (g)":0.003,"Omega-6 (g)":12.32}},

  "Cashews":       {"category":"Nut","calories":553,
    "macro":   {"Protein (g)":18.2,"Carbs (g)":30.2,"Fat (g)":43.8,"Fiber (g)":3.3,"Sugar (g)":5.9},
    "vitamins":{"Vit A (mcg)":0,"Vit C (mg)":0.5,"Vit D (mcg)":0,"Vit E (mg)":0.9,"Vit K (mcg)":34.7,"Vit B1 (mg)":0.42,"Vit B2 (mg)":0.06,"Vit B3 (mg)":1.06,"Vit B5 (mg)":0.86,"Vit B6 (mg)":0.42,"Vit B9 (mcg)":25,"Vit B12 (mcg)":0},
    "minerals":{"Calcium (mg)":37,"Iron (mg)":6.7,"Magnesium (mg)":292,"Phosphorus (mg)":593,"Potassium (mg)":660,"Sodium (mg)":12,"Zinc (mg)":5.78,"Selenium (mcg)":19.9},
    "amino":   {"Tryptophan (mg)":287,"Threonine (mg)":688,"Isoleucine (mg)":789,"Leucine (mg)":1472,"Lysine (mg)":928,"Methionine (mg)":362,"Phenylalanine (mg)":951,"Valine (mg)":1094,"Histidine (mg)":456},
    "fats":    {"Saturated (g)":7.78,"Monounsat (g)":23.8,"Polyunsat (g)":7.84,"Omega-3 (g)":0.062,"Omega-6 (g)":7.78}},

  "Walnuts":       {"category":"Nut","calories":654,
    "macro":   {"Protein (g)":15.2,"Carbs (g)":13.7,"Fat (g)":65.2,"Fiber (g)":6.7,"Sugar (g)":2.6},
    "vitamins":{"Vit A (mcg)":1,"Vit C (mg)":1.3,"Vit D (mcg)":0,"Vit E (mg)":0.7,"Vit K (mcg)":2.7,"Vit B1 (mg)":0.34,"Vit B2 (mg)":0.15,"Vit B3 (mg)":1.13,"Vit B5 (mg)":0.57,"Vit B6 (mg)":0.54,"Vit B9 (mcg)":98,"Vit B12 (mcg)":0},
    "minerals":{"Calcium (mg)":98,"Iron (mg)":2.9,"Magnesium (mg)":158,"Phosphorus (mg)":346,"Potassium (mg)":441,"Sodium (mg)":2,"Zinc (mg)":3.09,"Selenium (mcg)":4.9},
    "amino":   {"Tryptophan (mg)":170,"Threonine (mg)":596,"Isoleucine (mg)":625,"Leucine (mg)":1170,"Lysine (mg)":424,"Methionine (mg)":236,"Phenylalanine (mg)":711,"Valine (mg)":753,"Histidine (mg)":391},
    "fats":    {"Saturated (g)":6.13,"Monounsat (g)":8.93,"Polyunsat (g)":47.17,"Omega-3 (g)":9.08,"Omega-6 (g)":38.09}},

  "Pistachios":    {"category":"Nut","calories":562,
    "macro":   {"Protein (g)":20.6,"Carbs (g)":27.7,"Fat (g)":45.4,"Fiber (g)":10.3,"Sugar (g)":7.7},
    "vitamins":{"Vit A (mcg)":26,"Vit C (mg)":5.6,"Vit D (mcg)":0,"Vit E (mg)":2.86,"Vit K (mcg)":13.2,"Vit B1 (mg)":0.87,"Vit B2 (mg)":0.16,"Vit B3 (mg)":1.3,"Vit B5 (mg)":0.52,"Vit B6 (mg)":1.7,"Vit B9 (mcg)":51,"Vit B12 (mcg)":0},
    "minerals":{"Calcium (mg)":105,"Iron (mg)":3.9,"Magnesium (mg)":121,"Phosphorus (mg)":490,"Potassium (mg)":1025,"Sodium (mg)":1,"Zinc (mg)":2.2,"Selenium (mcg)":7},
    "amino":   {"Tryptophan (mg)":260,"Threonine (mg)":695,"Isoleucine (mg)":895,"Leucine (mg)":1542,"Lysine (mg)":1139,"Methionine (mg)":335,"Phenylalanine (mg)":1073,"Valine (mg)":1175,"Histidine (mg)":498},
    "fats":    {"Saturated (g)":5.44,"Monounsat (g)":23.3,"Polyunsat (g)":13.74,"Omega-3 (g)":0.259,"Omega-6 (g)":13.48}},

  # ════════════════════════════════════════════════════════════════════════════
  # SEEDS
  # ════════════════════════════════════════════════════════════════════════════
  "Chia Seeds":    {"category":"Seed","calories":486,
    "macro":   {"Protein (g)":16.5,"Carbs (g)":42.1,"Fat (g)":30.7,"Fiber (g)":34.4,"Sugar (g)":0.0},
    "vitamins":{"Vit A (mcg)":54,"Vit C (mg)":1.6,"Vit D (mcg)":0,"Vit E (mg)":0.5,"Vit K (mcg)":0,"Vit B1 (mg)":0.62,"Vit B2 (mg)":0.17,"Vit B3 (mg)":8.83,"Vit B5 (mg)":0.94,"Vit B6 (mg)":0.19,"Vit B9 (mcg)":49,"Vit B12 (mcg)":0},
    "minerals":{"Calcium (mg)":631,"Iron (mg)":7.7,"Magnesium (mg)":335,"Phosphorus (mg)":860,"Potassium (mg)":407,"Sodium (mg)":16,"Zinc (mg)":4.58,"Selenium (mcg)":55.9},
    "amino":   {"Tryptophan (mg)":436,"Threonine (mg)":564,"Isoleucine (mg)":800,"Leucine (mg)":1369,"Lysine (mg)":970,"Methionine (mg)":588,"Phenylalanine (mg)":1028,"Valine (mg)":952,"Histidine (mg)":530},
    "fats":    {"Saturated (g)":3.33,"Monounsat (g)":2.31,"Polyunsat (g)":23.67,"Omega-3 (g)":17.83,"Omega-6 (g)":5.84}},

  "Flaxseeds":     {"category":"Seed","calories":534,
    "macro":   {"Protein (g)":18.3,"Carbs (g)":28.9,"Fat (g)":42.2,"Fiber (g)":27.3,"Sugar (g)":1.5},
    "vitamins":{"Vit A (mcg)":0,"Vit C (mg)":0.6,"Vit D (mcg)":0,"Vit E (mg)":0.31,"Vit K (mcg)":4.3,"Vit B1 (mg)":1.64,"Vit B2 (mg)":0.16,"Vit B3 (mg)":3.08,"Vit B5 (mg)":0.98,"Vit B6 (mg)":0.47,"Vit B9 (mcg)":87,"Vit B12 (mcg)":0},
    "minerals":{"Calcium (mg)":255,"Iron (mg)":5.7,"Magnesium (mg)":392,"Phosphorus (mg)":642,"Potassium (mg)":813,"Sodium (mg)":30,"Zinc (mg)":4.34,"Selenium (mcg)":25.4},
    "amino":   {"Tryptophan (mg)":297,"Threonine (mg)":769,"Isoleucine (mg)":893,"Leucine (mg)":1235,"Lysine (mg)":862,"Methionine (mg)":370,"Phenylalanine (mg)":953,"Valine (mg)":980,"Histidine (mg)":483},
    "fats":    {"Saturated (g)":3.66,"Monounsat (g)":7.53,"Polyunsat (g)":28.73,"Omega-3 (g)":22.81,"Omega-6 (g)":5.9}},

  "Sesame Seeds":  {"category":"Seed","calories":573,
    "macro":   {"Protein (g)":17.7,"Carbs (g)":23.5,"Fat (g)":49.7,"Fiber (g)":11.8,"Sugar (g)":0.3},
    "vitamins":{"Vit A (mcg)":9,"Vit C (mg)":0.0,"Vit D (mcg)":0,"Vit E (mg)":0.25,"Vit K (mcg)":0,"Vit B1 (mg)":0.79,"Vit B2 (mg)":0.25,"Vit B3 (mg)":4.52,"Vit B5 (mg)":0.05,"Vit B6 (mg)":0.79,"Vit B9 (mcg)":97,"Vit B12 (mcg)":0},
    "minerals":{"Calcium (mg)":975,"Iron (mg)":14.6,"Magnesium (mg)":351,"Phosphorus (mg)":629,"Potassium (mg)":468,"Sodium (mg)":11,"Zinc (mg)":7.75,"Selenium (mcg)":34.4},
    "amino":   {"Tryptophan (mg)":330,"Threonine (mg)":742,"Isoleucine (mg)":758,"Leucine (mg)":1358,"Lysine (mg)":568,"Methionine (mg)":586,"Phenylalanine (mg)":938,"Valine (mg)":982,"Histidine (mg)":519},
    "fats":    {"Saturated (g)":6.96,"Monounsat (g)":18.76,"Polyunsat (g)":21.77,"Omega-3 (g)":0.38,"Omega-6 (g)":21.38}},

  # ── Indian seeds ──
  "Fenugreek Seeds": {"category":"Seed","calories":323,
    "macro":   {"Protein (g)":23.0,"Carbs (g)":58.4,"Fat (g)":6.4,"Fiber (g)":24.6,"Sugar (g)":0.0},
    "vitamins":{"Vit A (mcg)":3,"Vit C (mg)":3.0,"Vit D (mcg)":0,"Vit E (mg)":0.0,"Vit K (mcg)":0,"Vit B1 (mg)":0.32,"Vit B2 (mg)":0.37,"Vit B3 (mg)":1.64,"Vit B5 (mg)":0.0,"Vit B6 (mg)":0.6,"Vit B9 (mcg)":57,"Vit B12 (mcg)":0},
    "minerals":{"Calcium (mg)":176,"Iron (mg)":33.5,"Magnesium (mg)":191,"Phosphorus (mg)":296,"Potassium (mg)":770,"Sodium (mg)":67,"Zinc (mg)":2.5,"Selenium (mcg)":6.3},
    "amino":   {"Tryptophan (mg)":232,"Threonine (mg)":809,"Isoleucine (mg)":1034,"Leucine (mg)":1561,"Lysine (mg)":1490,"Methionine (mg)":221,"Phenylalanine (mg)":1011,"Valine (mg)":1102,"Histidine (mg)":571},
    "fats":    {"Saturated (g)":1.46,"Monounsat (g)":1.4,"Polyunsat (g)":1.97,"Omega-3 (g)":0.0,"Omega-6 (g)":1.97}},

  "Mustard Seeds": {"category":"Seed","calories":508,
    "macro":   {"Protein (g)":26.1,"Carbs (g)":28.1,"Fat (g)":36.2,"Fiber (g)":12.2,"Sugar (g)":6.8},
    "vitamins":{"Vit A (mcg)":31,"Vit C (mg)":7.1,"Vit D (mcg)":0,"Vit E (mg)":5.07,"Vit K (mcg)":5.4,"Vit B1 (mg)":0.81,"Vit B2 (mg)":0.26,"Vit B3 (mg)":4.73,"Vit B5 (mg)":0.81,"Vit B6 (mg)":0.4,"Vit B9 (mcg)":162,"Vit B12 (mcg)":0},
    "minerals":{"Calcium (mg)":266,"Iron (mg)":9.2,"Magnesium (mg)":370,"Phosphorus (mg)":828,"Potassium (mg)":738,"Sodium (mg)":13,"Zinc (mg)":6.08,"Selenium (mcg)":208},
    "amino":   {"Tryptophan (mg)":285,"Threonine (mg)":928,"Isoleucine (mg)":1078,"Leucine (mg)":1805,"Lysine (mg)":1237,"Methionine (mg)":503,"Phenylalanine (mg)":1123,"Valine (mg)":1292,"Histidine (mg)":594},
    "fats":    {"Saturated (g)":1.99,"Monounsat (g)":22.52,"Polyunsat (g)":10.09,"Omega-3 (g)":5.9,"Omega-6 (g)":4.19}},

  # ════════════════════════════════════════════════════════════════════════════
  # LEGUMES
  # ════════════════════════════════════════════════════════════════════════════
  "Chickpeas":     {"category":"Legume","calories":164,
    "macro":   {"Protein (g)":8.9,"Carbs (g)":27.4,"Fat (g)":2.6,"Fiber (g)":7.6,"Sugar (g)":4.8},
    "vitamins":{"Vit A (mcg)":1,"Vit C (mg)":1.3,"Vit D (mcg)":0,"Vit E (mg)":0.35,"Vit K (mcg)":4,"Vit B1 (mg)":0.12,"Vit B2 (mg)":0.06,"Vit B3 (mg)":0.53,"Vit B5 (mg)":0.29,"Vit B6 (mg)":0.14,"Vit B9 (mcg)":172,"Vit B12 (mcg)":0},
    "minerals":{"Calcium (mg)":49,"Iron (mg)":2.9,"Magnesium (mg)":48,"Phosphorus (mg)":168,"Potassium (mg)":291,"Sodium (mg)":7,"Zinc (mg)":1.53,"Selenium (mcg)":3.7},
    "amino":   {"Tryptophan (mg)":93,"Threonine (mg)":376,"Isoleucine (mg)":401,"Leucine (mg)":683,"Lysine (mg)":624,"Methionine (mg)":102,"Phenylalanine (mg)":533,"Valine (mg)":431,"Histidine (mg)":253},
    "fats":    {"Saturated (g)":0.27,"Monounsat (g)":0.58,"Polyunsat (g)":1.16,"Omega-3 (g)":0.05,"Omega-6 (g)":1.1}},

  "Black Beans":   {"category":"Legume","calories":132,
    "macro":   {"Protein (g)":8.9,"Carbs (g)":23.7,"Fat (g)":0.5,"Fiber (g)":8.7,"Sugar (g)":0.3},
    "vitamins":{"Vit A (mcg)":0,"Vit C (mg)":0.0,"Vit D (mcg)":0,"Vit E (mg)":0.87,"Vit K (mcg)":5.6,"Vit B1 (mg)":0.24,"Vit B2 (mg)":0.06,"Vit B3 (mg)":0.51,"Vit B5 (mg)":0.42,"Vit B6 (mg)":0.07,"Vit B9 (mcg)":149,"Vit B12 (mcg)":0},
    "minerals":{"Calcium (mg)":27,"Iron (mg)":2.1,"Magnesium (mg)":70,"Phosphorus (mg)":140,"Potassium (mg)":355,"Sodium (mg)":1,"Zinc (mg)":1.12,"Selenium (mcg)":1.2},
    "amino":   {"Tryptophan (mg)":95,"Threonine (mg)":381,"Isoleucine (mg)":400,"Leucine (mg)":723,"Lysine (mg)":602,"Methionine (mg)":126,"Phenylalanine (mg)":527,"Valine (mg)":472,"Histidine (mg)":264},
    "fats":    {"Saturated (g)":0.13,"Monounsat (g)":0.04,"Polyunsat (g)":0.22,"Omega-3 (g)":0.18,"Omega-6 (g)":0.04}},

  "Soybeans":      {"category":"Legume","calories":173,
    "macro":   {"Protein (g)":16.6,"Carbs (g)":9.9,"Fat (g)":9.0,"Fiber (g)":6.0,"Sugar (g)":3.0},
    "vitamins":{"Vit A (mcg)":1,"Vit C (mg)":6.0,"Vit D (mcg)":0,"Vit E (mg)":0.35,"Vit K (mcg)":33,"Vit B1 (mg)":0.44,"Vit B2 (mg)":0.28,"Vit B3 (mg)":0.4,"Vit B5 (mg)":0.15,"Vit B6 (mg)":0.38,"Vit B9 (mcg)":165,"Vit B12 (mcg)":0},
    "minerals":{"Calcium (mg)":102,"Iron (mg)":5.1,"Magnesium (mg)":86,"Phosphorus (mg)":245,"Potassium (mg)":515,"Sodium (mg)":1,"Zinc (mg)":1.15,"Selenium (mcg)":7.3},
    "amino":   {"Tryptophan (mg)":237,"Threonine (mg)":756,"Isoleucine (mg)":907,"Leucine (mg)":1383,"Lysine (mg)":1108,"Methionine (mg)":252,"Phenylalanine (mg)":897,"Valine (mg)":905,"Histidine (mg)":501},
    "fats":    {"Saturated (g)":1.3,"Monounsat (g)":1.98,"Polyunsat (g)":5.06,"Omega-3 (g)":0.6,"Omega-6 (g)":4.47}},

  # ── Indian legumes ──
  "Black-eyed Peas": {"category":"Legume","calories":116,
    "macro":   {"Protein (g)":7.7,"Carbs (g)":20.8,"Fat (g)":0.5,"Fiber (g)":6.5,"Sugar (g)":3.3},
    "vitamins":{"Vit A (mcg)":1,"Vit C (mg)":0.4,"Vit D (mcg)":0,"Vit E (mg)":0.0,"Vit K (mcg)":1.7,"Vit B1 (mg)":0.2,"Vit B2 (mg)":0.05,"Vit B3 (mg)":0.52,"Vit B5 (mg)":0.41,"Vit B6 (mg)":0.1,"Vit B9 (mcg)":208,"Vit B12 (mcg)":0},
    "minerals":{"Calcium (mg)":24,"Iron (mg)":2.5,"Magnesium (mg)":53,"Phosphorus (mg)":156,"Potassium (mg)":278,"Sodium (mg)":4,"Zinc (mg)":1.29,"Selenium (mcg)":2.5},
    "amino":   {"Tryptophan (mg)":83,"Threonine (mg)":312,"Isoleucine (mg)":361,"Leucine (mg)":613,"Lysine (mg)":563,"Methionine (mg)":101,"Phenylalanine (mg)":442,"Valine (mg)":390,"Histidine (mg)":218},
    "fats":    {"Saturated (g)":0.13,"Monounsat (g)":0.04,"Polyunsat (g)":0.23,"Omega-3 (g)":0.07,"Omega-6 (g)":0.16}},

  "Moth Beans":    {"category":"Legume","calories":343,
    "macro":   {"Protein (g)":22.9,"Carbs (g)":62.1,"Fat (g)":1.6,"Fiber (g)":10.8,"Sugar (g)":0.0},
    "vitamins":{"Vit A (mcg)":3,"Vit C (mg)":2.0,"Vit D (mcg)":0,"Vit E (mg)":0.0,"Vit K (mcg)":0,"Vit B1 (mg)":0.35,"Vit B2 (mg)":0.18,"Vit B3 (mg)":2.1,"Vit B5 (mg)":0.0,"Vit B6 (mg)":0.38,"Vit B9 (mcg)":149,"Vit B12 (mcg)":0},
    "minerals":{"Calcium (mg)":150,"Iron (mg)":8.0,"Magnesium (mg)":220,"Phosphorus (mg)":339,"Potassium (mg)":1096,"Sodium (mg)":30,"Zinc (mg)":2.68,"Selenium (mcg)":2.0},
    "amino":   {"Tryptophan (mg)":232,"Threonine (mg)":875,"Isoleucine (mg)":956,"Leucine (mg)":1730,"Lysine (mg)":1555,"Methionine (mg)":174,"Phenylalanine (mg)":1168,"Valine (mg)":1094,"Histidine (mg)":601},
    "fats":    {"Saturated (g)":0.42,"Monounsat (g)":0.13,"Polyunsat (g)":0.73,"Omega-3 (g)":0.22,"Omega-6 (g)":0.51}},

  # ════════════════════════════════════════════════════════════════════════════
  # LENTILS
  # ════════════════════════════════════════════════════════════════════════════
  "Green Lentils": {"category":"Lentil","calories":116,
    "macro":   {"Protein (g)":9.0,"Carbs (g)":20.1,"Fat (g)":0.4,"Fiber (g)":7.9,"Sugar (g)":1.8},
    "vitamins":{"Vit A (mcg)":1,"Vit C (mg)":1.5,"Vit D (mcg)":0,"Vit E (mg)":0.11,"Vit K (mcg)":1.7,"Vit B1 (mg)":0.17,"Vit B2 (mg)":0.07,"Vit B3 (mg)":1.06,"Vit B5 (mg)":0.64,"Vit B6 (mg)":0.18,"Vit B9 (mcg)":181,"Vit B12 (mcg)":0},
    "minerals":{"Calcium (mg)":19,"Iron (mg)":3.3,"Magnesium (mg)":36,"Phosphorus (mg)":180,"Potassium (mg)":369,"Sodium (mg)":2,"Zinc (mg)":1.27,"Selenium (mcg)":2.8},
    "amino":   {"Tryptophan (mg)":76,"Threonine (mg)":366,"Isoleucine (mg)":432,"Leucine (mg)":699,"Lysine (mg)":624,"Methionine (mg)":77,"Phenylalanine (mg)":483,"Valine (mg)":477,"Histidine (mg)":271},
    "fats":    {"Saturated (g)":0.05,"Monounsat (g)":0.07,"Polyunsat (g)":0.19,"Omega-3 (g)":0.04,"Omega-6 (g)":0.15}},

  "Red Lentils":   {"category":"Lentil","calories":116,
    "macro":   {"Protein (g)":9.0,"Carbs (g)":20.1,"Fat (g)":0.4,"Fiber (g)":7.9,"Sugar (g)":1.8},
    "vitamins":{"Vit A (mcg)":1,"Vit C (mg)":1.5,"Vit D (mcg)":0,"Vit E (mg)":0.11,"Vit K (mcg)":1.7,"Vit B1 (mg)":0.17,"Vit B2 (mg)":0.07,"Vit B3 (mg)":1.06,"Vit B5 (mg)":0.64,"Vit B6 (mg)":0.18,"Vit B9 (mcg)":181,"Vit B12 (mcg)":0},
    "minerals":{"Calcium (mg)":19,"Iron (mg)":3.3,"Magnesium (mg)":36,"Phosphorus (mg)":180,"Potassium (mg)":369,"Sodium (mg)":2,"Zinc (mg)":1.27,"Selenium (mcg)":2.8},
    "amino":   {"Tryptophan (mg)":76,"Threonine (mg)":366,"Isoleucine (mg)":432,"Leucine (mg)":699,"Lysine (mg)":624,"Methionine (mg)":77,"Phenylalanine (mg)":483,"Valine (mg)":477,"Histidine (mg)":271},
    "fats":    {"Saturated (g)":0.05,"Monounsat (g)":0.07,"Polyunsat (g)":0.19,"Omega-3 (g)":0.04,"Omega-6 (g)":0.15}},

  # ── Indian dals ──
  "Chana Dal":     {"category":"Lentil","calories":360,
    "macro":   {"Protein (g)":20.5,"Carbs (g)":59.8,"Fat (g)":5.6,"Fiber (g)":16.0,"Sugar (g)":0.0},
    "vitamins":{"Vit A (mcg)":2,"Vit C (mg)":0.0,"Vit D (mcg)":0,"Vit E (mg)":0.0,"Vit K (mcg)":0,"Vit B1 (mg)":0.41,"Vit B2 (mg)":0.15,"Vit B3 (mg)":1.74,"Vit B5 (mg)":0.0,"Vit B6 (mg)":0.54,"Vit B9 (mcg)":557,"Vit B12 (mcg)":0},
    "minerals":{"Calcium (mg)":202,"Iron (mg)":5.3,"Magnesium (mg)":115,"Phosphorus (mg)":312,"Potassium (mg)":846,"Sodium (mg)":6,"Zinc (mg)":3.43,"Selenium (mcg)":8.2},
    "amino":   {"Tryptophan (mg)":196,"Threonine (mg)":731,"Isoleucine (mg)":836,"Leucine (mg)":1390,"Lysine (mg)":1187,"Methionine (mg)":186,"Phenylalanine (mg)":1025,"Valine (mg)":875,"Histidine (mg)":486},
    "fats":    {"Saturated (g)":0.58,"Monounsat (g)":1.24,"Polyunsat (g)":2.52,"Omega-3 (g)":0.1,"Omega-6 (g)":2.42}},

  "Urad Dal":      {"category":"Lentil","calories":341,
    "macro":   {"Protein (g)":25.2,"Carbs (g)":59.6,"Fat (g)":1.6,"Fiber (g)":18.3,"Sugar (g)":0.0},
    "vitamins":{"Vit A (mcg)":0,"Vit C (mg)":0.0,"Vit D (mcg)":0,"Vit E (mg)":0.0,"Vit K (mcg)":0,"Vit B1 (mg)":0.27,"Vit B2 (mg)":0.25,"Vit B3 (mg)":1.5,"Vit B5 (mg)":0.0,"Vit B6 (mg)":0.28,"Vit B9 (mcg)":149,"Vit B12 (mcg)":0},
    "minerals":{"Calcium (mg)":138,"Iron (mg)":7.6,"Magnesium (mg)":267,"Phosphorus (mg)":379,"Potassium (mg)":983,"Sodium (mg)":38,"Zinc (mg)":3.35,"Selenium (mcg)":0},
    "amino":   {"Tryptophan (mg)":239,"Threonine (mg)":868,"Isoleucine (mg)":1028,"Leucine (mg)":1715,"Lysine (mg)":1612,"Methionine (mg)":196,"Phenylalanine (mg)":1200,"Valine (mg)":1148,"Histidine (mg)":616},
    "fats":    {"Saturated (g)":0.42,"Monounsat (g)":0.13,"Polyunsat (g)":0.73,"Omega-3 (g)":0.22,"Omega-6 (g)":0.51}},

  "Moong Dal":     {"category":"Lentil","calories":347,
    "macro":   {"Protein (g)":24.0,"Carbs (g)":59.9,"Fat (g)":1.2,"Fiber (g)":16.3,"Sugar (g)":0.0},
    "vitamins":{"Vit A (mcg)":114,"Vit C (mg)":4.8,"Vit D (mcg)":0,"Vit E (mg)":0.0,"Vit K (mcg)":0,"Vit B1 (mg)":0.62,"Vit B2 (mg)":0.23,"Vit B3 (mg)":2.25,"Vit B5 (mg)":0.0,"Vit B6 (mg)":0.38,"Vit B9 (mcg)":625,"Vit B12 (mcg)":0},
    "minerals":{"Calcium (mg)":132,"Iron (mg)":6.7,"Magnesium (mg)":189,"Phosphorus (mg)":367,"Potassium (mg)":1246,"Sodium (mg)":15,"Zinc (mg)":2.68,"Selenium (mcg)":8.2},
    "amino":   {"Tryptophan (mg)":247,"Threonine (mg)":851,"Isoleucine (mg)":984,"Leucine (mg)":1698,"Lysine (mg)":1625,"Methionine (mg)":228,"Phenylalanine (mg)":1232,"Valine (mg)":1114,"Histidine (mg)":598},
    "fats":    {"Saturated (g)":0.35,"Monounsat (g)":0.16,"Polyunsat (g)":0.53,"Omega-3 (g)":0.14,"Omega-6 (g)":0.39}},

  # ════════════════════════════════════════════════════════════════════════════
  # GRAINS
  # ════════════════════════════════════════════════════════════════════════════
  "Brown Rice":    {"category":"Grain","calories":112,
    "macro":   {"Protein (g)":2.6,"Carbs (g)":23.0,"Fat (g)":0.9,"Fiber (g)":1.8,"Sugar (g)":0.4},
    "vitamins":{"Vit A (mcg)":0,"Vit C (mg)":0.0,"Vit D (mcg)":0,"Vit E (mg)":0.11,"Vit K (mcg)":1.9,"Vit B1 (mg)":0.18,"Vit B2 (mg)":0.02,"Vit B3 (mg)":2.97,"Vit B5 (mg)":0.6,"Vit B6 (mg)":0.15,"Vit B9 (mcg)":9,"Vit B12 (mcg)":0},
    "minerals":{"Calcium (mg)":10,"Iron (mg)":0.5,"Magnesium (mg)":44,"Phosphorus (mg)":83,"Potassium (mg)":79,"Sodium (mg)":5,"Zinc (mg)":0.63,"Selenium (mcg)":9.8},
    "amino":   {"Tryptophan (mg)":30,"Threonine (mg)":94,"Isoleucine (mg)":107,"Leucine (mg)":210,"Lysine (mg)":89,"Methionine (mg)":55,"Phenylalanine (mg)":135,"Valine (mg)":147,"Histidine (mg)":63},
    "fats":    {"Saturated (g)":0.18,"Monounsat (g)":0.33,"Polyunsat (g)":0.32,"Omega-3 (g)":0.02,"Omega-6 (g)":0.3}},

  "Oats":          {"category":"Grain","calories":389,
    "macro":   {"Protein (g)":16.9,"Carbs (g)":66.3,"Fat (g)":6.9,"Fiber (g)":10.6,"Sugar (g)":0.0},
    "vitamins":{"Vit A (mcg)":0,"Vit C (mg)":0.0,"Vit D (mcg)":0,"Vit E (mg)":0.42,"Vit K (mcg)":2,"Vit B1 (mg)":0.76,"Vit B2 (mg)":0.14,"Vit B3 (mg)":0.96,"Vit B5 (mg)":1.35,"Vit B6 (mg)":0.12,"Vit B9 (mcg)":56,"Vit B12 (mcg)":0},
    "minerals":{"Calcium (mg)":54,"Iron (mg)":4.7,"Magnesium (mg)":177,"Phosphorus (mg)":523,"Potassium (mg)":429,"Sodium (mg)":2,"Zinc (mg)":4.0,"Selenium (mcg)":28.9},
    "amino":   {"Tryptophan (mg)":234,"Threonine (mg)":588,"Isoleucine (mg)":694,"Leucine (mg)":1284,"Lysine (mg)":701,"Methionine (mg)":312,"Phenylalanine (mg)":895,"Valine (mg)":937,"Histidine (mg)":405},
    "fats":    {"Saturated (g)":1.22,"Monounsat (g)":2.18,"Polyunsat (g)":2.54,"Omega-3 (g)":0.11,"Omega-6 (g)":2.42}},

  "Quinoa":        {"category":"Grain","calories":120,
    "macro":   {"Protein (g)":4.4,"Carbs (g)":21.3,"Fat (g)":1.9,"Fiber (g)":2.8,"Sugar (g)":0.9},
    "vitamins":{"Vit A (mcg)":1,"Vit C (mg)":0.0,"Vit D (mcg)":0,"Vit E (mg)":0.63,"Vit K (mcg)":0,"Vit B1 (mg)":0.1,"Vit B2 (mg)":0.11,"Vit B3 (mg)":0.41,"Vit B5 (mg)":0.26,"Vit B6 (mg)":0.12,"Vit B9 (mcg)":42,"Vit B12 (mcg)":0},
    "minerals":{"Calcium (mg)":17,"Iron (mg)":1.5,"Magnesium (mg)":64,"Phosphorus (mg)":152,"Potassium (mg)":172,"Sodium (mg)":7,"Zinc (mg)":1.09,"Selenium (mcg)":5.3},
    "amino":   {"Tryptophan (mg)":52,"Threonine (mg)":153,"Isoleucine (mg)":175,"Leucine (mg)":283,"Lysine (mg)":239,"Methionine (mg)":70,"Phenylalanine (mg)":220,"Valine (mg)":210,"Histidine (mg)":127},
    "fats":    {"Saturated (g)":0.23,"Monounsat (g)":0.53,"Polyunsat (g)":1.08,"Omega-3 (g)":0.26,"Omega-6 (g)":0.82}},

  # ── Indian grains ──
  "Jowar (Sorghum)": {"category":"Grain","calories":329,
    "macro":   {"Protein (g)":11.3,"Carbs (g)":72.6,"Fat (g)":3.3,"Fiber (g)":6.3,"Sugar (g)":0.0},
    "vitamins":{"Vit A (mcg)":0,"Vit C (mg)":0.0,"Vit D (mcg)":0,"Vit E (mg)":0.0,"Vit K (mcg)":0,"Vit B1 (mg)":0.24,"Vit B2 (mg)":0.14,"Vit B3 (mg)":2.92,"Vit B5 (mg)":0.0,"Vit B6 (mg)":0.44,"Vit B9 (mcg)":0,"Vit B12 (mcg)":0},
    "minerals":{"Calcium (mg)":25,"Iron (mg)":4.4,"Magnesium (mg)":165,"Phosphorus (mg)":287,"Potassium (mg)":350,"Sodium (mg)":6,"Zinc (mg)":1.67,"Selenium (mcg)":0},
    "amino":   {"Tryptophan (mg)":107,"Threonine (mg)":358,"Isoleucine (mg)":430,"Leucine (mg)":1340,"Lysine (mg)":212,"Methionine (mg)":148,"Phenylalanine (mg)":507,"Valine (mg)":549,"Histidine (mg)":226},
    "fats":    {"Saturated (g)":0.46,"Monounsat (g)":0.99,"Polyunsat (g)":1.43,"Omega-3 (g)":0.06,"Omega-6 (g)":1.37}},

  "Ragi (Finger Millet)": {"category":"Grain","calories":328,
    "macro":   {"Protein (g)":7.3,"Carbs (g)":72.0,"Fat (g)":1.3,"Fiber (g)":3.6,"Sugar (g)":0.0},
    "vitamins":{"Vit A (mcg)":0,"Vit C (mg)":0.0,"Vit D (mcg)":0,"Vit E (mg)":0.0,"Vit K (mcg)":0,"Vit B1 (mg)":0.33,"Vit B2 (mg)":0.11,"Vit B3 (mg)":1.1,"Vit B5 (mg)":0.0,"Vit B6 (mg)":0.12,"Vit B9 (mcg)":0,"Vit B12 (mcg)":0},
    "minerals":{"Calcium (mg)":344,"Iron (mg)":3.9,"Magnesium (mg)":137,"Phosphorus (mg)":283,"Potassium (mg)":408,"Sodium (mg)":11,"Zinc (mg)":2.3,"Selenium (mcg)":0},
    "amino":   {"Tryptophan (mg)":107,"Threonine (mg)":270,"Isoleucine (mg)":364,"Leucine (mg)":854,"Lysine (mg)":195,"Methionine (mg)":214,"Phenylalanine (mg)":445,"Valine (mg)":476,"Histidine (mg)":176},
    "fats":    {"Saturated (g)":0.19,"Monounsat (g)":0.24,"Polyunsat (g)":0.64,"Omega-3 (g)":0.07,"Omega-6 (g)":0.57}},

  # ════════════════════════════════════════════════════════════════════════════
  # CEREALS
  # ════════════════════════════════════════════════════════════════════════════
  "Bran Flakes":   {"category":"Cereal","calories":319,
    "macro":   {"Protein (g)":7.5,"Carbs (g)":68.0,"Fat (g)":1.9,"Fiber (g)":15.0,"Sugar (g)":15.0},
    "vitamins":{"Vit A (mcg)":0,"Vit C (mg)":0.0,"Vit D (mcg)":0,"Vit E (mg)":0.0,"Vit K (mcg)":0,"Vit B1 (mg)":0.72,"Vit B2 (mg)":0.85,"Vit B3 (mg)":9.5,"Vit B5 (mg)":0.61,"Vit B6 (mg)":0.92,"Vit B9 (mcg)":195,"Vit B12 (mcg)":1.5},
    "minerals":{"Calcium (mg)":40,"Iron (mg)":13.0,"Magnesium (mg)":80,"Phosphorus (mg)":350,"Potassium (mg)":550,"Sodium (mg)":600,"Zinc (mg)":3.8,"Selenium (mcg)":5.0},
    "amino":   {"Tryptophan (mg)":100,"Threonine (mg)":270,"Isoleucine (mg)":302,"Leucine (mg)":552,"Lysine (mg)":260,"Methionine (mg)":148,"Phenylalanine (mg)":390,"Valine (mg)":388,"Histidine (mg)":183},
    "fats":    {"Saturated (g)":0.3,"Monounsat (g)":0.25,"Polyunsat (g)":0.8,"Omega-3 (g)":0.05,"Omega-6 (g)":0.75}},

  "Granola":       {"category":"Cereal","calories":471,
    "macro":   {"Protein (g)":7.8,"Carbs (g)":60.0,"Fat (g)":18.0,"Fiber (g)":5.2,"Sugar (g)":22.0},
    "vitamins":{"Vit A (mcg)":0,"Vit C (mg)":0.0,"Vit D (mcg)":0,"Vit E (mg)":0.42,"Vit K (mcg)":0,"Vit B1 (mg)":0.32,"Vit B2 (mg)":0.1,"Vit B3 (mg)":1.3,"Vit B5 (mg)":0.5,"Vit B6 (mg)":0.1,"Vit B9 (mcg)":30,"Vit B12 (mcg)":0},
    "minerals":{"Calcium (mg)":50,"Iron (mg)":3.0,"Magnesium (mg)":80,"Phosphorus (mg)":200,"Potassium (mg)":280,"Sodium (mg)":55,"Zinc (mg)":1.5,"Selenium (mcg)":13.0},
    "amino":   {"Tryptophan (mg)":105,"Threonine (mg)":270,"Isoleucine (mg)":310,"Leucine (mg)":578,"Lysine (mg)":284,"Methionine (mg)":150,"Phenylalanine (mg)":410,"Valine (mg)":420,"Histidine (mg)":188},
    "fats":    {"Saturated (g)":2.9,"Monounsat (g)":8.5,"Polyunsat (g)":4.3,"Omega-3 (g)":0.3,"Omega-6 (g)":4.0}},
}


def get_chart_data(selected_foods):
    """Return JSON with all nutrient groups for all selected foods,
    sorted alphabetically by food name."""
    foods = sorted([f for f in selected_foods if f in FOODS])
    first = list(FOODS.values())[0]
    # Get all nutrient group keys from the first entry
    macro_keys   = list(first["macro"].keys())
    vitamin_keys = list(first["vitamins"].keys())
    mineral_keys = list(first["minerals"].keys())
    amino_keys   = list(first["amino"].keys())
    fat_keys     = list(first["fats"].keys())

    result = {
        "foods":        foods,
        "macro_keys":   macro_keys,
        "vitamin_keys": vitamin_keys,
        "mineral_keys": mineral_keys,
        "amino_keys":   amino_keys,
        "fat_keys":     fat_keys,
        "macro":    {n: [FOODS[f]["macro"][n]    for f in foods] for n in macro_keys},
        "vitamins": {n: [FOODS[f]["vitamins"][n]  for f in foods] for n in vitamin_keys},
        "minerals": {n: [FOODS[f]["minerals"][n]  for f in foods] for n in mineral_keys},
        "amino":    {n: [FOODS[f]["amino"][n]     for f in foods] for n in amino_keys},
        "fats":     {n: [FOODS[f]["fats"][n]      for f in foods] for n in fat_keys},
        "calories": [FOODS[f]["calories"] for f in foods],
    }
    return json.dumps(result)