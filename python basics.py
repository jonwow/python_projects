# multi line string
text = '''
line one
line two
line three
'''
print(text)

# printing tricks
random = 'ending'
print(random[-1])
print(random[0:3])

# from 1th to end
print(random[1:])
# from 1th to the end -1
print(random[1:-1])



# formatted string
first = 'john'
last = 'thomasson'
print (f'{first} [{last}] is a coder')


#find index of 'n' in a string. if no such letter is present,
#it returns -1
#.find('n')
#.find('fullword')

#.replace('old_word', 'new_word')
#.upper()

# True or False
print('john' in first)

# 10 // 3 = 3
# 10 /3 = 3.33333333
# 10 ** 3 = 10 to the poewr of 3


# project 1
house = 1000000
down_payment = 0.2*house
good_credit = False
if good_credit:
  down_payment = 0.1*house
print("You need to pay" + str(down_payment))



# project 2
has_high_income = True
criminal = False
if has_high_income and not criminal:
  print("Eligible for loan")


# project 3
weight = input("Weight: ")
weight_type = input("(L)bs or (K)gs: ")

if weight_type.upper() == 'K':
  print(f'{float(weight)*2.2} lbs')
else:
  print(f'{float(weight)*0.45} kgs')