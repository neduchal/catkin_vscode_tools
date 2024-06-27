#!/usr/bin/python3

import argparse
import os
import os.path
import shutil
from distutils.dir_util import copy_tree
from patch_keybindings import *

def main():
    parser = argparse.ArgumentParser(description='Catkin Tools Workspace Creator')
    parser.add_argument('-w', '--workspace',
                        help='Workspace path',
                        default='~/catkin_ws')
    parser.add_argument('-k', '--keybindings', dest="keybindings", action="store_true")
    parser.set_defaults(keybindings=False)
    args = parser.parse_args()

    print("CATKIN TOOLS WORKSPACE CREATOR FOR VSCODE")
    print()

    vscode_path = os.path.join(args.workspace, ".vscode")
    src_path = os.path.join(args.workspace, "src")

    if not os.path.exists(args.workspace):
        print(" - creating workspace folder: " + args.workspace)
        print(" - creating src subfolder")
        os.makedirs(src_path)
        print(" - copying create_pkg.py script")
        shutil.copyfile("./create_pkg.py", os.path.join(src_path, "create_pkg.py"))
        copy_tree("./settings/dependencies", os.path.join(src_path, "dependencies"))
        print(" - creating .vscode subfolder")
        os.makedirs(vscode_path)
        print(" - copying tasks.json file")
        shutil.copyfile("./settings/tasks.json", os.path.join(vscode_path, "tasks.json"))
        if args.keybindings:
            print(" - patching keybindings file")
            patch_keybindings()
        print(" - changing directory to workspace")
        os.chdir(args.workspace)
        print(" - catkin init")
        os.system("catkin init")
        #print(" - running vscode")
        #os.system("code " + args.workspace)
        print("WORKSPACE CREATED")
    else:
        print("Workspace folder already exists")
        
if __name__ == "__main__":
    main()
        









