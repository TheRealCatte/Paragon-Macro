---@diagnostic disable: undefined-global

local configs = {
    mode = "easy", -- Defaults to "easy" if not found
    map = "dead ahead", -- Doesnt need to be the full name, only enough to make the wanted map to show up on top
    canUseTimescale = true,
    --screenResolution = {1920,1080}, -- Change it to your screens so its accurate
    loadout = {
        -- ex: "soldier" or "g-soldier"
        -- It WILL unselect the golden attribute if not specified (It has to be "g-TOWERNAME" to be recognized)
        -- Putting an or statement will make it select the other tower if its not found
        -- If nothing is specified then it'll use the current loadout it has (Not recommended obviously)
        "g-soldier"
    },
    modifiers = {
        -- ex: "hidden" (Only put the first word of the wanted modifer)
        --"hidden",
    },

    --[[
        You are able to use functions like scalePixel()
        Unless changed, the camera position will always be at the map spawn, angled down, and zoomed out fully

        How to add:
            {Name, Action, args...}
            {"_USE_ABILITY", abilityName, x, y}
            ^^^ X,Y are used for abilities like hacker's clone
            ^^^ For ability name's look at the github for the names
            ^^^ To add missing abilities, add the ability image to .../MACRO/images/abilities
            {"_WAIT_UNTIL_WAVE", waveNumber}
            {"_FUNCTION", functionName, args...} <-- This is to use functions
            {"_REPEAT", count, {STEPS}} <-- For STEPS just add {}tables
            {"_CONTINUE_FROM", {STEPS}} <-- Allows to run a _REPEAT without halting
        
        Actions:
            place (towerSlot, x, y)
            upgrade (count)
            sell ()
            target (targetName)

        Example:
            {"soldier1", "place", 50, 273}
            {"soldier1", "upgrade", 1}
            {"soldier1", "target", "last"}
            {"_WAIT_UNTIL_WAVE", 8}
            {"dj", "place", 84, 1235}
            {"dj", "upgrade", 3}
            {"_CONTINUE_FROM", {
                {"_REPEAT", 99999, {
                    {"_USE_ABILITY", "dropTheBeat"}
                }}
            }}
            {"_FUNCTION", "wait", 2}

    ]]
    steps = {
        {"placement1", "place", 1, 1}
    },
}

return configs