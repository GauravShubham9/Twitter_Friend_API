import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    print('')
    acct = input('Enter Twitter Account:')
    if len(acct) < 1:
        break
    url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'count': '5'})
    print('Retrieving', url)
    connection = urllib.request.urlopen(url, context=ctx)

    data = connection.read().decode()
    js = json.loads(data)
    print(json.dumps(js, indent=2))

    headers = dict(connection.getheaders())
    print('Remaining attempts:', headers['x-rate-limit-remaining'])

    for i in js['users']:
        print(i['screen_name'])
        if 'status' not in i:
            print('***NO STATUS***')
            continue
        s = i['status']['text']
        print(' ', s[:50])

