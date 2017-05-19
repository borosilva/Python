import urllib.request, json

password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()

urlTest = ""
urlTestSub = ""
userValue = ""
passValue = ""

top_level_url = urlTest
password_mgr.add_password(None, top_level_url, userValue, passValue)

handler = urllib.request.HTTPBasicAuthHandler(password_mgr)

opener = urllib.request.build_opener(handler)

opener.open(urlTest)

urllib.request.install_opener(opener)
with urllib.request.urlopen(urlTestSub) as url:
    data = json.loads(url.read().decode())

def recursive_iter(obj):
    if isinstance(obj, dict):
        for item in obj.values():
            yield from recursive_iter(item)
    elif any(isinstance(obj, t) for t in (list, tuple)):
        for item in obj:
            yield from recursive_iter(item)
    else:
        yield obj 

print('---------------------------------------')

for i in recursive_iter(data):
            print('    Value:  ', i)

print('---------------------------------------')