my_dict = {'name': 'Ahmed', 'age': 20, 'job': 'Engineer'}
print(my_dict.values())
print(my_dict.keys())
print(my_dict["name"])
my_dict["age"] = 32
my_dict["workplace"] = "GSG"
print(my_dict)
####################################################################
my_tuple = (('name', 'Ahmed'), ('age', 23), ('job', 'Doctor'))
my_dict = {}
for k, v in my_tuple:
    my_dict[v] = k
print(my_dict)
####################################################################
dic1 = {'name': 'Dema', 'age': 20}
dic2 = {'job': 'Engineer', 'ID': 456367}
dic3 = {'Year': 2003}
new_dict = {}
new_dict.update(dic1)
new_dict.update(dic2)
new_dict.update(dic3)
print(new_dict)
####################################################################
my_dict = {'num1': 648, 'num2': 4194, 'num3': 60}
print(f'Maximum value: {max(my_dict.values())}')
print(f'Minimum value: {min(my_dict.values())}')
####################################################################
my_dict = {'name': 'Abed', 'age': 31, 'job': 'Teacher'}
ID_check = 'ID' in my_dict.keys()
print(ID_check)
####################################################################
Languages2023 = {'Programming Language': ['python', 'Java', 'JavaScript', 'C#'],
                 'Market Share %': [27.99, 15.9, 9.36, 6.67]}
keys = Languages2023['Programming Language']
values = Languages2023['Market Share %']
result = [{'Programming Language': key, 'Market Share %': value} for key, value in zip(keys, values) ]
print(result)
####################################################################
