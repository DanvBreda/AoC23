test = "n"
day = "01"

if test == "y":  
    file_name = "day"+day+"_test"
else:
    file_name = "day"+day

with open(file_name) as file:
    myList = [i for i in file.read().strip().split("\n")]

string = []

for row in myList:
    mini_int = []
    for i in row:
        if i.isdigit() == True:
            mini_int.append(i)
    string.append(mini_int)

integers = []

for i in string:
        integers.append(int(i[0]+i[-1]))

print("answer 1: "+str(sum(integers)))

if test == "y":  
    file_name = "day"+day+"_test2"
else:
    file_name = "day"+day

with open(file_name) as file:
    myList = [i for i in file.read().strip().split("\n")]

book = {"eight":"8","seven":"7","three":"3","nine":"9","five":"5","four":"4","six":"6","two":"2","one":"1"}
integers = []

for rows in myList:
    
    mini_list = []

    for i in range(len(rows)):
        if rows[i].isdigit() == True:
            mini_list.append(rows[i])
        elif rows[i:5+i] in book.keys():      
            mini_list.append(book[rows[i:5+i]])
        elif rows[i:4+i] in book.keys():      
            mini_list.append(book[rows[i:4+i]])
        elif rows[i:3+i] in book.keys():      
            mini_list.append(book[rows[i:3+i]])
    
    integers.append(int(mini_list[0]+mini_list[-1]))

print("answer 2: "+str(sum(integers)))