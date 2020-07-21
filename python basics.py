# multi line string
#text = '''
#line one
#line two
#line three
#'''
#print(text)

# printing tricks
#random = 'ending'
#print(random[-1])
#print(random[0:3])

# from 1th to end
#print(random[1:])
# from 1th to the end -1
#print(random[1:-1])



# formatted string
#first = 'john'
#last = 'thomasson'
#print (f'{first} [{last}] is a coder')


#find index of 'n' in a string. if no such letter is present,
#it returns -1
#.find('n')
#.find('fullword')

#.replace('old_word', 'new_word')
#.upper()

# True or False
#print('john' in first)

# 10 // 3 = 3
# 10 /3 = 3.33333333
# 10 ** 3 = 10 to the poewr of 3


# project 1
#house = 1000000
#down_payment = 0.2*house
#good_credit = False
#if good_credit:
#  down_payment = 0.1*house
#print("You need to pay" + str(down_payment))



# project 2
#has_high_income = True
#criminal = False
#if has_high_income and not criminal:
#  print("Eligible for loan")


# project 3
#weight = input("Weight: ")
#weight_type = input("(L)bs or (K)gs: ")

#if weight_type.upper() == 'K':
#  print(f'{float(weight)*2.2} lbs')
#else:
#  print(f'{float(weight)*0.45} kgs')


#i = 1
#while i<=5:
#  print(i)
#  i = i + 1

"""
car game
instructions = '''start - starts the engine
stop - stops the engine
quit - quits the game'''
choice = ''
engine = 0

while choice != "QUIT":
  choice = input().upper()

  if engine == 1 and choice == 'START':
    print('already started')
  
  if engine == 0 and choice == 'STOP':
    print('already stopped')

  
  if choice == "START" and engine == 0 :
    print('starting the engine... ready to go!')
    engine = 1

  if choice == "STOP" and engine == 1:
    print('stopping the engine...')
    engine = 0 

  if choice == "HELP":
    print(instructions)
  
  if choice != "HELP" and choice != "START" and choice != "STOP" and choice != "QUIT":
    print('i dont understand that!')

"""


"""
for item in range(5,10,2):
  print(item)
"""



"""
price = 0
prices = [10, 20, 30]
for item in prices:
  price += item

print(price)
"""


"""
numbers = [1,1,1,1,1,1,1,7]
for item in numbers:
  x = ''
  for i in range(item):
    x+='x'
  print(x)
"""


#lists
numbers = [4, 2, 10, 20, 14]
largest = 0

for i in numbers:
  if i > largest:
    largest = i

print(largest)
