import PySimpleGUI as gui
import os.path

# Window layout
column_layout = [
    [
        gui.Text("Image Folder"),
        gui.In(size = (25, 1), enable_events = True, key = "-FOLDER DIR-"),
        gui.FolderBrowse(),
    ],

    # Display list of paths to the images 
    [
        gui.Listbox(
            values=[], enable_events=True, size=(40, 20), key="-FILE LIST-"
        )
    ],
]

# Display image layout
image_view = [
    [gui.Text("Choose image from list:")],
    [gui.Text(size=(40, 1), key = "-NAME-")],
    [gui.Image(key="-IMAGE-")],
]

# Implement layout
layout = [
    [
        gui.Column(column_layout),
        gui.VSeperator(),
        gui.Column(image_view),
    ]
]
window = gui.Window("PyIm Viewer", layout)

# Event loop
while True:
    event, values = window.read()
    if event == "Exit" or event == gui.WIN_CLOSED:
        break

    # If folder name provided, make a list of files in the folder
    if event == "-FOLDER DIR-":
        folder = values["-FOLDER DIR-"]
        try: # Get list
            file_list = os.listdir(folder)
        except:
            file_list = []

        fnames = [
            f
            for f in file_list
                if os.path.isfile(os.path.join(folder, f))
                and f.lower().endswith((".png", ".gif"))
        ]
        window["-FILE LIST-"].update(fnames)
        
    elif event == "-FILE LIST-":  # A file was chosen from list
        try:
            filename = os.path.join(
                values["-FOLDER DIR-"], values["-FILE LIST-"][0]
            )
            window["-NAME-"].update(filename)
            window["-IMAGE-"].update(filename=filename)
        except:
            pass

window.close()