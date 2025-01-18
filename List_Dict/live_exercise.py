## What is a list?
# In python a list have the symbol= []
# In python a dictionary have the symbol= {}
# list of numbers: A1 =[1,2]
# list of str: A2 =['1','2','not well']
# mix list: A3 =[1,2,'1','2',1.5,'name']

## Length of a list is the total numbers of items in the list:
# Length of A1 =2, A2 =3 and A3=6

######### A string have a length as well
# B ='I am not' B2 = '1', B4=' 24 years'
# The length of theses strings are:
# B=8, B2=1 and B4=9
# To estimate length, you use len()
A1 =[1,2]
print(f"What is the length of A1: {len(A1)}")
A2 =['1','2','not well']
print(f"What is the length of A2: {len(A2)}")
A3 =[1,2,'1','2',1.5,'name']
print(f"What is the length of A3: {len(A3)}")
############################
B1 ='I am not' 
B2 = '1'
B3=' 24 years'
fullname= 'Sheb Michel'
# Find the length of these strings, B1, B2 and B3?

print(f"What is the length of this sentence <{B1}>: {len(B1)}")
print(f"What is the length of this sentence <{B2}>: {len(B2)}")
print(f"What is the length of this sentence <{B3}>: {len(B3)}")

print(f"What is the length of my full name <{fullname}>: {len(fullname)}")