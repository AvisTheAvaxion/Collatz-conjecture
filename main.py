from time import sleep
ogNum = int(input("Number: "))
num = ogNum

while True:
  if num % 2 == 0:
    num = num / 2
  
  else:
    num = ((3*num)+1)
  
  num = int(num)
  print(str(num) + ": " + ("*" * num))
  sleep(.1)
  if num == 1:
    print("Completed")
    break