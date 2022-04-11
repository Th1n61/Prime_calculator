list = []
count = 1
number = int(input('''please enter the prime number you wish to find.
>'''))
numberOfMultipliers=0
number+=1
while True:
  
  for i in range(1,count+1):
    if count%i==0:
      numberOfMultipliers+=1
      
  if numberOfMultipliers<3:
    list.append(count)  
  else:
    pass
    
  numberOfMultipliers=0
  count += 1
  print("Count="+ str(count))
  if len(list)==number:
    break
print(list)