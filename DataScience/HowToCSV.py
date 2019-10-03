import csv

with open('marks.csv') as file:
    readCSV = csv.reader(file, delimiter=",")
    names = []
    nums = []
    aList = []
    bList = []
    max = 0

    for row in readCSV:
        name = row[0]
        a = row[1]
        b = row[2]

        c = int(a)+int(b)

        names.append(name)
        nums.append(c)
        aList.append(a)
        bList.append(b)

    file.close()
    
    for i, v in enumerate(nums):
        if nums[i] > max:
            max = nums[i]
            a = i

print(names[a] + " " + aList[a] + " " + bList[a])

textFile = open("marks.txt","w")
textFile.write("The student with the highest score:\n")
textFile.write(names[a] + " " + aList[a] + " " + bList[a])
textFile.close()