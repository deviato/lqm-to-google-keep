#!/usr/bin/env python
import gkeepapi,keyring,csv

# Change with your gmail and password!
username='xxxxxxxxxxx@gmail.com'
password='your-password'
# Change with the directory where notes.csv is located. Default to current.
path='.'
# Google blocks too frequent api calls, set the limit of notes to process at a time (default set to 50).
# The program will stop every X note creation and resume through user input.
ratelimit=50

keep=gkeepapi.Keep()
token=keyring.get_password('google-keep-token',username)
if token:
  print('Authenticating with resume token...')
  keep.resume(username,token)
else:
  print('Authenticating with username and password...')
  try:
    success=keep.login(username,password)
  except:
    print('\n *** Please open this link in a browser to enable permissions: https://accounts.google.com/b/0/DisplayUnlockCaptcha ***\n')
    raise
  token=keep.getMasterToken()
  keyring.set_password('google-keep-token', username, token)

print('Auth OK')
with open(path+'/notes.csv') as notes:
  reader=csv.reader(notes)
  cnt=0
  next(reader)
  for row in reader:
    # Create a note with CreationDate as title, and ImageTitle + BrowserURL + DescRaw as content. You can change the fields
    # to your needs. Unfortunately gkeep api doesn't support image uploading, so you only have a reference.
    title=row[0]
    text=''
    if row[1]: text=row[1]+'\n'
    if row[2]: text=text+row[2]+'\n'
    text=text+row[3]

    cnt=cnt+1
    print(cnt,title)
    note=keep.createNote(title,text)
    if(cnt==ratelimit):
      cnt=0
      keep.sync()
      input("Wait a little, than press Enter to continue")
  keep.sync()
