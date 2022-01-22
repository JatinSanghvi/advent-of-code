function solve(path)
    line = nothing
    open(path) do file
        line = readline(file)
    end

    pos = (0, 0)
    positions = Set()
    push!(positions, pos)

    for char in line
        if char == '^'
            pos = (pos[1], pos[2] - 1)
        elseif char == 'v'
            pos = (pos[1], pos[2] + 1)
        elseif char == '<'
            pos = (pos[1] - 1, pos[2])
        elseif char == '>'
            pos = (pos[1] + 1, pos[2])
        end

        push!(positions, pos)
    end

    println(length(positions))
end

solve("input-test1.txt")
solve("input-test2.txt")
solve("input.txt")
