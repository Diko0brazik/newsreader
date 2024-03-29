import PySimpleGUI as sg
import os.path
import dbque

# First the window layout in 2 columns

word_list_column = [
    [
        sg.Text("words"),
        
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40, 20), key="-WORD LIST-"
        )
    ],
]

# For now will only show the name of the file that was chosen
word_history = [
    [sg.Text("Choose an word for view history:")],
    [sg.Text(size=(40, 1), key="-HISTORY-")],
    [sg.Image(key="-IMAGE-")],
]

# ----- Full layout -----
layout = [
    [
        sg.Column(word_list_column),
        sg.VSeperator(),
        sg.Column(word_history),
    ]
]

window = sg.Window("Image Viewer", layout)

# Run the Event Loop
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    # Folder name was filled in, make a list of files in the folder
    if event == "-FOLDER-":
        folder = values["-FOLDER-"]
        try:
            # Get list of files in folder
            file_list = dbque.words()
        except:
            file_list = []

        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith((".png", ".gif"))
        ]
        window["-FILE LIST-"].update(fnames)
    elif event == "-FILE LIST-":  # A file was chosen from the listbox
        try:
            filename = os.path.join(
                values["-FOLDER-"], values["-FILE LIST-"][0]
            )
            window["-TOUT-"].update(filename)
            window["-IMAGE-"].update(filename=filename)

        except:
            pass

window.close()