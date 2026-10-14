---@diagnostic disable: undefined-global

-- Locals
local path = getPath()
local settings = getSettings()

local macroSettings = settings["macro"]
local grindSettings = macroSettings["grind"]
local methods = grindSettings["methods"]

local totalRepetitions = 0

-- Functions
local function doMethod(configs, currentCount)
    local mode = string.lower(configs.mode)
    local map = configs.map
    local modifiers = configs.modifiers
    local loadout = configs.loadout
    local steps = configs.steps
    local lastRepetition = false

    if currentCount >= totalRepetitions then
        lastRepetition = true
    end

    -- runScript("actions", "goToGameMode", mode)
    -- runScript("actions", "closeChat")
    -- runScript("actions", "selectModifiers", modifiers)
    -- runScript("actions", "equipLoadout", loadout)
    runScript("paths", "spawnToMapOverride")
    runScript("actions", "selectMapOnMapOverride", map)
    runScript("paths", "mapOverrideToMap")

    wait(7)

    runScript("actions", "moveCameraDown")
end

-- Main
-- Goes through every method given before continuing off to other tasks
for items in python.iter(methods) do
    local method = items["method"]
    local count = items["count"]

    totalRepetitions = count

    local methodConfigs = runScript("methods", method)
    for i=1,count do
        doMethod(methodConfigs, i)
    end
end