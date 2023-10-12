paradigm= [ 'p','a','r','a','d','i','g','m']
for x in paradigm:
     print (x)

numbers= ['0','1','2','3','4']
for x in numbers:
     print(x)

AnimalList = ['Cat','Dog','Tiger','Cow']
for x in AnimalList:
    print(x)

flowers = ['Jasmine','Lotus','Rose','Sunflower']
for x in flowers:
     print (x)

else:
     print ("Done")

list1= [5,10,15,20]
list2= ['tomatoes','potatoes','carrots','cucumbers']
for i in list1:
  for j in list2:
    print(i, j)
    
    
vehicles = ['Car','Cycle','Bus','Tempo']
for i in vehicles:
     if i == "Bus":
          continue
     print(i)

numbers = [12,3,56,67,89,90]
count = 0

list1 = ['Mango','Banana','Orange']
list2 = []
for i in list1:
     list2.append(i)
print(list2)

numbers = [1,4,50,80,12]
max = numbers[0]
for i in numbers:
    if i > max:
          max = i
print(max)

numbers = [1,4,50,80,12]
min = 1000
for i in numbers:
    if i < min:
        min = i
print(min)

numbers = [1,4,50,80,12]
numbers.sort ()
print(numbers)

numbers = [1,4,50,80,12]
numbers.sort(reverse=True)
print(numbers)

