length = int(input())
for i in range(0,length): #More than 2 lines will result in 0 score. Do not leave a blank line also
    line = str(i)
    line = line * i
    print(line)