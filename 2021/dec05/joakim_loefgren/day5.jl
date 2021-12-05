function parse_input(input_file="./input_day5.txt")
    lines = open(input_file, "r") do f
        readlines(f)
    end
    re = r"(\d+)"
    vents = zeros(Int64, 4, length(lines))
    for (i, line) in enumerate(lines)
        nums = parse.(Int, SubString.(line, findall(re, line))) .+ 1
        if nums[1] > nums[3]
            nums[1], nums[3] = nums[3], nums[1]
            nums[2], nums[4] = nums[4], nums[2]
        end
        vents[:, i] = nums
    end
    return vents
end


function build_seafloor(vents::Array{Int64, 2}, diagonal::Bool=false)
    nx = max(maximum(@view vents[1, :]), maximum(@view vents[3, :]))
    ny = max(maximum(@view vents[2, :]), maximum(@view vents[4, :]))
    seafloor = zeros(Int, ny, nx)
    nvents = size(vents)[2]
    for n in 1:nvents
        if vents[1, n] == vents[3, n]  # vertical
            jmin = min(vents[2, n], vents[4, n]) 
            jmax = max(vents[2, n], vents[4, n]) 
            seafloor[jmin : jmax, vents[1, n]] .+= 1
        elseif vents[2, n] == vents[4, n]  # horizontal
            seafloor[vents[2, n], vents[1, n] : vents[3, n]] .+= 1
        else
            if diagonal == true  # diagonal
                if vents[4, n] > vents[2, n]
                    for k in 0:(vents[3, n] - vents[1, n])
                        seafloor[vents[2, n] + k, vents[1, n] + k] += 1
                    end
                else
                    for k in 0:(vents[3, n] - vents[1, n])
                        seafloor[vents[2, n] - k, vents[1, n] + k] += 1
                    end
                end
            end
        end
    end
    return seafloor
end

function main() 
    # Part I
    vents = parse_input()
    seafloor = build_seafloor(vents)
    println(sum(seafloor .>= 2))

    # Part II
    seafloor = build_seafloor(vents, true)
    println(sum(seafloor .>= 2))
end

main()
