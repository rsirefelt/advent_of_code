local sum = 0
-- holds calorie counts for the top elves
-- use top = {0} for part I
local top = {0, 0, 0}

for line in io.lines('input.txt') do
    local cal = tonumber(line)
    if cal then
        sum = sum + cal
    else
        for i, val in ipairs(top) do
            if sum > val then
                for j = #top - i + 1, i + 1, -1 do
                    top[j] = top[j - 1]
                end
                top[i] = sum
                break
            end
        end
        sum = 0
    end
end

-- handle the last elf
for i, val in ipairs(top) do
    if sum > val then
        for j = #top - i + 1, i + 1, -1 do
            top[j] = top[j - 1]
        end
        top[i] = sum
        break
    end
end

local tot = 0
for _, cal in ipairs(top) do
    tot = tot + cal
end
print(tot)
