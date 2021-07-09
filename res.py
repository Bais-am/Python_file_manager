from imgView import folder 
import os 

def isImg(str):
  ext = ".png .jpg .jpeg .gif"
  if any(e in str for e in ext.split()) :
    return True
  else: return False

def isAudio(str):
  ext = ".mp3 .m4a"
  if any(e in str for e in ext.split()) :
    return True
  else : return False 

def isVideo(str):
  ext = ".mp4 .avi .3gp"
  if any(e in str for e in ext.split()):
    return True
  else: return False

def isDoc(str):
  ext = ".pdf .doc .docx .ppt .pptx .xls .xlsx .xlsm .xlt .xltm .txt"
  if any(e in str for e in ext.split()) :
    return True
  else: return False

try:
  # Get list of files in folder
  file_list = os.listdir(path=folder)
except:
  file_list = []

imgs = [
  f
  for f in file_list
  if os.path.isfile(os.path.join(folder, f))
  and isImg(f)
]
audios = [
  f
  for f in file_list
  if os.path.isfile(os.path.join(folder, f))
  and isAudio(f)
]
videos = [
  f
  for f in file_list
  if os.path.isfile(os.path.join(folder, f))
  and isVideo(f)
]
docs = [
  f
  for f in file_list
  if os.path.isfile(os.path.join(folder, f))
  and isDoc(f)
]
miscs = [
  f
  for f in file_list
  if os.path.isfile(os.path.join(folder, f))
  and f not in imgs or f not in audios or f not in videos or f not in docs
]


for img in imgs:
  print(img)

for audio in audios:
  print(audio)

for video in videos:
  print(video)

for doc in docs:
  print(doc)

for misc in miscs:
  print(misc)

