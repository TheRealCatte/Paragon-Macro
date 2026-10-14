---@diagnostic disable: undefined-global

local map = ...
if image("all_maps", 0.7) then
    click(735, 225)
    write(map)
    click(735, 340)
end