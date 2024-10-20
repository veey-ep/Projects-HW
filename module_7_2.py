from pprint import pprint

def custom_write(file_name, strings):
    strings_positions = {}
    nm = 1
    file = open(file_name, 'a', encoding='utf-8')
    for i in strings:
        bt = file.tell()
        pprint(file.write(f'{i}\n'))
        strings_positions.update({(nm, bt) : i})
        nm += 1
    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)

