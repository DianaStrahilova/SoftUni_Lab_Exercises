import math

budget = float(input())

price_per_kg_flour = float(input())

pack_eggs_price = price_per_kg_flour * 0.75
price_milk = price_per_kg_flour + price_per_kg_flour * 0.25


loaf_price = price_per_kg_flour + pack_eggs_price + (price_milk * 0.25)

loaves_made = math.floor(budget / loaf_price)
colored_eggs = 0
money_left = budget - loaves_made * loaf_price

for current_loaf in range(1, loaves_made + 1):
    colored_eggs += 3
    if current_loaf % 3 == 0:
        colored_eggs -= current_loaf - 2


print(f"You made {loaves_made} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left:.2f}BGN left.")

