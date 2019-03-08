
# A Dictionary Example
# creat a maooing of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a set of state and cities in them

cities = {
    'CA' : 'San Fracisco',
    'MI' : 'Detroit',
    'FL' : 'Jacksoncille'
}

#add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'portland'

#print out some cities
print('_ '* 10)
print("NY state has: ", cities['NY'])
print("OR state has: ", cities['OR'])
 # print some states

print('-'* 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

#do it by using state then dict
print('..' *10)

print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

print(':-' * 10)

for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

# print every city in state
print('- ' * 10)

for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# Now do both at the same time
print('- ' * 15)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('- ' * 20)

state = states.get('Texas')
if not state:
    print("Sorry, no Texas.")
# get a city with a default value

city = cities.get('TX', 'No Texas.')
print(f"The city for the state 'TX' is: {city}" )
