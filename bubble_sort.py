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

# Short Bubble para com as trocas no momento que descobre que a lista está ordenada, sem realizar mais trocas desnecessárias
def shortBubble(list):
  exchanges = True
  passnum = len(list) - 1
  while passnum > 0 and exchanges:
    exchanges = False
    for i in range(passnum):
      if list[i] > list[i+1]:
        exchanges = True
        temp = list[i]
        list[i] = list[i+1]
        list[i+1] = temp
    passnum = passnum - 1

list = [4,3,78,2,0,2]
shortBubble(list)
print(list)