# dict { } set ([ ]) pay attention to the bracket
names=['Michael', 'Bob', 'Tracy']
scores=[95,75,85]
d={'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])
d['Adam']=67
print(d['Adam'])
print(d.get('Thomas'))
print(d.pop('Bob'))
print(d)
s=set([1, 1, 2, 2, 3, 3])
print(s)
s.add(4)
print(s)
s.remove(4)
print(s)
s1=set([1, 2, 3])
s2=set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)
