d = {'name1': 'id1', 'name2': 'id2', 'name3': 'id3'}

t = d['name1']
d['name1'] = d['name2']
d['name2'] = d['name3']
d['name3'] = t

print(d)