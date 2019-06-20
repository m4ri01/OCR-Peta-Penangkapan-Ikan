from PIL import Image
import pytesseract
import pandas as pd
image = Image.open("jbn_20190515_16.png")
crop = image.crop((2850,30,3430,1450))
text = pytesseract.image_to_string(crop)
text = text.splitlines()
text = [i for i in text if len(i)>2]
del text[0:3]
a = text.index("Daerah Potensi Ikan")
del text[a:]
newtext = []
for idx,val in enumerate(text):
    try:
        ubah = str(val)
        newtext.append(ubah)
    except:
        pass
s="?"
nk = s.join(newtext)
nk = nk.replace('\n','')
nk = nk.replace(' ','')
nk = nk.replace('}','|')
nk = nk.replace('{','|')
nk = nk.replace(')','|')
nk = nk.replace('(','|')
nk = nk.replace('/','|')
nk = nk.replace(']','|')
nk = nk.replace('||','|')
nk = nk.replace(';','|')
nk = nk.replace('.','')
nk = nk.replace(',','.')
newtext = nk.split("?")
panjanglist=len(newtext)
hapus=[]
for i in range(panjanglist-1):
    val = newtext[i]
    a = val.split("|")
    if len(a)!=7:
	hapus.append(i)
    else:
	pass
for index in sorted(hapus, reverse=True):
    del newtext[index]

with open('data.txt','w') as writer:
    writer.write('\n'.join(newtext))
longlattotal=[]
data = pd.read_csv('data.txt',sep="|",header=None)
data = data.dropna()
data.columns=["no","bd","bm","bs","ld","lm","ls"]
for index, row in data.iterrows():
    a = data.loc[index]
    nilai1 = int(a['bd']) + float(a['bm']) / 60 + float(a['bs']) / 3600
    nilai2 = int(a['ld']) + float(a['lm']) / 60 + float(a['ls']) / 3600
    if nilai2 > 0:
	nilai2 = -1.0*nilai2
    else:
	pass
    longlat = str(nilai2)+","+str(nilai1)
    longlattotal.append(longlat)

with open ("longlat.txt","w") as f:
    for item in longlattotal:
	f.write("%s\n"%item)
print("berhasil")




