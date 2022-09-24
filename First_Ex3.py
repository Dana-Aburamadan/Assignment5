#solution_1:
array =["7", "6", "5", "4", "2"]
result = array.reverse()
string = ""
for item in array:
    string += item
print(int(string))

#Solution_2:
number = "76542"
number_reversed = number[::-1]
num_reversed = int(number_reversed)
print(num_reversed)


