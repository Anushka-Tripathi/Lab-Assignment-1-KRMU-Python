# Name: [Anushka Tripathi]
#Roll Number: 2501730077
# Date: 01-11-2025
# Title: Daily Calorie Tracker CLI Tool

print("Welcome to the Daily Calorie Tracker CLI Tool!")
print("Track your meals and calories easily.\n")

# Task 2: Input & Data Collection
meal_names = []
calorie_amounts = []

num_meals = int(input("Enter the number of meals you want to track: "))

for i in range(num_meals):
    meal = input(f"Enter meal name #{i+1}: ")
    calories = float(input(f"Enter calories for {meal}: "))
    meal_names.append(meal)
    calorie_amounts.append(calories)

# Task 3: Calorie calculations
total_calories = sum(calorie_amounts)
average_calories = total_calories / num_meals

daily_limit = float(input("\nEnter your daily calorie limit: "))

# Task 4: Limit Warning system
if total_calories > daily_limit:
    print("\nWarning: Your total calorie intake exceeds your daily limit!")
else:
    print("\nWell Done! Your calorie intake is within the daily limit.")

# Task 5: Formatted output
print("\nMeal Name\tCalories")
print("---------------------------")
for meal, cal in zip(meal_names, calorie_amounts):
    print(f"{meal:10}\t{cal:.2f}")
print("---------------------------")
print(f"{'Total':10}\t{total_calories:.2f}")
print(f"{'Average':10}\t{average_calories:.2f}")

# Task 6: Save to file
save_option = input("\nDo you want to save this data to a file? (yes/no): ").strip().lower()
if save_option == 'yes':
    filename = input("Enter the filename to save (e.g., calorie_report.txt): ")
    with open(filename, 'w') as file:
        file.write("Meal Name\tCalories\n")
        file.write("---------------------------\n")
        for meal, cal in zip(meal_names, calorie_amounts):
            file.write(f"{meal:10}\t{cal:.2f}\n")
        file.write("---------------------------\n")
        file.write(f"{'Total':10}\t{total_calories:.2f}\n")
        file.write(f"{'Average':10}\t{average_calories:.2f}\n")