# notepad_backup

This script bascially run in the background and keeps a watch at your unsaved notepad files and keeps on backing it up in the folder specified.

To make the script run automatically on every startup in Windows, you can create a shortcut to the script and then add it to the startup folder. Here are the steps:

Create a shortcut to the Python script by right-clicking on the script file and selecting "Create shortcut".
Right-click on the shortcut and select "Properties".


In the "Target" field, add python followed by the path to the script file. For example, if your script file is located at C:\Users\Username\Documents\backup.py, the target field should look like: pythonw C:\Users\Username\Documents\backup.py.

Click "Apply" and then "OK" to save the changes.

Press the Windows key + R to open the Run dialog box.

Type shell:startup and press Enter. This will open the Startup folder.

Move the shortcut to the Startup folder.

Restart your computer to see the script run automatically on startup.

This should ensure that your Python script is executed every time your computer starts up.
