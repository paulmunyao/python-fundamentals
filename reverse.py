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

# # create a for loop with a range
# for i in range(1500,2700):
#     # iterate over the list
#     if i % 5==0 and i % 7==0:
#         print(i)


# Formula for converting degrees to farenheit= (°C × 9/5) + 32 = 140°F
# Formula for converting farenheit to degrees (°F − 32) × 5/9 = °C
# create a variable for temperature input
print("Hi stranger")
ask = str(input("Do you want Celsius or Farenheit"))
temperature = int(input("Kindly input temperature: "))
# Create a variable for storing data from the input the input will be converted using a formula
temp = (temperature * 9/5) + 32
print(temp)
