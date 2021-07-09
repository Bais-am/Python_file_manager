import PySimpleGUI as sg
import os.path

#define layout
img_list_column = [
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40, 20), key="-IMG LIST-"
        )
    ],
]
doc_list_column = [
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40, 20), key="-DOC LIST-"
        )
    ],
]
aud_list_column = [
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40, 20), key="-AUD LIST-"
        )
    ],
]

# For now will only show the name of the file that was chosen
img_viewer_column = [
    [sg.Text("Choose an image from list on left:")],
    [sg.Text(size=(40, 1), key="-IMGOUT-")],
    [sg.Image(key="-IMG-")],
]
doc_viewer_column = [
    [sg.Text("Choose a document from list on left:")],
    [sg.Text(size=(40, 1), key="-DOCOUT-")],
    [sg.Image(key="-DOC-")],
]
aud_viewer_column = [
    [sg.Text("Choose an audio file from list on left:")],
    [sg.Text(size=(40, 1), key="-AUDOUT-")],
    [sg.Image(key="-AUD-")],
]


layout1 = [
    [
        sg.Column(img_list_column),
        sg.VSeperator(),
        sg.Column(img_viewer_column),
    ]
]
layout2 = [
    [
        sg.Column(doc_list_column),
        sg.VSeperator(),
        sg.Column(doc_viewer_column),
    ]
]
layout3 = [
    [
        sg.Column(aud_list_column),
        sg.VSeperator(),
        sg.Column(aud_viewer_column),
    ]
]
#Define Layout with Tabs         
tabgrp = [[sg.TabGroup([[sg.Tab('Images', layout1, title_color='Red', border_width =10, background_color='Green', element_justification= 'center'),
                    sg.Tab('Documents', layout2, title_color='Blue', border_width =10, background_color='Green', element_justification= 'center'),
                    sg.Tab('Audio', layout3, title_color='Black', border_width =10, background_color='Green', element_justification= 'center')]], tab_location='centertop', title_color='Red', tab_background_color='Purple',selected_title_color='Green', selected_background_color='Gray', border_width=5),
                    sg.Button('Close')]]  
        
#Define Window
window =sg.Window("Tabs",tabgrp)
#Read  values entered by user
event,values=window.read()
#access all the values and if selected add them to a string
window.close()