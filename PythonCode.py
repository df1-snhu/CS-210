import re
import string


# Devin Foster
# CS 210
# 8/21/22
# 
# Project Three py file

def printsomething():
    print("Hello from python!")

def PrintMe(v):
    print("You sent me: " + v)
    return 100;

def SquareValue(v):
    return v * v

# prints frequency of each item in file
def CountAll(filename):
    item_list = {}

    # iterate through file
    with open(filename) as file:
        for line in file:
            # if item is in list, then add one to value
            if(line.strip() in item_list):
                item_list[line.strip()] += 1
            # if items is not in list, then item value = 1
            else:
                item_list[line.strip()] = 1

    # print each item and frequency
    for item, freq in item_list.items():
        print(item + " " + str(freq) + "\n")

# returns frequency of input item
def CountOne(item):
    count = 0
    with open("CS210_Project_Three_Input_File.txt") as file:
        for line in file:
            if(line.strip() == item.strip()):
                count += 1
    return count;

# Writes frequency.dat file based on Project Three input file
def WriteFile():
    item_list = {}

    with open("CS210_Project_Three_Input_File.txt") as file:
        for line in file:
            if(line.strip() in item_list):
                item_list[line.strip()] += 1
            else:
                item_list[line.strip()] = 1
                
    file = open("frequency.dat","x")
    # for each item in the project file, write the item and corresponding frequency
    for item, freq in item_list.items():
        file.write(item.strip() + " " + str(freq) + "\n")

