#Charles Ajjan
#Week 07
#Lab 01
#CMP 131
#Date 10-21-2026
CALORIES_PER_MINUTE = 3.6

print(f"{'Minutes':<15} | {'Calories Burned':<15}")
print("-" * 33)

for minutes in range(5, 31, 5):
    calories_burned = minutes * CALORIES_PER_MINUTE
    print(f"{minutes:<15} | {calories_burned:<15.1f}")
