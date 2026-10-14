#!/usr/bin/env python3
# Imports
from pynput import keyboard
from pathlib import Path

import threading as thr
import subprocess as sp
import customtkinter as tk

import psutil
import atexit
import yaml
import os

# Variables
project = Path(__file__).resolve().parent
settingsFile = f"{project}/settings.yaml"
data = yaml.safe_load(open(settingsFile, "r"))
hotKeys = data["hotKeys"]

macroActive = False
macroPaused = False
widgets = {}


# Definitions
def whatToAllMacros(type):
    for macro in psutil.Process(os.getpid()).children(recursive=True):
        if type == "terminate":
            macro.terminate()
        elif type == "suspend":
            macro.suspend()
        elif type == "resume":
            macro.resume()

def startMacro():
    global macroActive

    if not macroActive:
        with open(settingsFile, 'w') as file:
            yaml.safe_dump(data, file, default_flow_style=False, sort_keys=False)
        sp.Popen(["python", f"{project}/macros/mainMacro.py"])
        widgets["startButton"].configure(fg_color="#222222")
        macroActive = True
    
def stopMacro():
    global macroActive

    whatToAllMacros("terminate")
    widgets["startButton"].configure(fg_color="#444444")
    widgets["pauseButton"].configure(fg_color="#444444")
    macroActive = False

def pauseMacro():
    global macroActive
    global macroPaused

    if macroActive:
        macroPaused = not macroPaused
        if macroPaused:
            whatToAllMacros("suspend")
            widgets["pauseButton"].configure(fg_color="#888888")
        else:
            whatToAllMacros("resume")
            widgets["pauseButton"].configure(fg_color="#444444")

def onExit():
    whatToAllMacros("terminate")

def registerHotkeys():
    def keyPressed(key):
        for hotKey in hotKeys:
            if keyboard.Key[hotKey["key"]] == key:
                globals().get(hotKey["func"])()
    with keyboard.Listener(on_press=keyPressed) as listener:
        listener.join()

# Classes
class WebView(tk.CTk):
    def __init__(self):
        super().__init__()

        # Top level
        self.title("Macro")
        self.maxsize(600,350)
        self.minsize(600,350)
        self.configure(fg_color="#111111")
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)

        # Tabs
        tabView = tk.CTkTabview(self, 500, 330, 0, fg_color="transparent")
        tabView.place(x=100, y=-20)
        mainTab = tabView.add("main")
        grindingTab = tabView.add("grinding")
        collectTabe = tabView.add("collect")
        settingsTab = tabView.add("settings")
        tabView._segmented_button.grid_forget()
        tabView.set("main")

        # Side bar
        sideBar = Frame(self, ["grid", 0, 0, 0, 0, "nsw"], 100, 0, "#2b2b2b")
        Button(sideBar, ["grid", 0, 0, 0, 2, ""], 100, 30, "Main", lambda:tabView.set("main"))
        Button(sideBar, ["grid", 1, 0, 0, 2, ""], 100, 30, "Grinding", lambda:tabView.set("grinding"))
        Button(sideBar, ["grid", 2, 0, 0, 2, ""], 100, 30, "Collect", lambda:tabView.set("collect"))
        Button(sideBar, ["grid", 10, 0, 0, 2, ""], 100, 30, "Settings", lambda:tabView.set("settings"))

        # Bottom bar
        bottomBar = Frame(self, ["grid", 0, 0, 0, 0, "sew"], 0, 40, "#2b2b2b")
        widgets["startButton"] = Button(bottomBar, ["grid", 0, 0, 2, 5, ""], 100, 30, "Start Macro: F1", startMacro)
        widgets["pauseButton"] = Button(bottomBar, ["grid", 0, 1, 2, 5, ""], 100, 30, "Pause Macro: F2", pauseMacro)
        Button(bottomBar, ["grid", 0, 2, 2, 5, ""], 100, 30, "Stop Macro: F3", stopMacro)

class Frame(tk.CTkFrame):
    def __init__(self, Master, Geometry, Width, Height, FGColor):
        super().__init__(
            master=Master,
            width=Width,
            height=Height,
            corner_radius=0,
            fg_color=FGColor
        )
        self.grid_propagate(False)
        if Geometry[0] == "grid":
            self.grid(row=Geometry[1], column=Geometry[2], padx=Geometry[3], pady=Geometry[4], sticky=Geometry[5])
        elif Geometry[0] == "place":
            self.place(x=Geometry[1], y=Geometry[2], relx=Geometry[3], rely=Geometry[4])

class Button(tk.CTkButton):
    def __init__(self, Master, Geometry, Width, Height, Text, Func):
        super().__init__(
            master=Master,
            width=Width,
            height=Height,
            text=Text,
            command=Func,
            corner_radius=0,
            fg_color="#444444",
            hover_color="#666666",
        )
        if Geometry[0] == "grid":
            self.grid(row=Geometry[1], column=Geometry[2], padx=Geometry[3], pady=Geometry[4], sticky=Geometry[5])
        elif Geometry[0] == "place":
            self.place(x=Geometry[1], y=Geometry[2], relx=Geometry[3], rely=Geometry[4])

# Main
if __name__ == "__main__":
    atexit.register(onExit)
    thr.Thread(target=registerHotkeys, daemon=True).start()

    # Should be last
    WebView().mainloop()