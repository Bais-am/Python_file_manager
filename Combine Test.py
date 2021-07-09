from math import trunc
from tkinter import Event
import PySimpleGUI as sg
import os 

folder_select = [
    [
        sg.Text("Specify Path"),
        sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse(),
    ]]

folderwindow = sg.Window("folder selection", folder_select)

while True:
  event, values = folderwindow.read()
  if event == "Exit" or event == sg.WIN_CLOSED:
    break
  if event == "-FOLDER-":
    folder = values["-FOLDER-"]
    specified = True
    break

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
  file_list = os.listdir(folder)
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

img_list_column = [
    [
        sg.Listbox(
            values=[imgs], enable_events=True, size=(40, 20), key="-IMGLIST-"
        )
    ],
]
aud_list_column = [
    [
        sg.Listbox(
            values=[audios], enable_events=True, size=(40, 20), key="-AUDLIST-"
        )
    ],
]
vid_list_column = [
    [
        sg.Listbox(
            values=[imgs], enable_events=True, size=(40, 20), key="-IMGLIST-"
        )
    ],
]
doc_list_column = [
    [
        sg.Listbox(
            values=[docs], enable_events=True, size=(40, 20), key="-DOCLIST-"
        )
    ],
]
misc_list_column = [
    [
        sg.Listbox(
            values=[imgs], enable_events=True, size=(40, 20), key="-IMGLIST-"
        )
    ],
]
# For now will only show the name of the file that was chosen
img_viewer_column = [
    [sg.Text("Choose an image from list on left:")],
    [sg.Text(size=(40, 1), key="-IMGOUT-")],
    [sg.Image(key="-IMG-")],
]
aud_viewer_column = [
    [sg.Text("Choose an audio file from list on left:")],
    [sg.Text(size=(40, 1), key="-AUDOUT-")],
    [sg.Image(key="-AUD-")],
]
vid_viewer_column = [
    [sg.Text("Choose a video file from list on left:")],
    [sg.Text(size=(40, 1), key="-VIDOUT-")],
    [sg.Image(key="-AUD-")],
]
doc_viewer_column = [
    [sg.Text("Choose a document from list on left:")],
    [sg.Text(size=(40, 1), key="-DOCOUT-")],
    [sg.Image(key="-DOC-")],
]

imglayout = [
    [
        sg.Column(img_list_column),
        sg.VSeperator(),
        sg.Column(img_viewer_column),
    ]
]
audlayout = [
    [
        sg.Column(aud_list_column),
        sg.VSeperator(),
        sg.Column(aud_viewer_column),
    ]
]
vidlayout = [
    [
        sg.Column(vid_list_column),
        sg.VSeperator(),
        sg.Column(vid_viewer_column),
    ]
]
doclayout = [
    [
        sg.Column(doc_list_column),
        sg.VSeperator(),
        sg.Column(doc_viewer_column),
    ]
]
misclayout = [
    [
        sg.Column(misc_list_column),
    ]
]
#Define Layout with Tabs         
tabgrp = [[sg.TabGroup([[sg.Tab('Images', imglayout, title_color='Red', border_width =10, background_color='Green', element_justification= 'center'),
                    sg.Tab('Audio', audlayout, title_color='Black', border_width =10, background_color='Green', element_justification= 'center'),
                    sg.Tab('Videos', vidlayout, title_color='Red', border_width =10, background_color='Green', element_justification= 'center'),
                    sg.Tab('Documents', doclayout, title_color='Blue', border_width =10, background_color='Green', element_justification= 'center'),
                    sg.Tab('Misc', misclayout, title_color='Red', border_width =10, background_color='Green', element_justification= 'center'),]],
tab_location='centertop', title_color='Red', tab_background_color='Purple',selected_title_color='Green', selected_background_color='Gray', border_width=5),
                    sg.Button('Close')]]  
        
#Define Window
sorterwindow =sg.Window("Tabs",tabgrp)

while True:
  specified = True
  event, values = sorterwindow.read()
  if event == "Close" or event == sg.WIN_CLOSED:
    break