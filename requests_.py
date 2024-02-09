import requests
'''
pyload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('https://httpbin.org/get', params=payload)
'''

'''
res = requests.get('https://api.github.com/events')
print(res.url)
#print(res.json())
#print(res.headers['content-type'])
#print(res.content)
print(res.encoding)
#print(res.text)
'''


url = 'https://api.github.com/some/endpoint'
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url, headers=headers)
print(r.json())
print(r.text)

'''
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("https://httpbin.org/post", data=payload)
#print(r.text)
print(r.status_code)
'''

'''
url = 'http://example.com/some/cookie/setting/url'
r = requests.get(url)
#print(r.cookies['example_cookie_name'])
'''

'''
url = 'https://httpbin.org/cookies'
cookies = dict(cookies_are='working')
r = requests.get(url, cookies=cookies)
print(r.text)
'''

'''
r = requests.get('http://digitology.tech/')
print(r.url)
print(r.status_code)
print(r.history)
'''

#requests.get('https://digitology.tech/', timeout=0.001)

'''
url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
r = requests.post(url, json=payload)
'''

'''
r = requests.get('https://api.github.com/events', stream=True)
print(r.raw)
'''

'''
s = requests.Session()
s.auth = ('user', 'pass')
s.headers.update({'x-test': 'true'})

# отправляются как «x-test», так и «x-test2»
r = s.get('https://httpbin.org/headers', headers={'x-test2': 'true'})
print (r.text)
'''

'''
with requests.Session() as s:
    r = s.get('https://httpbin.org/cookies/set/sessioncookie/123456789', headers={'x-test2': 'true'})
print(r.text)
print(r.content)
print(r.headers)
'''


'''
r = requests.get('https://en.wikipedia.org/wiki/Monty_Python')
print(r.headers)
print(r.request.headers) # заголовок запроса!!!!!!!!!!!!!!!!!!!!!!!!!! ???????
'''
