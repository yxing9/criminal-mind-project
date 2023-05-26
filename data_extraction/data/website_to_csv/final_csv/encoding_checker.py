import chardet

with open('killers.csv', 'rb') as file:
    raw_data = file.read()
    result = chardet.detect(raw_data)

print(result['encoding'])
