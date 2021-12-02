mutable struct Submarine
    x::Int
    y::Int
    aim::Int
end


function execute_simple!(submarine::Submarine, instruction::Tuple{String, Int})
    name, value = instruction
    if name == "forward"
        submarine.x += value
    elseif name == "up"
        submarine.y -= value
    elseif name == "down"
        submarine.y += value
    end
end


function execute!(submarine::Submarine, instruction::Tuple{String, Int})
    name, value = instruction
    if name == "forward"
        submarine.x += value
        submarine.y += submarine.aim * value
    elseif name == "up"
        submarine.aim -= value
    elseif name == "down"
        submarine.aim += value
    end
end


function parse_instructions(file_path::String)
    lines = open(file_path, "r") do f
        readlines(f)
    end
    instructions = Vector{Tuple{String, Int}}(undef, length(lines))
    for (i, line) in enumerate(lines)
        name, val = split(line)
        val = parse(Int, val)
        instructions[i] = (name, val)
    end
    return instructions
end


function main()
    instructions = parse_instructions("./input_day2.txt")

    sub1 = Submarine(0, 0, 0)
    sub2 = Submarine(0, 0, 0)
    for instr in instructions
        execute_simple!(sub1, instr)
        execute!(sub2, instr)
    end

    # Part I
    println(sub1.x * sub1.y)

    # Part II
    println(sub2.x * sub2.y)
end
