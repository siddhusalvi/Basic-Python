"""
10. Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2. 
Test Data : 
color_list_1 = set(["White", "Black", "Red"]) 
"""
def data_not_present_in_second_set(set1,set2): #fuction to check data which is not present in second list
    list = []
    for color in set1:
        if color not in set2:
            list.append(color)
    new_set = (*list,)
    print(new_set)



color_set_1 = set(["White", "Black", "Red"])
color_set_2 = set(["Red", "Green"])
data_not_present_in_second_set(color_set_1,color_set_2)
     
