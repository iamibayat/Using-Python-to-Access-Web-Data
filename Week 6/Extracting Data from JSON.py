import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
import json

x = input('Enter Location: ')
fhand = urllib.request.urlopen(x)
fhand = fhand.read()

info = json.loads(fhand)
print('User count:', len(info))
# print(info)
# print(len(info['comments']))

comment_dic = info['comments']
# print(comment_dic)

summation = 0
for item in comment_dic:
    summation = summation + int(item["count"])
    # print(item['count'])
print(summation)
