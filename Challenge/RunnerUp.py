def findSecond(arr):
    a = max(arr)
    for i in range(arr.count(a)):
    	arr.remove(a)
    b = max(arr)
    return b


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    print(findSecond(arr))

