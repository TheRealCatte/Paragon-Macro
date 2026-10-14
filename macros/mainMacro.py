# Imports
from submacros import luaHandler as lh
from pathlib import Path

import pyautogui as macro

import time
import yaml

# Variables
project = Path(__file__).resolve().parent.parent
macros = f"{project}/macros"
settings = yaml.safe_load(open(f"{project}/settings.yaml", "r"))
imagesFolder = f"{project}/images"

state = "none"

# Definitions

# Main
if __name__ == "__main__":
    #while True: # Loops
        time.sleep(1)

        try:
            if lh.image("timed_rewards", 0.8):
                lh.runScript("submacros", "collect")
        except:
            print("not found")
        lh.runScript("submacros", "grind")