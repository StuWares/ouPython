# swap the conents of a list without making any extra lists

gloves = [5, 3, 8, 10]
print("Original list:" + str(gloves))
temp = gloves[0]
gloves[0] = gloves[3]
gloves[3] = temp
temp = gloves[1]
gloves[1] = gloves[2]
gloves[2] = temp
print("Reversed list:" + str(gloves))
