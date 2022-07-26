# Reversing a list using the reversed method
# The output is mostly in a straightforward way going down
# creating a list of integers
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# print(list(reversed(list1)))- For the list to appear as a list
# using a for loop to iterate through the list
# for new in reversed(list):
#  print(new(list))

# Reversing using a for loop
# create a list of integers
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# Print the list
# print(list1)
# Create an empty list
# new_list = []
# iterating through the original list which had been created initially
# for new in list1:
# using insert method to insert the new item into the new list
# new_list.insert(0,new)
# print(new_list)

# Reversing a list using a while loop
# Create a new list
# list1= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# Create a new empty list
# list2=[]
# length=len(list1)
# while length > 0:
# add list1 to list2 using append function
# list2.append(list1[length-1])
# length = length - 1
# print(list2)

# create a for loop with a range
# for i in range(1500,2700):
# iterate over the list
# if i % 5==0 and i % 7==0:
# print(i)


# Formula for converting degrees to farenheit= (°C × 9/5) + 32 = 140°F
# Formula for converting farenheit to degrees (°F − 32) × 5/9 = °C
# create a variable for temperature input
# print("Hi stranger")
# temperature = int(input("Kindly input temperature: "))
# Create a variable for storing data from the input the input will be converted using a formula


# temperature = int(input("Kindly input temperature: "))
# faren = (temperature - 32) * 5/9
# print(faren)


# print("Enter 1 to change temperature from Fahrenheit to Celsius")
# print("Enter 2 to change temperature from Celsius to Fahrenheit")
# ch = int(input(""))
# if ch==1:
# ut= float(input("Enter Temperature in Fahrenheit: " ))
# ct=(ut-32)/1.8
# print(ct,"C")
# if ch==2:
# ut= float(input("Enter Temperature in Celsius: " ))
# ct=(1.8*ut)+32
# print(ct,"F")


# converting a list to a dictionary

# create a function

# create a list of ingredients
list = ['450 g long grain white rice, preferably basmati' + " \n",'75 ml vegetable oil', '2 medium onions, chopped', '1 medium chicken or 700â€“900 g lamb on the bone cut in pieces', '570 ml water, plus 110 ml water', 'peel of 1 large orange', '50 g sugar',
        '50 g blanched and flaked almonds', '50 g blanched and flaked pistachios', 'Â½ tsp saffron or egg yellow food colour  (optional)', '25 ml rosewater (optional)', '1 tsp ground green or white cardamom seeds  (optional)', 'salt and pepper']

dictOfWords = { i : list[i] for i in range(0, len(list) )}

print(dictOfWords)

