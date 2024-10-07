# import re
#
# text = '''
# Visit my website at https://www.example.com
# or you can check out https://www.someotherexample.com
# '''
# pattern = re.compile(r"htpps://(www\.)?(w\+)(\.\w+)")
# result = pattern.finditer(text)
# for i in result:
#     print(i)
# print(result)

import re

text = 'Позвоните мне по номеру 555-123-4567 или 555-987-6543'

pattern = re.compile(r"(\d\d\d+)-(\d\d\d+)-(\d\d\d+)")

matches = pattern.finditer(text)

# urls = [match.group() for match in matches]

for i in matches:
    print(i)

text = 'Цвет неба - синий.'

pattern = re.sub('')