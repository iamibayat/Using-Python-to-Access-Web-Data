import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

x = input('Enter Location: ')

fhand = urllib.request.urlopen(x)
fhand = fhand.read()
tree = ET.fromstring(fhand)
lst = tree.findall('comments/comment')
print('User count:', len(lst))

summation = 0
for item in lst:
    summation = summation + int(item.find('count').text)

print(summation)
