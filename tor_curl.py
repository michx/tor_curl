import requests
import sys
import json
url=sys.argv[1]

def check_my_ip(s):
    try:
        ip=s.get('http://httpbin.org/ip')
        return json.loads(ip.text)['origin']
    except requests.exceptions.ConnectionError as C:
            print "Error: ",C

clear_session=requests.session()
print "Your Clear IP address is: ", check_my_ip(clear_session)

session = requests.session()
session.proxies = {}

session.proxies['http'] = 'socks5h://localhost:9050'
session.proxies['https'] = 'socks5h://localhost:9050'

headers = {}
headers['User-agent'] = "Me/1.1"

print "You Tor hidden IP now is :", check_my_ip(session)

try:
    r = session.get(url, headers=headers)
    print r.text
except requests.exceptions.ConnectionError as C:
    print "Error: ",C

