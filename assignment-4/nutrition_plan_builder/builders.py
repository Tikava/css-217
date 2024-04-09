from typing import List
from nutrition_plan import NutritionPlan

class NutritionPlanBuilder:
    def __init__(self):
        self.nutrition_plan = NutritionPlan()
    
    def set_caloric_intake(self, caloric_intake: int):
        self.nutrition_plan.caloric_intake = caloric_intake
    
    def set_macronutrient_ratios(self, carbo_hydrates_ratio: int, proteins_ratio: int, fats_ratio: int):
        self.nutrition_plan.carbohydrates_ratio = carbo_hydrates_ratio
        self.nutrition_plan.proteins_ratio = proteins_ratio
        self.nutrition_plan.fats_ratio = fats_ratio
    
    def set_meal_plans(self, meal_plans: List[str]):
        self.nutrition_plan.meal_plans = meal_plans
    
    def set_fitness_goal(self, fitness_goal: str):
        self.nutrition_plan.fitness_goal = fitness_goal
    
    def set_dietary_restrictions(self, dietary_restrictions: List[str]):
        self.nutrition_plan.dietary_restrictions = dietary_restrictions
    
    def build(self) -> NutritionPlan:
        return self.nutrition_plan
    
        
class WeightLossNutritionPlanBuilder(NutritionPlanBuilder):
    def __init__(self):
        super().__init__()

class WeightGainNutritionPlanBuilder(NutritionPlanBuilder):
    def __init__(self):
        super().__init__()
        
class MaintenanceNutritionPlanBuilder(NutritionPlanBuilder):
    def __init__(self):
        super().__init__()