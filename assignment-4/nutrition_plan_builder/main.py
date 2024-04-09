from director import NutritionPlanDirector
from builders import WeightLossNutritionPlanBuilder

def main():
    director = NutritionPlanDirector()
    builder = WeightLossNutritionPlanBuilder()
    director.set_builder(builder)
    director.create_nutrition_plan()
    nutrition_plan = builder.build()
    print_nutrition_plan(nutrition_plan)
    
def print_nutrition_plan(nutrition_plan):
    print("Nutrition Plan:")
    print("Caloric Intake:", nutrition_plan.caloric_intake)
    print("Macronutrient Ratios (Carbs, Proteins, Fats):", nutrition_plan.carbohydrates_ratio, nutrition_plan.proteins_ratio, nutrition_plan.fats_ratio)
    print("Meal Plans:", nutrition_plan.meal_plans)
    print("Fitness Goal:", nutrition_plan.fitness_goal)
    print("Dietary Restrictions:", nutrition_plan.dietary_restrictions)
    
if __name__ == "__main__":
    main()
