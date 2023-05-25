filename = 'sl.txt'


dict1 = {}


with open('sl.txt') as fh:
    for line in fh:

        command, description = line.strip().split(" - ")

        dict1[command] = description.strip()

out_file = open("test1.json", "w")
json.dump(dict1, out_file, ensure_ascii=False, indent=4, sort_keys=False)
out_file.close()

with open('test1.json', encoding='utf-8') as f:
    data = json.load(f)

new_dict = dict([(value, key) for key, value in data.items()])
print(new_dict)
new_d = list(new_dict.keys())
new_d.sort()
for i in new_d:
    f = (i, '-', new_dict[i])
    e = (' '.join(f))
    with open ('sl2.txt','a',encoding='utf-8') as file:
        file.write(e + '\n')
