#!/usr/bin/env python
from zipfile import ZipFile
import json,csv,datetime,os

# Change the path to your needs. Default to current.
path="."

notes=open('notes.csv','w')
writer=csv.writer(notes,delimiter=',',quotechar='"')
writer.writerow(['CreationDate','PreviewImage','BrowserURL','DescRaw','Desc'])
print('-Processing...')
for f in os.listdir(path):
  if f.endswith('.lqm'):
    arc=ZipFile(f,'r')
    memofile=arc.read('memoinfo.jlqm');
    data=json.loads(memofile)
    memo=data.get('Memo')
    memoobj=data.get('MemoObjectList')[0]
    dc=datetime.datetime.fromtimestamp(memo.get('CreatedTime')/1000).date().isoformat()
    url=memo.get('BrowserUrl')
    img=memo.get('PreviewImage')
    if(img):
      arc.extract('images/'+img, path);
    dsc=memo.get('Desc')
    dscraw=memoobj.get('DescRaw')
    print(f,'->',dc,img);
    writer.writerow([dc,img,url,dscraw,dsc])
    arc.close()
print('\n-Output written in notes.csv file\n-Pictures are in images/ directory\n')
