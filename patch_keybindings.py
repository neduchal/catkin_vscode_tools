#!/usr/bin/python3

import os
import os.path
import shutil


def patch_keybindings():
    homedir = os.path.expanduser("~")
    keybindingsPath = os.path.join(
        homedir, ".config/Code/User/keybindings.json")
    if os.path.exists(keybindingsPath):
        keybindings = open(keybindingsPath, "r").read().split("\n")
        closingCharPos = searchForClosingChar(keybindings)
        if closingCharPos == -1:
            print("It is not possible to patch keybindings.")
            return False
        keybindingsLocal = open(
            "./settings/keybindings.json", "r").read().split("\n")
        closingCharPosLocal = searchForClosingChar(keybindingsLocal)
        if closingCharPosLocal == -1:
            print("Local keybindings file is corrupted.")
            return False
        startingCharPosLocal = searchForStartingChar(keybindingsLocal)
        if startingCharPosLocal == -1:
            print("Local keybindings file is corrupted.")
            return False
        keybindingsFinal = []
        for i, line in enumerate(keybindings):
            if i < closingCharPos:
                keybindingsFinal.append(line)
                if i == closingCharPos-1:
                    if (keybindingsFinal[-1][-1] != ","):
                        keybindingsFinal[-1] = keybindingsFinal[-1] + ","
        for i, line in enumerate(keybindingsLocal):
            if (i > startingCharPosLocal) and (i < closingCharPosLocal):
                keybindingsFinal.append(line)
        keybindingsFinal.append("]")

        f = open(keybindingsPath, "w")
        for line in keybindingsFinal:
            f.write(line + "\n")
        f.close()    
    else:
        shutil.copyfile("./settings/keybindings.json", keybindingsPath)
    return True

def searchForStartingChar(data):
    for i, line in enumerate(data):
        if line == "[":
            return i
    return -1


def searchForClosingChar(data):
    for i, line in enumerate(data):
        if line == "]":
            return i
    return -1


if __name__ == "__main__":
    patch_keybindings()
    pass
