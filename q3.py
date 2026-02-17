luggage = [100, 200, 50, 150, 100]
current_weight = 0

for weight in luggage:
    item = input(f"Next bag is {weight} kg. Add to elevator? (yes/no): ")
    if item.lower() != "yes":
        print("Bag skipped.")
        continue
    if current_weight + weight > 500:
        print("Elevator Full.")
        break
    current_weight += weight

print(f"Total weight: {current_weight} kg")