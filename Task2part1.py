import urllib.request, json
import time
start=time.time()
for i in range (1,201):
    name=('xkcd%d.json'%i)
    with open(name, 'w') as f:
        print("The json file %d is created"%i)

    with urllib.request.urlopen("https://xkcd.com/%d/info.0.json"%i) as url:
        data = json.loads(url.read().decode())

    json_string = json.dumps(data)

    with open(name, 'w') as outfile:
        outfile.write(json_string)
    print("The json file %d written"%i)
        

time_taken = time.time() - start
print('Time Taken {0}'.format(time_taken))

        
