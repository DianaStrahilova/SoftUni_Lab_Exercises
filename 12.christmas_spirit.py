number_of_decorations = int(input())
days_left_until_christmas = int(input())

price_ornament_set = 2
price_tree_skirt  = 5
price_tree_garland = 3
price_tree_lights = 15

christmas_spirit_points = 0
total = 0

for day in range(1, days_left_until_christmas + 1):
    if day % 11 == 0:
        number_of_decorations += 2

    if day % 2 == 0:
        total += number_of_decorations * price_ornament_set
        christmas_spirit_points += 5

    if day % 3 == 0:
        total += (price_tree_skirt + price_tree_garland) * number_of_decorations
        christmas_spirit_points += 13

    if day % 5 == 0:
        total += price_tree_lights * number_of_decorations
        christmas_spirit_points += 17
        if day % 3 == 0:
            christmas_spirit_points += 30

    if day % 10 == 0:
        christmas_spirit_points -= 20
        total += price_tree_lights + price_tree_skirt + price_tree_garland

if days_left_until_christmas % 10 == 0:
    christmas_spirit_points -= 30

print(f"Total cost: {total}")
print(f"Total spirit: {christmas_spirit_points}")

