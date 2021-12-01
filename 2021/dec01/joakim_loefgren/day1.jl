using DelimitedFiles

# part I
depths = readdlm("./input_day1.txt")[:]
count = sum(diff(depths) .> 0)
println(count)

# part II
function depth_increases(arr::Array{<:Real}, win_size::Int)
    count = 0
    old = 1e10
    for i in 1:length(depths) - win_size + 1
        new = sum(depths[i:i + win_size - 1])
        if new > old
            count += 1
        end
        old = new
    end
    return count
end

println(depth_increases(depths, 3))
