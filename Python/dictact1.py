'''
marks={}
n = int(input("How many users you need to add? "))
for i in range(n):
    student = input("\n\tEnter Student name: ")
    mark = int(input("\tEnter marks: "))
    count = len(marks)
    user = "user"+str(count+1)
    marks[user] = {"StudentName":student, "password":mark}

for j in marks.keys():
    print("\n\tName\tMarks")
    print("\t",marks[j]["StudentName"],"\t",marks[j]["password"])

'''
n = int(input("How many elements? "))
org_array = []
for i in range(n):
    org_array.append(int(input("Enter element at "+str((i+1))+": ")))

 

print("1. Bubble Sort.")
print("2. Insertion Sort")
choice = int(input("Enter your choice: "))
if choice==1:
    l = org_array
    print("Lits before sorting: ", l)
    n = len(l)
    for i in range(n):
        t=0
        for j in range(n-i-1):
            if l[j] > l[j+1]:   
                t = l[j]
                l[j] = l[j+1]
                l[j+1] = t
    print("List after sorting: ", l)
elif choice==2:
    arry = org_array
    print("\nThe original list is: ", array)
    print("\nSorting Begins......")
    for i in range(1, n):
        key = array[i]
        j = i-1
        while j >=0 and key < array[j]:
            print("\t.")
            array[j+1] = array[j]
            j = j - 1
        array[j+1] = key
    print("\ndone.")
    print("The sorted list is: ", array)
else:
    print("\nInvalid Choice!!!!")
