import os
import shutil
import pywinauto
import datetime
import time
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
        date_string = datetime.datetime.now().strftime("%Y-%m-%d")
        #backup_file_path = os.path.join(backup_dir, file_name)
        backup_filename = f"{backup_dir}\\{date_string}_{file_name.replace(' ', '_').replace('-', '_').replace('*','')}.bak"
        if file_contents.strip() != "":
            with open(backup_filename, "a") as backup_file:                
                backup_file.write(file_contents)
                backup_file.write("=================================")
                backup_file.write("\n\n\n\n\n")


if __name__ == "__main__":
    while True:
        backup_notepad_files()
        print("Backed up. Now Sleeping for 10 minutes")
        # sleep for 10 minutes
        time.sleep(600)
