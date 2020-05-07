import os

def filenot(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def move(folderName,files):
    for file in files:
        os.replace(file,f"{folderName}/{file}")



files=os.listdir()
files.remove("main.py")
print(files)




filenot('Images')
filenot('Docs')
filenot('Media')
filenot('others')


imagesextension=[".png",".jpeg",".jpg"]
images=[file for file in files if os.path.splitext(file)[1].lower() in imagesextension]
print(images)

docsextension=[".pdf",".doc",".docx",".txt"]
docs=[file for file in files if os.path.splitext(file)[1].lower() in docsextension]
print(docs)


mediaextensions=[".mp4",".mp3"]
media=[file for file in files if os.path.splitext(file)[1].lower() in mediaextensions]
print(media)
others=[]
for file in  files:
    ext=os.path.splitext(file)[1]
    if (ext not  in mediaextensions) and  (ext not  in docsextension) and (ext not  in imagesextension) and os .path .isfile(file):
        others.append(file)
print(others)
move("Images",images)
move("Docs",docs)
move("Media",media)
move("others",others)

