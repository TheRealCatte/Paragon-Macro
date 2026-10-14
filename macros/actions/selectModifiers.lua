---@diagnostic disable: undefined-global

local modifiers = ...
if #modifiers > 0 then
    image("modifiers", 0.8, true, 0.4, true)
    for _,modifier in pairs(modifiers) do
        modifier = string.lower(modifier)
        image("modifiers/"..modifier, 0.8, true, 0.4, true)
    end
    image("close", 0.8, true, 0.4, true) 
end