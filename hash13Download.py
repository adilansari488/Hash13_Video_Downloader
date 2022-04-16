from tqdm import tqdm
import requests

v2 = 'v2' # text filename of links

file = open(v2,'r')
lines = file.readlines()
length = len(lines)
filename = input('Enter Filename (without extension) to Save : ')
filename = filename+'.ts'
with open(filename, 'ab') as file2 :
    for i in tqdm(range(7,length,2),desc="Downloading…",ascii=False, ncols=100):
        url = 'https://embed-fastly.wistia.com' + lines[i].strip()
        r = requests.get(url, allow_redirects=True)
        file2.write(r.content)
        # open(filename, 'ab').write(r.content)
print("Download Completed.")
file.close()
