
import random
import time

# def roll_dice():
#     return random.randint(1, 6)
# Let define an empty list empty_list=[]
# def function_to_give_dice_results():
empty_list=[]
# to add something in a list we use [].append(a)
for i in range(5):
    my_dice_rol = random.randint(1, 6)
    #print("Rolling the dice...")
    print(f"For roll number= {i+1} dice show nbre= {my_dice_rol}")
    empty_list.append(my_dice_rol)
    print(f"Give me the list every time I roll the dice {empty_list}")
    time.sleep(6)
    #return empty_list
print(f"What is the the final list {empty_list}")

#dice_list = function_to_give_dice_results()
#print(f"What is the the final list {dice_list}")