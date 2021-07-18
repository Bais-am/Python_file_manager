import PySimpleGUI as sg
import os 

folder_select = [
  [
    sg.Text("Specify Path"),
    sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
    sg.FolderBrowse(),
  ]
]

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
  ext = ".png .jpg .jpeg .gif .img"
  if any(e in str.lower() for e in ext.split()) :
    return True
  else: return False

def isAud(str):
  ext = ".mp3 .m4a .wav"
  if any(e in str.lower() for e in ext.split()) :
    return True
  else : return False 

def isVid(str):
  ext = ".mp4 .avi .3gp .webp .webm .mov .m4v"
  if any(e in str.lower() for e in ext.split()):
    return True
  else: return False

def isDoc(str):
  ext = ".pdf .doc .docx .ppt .pptx .ppsx .xls .xlsx .xlsm .xlt .xltm .txt"
  if any(e in str.lower() for e in ext.split()) :
    return True
  else: return False

# file_paths = list()
files = list()
for dirpath, dirnames, filenames in os.walk(folder, topdown = True):
  # file_paths += [os.path. join(dirpath, n) for n in filenames]
  files += [n for n in filenames]


imgs = [
  f
  for f in files
  if isImg(f)
]
audios = [
  f
  for f in files
  if isAud(f)
]
videos = [
  f
  for f in files
  if isVid(f)
]
docs = [
  f
  for f in files
  if isDoc(f)
]
miscs = [
  f
  for f in files
  if isImg(f) == False
  and isAud(f) == False
  and isVid(f) == False
  and isDoc(f) == False
]

img_list_column = [
  [
    sg.Listbox(
      values=[], enable_events=True, size=(80, 25), key="-IMGLIST-"
    )
  ],
]
aud_list_column = [
  [
    sg.Listbox(
      values=[], enable_events=True, size=(80, 25), key="-AUDLIST-"
    )
  ],
]
vid_list_column = [
  [
    sg.Listbox(
      values=[], enable_events=True, size=(80, 25), key="-VIDLIST-"
    )
  ],
]
doc_list_column = [
  [
    sg.Listbox(
      values=[], enable_events=True, size=(80, 25), key="-DOCLIST-"
    )
  ],
]
misc_list_column = [
  [
    sg.Listbox(
      values=[], enable_events=True, size=(80, 25), key="-MISCLIST-"
    )
  ],
]

#INDIVISUAL TAB LAYOUTS
imglayout = [
  [
    sg.Column(img_list_column),
  ]
]
audlayout = [
  [
    sg.Column(aud_list_column),
  ]
]
vidlayout = [
  [
    sg.Column(vid_list_column),
  ]
]
doclayout = [
  [
    sg.Column(doc_list_column),
  ]
]
misclayout = [
  [
    sg.Column(misc_list_column),
  ]
]

#Define Layout with Tabs         
tabgrp = [
  [sg.TabGroup(
    [
      [
        sg.Tab(
          'Images', imglayout, title_color='Red', border_width =10, background_color='black', element_justification= 'center'
        ),
        sg.Tab(
          'Audio', audlayout, title_color='Black', border_width =10, background_color='black', element_justification= 'center'
        ),
        sg.Tab(
          'Videos', vidlayout, title_color='Red', border_width =10, background_color='black', element_justification= 'center'
        ),
        sg.Tab(
          'Documents', doclayout, title_color='Blue', border_width =10, background_color='black', element_justification= 'center'
        ),
        sg.Tab(
          'Misc', misclayout, title_color='Red', border_width =10, background_color='black', element_justification= 'center'
        ),
      ]
    ],
  tab_location='centertop', title_color='#080A0A', tab_background_color='#E13758',selected_title_color='#080A0A', selected_background_color='#2E6A9C'),
  sg.CButton("Quit"),
  sg.Button("Refresh"),
  ],
]

#Define Window
sorterwindow =sg.Window("Tabs",tabgrp)

while specified == True:
  event, values = sorterwindow.read()
  if event == "Refresh":
    sorterwindow["-IMGLIST-"].update(imgs)
    sorterwindow["-AUDLIST-"].update(audios)
    sorterwindow["-VIDLIST-"].update(videos)
    sorterwindow["-DOCLIST-"].update(docs)
    sorterwindow["-MISCLIST-"].update(miscs)
  if event == "Close" or event == sg.WIN_CLOSED:
    break
