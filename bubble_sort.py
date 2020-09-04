def bubbleSort(list):
  for passnum in range(len(list)-1,0,-1):
    for i in range(passnum):
      if list[i]>list[i+1]:
        temp = list[i]
        list[i] = list[i+1]
        list[i+1] = temp

list = [4,3,78,2,0,2]
bubbleSort(list)
print(list)