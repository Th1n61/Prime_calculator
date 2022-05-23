import time
from math import ceil
list = []
count = 1
isNotPrime=False
number = int(input('''please enter the prime number you wish to find.
>'''))
numberOfMultipliers=0
number+=1
print('...')
timea=time.perf_counter()
while True:
  
  for i in range(1,ceil((count+1)/2)):
    if numberOfMultipliers==2:
      break
    if count%i==0:
      numberOfMultipliers+=1
      
  if numberOfMultipliers<2:
    list.append(count)  
  else:
    pass

    
  numberOfMultipliers=0
  count += 1
  if len(list)==number:
    break
print(list[number-1])
timeb=time.perf_counter()
print('it took about',round(timeb-timea),'seconds.')