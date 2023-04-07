import os
import shutil
import pywinauto
import datetime

# Specify the directory to backup the files to
backup_dir = "C:\\NotepadBackup"


def backup_notepad_files():
    # Get a list of all open Notepad files
    notepad_files = []
    for window in pywinauto.findwindows.find_windows(title_re=".* - Notepad"):
        app = pywinauto.Application().connect(handle=window)
        notepad = app.window(handle=window)
        notepad_files.append(notepad)

    # Backup each file to the specified directory
    for notepad in notepad_files:
        file_name = os.path.basename(notepad.texts()[0])
        edit = notepad.child_window(class_name='Edit')
        file_contents = edit.window_text()
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        file_name = current_date + "_" + file_name+".bak"
        backup_file_path = os.path.join(backup_dir, file_name)
        with open(backup_file_path, "a") as backup_file:
            backup_file.write(file_contents)
            backup_file.write("=================================")
            backup_file.write("\n\n\n\n\n")


if __name__ == "__main__":
    while True:
        os.system("timeout 10")
        backup_notepad_files()
