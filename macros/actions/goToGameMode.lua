---@diagnostic disable: undefined-global

local mode = ...
local clickPlay = image("play", 0.8, true, 0.4, true)
if clickPlay then
    wait(0.25)
    image("modes/"..mode, 0.8, true, 0.4, true)
    wait(0.25)
    click(760, 400, 1, 0.1)
    pixelMatchesColor(990, 400, "241, 226, 178", 0.5, true, true)
    pixelMatchesColor(990, 400, "241, 226, 178", 0.5, true, false)
end