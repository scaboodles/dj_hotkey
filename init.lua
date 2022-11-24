spaces = require("hs.spaces")
hotkey = require("hs.hotkey")
window = require("hs.window")
alert = require("hs.alert")

hs.hotkey.bind({"cmd", "ctrl"}, "l", function()
  moveWindowSpace(1)
end)

hs.hotkey.bind({"cmd", "ctrl"}, "h", function()
  moveWindowSpace(-1)
end)

hs.hotkey.bind({"ctrl", "option"}, "h", function()
  moveSpace(-1)
end)

hs.hotkey.bind({"ctrl", "option"}, "l", function()
  moveSpace(1)
end)

hs.hotkey.bind({"ctrl"}, "q", function()
  inputPath = os.tmpname()
  inputFile = io.open(inputPath, "w")
  button, log = hs.dialog.textPrompt("dj hotkey", "Add a song to the end of playback queue", "Song [, Artist]", "Queue it!", "Cancel")
  if button == "Queue it!" then
    inputFile:write(log)
    result = hs.execute("cd ~/dev/spotify/dj_hotkey/ && poetry run ./main.py " .. inputPath, true)
    print("result:")
    print(result)
    resultTable = split(result, "|")
    if inString(resultTable[3], "204") then
      queueAlertText = resultTable[1] .. " by " .. resultTable[2] .. " queued successfully"
      alert.show(queueAlertText, nil, nil, 10)
    else
      alert.show("Error queuing song", nil, nil, 10)
    end
  end
inputFile:close()
end)

function inString(s, substring)
  return s:find(substring, 1, true)
end

function split(str, sep)
  local t={}
  for match in string.gmatch(str, "([^"..sep.."]+)") do
    print(match)
    table.insert(t, match)
  end
  return t
end

function moveSpace(direction)
    local screen, index = getCurrentScreenSpace()
    local nextSpace = spaces.allSpaces()[screen][index+direction]
    if nextSpace then
        spaces.gotoSpace(nextSpace)
    end
end

function moveWindowSpace(direction)
  local win = window.focusedWindow()
  local screen, index = getCurrentScreenSpace()
  local nextSpace = spaces.allSpaces()[screen][index+direction]
  if nextSpace then
    spaces.moveWindowToSpace(win, nextSpace)
    spaces.gotoSpace(nextSpace)
    --else create space?
  end
end

function getCurrentScreenSpace()
  local spaceTable = spaces.allSpaces()
  local fs = spaces.focusedSpace()
  for screen,spaceIds in pairs(spaceTable) do
    for i,spaceId in pairs(spaceIds) do
      if spaceId == fs then
        return screen, i
      end
    end
  end
end

hs.grid.setGrid('3x2')
hs.hotkey.bind({"cmd", "ctrl"}, "i", function()
  hs.grid.show()
end)
