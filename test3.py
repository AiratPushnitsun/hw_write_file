general_text = {}

with open('1.txt', 'r', encoding='utf=8') as f:
    name = '1.txt'
    text = []
    for line in f:
        text.append(line)
    general_text.setdefault(name, text)

with open('2.txt', 'r', encoding='utf=8') as f:
    name = '2.txt'
    text = []
    for line in f:
        text.append(line)
    general_text.setdefault(name, text)

with open('3.txt', 'r', encoding='utf=8') as f:
    name = '3.txt'
    text = []
    for line in f:
        text.append(line)
    general_text.setdefault(name, text)

with open('text.txt', 'w', encoding='utf=8') as f:
    for k, v in sorted(general_text.items(), key=lambda x: len(x[1])):
        f.write(f'{k}\n')
        f.write(f'{(str(len(v)))}\n')
        f.write(''.join(v))
        f.write('\n')