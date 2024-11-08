my_dict = { 'carrot' : 22,  'pumpkin' : 33 }
print(my_dict)
print(my_dict['carrot'], my_dict.get('Orange'))
my_dict.update({'Hurma' : 44, 'Orange': 11})
print(my_dict.pop('carrot'))
print(my_dict)

my_set = {11, '11', True, (11 , 11)}
print(set(my_set))
my_set.add(5)
my_set.add("eleven")
my_set.remove(11)
print(my_set)