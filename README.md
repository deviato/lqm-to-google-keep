# lqm-to-google-keep
Script to convert notes exported from LG QuickMemoPlus format in csv, and import them into Google Keep

# Requirements
The scripts require tha installation of python with **gkeep** and **keyring** libs. Install with:
```
$ pip install gkeep keyring
```
# How To Use #
1. Export all memos from QuickMemo+ to your sdcard (Three Dots Options, Export, Select all, Export, SD Card).
2. Copy all of the exported files (.lqm) in the same directory of this scripts (or to another directory setting it accordingly in the scripts)
3. Execute the first script to convert the memos in a single csv file
```
$ python lqm2csv
```
The results are a **notes.csv** file, and a directory **images** with all of the extracted pictures
4. Check the csv file, possibly modifying the order in which the fields will be used to fill in the memos. By default, **CreationDate** is used as the title, and **PreviewFileTitle** (if it exists) + **BrowserURL** (if it exists) + **DescRaw** as the note text.
5. Edit **csv2keep.py** inserting your gmail and password, keep the notes.csv file in the same directory, and run the script with:
```
$ python csv2keep
```
The first time it tries to authenticate, google could throw an error, visit the link provided by the script to bypass it.
6. The program will stop every 50 memos created (you can change this value, but it's not recommended). Check online on keep.google.com if they're ok, then press Enter to resume the script. Don't do it too quickly, or google will block you with Rate Limit Exceeded error.
# Limitations #
The script will only work for text or link notes, not for pictures due to limitation of gkeep api. You'll get only a file reference in the memo, and all physical files in **images** directory.
