# Create a tuple named zoo that contains your favorite animals.
zoo = tuple(('Lion', 'Tiger', 'Bear', 'Monkey', 'Rabbit'))
# Find one of your animals using the .index(value) method on the tuple.
print(zoo.index('Lion'))
# Determine if an animal is in your tuple by using value in tuple.
if 'Lion' in zoo:
    print("There animal exists at this zoo.")
# Create a variable for each of the animals in your tuple with this cool feature of Python.
(lizard, fox, mammoth, wolf, yak) = zoo
print(lizard)
# Convert your tuple into a list.
zoo_list = list(zoo)
print('tuple to list', zoo_list)
# Use extend() to add three more animals to your zoo.
zoo_list.extend(['Dolphin', 'Crab', 'Rhino'])
print(zoo_list)
# Convert the list back into a tuple.
zoo = tuple(zoo_list)
print('back to tuple', zoo)