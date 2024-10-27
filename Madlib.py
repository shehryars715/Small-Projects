import random

adjective = input("Give an adjective ")
noun = input("Give a noun ")

l1 = f"The {adjective} dragon flew over the quiet {noun}, searching for a delicious snack to eat."
l2 = f"On a {adjective} afternoon, a brave {noun} set out on a dangerous quest to find the legendary treasure."
l3 = f"In the {adjective} forest, a curious {noun} discovered a hidden path leading to an ancient castle."
l4 = f"The {adjective} puppy chased the bouncing {noun} across the green field, barking with joy."
l5 = f"At the {adjective} market, a friendly {noun} sold fresh vegetables and colorful fruits to eager customers."

madlib = random.choice([l1, l2 , l3, l4, l5])

print(madlib)