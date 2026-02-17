player = {"name": "Aragon", "level": 10, "health": 50}
item = input("What item does the player use? ")

if item.lower() == "healing potion":
    player["health"] += 20
    print("New health:", player["health"])
else:
    print("No effect. Health:", player["health"])