# Tony Yu
# 11/23/17
# Story Generator 2.0!
# Version 0.7.2
import time

print("="*50)
print("Welcome to Billy's Story Generator!")
print("="*50)

time.sleep(1)
print()

print("You will have to enter about 15 different words to generate the story")

time.sleep(1)
print()

print("Ok! Let's get started.")

time.sleep(0.5)
print()

animal_1 = input("Please enter an animal: ")

time.sleep(0.5)
print()
      
name_1 = input("Please enter a name: ")

time.sleep(0.5)
print()

food_1 = input("How about a food: ")

time.sleep(0.5)
print()

verb_1 = input("Now enter a verb that describes something you would do to a food: ")

time.sleep(0.5)
print()

place_1 = input ("Now enter a place: ")

time.sleep(0.5)
print()

vehicle_1 = input("Now enter a vehicle: ")

time.sleep(0.5)
print()

animal_2 = input("How 'bout another animal: ")

time.sleep(0.5)
print()

greeting_1 = input("Now enter a greeting: ")

print()

time.sleep(0.5)
print()

verb_2 = input("How about another eating verb: ")

time.sleep(0.5)
print()

time_1 = input("Now enter a unit of time: ")

time.sleep(0.5)
print()

animal_3 = input("How about ANOTHER animal: ")

time.sleep(0.5)
print()

restaurant_1 = input("Now enter a name of a restaurant that has the food you entered: ")

time.sleep(0.8)

print("generating story",end='')
time.sleep(0.4)
print(".",end='')
time.sleep(0.4)
print(".",end='')
time.sleep(0.4)
print(".",end='')

time.sleep(0.4)
print()
print()

print("Once upon a time, there was a "  + animal_1.lower() + " named " + name_1 + 
". He really wanted to " + verb_1.lower() + " " + food_1.lower() + ". Unfortunatly, " /
+ food_1.lower() + " could not be found in the land that " + name_1 + " lived in!" 
+ " However, " + name_1 + " heard from his friend that " + food_1.lower() + 
" could be found in " + place_1 + ". So, he packed up all his stuff and took a "
+ vehicle_1.lower() + " to " + place_1 + ". When he arrived, he looked around and saw a "
+ animal_2.lower() + " walking around! He was about to say " + greeting_1 + " to the " + animal_2.lower() /
+ " when he noticed the " + animal_2.lower() + " was " + verb_2.lower() + " a " + 
food_1.lower() + "! " + name_1 + " continued on with saying " + greeting_1 + " to the " + animal_2.lower()
+ " but it glared at " + name_1 + " and ran away. " + name_1 + """ sighed and started walking around aimlessly. 
 After a few """ + time_1 + "s " + name_1 " saw a " + animal_3.upper() + " with some" + food_1.lower() +
". " + name_1 + " started running over to the " + animal_3.upper() + " and asked it where it got the " + food_1.lower() +
". It said it got it from a " + restaurant_1 + " nearby! " + name_1 + "ran into it, asked for some of the " + food_1 +
", waited a one " + time_1 ", and finally got some" + food_1 + "! " + name_1 + """ savoured the smell, and then finally ate it!
It tasted awesome, and """ + name_1 + " ordered some more " + food_1 + " to take home, and then went home to live there hapilly ever after.")
