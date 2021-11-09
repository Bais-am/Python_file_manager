import PySimpleGUI as sg
import os 
import shutil

from PySimpleGUI.PySimpleGUI import Print

folder_select = [
  [
    sg.Text("Specify Path"),
    sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
    sg.FolderBrowse(),
  ]
]

folderwindow = sg.Window("folder selection", folder_select, auto_close=True)

while True:
  event, values = folderwindow.read()
  if event == "-FOLDER-":
    folder = values["-FOLDER-"]
  if event == "Exit" or event == sg.WIN_CLOSED:
    break


def isImg(str):
  ext = ".png .jpg .jpeg .gif .img .webp"
  if any(e in str.lower() for e in ext.split()) :
    return True
  else: return False

def isAud(str):
  ext = ".mp3 .m4a .wav"
  if any(e in str.lower() for e in ext.split()) :
    return True
  else : return False 

def isVid(str):
  ext = ".mp4 .avi .3gp .webm .mov .m4v"
  if any(e in str.lower() for e in ext.split()):
    return True
  else: return False

def isDoc(str):
  ext = ".pdf .doc .docx .ppt .pptx .ppsx .xls .xlsx .xlsm .xlt .xltm .txt"
  if any(e in str.lower() for e in ext.split()) :
    return True
  else: return False

filesrc = list()
files = list()
for dirpath, dirnames, filenames in os.walk(folder, topdown = True):
  filesrc += [os.path.join(dirpath, n) for n in filenames]
  files += [n for n in filenames]


imgs = [
  f
  for f in files
  if isImg(f)
]
imgsrc = [
  f
  for f in filesrc
  if isImg(f)
]

aud = [
  f
  for f in files
  if isAud(f)
]
audsrc = [
  f
  for f in filesrc
  if isAud(f)
]

vid = [
  f
  for f in files
  if isVid(f)
]
vidsrc = [
  f
  for f in filesrc
  if isVid(f)
]

docs = [
  f
  for f in files
  if isDoc(f)
]
docsrc = [
  f
  for f in filesrc
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
miscsrc = [
  f
  for f in filesrc
  if isImg(f) == False
  and isAud(f) == False
  and isVid(f) == False
  and isDoc(f) == False
]


img_list_column = [
  [
    sg.Listbox(
      values=[], enable_events=True, size=(80, 25), key="-IMGLIST-"
    ),
  ],
]
img_btns = [
  [sg.Button("Copy All", key="-IMGCOPY-"), sg.Button("Move All", key="-IMGMOVE-")],
  [
    sg.Text("Destination"),
    sg.In(size=(25, 1), enable_events=True, key="-IMGOUT-"),
    sg.FolderBrowse(),
  ]
]

aud_list_column = [
  [
    sg.Listbox(
      values=[], enable_events=True, size=(80, 25), key="-AUDLIST-"
    )
  ],
]
aud_btns = [
  [sg.Button("Copy All", key="-AUDCOPY-"), sg.Button("Move All", key="-AUDMOVE-")],
  [
    sg.Text("Destination"),
    sg.In(size=(25, 1), enable_events=True, key="-AUDOUT-"),
    sg.FolderBrowse(),
  ]
]

vid_list_column = [
  [
    sg.Listbox(
      values=[], enable_events=True, size=(80, 25), key="-VIDLIST-"
    )
  ],
]
vid_btns = [
  [sg.Button("Copy All", key="-VIDCOPY-"), sg.Button("Move All", key="-VIDMOVE-")],
  [
    sg.Text("Destination"),
    sg.In(size=(25, 1), enable_events=True, key="-VIDOUT-"),
    sg.FolderBrowse(),
  ]
]

doc_list_column = [
  [
    sg.Listbox(
      values=[], enable_events=True, size=(80, 25), key="-DOCLIST-"
    )
  ],
]
doc_btns = [
  [sg.Button("Copy All", key="-DOCCOPY-"), sg.Button("Move All", key="-DOCMOVE-")],
  [
    sg.Text("Destination"),
    sg.In(size=(25, 1), enable_events=True, key="-DOCOUT-"),
    sg.FolderBrowse(),
  ]
]

misc_list_column = [
  [
    sg.Listbox(
      values=[], enable_events=True, size=(80, 25), key="-MISCLIST-"
    )
  ],
]
misc_btns = [
  [sg.Button("Copy All", key="-MISCCOPY-"), sg.Button("Move All", key="-MISCMOVE-")],
  [
    sg.Text("Destination"),
    sg.In(size=(25, 1), enable_events=True, key="-MISCOUT-"),
    sg.FolderBrowse(),
  ]
]

#INDIVISUAL TAB LAYOUTS
imglayout = [
  [
    sg.Column(img_list_column),
    sg.Column(img_btns, element_justification='center'),
  ],
]
audlayout = [
  [
    sg.Column(aud_list_column),
    sg.Column(aud_btns, element_justification='center'),
  ]
]
vidlayout = [
  [
    sg.Column(vid_list_column),
    sg.Column(vid_btns, element_justification='center'),
  ]
]
doclayout = [
  [
    sg.Column(doc_list_column),
    sg.Column(doc_btns, element_justification='center'),
  ]
]
misclayout = [
  [
    sg.Column(misc_list_column),
    sg.Column(misc_btns, element_justification='center'),
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
  ],
  [
  sg.CButton("Quit"),
  sg.Button("Refresh"),
  ],
]

def copy(src, dest): {
  shutil.copy2(src, dest, follow_symlinks=False)
}
def delete(path): {
  os.remove(path)
}

#Define Window
sorterwindow =sg.Window("Tabs",tabgrp)

while True:
  event, values = sorterwindow.read()
  if event == "Refresh":
    sorterwindow["-IMGLIST-"].update(imgs)
    sorterwindow["-AUDLIST-"].update(aud)
    sorterwindow["-VIDLIST-"].update(vid)
    sorterwindow["-DOCLIST-"].update(docs)
    sorterwindow["-MISCLIST-"].update(miscs)

  if values["-IMGOUT-"] and event == "-IMGCOPY-":
    imgdst = values["-IMGOUT-"]
    for F in imgsrc:
      copy(F, imgdst)
  if values["-IMGOUT-"] and event == "-IMGMOVE-":
    imgdst = values["-IMGOUT-"]
    for F in imgsrc:
      copy(F, imgdst)
      delete(F)

  if values["-AUDOUT-"] and event == "-AUDCOPY-":
    auddst = values["-AUDOUT-"]
    for F in audsrc:
      copy(F, auddst)
  if values["-AUDOUT-"] and event == "-AUDMOVE-":
    auddst = values["-AUDOUT-"]
    for F in audsrc:
      copy(F, auddst)
      delete(F)

  if values["-VIDOUT-"] and event == "-VIDCOPY-":
    viddst = values["-VIDOUT-"]
    for F in vidsrc:
      copy(F, viddst)
  if values["-VIDOUT-"] and event == "-VIDMOVE-":
    viddst = values["-VIDOUT-"]
    for F in vidsrc:
      copy(F, viddst)
      delete(F)

  if values["-DOCOUT-"] and event == "-DOCCOPY-":
    docdst = values["-DOCOUT-"]
    for F in docsrc:
      copy(F, docdst)
  if values["-DOCOUT-"] and event == "-DOCMOVE-":
    docdst = values["-DOCOUT-"]
    for F in docsrc:
      copy(F, docdst)
      delete(F)

  if values["-MISCOUT-"] and event == "-MISCCOPY-":
    miscdst = values["-MISCOUT-"]
    for F in miscsrc:
      copy(F, miscdst)
  if values["-MISCOUT-"] and event == "-MISCMOVE-":
    miscdst = values["-MISCOUT-"]
    for F in miscsrc:
      copy(F, miscdst)
      delete(F)

  if event == "Close" or event == sg.WIN_CLOSED:
    break
