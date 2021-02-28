from timeit import default_timer
import xmltodict

handle = open("test_data.xml", "r")

content = handle.read()

d = xmltodict.parse(content)
print(type(d['event']['attributes']))
print(d['event']['attributes']['item'][0]['@key'])

for item in d['event']['attributes']['item']:
    print(item)


