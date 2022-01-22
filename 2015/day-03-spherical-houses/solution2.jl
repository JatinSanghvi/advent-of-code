function solve(path)
    line = nothing
    open(path) do file
        line = readline(file)
    end

    pos = [(0, 0), (0, 0)]
    positions = Set()
    push!(positions, (0, 0))

    for (index, char) in enumerate(line)
        turn = index % 2 + 1

        if char == '^'
            pos[turn] = (pos[turn][1], pos[turn][2] - 1)
        elseif char == 'v'
            pos[turn] = (pos[turn][1], pos[turn][2] + 1)
        elseif char == '<'
            pos[turn] = (pos[turn][1] - 1, pos[turn][2])
        elseif char == '>'
            pos[turn] = (pos[turn][1] + 1, pos[turn][2])
        end

        push!(positions, pos[turn])
    end

    println(length(positions))
end

solve("input-test1.txt")
solve("input-test2.txt")
solve("input.txt")
