
list1 = []

ascii_dict = {}
count_dict = {}

c = 1

check = 0

T = int(input("Enter the number of test cases:"))

for i in range(0, T):
    list1.append(input("Enter the string: "))
    
for i in range(97, 122+1):
    ascii_dict["%c"%i] = c
    c += 1
    


for i in range(0, len(list1)):
    a1 = list1[i]
    for j in range(0, len(a1)):
        if a1[j] not in count_dict:
            count_dict[a1[j]] = 1
        else:
            count_dict[a1[j]] += 1
            
    for k in count_dict:
        if count_dict[k] == ascii_dict[k]:
            check += 1
            
        
    if check == len(count_dict):
        print("yes")
    else:
        print("no")
        

    count_dict = {}
    check = 0
    
