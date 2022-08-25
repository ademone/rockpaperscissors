import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
rangeint = (len(names) - 1)
listnum = random.randint(0,rangeint)
print(listnum)

whopays = names[listnum]
print(f"{whopays} is going to buy the meal today!") 