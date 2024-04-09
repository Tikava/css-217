from builders import NutritionPlanBuilder

class NutritionPlanDirector:
    def __init__(self):
        self.builder = None
    
    def set_builder(self, builder: NutritionPlanBuilder):
        self.builder = builder
    
    def create_nutrition_plan(self):
        self.builder.set_caloric_intake(2000)
        self.builder.set_macronutrient_ratios(40, 30, 30)
        self.builder.set_meal_plans(["Breakfast: ", "Lunch: ", "Dinner", "Snacks: "])
        self.builder.set_fitness_goal("weight loss")
        self.builder.set_dietary_restrictions([])