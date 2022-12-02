-- Day 2 without if-statements, for fun
local M = {}

SHAPE_SCORES = {['A'] = 1, ['B'] = 2, ['C'] = 3, ['X'] = 1, ['Y'] = 2, ['Z'] = 3}
-- map difference in shape scores to win/lose/draw
DIFF_SCORES = {[-2] = 6, [-1] = 0, [0] = 3, [1] = 6, [2] = 0}


function M.play_game(file, play_round)
    local tot_score1 = 0
    local tot_score2 = 0
    for line in io.lines(file) do
        local shape1 = string.sub(line, 1, 1)
        local shape2 = string.sub(line, 3, 3)
        local score1, score2 = play_round(shape1, shape2)
        tot_score1 = tot_score1 + score1
        tot_score2 = tot_score2 + score2
    end
    return tot_score1, tot_score2
end

-- part I
function M.play_round_part1(char1, char2)
    local score1 = SHAPE_SCORES[char1]
    local score2 = SHAPE_SCORES[char2]
    local diff = score1 - score2
    score1 = score1 + DIFF_SCORES[diff]
    score2 = score2 + DIFF_SCORES[-diff]
    return score1, score2
end

print(M.play_game('test.txt', M.play_round_part1))

-- part II
-- for part II: map outcome X/Y/Z to increment on opponents
-- score needed to achieve outcome
STRATEGY = {['X'] = -1, ['Y'] = 0, ['Z'] = 1}

function M.play_round_part2(char1, char2)
    local score1 = SHAPE_SCORES[char1]
    local inc = STRATEGY[char2]
    local score2 = (score1 - 1 + inc) % 3 + 1
    local diff = score1 - score2
    score1 = score1 + DIFF_SCORES[diff]
    score2 = score2 + DIFF_SCORES[-diff]
    return score1, score2
end

print(M.play_game('input.txt', M.play_round_part2))
