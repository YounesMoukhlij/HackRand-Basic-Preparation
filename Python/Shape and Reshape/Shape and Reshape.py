import numpy



inputNums = list(map(int, input().split()))


arr = numpy.array(inputNums)

try:
    newArr = numpy.reshape(arr, (3,3))
    print(newArr)
except Exception as e:
    print("Error:", e)
