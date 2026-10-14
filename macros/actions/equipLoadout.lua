---@diagnostic disable: undefined-global

local loadout = ...
image("inventory", 0.8, true, 0.4, true)
for i=1,5 do
    click(650, 200, 1, 0.1)
    click(685, 270, 1, 0.1)
    click(350, 400, 1, 0.1)

    wait(0.2)

    if pixelMatchesColor(280, 720, "85, 255, 127", 10) then
        click(1285, 750, 1, 0.1)
    else
        click(650, 200, 1, 0.1)
        click(685, 270, 1, 0.1)
        break
    end
end

for _,tower in pairs(loadout) do
    print(tower)
    local usingGolden = string.find(tower, "g-", 1, true)
    if usingGolden then
        print("using golden")
        tower = split(tower, "g-")[1]
    end

    click(430, 210, 1, 0.1)
    write(tower)
    click(350, 400, 1, 0.1)
    click(1285, 750, 1, 0.1)

    if usingGolden then
        image("disabled_golden_perk", 0.75, true, 0.7, true)
    end
end
click(1100, 85, 1, 0.1)