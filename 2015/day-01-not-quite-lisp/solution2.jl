function solve(path)
    line = ""
    open(path) do file
        line = readline(file)
    end

    floor = 0
    for index in 1:length(line)
        floor += line[index] == '(' ? 1 : -1
        if (floor == -1)
            println(index)
            return
        end
    end
end

solve("input-test.txt")
solve("input.txt")
