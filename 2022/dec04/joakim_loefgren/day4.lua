local f = assert(io.open('./input.txt', 'r'))
local text = f:read("*all")
local occ_contain = 0
local occ_overlap = 0
for lo1, hi1, lo2, hi2 in string.gmatch(text, '(%d+)%-(%d+),(%d+)%-(%d+)%\n') do
    lo1 = tonumber(lo1)
    hi1 = tonumber(hi1)
    lo2 = tonumber(lo2)
    hi2 = tonumber(hi2)
    if (lo1 <= lo2 and hi2 <= hi1) or (lo2 <= lo1 and hi1 <= hi2) then
        occ_contain = occ_contain + 1
    end
    if not (hi1 < lo2 or hi2 < lo1) then
        occ_overlap = occ_overlap + 1
    end
end

print(occ_contain)  -- part I
print(occ_overlap)  -- part II
