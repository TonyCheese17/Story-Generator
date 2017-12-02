# Tony Yu
# 11/23/17
# Story Generator 2.0!
# Version 0.4.1
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

verb_1 = input("Now enter a verb: ")

time.sleep(0.5)
print()

place_1 = input ("Now enter a place: ")

time.sleep(0.5)
print()

vehicle_1 = input("Now enter a vehicle: ")

time.sleep(0.5)
print()

animal_2 = input("How 'bout another animal: ")

print()

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
". He really wanted to " + verb_1.lower() + " " + food_1.lower() + ". Unfortunatly, "
+ food_1.lower() + " could not be found in the land that " + name_1 + " lived in!"
+ " However, " + name_1 + " heard from his friend that " + food_1.lower() +
" could be found in " + place_1 + ". So, he packed up all his stuff and took a "
+ vehicle_1.lower() + " to " + place_1 + ". When he arrived, he looked around and saw a "
+ animal_2 + " walking around!")
