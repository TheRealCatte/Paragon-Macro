---@diagnostic disable: undefined-global

-- Locals
local path = getPath()
local settings = getSettings()

local macroSettings = settings["macro"]
local collectSettings = macroSettings["collect"]
local timedRewards = collectSettings["timedRewards"]
local spinWheel = collectSettings["spinWheel"]

local getToTheWheelAttempt = 0

-- Functions
local function getLoginRewards()
    -- If the login page is showing, click on the Claim button
    local showingLoginRewards = image("login_rewards", 0.8)
    if showingLoginRewards then
        image("login_claim.png", 0.8, true, 0.4, true)
    end
end

local function getTimedRewards()
    -- If the timed reward button is visible, click on it
    local TimedRewards = image("timed_rewards", 0.8, false, 0, true)
    if TimedRewards then
        -- Repeat until there's no visible green claim button
        while true do wait(0.01)
            local claimed = image("rewards_claim", 0.8, true, 0.4, true, 6, 0.25)
            if not claimed then
                break
            end
        end

        moveTo(200,200)

        -- Close the timed rewards page
        image("timed_rewards", 0.8, false, 0, true)
    end
end

local function getWheel()
    -- Resets to reposition to spawn in case the player was moved before starting
    keyPress("esc")
    keyPress("r")
    keyPress("enter")

    wait(6)

    -- Scrolls out
    scroll(-50, 500, 500)

    local survivalSign = image("survival_sign", 0.8, true, 0.6)
    local storySign = image("story_sign", 0.8, true, 0.6)

    -- If survival or story sign is visible, then walk to there. If not just skip the entire process if failed 3 times
    if survivalSign then
        runScript("paths", "survivalSignToWheel")
    elseif storySign then
        runScript("paths", "storySignToWheel")
    else
        getToTheWheelAttempt = getToTheWheelAttempt + 1
        getWheel()
        if getToTheWheelAttempt >= 3 then
           return
        end
    end

    -- Repeats spinning the wheel until the close button from the shop is visible
    -- If it fails to spin the wheel 5 times, resets
    local oldPixel = pixelColor(500,500)
    local attempts = 0
    while true do wait(1)
        keyPress("e")
        wait(0.5)

        if image("close", 0.8, true, 0.4, true) then
            return
        elseif oldPixel ~= pixelColor(500,500) then
            oldPixel = pixelColor(500,500)
            attempts = 0

            wait(15)
            image("wheel_claim", 0.9, true, 0.4, true)
            moveTo(250, 250)
        end

        attempts = attempts + 1
        if attempts == 5 then
            getWheel()
            return
        end
    end
end

-- Main
getLoginRewards()

if timedRewards then
    getTimedRewards()
end
if spinWheel then
    getWheel()
end