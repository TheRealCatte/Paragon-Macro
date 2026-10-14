---@diagnostic disable: undefined-global

runScript("actions", "moveCameraDown")
scroll(-50, 500, 500)

keyDown("w")

local flipped = false
repeat wait(0.02)
    if pixelMatchesColor(950, 20, "244, 212, 149", 20) then
        flipped = true
        keyUp("w")
        keyDown("s")
    end
until pixelMatchesColor(950, 20, "166, 177, 183", 10) or pixelMatchesColor(920, 1070, "166, 177, 183", 15)
--wait(1)
keyUp("w")
keyUp("s")
if flipped then
    keyDown("a")
else
    keyDown("d")
end
repeat wait(0.02)
until image("e", 0.7)
keyUp("d")
keyUp("a")
keyPress("e", 1)