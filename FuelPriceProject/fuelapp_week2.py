# http://workshop.robin.com.au/chat/week3
##list

no_numbers = [] # empty list
numbers = [1, 2, 3]

things = [1, 'abc', [4, 'xyz']]

first_number = things[0]
second_item = things[1]

print(first_number)
print(second_item)

third_item = things[2]
print(third_item)

xyz = third_item[1]

print('----')
print(xyz)
print(things[2][1])

things.append('4th item')

print('there are', len(things), 'number of things')
print('things have', things)
print('Done with part 1')
print('###############')
##############
people = [
  ['Robin', 43, 'red'],
  ['John', 34, 'blue'],
]
print(people[0][2])
print('Done with part 2')
print('###############')
#############################
l = [2, 3, 4, 5]
l2 = []

for i in l:
  print(i)
  j = i + 1
  l2.append(j)
print('here is the appended list: ',l2)
print('Done with part 3')
print('###############')
###############
l = ['first', 'second']
l2 = []
for s in l:
  l2.append(s + '_word')
print(l2)
print('Done with part 4')
print('###############')
###############
print('Now joinning Lists')

# Note that l1 and l2 does not change but l3 contains 6 items.

l1 = [1, 2 ,3]
l2 = [10, 11 ,12]
l3 = l1 + l2 # Now l3 contains [1, 2, 3, 10, 11, 12]
print(l3)
print('Done with part 5')
print('###############')
###############
print('We are doing dictionaries now')
# DICTIONARIES

empty_dic = {}


person = ['Robin', 44, 'blue']
person2 = ['Mary', 55, 'blue', ]

person = {
  'name': 'Robin',
  'age': 44,
  'fav_colour': 'blue'
}

# person as list?
plist = ['Robin', 44]
print(plist[0])

print(person['name'], person['age'])

network = {
  'people': [
    {'name': 'Mary', 'age': 54},
    person,
    {'name': 'James', 'age': 45},
  ],
  'version': 1,
}      
people_list = network['people']

third_person = people_list[2]
print(third_person)
print('Done with part 6')
print('###############')
# Exercise:
# So how do you dynamically generate a list of ages?

## 
person = {
  'name': 'Robin',
  'age': 45,
  'friends': [
    {'name': 'John', 'age': 44},
    {'name': 'Mary', 'age': 23}
  ]
}
friends = person['friends']
print(friends[1]['age'])
print('Done with part 7')
print('###############')

## Setting new dictionary key values
person={'name': 'Robin'}

print(person)

person['fav_colour'] = 'blue'
  
print(person)

person2 = {**person,'age':12}
print(person)
print(person2)
print('Done with part 8')
print('###############')
###################################
print('we are sorting now: ')
from pprint import pprint
l1 = [{'name': 'Robin', 'age': 44}, {'name': 'John', 'age': 22}, {'name': 'Mary', 'age': 33}]

def by_age(item):
   # print(type(item))
   # print(item)
   return item['age']

sorted_l1 = sorted(l1, key=by_age)

pprint(l1)
print('-----------')
pprint(sorted_l1)

for x in l1:
    print(x['age'])
print('Done with part 9')
print('###############')
#####################
# SORTING EXAMPLE FOR DINETH


def by(ite):
  print(ite, type(ite))
  return ite[1]

l = [['xand', 1], ['zgan', 6], ['aten', 3]]
new_list = sorted(l, key=by)

print('----')
print(new_list)
print('Done with part 9')
print('###############')

#####################################
print('We are now using functions now: ')

import feedparser

product_id = 1
url = 'http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product='+str(product_id)+'&Suburb=Cloverdale'
data = feedparser.parse(url)
u_prices = data['entries']

print(data)

product_id = 2
url = 'http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product='+str(product_id)+'&Suburb=Cloverdale'
data = feedparser.parse(url)
pu_prices = data['entries']

print(u_prices)
print(pu_prices)
print('Done with part 10')
print('###############')

#####################################
people = [{'name': 'Robin', 'age': 99}, {'name': 'Kevin', 'age': 1}, {'name': 'Jane', 'age': 50}]

def get_people():
  return people

def get_people(older_than):
  new_people = []
  for person in people:
    if person['age'] > older_than:
      new_people.append(person)
      
  return new_people

print(get_people(0))
print(get_people(5))
print(get_people(50))

print('---')

def say(word):
  if word.lower() == 'shit':
    print('DO NOT USE SWEAR WORDS!')
  else:
    print('You said: ' + word)
  
say('Hello')
say('How are you?')
say('Shit')

print('Done with part 10')
print('###############')

########################################
print('side notes')
# list
l = [1,2]
print(l)
l.append(3)
print(l)

# tuple
t = (1,2)
print(t)
# t.append() does not work
t2 = t + (3,) # Note that the comma is necessary, it's a quirk of Python
print(t2)
print('Done with part 11')
print('###############')

##################
print('confusing tuples')
a = 1
b  = 1,
c = (1,)

print(a, type(a))
print(b, type(b))
print(c, type(c))
print('Done with part 12')
print('###############')
#############################
print('Looping Dictionary now: ')

person = {'name': 'Robin', 'age': 66}
keys = []
for key in person:
  keys.append(key)
  
print(keys)
print(person.keys())

##
person = {'name': 'Robin', 'age': 66}

values = []
for key in person:
  print(key)
  values.append( person[key] ) # <<<
  
print(values)

values = []
for key, value in person.items():
  values.append( value ) # <<<
  
print(values)

print(person.values())

####
d = {'abc': 3, 'xyz': 13 }

print(d['xyz'])
l = [1,2,3]
print(l)

#####for ANA
person2 = {
    'name': 'John',
    'age': 22,
    'friends': [
        {
            'name': 'Mary',
            'age': 43,
        },
        {
            'name': 'James',
            'age': 32,
        }
    ],
}

p2_friends = person2['friends']

print("person2's second friend's name is ", person2['friends'][1]['name'])
print('Done with part 13')
print('###############')

#################################
print('Looping the python way now')
# The non-python way
l = ['abc', 'xyz']

print(range(0, len(l)))

for i in range(0, len(l)):
  print(i)
  if i == 0:
    print('first', l[i])
  else:
    print('rest', l[i])
#Run
# The Python way
l = ['abc', 'xyz']

for item in l:
  print('each', item)
  
##

print(enumerate(l))
  
for i, item in enumerate(l):
  if i == 0:
    print('first', item)
  else:
    print('rest', item)
    
##

print('first', l[0])
    
for i, item in enumerate(l[1:]):
  print('rest', item)

print('Done with part 14')
print('###############')
##############################################
l1 = []
i = 234
s = 'text'

people_list = [11, 12, 13, 'blue', ['a', 'b'], s, i]

sub_list = people_list[4]
# print(sub_list[1])

# print(people_list[4][1])


robin = ['Robin', 66, 'blue']
john = ['John', 33, 'red']

people_list = [
    robin,
    john,
    ['Mary', 22, 'yellow']
]

#print(people_list[1][2])

robin = {'name': 'Robin', 'age': 66, 'fav_colour': 'blue'}

john = {
    'name': 'John',
    'age': 44,
    'fav_colour': 'red',
    'pets': [
        {'type': 'dog', 'name': 'Lucky'},
        {'type': 'cat', 'name': 'Mango'},
    ]
}

people_list = [robin, john, {'name': 'Mary', 'age': 22, 'fav_colour': 'yellow'}]

from pprint import pprint
#pprint(people_list)


second_person = people_list[1]


"""
print(second_person)

print(second_person['fav_colour'])

print(people_list[1]['fav_colour'])
"""

for person in people_list:
    person['has_drivers_licence'] = True
    person['fav_colour'] = 'green'

pprint(people_list)
print('Done with part 15')
print('###############')
##############################################
print('# CONVERTING LIST OF LIST TO LIST OF DICTINOARIES')
robin = ['Robin', 66, 'blue']
john = ['John', 33, 'red']

people_list = [
    robin,
    john,
    ['Mary', 22, 'yellow']
]

# print(people_list)

people_dicts = []

for p in people_list:
    d = {
        'name': p[0],
        'age': p[1],
    }
    people_dicts.append(d)

for p in people_list:
    people_dicts.append({
        'name': p[0],
        'age': p[1],
    })

from pprint import pprint
pprint(people_dicts)
print('Done with part 16')
print('###############')
##################
from pprint import pprint
robin = {
    'friends': [
        {'first_name': 'Mary', 'last_name': 'Jane', 'fav_colour': 'red'},
        {'first_name': 'John', 'last_name': 'Done', 'fav_colour': 'blue'},
        {'first_name': 'Dave', 'last_name': 'Lee', 'fav_colour': 'green'},
    ],
}

people = robin['friends']

people_with_full_names_only = []

for person in people:
    people_with_full_names_only.append({
        'full_name': person['first_name'] + ' ' + person['last_name']
    })

pprint(people_with_full_names_only)
############################
print('Only 3 stations in Bentley')

import feedparser
from pprint import pprint

feed1 = feedparser.parse('http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=1&Suburb=Bentley&Surrounding=no')

pprint(feed1)
#Run
import feedparser
import json

feed1 = feedparser.parse('http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=1&Suburb=Bentley&Surrounding=no')

print(json.dumps(feed1, indent=2))