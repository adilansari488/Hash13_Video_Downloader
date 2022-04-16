from tqdm import tqdm
import requests

v2 = 'aws part3' # text filename of links

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


# --------------------------------------------------------------------------------



# downloads = int((len(lines) - 7) / 2)
# downloaded = 0
# for i in range(7,length,2) :
#     progress = (downloaded/downloads)*100
#     downloaded+=1
#     print(progress,'%')







# #
# for line in lines :
#     print(line.strip())
# file.close()
#
# # url = 'https://embed-fastly.wistia.com/deliveries/5f543d377eee6f9a90d449cf45fa033942ab5a18.m3u8/v2/seg-1264-v1-a1.ts'
# # r = requests.get(url, allow_redirects=True)
# # open('try1.ts', 'wb').write(r.content)
# #
# #
# #
# # file2 = open('seg-1-v1-a1.ts','rb')
# #
# # with open('try1.ts','ab') as file :
# #     file.write(file2.read())
# # file2.close()
# #
# #
