while True:
    n = int(input("How many elements? "))
    org_array = []
    for i in range(n):
        org_array.append(int(input("Enter element at "+str((i+1))+": ")))

    print("1. Bubble Sort.")
    print("2. Insertion Sort")
    choice = int(input("Enter your choice: "))
    if choice==1:
        l = list(org_array)
        print("List before sorting: ", l)
        n = len(l)
        count1=0
        for i in range(n):
            t=0
            
            for j in range(n-i-1):
                if l[j] > l[j+1]:   
                    t = l[j]
                    l[j] = l[j+1]
                    l[j+1] = t
                    
                count1 += 1
            
        print("List after sorting: ", l)
        print("Total number of steps: ", count1)
    elif choice==2:
        array = list(org_array)
        count2=0
        print("\nThe original list is: ", array)
        print("\nSorting Begins......")
        for i in range(1, n):
            key = array[i]
            j = i-1
            while j >=0 and key < array[j]:
                print("\t.")
                array[j+1] = array[j]
                j = j - 1
            count2 += 1
            array[j+1] = key
        print("\ndone.")
        print("The sorted list is: ", array)
        print("Total number of steps: ", count2)
    else:
        print("\nInvalid Choice!!!!")
    ch = input("\nDo you want to try again(y/n)? ")
    if ch=='y':
        continue
    else:
        print('Bye')
        break
