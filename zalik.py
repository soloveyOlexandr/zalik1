with open('file.txt', encoding='utf-8') as file:
    for line in file:
        print(f'рядок: {line}')
        print(f'кількість символів: {len(line)}')
        print(f'кількість слів: {len(line.split())}')
