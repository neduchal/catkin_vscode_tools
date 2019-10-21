# catkin_vscode_tools
Set of scripts for easier creating of catkin build workspaces and packages

## Workspace Init

> python3 init_ws.py -w path/to/ws [-k]

Script creates WS, creates copy of default settings and create_pkg script. Finally it attempts to run VSCODE in WS folder. Parameter -k means keybindings. The script tries to append keybindings from settings subdirectory into /home/username/.config/Code/User/keybindings.json file.

## Package creator

Use it in the ws/src directory

> python3 create_pkg.py -p package_name -d dependencies_file -o other_dependencies [-w workspace]

Example:

> python3 create_pkg.py -p test_pkg -d default.txt -o cv_bridge

The example creates package test_pkg with dependencies in settings/dependencies/default.txt file and with additional dependency cv_bridge in the current workspace. If you specify parameter -w such as /home/user/catkin_ws/ than it creates new package in its src subdirectory.


