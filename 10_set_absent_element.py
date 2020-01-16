"""
10. Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2. 
Test Data : 
color_list_1 = set(["White", "Black", "Red"]) 
"""


def data_absent_in_second(set1, set2):  # function to check data which is not present in second set
    new_list = []
    for color in set1:
        if color not in set2:
            new_list.append(color)
    new_set = set(new_list)
    print(new_set)


color_set_1 = {"White", "Black", "Red"}_
color_set_2 = {"Red", "Green"}
print(color_set_1)
data_absent_in_second(color_set_1, color_set_2)
