#Charles Ajjan
#Week 07
#Lab 01
#CMP 131
#Shipping Charges
#Date 10-21-2026 
import math

print("--- Fast Freight Shipping Calculator ---")

weight = float(input("Enter package weight (in kg): "))

if weight <= 0:
    print("Error: Weight must be greater than 0 kg.")
elif weight > 20:
    print("Error: We cannot ship packages over 20 kg.")
else:
    distance = float(input("Enter shipping distance (in miles): "))

    if distance <= 0:
        print("Error: Distance must be greater than 0 miles.")
    else:
        if weight <= 2:
            rate = 1.10
        elif weight <= 6:
            rate = 2.20
        elif weight <= 10:
            rate = 3.70
        else:
            rate = 4.80

        distance_units = math.ceil(distance / 500)
        total_cost = distance_units * rate

        print("\n================================")
        print("        SHIPPING SUMMARY        ")
        print("================================")
        print(f"Package Weight    : {weight:.2f} kg")
        print(f"Distance          : {distance:.2f} miles")
        print(f"Rate per 500 mi   : ${rate:.2f}")
        print(f"500-Mile Blocks   : {distance_units}")
        print("--------------------------------")
        print(f"Total Shipping Fee: ${total_cost:.2f}")
        print("================================")
