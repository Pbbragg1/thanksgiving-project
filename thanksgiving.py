import math
import os
import time

def welcome():
    input('''Hi I'm here to help you figure out how to plan for your thanksgiving dinner
press enter to continue ''')
def pick(opt):
    picked = []
    for i in opt:
        error = True
        while error:
            temp = input(f"Would you like to have {i} at Thanksgiving? ")
            if temp == "yes":
                picked.append(i)
                error = False
            elif temp == "no":
                error = False
                pass
            else:
                input('''please try again, select either yes or no
press enter to continue > ''')
    return picked
def clean_count():
    count_error = True
    while count_error:
        try:
            count = input("How many people, including yourself do you plan on having for dinner? ")
            count = int(count)
            if count == 0:
                raise ValueError
        except ValueError:
            input('''please enter a valid number
    please press enter to continue ''')
            continue
        if type(count) == int:
            return count
def cost(picked_food, price, count):
    out = 0
    for i in range(0, len(picked_food)):
        out += (price[picked_food[i]] * count[i])
    out = round(out, 2)
    return out

def items_needed(count, food_serves, foods_picked):
    items = []
    for food in foods_picked:
        items.append(int(math.ceil(count / food_serves[food])))
    return items
    
        

def app():
    food_price = {"turkey":26.56, "mashed potatoes":3.24, "pumpkin pie":5.87, "dinner roll":3.24, "mac and cheese":8.73}
    food_serves = {"turkey":12, "mashed potatoes":5, "pumpkin pie":6, "dinner roll":12, "mac and cheese":7}
    foods_picked = pick(food_price)
    count = clean_count()
    items = items_needed(count, food_serves, foods_picked)
    for i in range(0, len(foods_picked)):
        if items[i] == 1:
            print(f"You will need {items[i]} {foods_picked[i]}, ${food_price[foods_picked[i]]}")
        else:
            print(f"You will need {items[i]} {foods_picked[i]}'s, ${food_price[foods_picked[i]]}")
    price = cost(foods_picked, food_price, items)
    print(f"In total you will owe: ${price}")

if __name__ == "__main__":
    os.system("clear")
    welcome()
    os.system("clear")
    Play = True
    while Play:
        app()
        play = False
        while play != "yes" or play != "no":
            play = input("Do you need help with anything else? ")
            if play == "yes":
                os.system("clear")
                break
            elif play == "no":
                Play = False
                os.system("clear")
                break
            else:
                input('''please enter yes or no
press enter to continue''')
    print("Thank you for letting me help, I hope you have a great thanksgiving!")
    time.sleep(4)
    os.system("clear")
