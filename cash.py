from cs50 import get_float

# Prompt user for amount of change
while True:
    change_owed = get_float("Change Owed: ")
    if change_owed >= 0:
        break

# convert change  owed to cents
change_owed_cents = round(change_owed * 100)

# start cents to customer to 0
num_coins = 0

# calculate number of coins needed
while change_owed_cents > 0:
    if change_owed_cents >= 25:
        change_owed_cents -= 25
        num_coins += 1
    elif change_owed_cents >= 10:
        change_owed_cents -= 10
        num_coins += 1
    elif change_owed_cents >= 5:
        change_owed_cents -= 5
        num_coins += 1
    else:
        change_owed_cents -= 1
        num_coins += 1

# print number of coins
print(num_coins)
