string= [[5,2,3],[10,8,9]]

students = [{'first_name': 'Michael', 'last_name' : 'Jordan'},
{'first_name' : 'John', 'last_name' : 'Rosales'}]

sports_directory = {'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
'soccer' : ['Messi', 'Ronaldo', 'Rooney']}

z= [ {'x': 10, 'y': 20} ]
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# # Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].

def replace(string):
    for i in range(len(string)):
        for j in range(len(string[i])):
            if(string[i][j] == 10):
                string[i][j] = 15
                return string
    return string
print(replace(string))
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Change the last_name of the first student from 'Jordan' to 'Bryant'

def replace(students): 
    for i in range(len(students)):
        if students[i]['first_name'] == 'Michael':
            students[i]['last_name'] ='Bryant'
            return students
    return students
print(replace(students))
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# In the sports_directory, change 'Messi' to 'Andres'

def replace(sports_directory):
    for i in (sports_directory.values()):
        for val in range(len(i)):
            if i[val] == 'Messi':
                i[val] = 'Andres'
            print(i[val])
    return
print(replace(sports_directory))

sports_directory['soccer'][0]= 'Andres'
print(sports_directory['soccer'][0])
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Change the value 20 in z to 30

z[0]["y"]=30
print(z)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Iterate Through a List of Dictionaries
# Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key
# and the associated value. For example, given the following list:


students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
# iterateDictionary(students) 
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

def call(students):
    for i in (students):
            print(i)
print (call(students))
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Get Values From a List of Dictionaries
# Create a function iterateDictionary2(key_name, some_list) that, given a list of 
# dictionaries and a key name, the function prints the value stored in that key
# for each dictionary. For example, iterateDictionary2('first_name', students) 
# should output:

# Michael
# John
# Mark
# KB
# Jordan
# Rosales
# Guillen
# Tonel


def first_name(students):
    for i in range(len(students)):
        print (students[i]['first_name'])
        # print (students[i].keys())

def last_name(students):
    for i in range(len(students)):
        print (students[i]['last_name'])

first_name(students)
last_name(students)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Create a function printInfo(some_dict) that given a dictionary whose values are all
# lists, prints the name of each key along with the size of its list, and then prints
# the associated values within each key's list. For example:
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
# printInfo(dojo)
# # output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank

# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon

def compile(sports_directory):
    x=(sports_directory['basketball'])
    print(f"there are {len(x)} players in basketball")
    print(x)
    i=(sports_directory['soccer'])
    print(f"there are {len(i)} players in Soccer")
    print(i)

compile(sports_directory)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
