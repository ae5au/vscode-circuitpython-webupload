# vscode-circuitpython-webupload
Task definition and Python script to upload from VS Code to CircuitPython board via web workflow REST API.

CircuitPython 8.x adds [web workflow](https://docs.circuitpython.org/en/latest/docs/workflows.html#web) allowing code to be edited/uploaded via the local network. There is built-in browser support and also a Web REST API. This project utilizes the latter to upload a file directly from VS Code.

***NOTE: This is very rough and you will find some bugs. PRs appreciated!***

## Setup
* Python 3 installed and in your path.
* Copy .vscode directory from this project to the root of your CircuitPython project. It does not have to be copied to your CircuitPython board, just the machine running VS Code.
* Edit .vscode/cp-web-upload.py - set baseURL and password.
* From the file you want to upload, execute the "Run Task..." command.
  * Menu: _Terminal, Run Task..._
  * Command pallet: _Tasks: Run Task_
  * Shortcut keys: TODO:DOCUMENT_THESE
  * [Keybindings can be configured to call a specific task](https://code.visualstudio.com/docs/editor/tasks#_binding-keyboard-shortcuts-to-tasks).

## Notes
* Directories in the file's path are created if they don't exist.
* Only single files can be uploaded.
* Moved files will be recreated in the new location but the old file/directories will not be removed.
* Existing files will be overwritten, even if they haven't changed.

## TODO
- [ ] get password from /.env
- [ ] set/get URL from /.env
- [ ] Get timestamp from source file and set on new file
- [ ] use argparse
