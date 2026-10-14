---@diagnostic disable: undefined-global

local color = pixelColor(950,20)
repeat
    moveTo(500, 500)
    dragTo(500, 800, "right", 0.1)
until not pixelMatchesColor(950,20, color, 10)