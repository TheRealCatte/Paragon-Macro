# Imports
from lupa import LuaRuntime
from pathlib import Path
from collections import Counter

import pyautogui as macro

import json
import time
import yaml

# Variables
project = Path(__file__).resolve().parent.parent.parent
macros = f"{project}/macros"
settings = yaml.safe_load(open(f"{project}/settings.yaml", "r"))
images = f"{project}/images"

baseWidth = 1920
baseHeight = 1080
winWidth, winHeight = macro.size()
scaleX, scaleY = winWidth / baseWidth, winHeight / baseHeight

lua = LuaRuntime(unpack_returned_tuples=True)

# Definitions
def runScript(type, actionName, *args):
    runner = lua.eval("""
        function(path, ...)
            chunk = loadfile(path)
            return chunk(...)
        end
    """)
    return runner(f"{macros}/{type}/{actionName}.lua", *args)

def scalePixel(x, y):
    return int(x * scaleX), int(y * scaleY)

# Basic definitions
def getSettings():
    return settings

def getPath():
    return macros

def getImages():
    return images

def wait(seconds):
    time.sleep(seconds)

def keyPress(key, duration=0.02):
    macro.keyDown(key)
    time.sleep(duration)
    macro.keyUp(key)

def keyDown(key):
    macro.keyDown(key)

def keyUp(key):
    macro.keyUp(key)

def write(string):
    macro.write(string, 0.02)

def moveTo(x, y, duration=0):
    macro.moveTo(*scalePixel(x, y), duration)

def dragTo(x, y, button="left", duration=0):
    macro.dragTo(*scalePixel(x, y), duration, button=button)

def click(x, y, clicks=1, duration=0.1, button="left", interval=0):
    macro.moveTo(*scalePixel(x, y), duration)
    time.sleep(0.02)
    macro.click(clicks=clicks, interval=interval, button=button)

def scroll(amount, x, y):
    macro.scroll(amount, *scalePixel(x, y))

def pixelColor(x, y):
    RGB = macro.pixel(*scalePixel(x, y))
    return f"{RGB[0]}, {RGB[1]}, {RGB[2]}"

# Complex definitions
def pixelMatchesColor(x, y, RGBColor=[0,0,0], tolerance=0, waitUntil=False, visible=False):
    if isinstance(RGBColor, str):
        RGBColor = tuple(map(int, RGBColor.split(',')))
    if waitUntil:
        while True:
            time.sleep(0.05)
            if visible:
                if macro.pixelMatchesColor(*scalePixel(x, y), RGBColor, tolerance):
                    break
            else:
                if not macro.pixelMatchesColor(*scalePixel(x, y), RGBColor, tolerance):
                    break
    return macro.pixelMatchesColor(*scalePixel(x, y), RGBColor, tolerance)

def image(imageName, confidence=0.5, decreaseConfidenceUntilFound=False, untilCondifence=0.4, clickIt=False, clicks=1, interval=0, grayscale=False):
    def getImage():
        try:
            centerPosition = macro.locateCenterOnScreen(f"{images}/{imageName}.png", confidence=confidence, grayscale=grayscale)
            if clickIt:
                click(centerPosition.x, centerPosition.y, clicks, 0.1, "left", interval)
            return {"x":centerPosition.x, "y":centerPosition.y}
        except macro.ImageNotFoundException:
            return None

    found = None
    if decreaseConfidenceUntilFound:
        while not found:
            if confidence <= untilCondifence:
                return None
            
            time.sleep(0.02)
            found = getImage()
            confidence -= 0.05
        return found
    else:
        return getImage()

def split(string, seperator):
    return str.split(string, seperator)

# Main
# Lua Functions
lua.globals().runScript = runScript
lua.globals().getSettings = getSettings
lua.globals().getPath = getPath
lua.globals().getImages = getImages

lua.globals().wait = wait
lua.globals().keyPress = keyPress
lua.globals().keyDown = keyDown
lua.globals().keyUp = keyUp
lua.globals().write = write
lua.globals().moveTo = moveTo
lua.globals().click = click
lua.globals().dragTo = dragTo
lua.globals().scroll = scroll
lua.globals().pixelColor = pixelColor
lua.globals().pixelMatchesColor = pixelMatchesColor
lua.globals().image = image
lua.globals().split = split