function solve(path)
    line = ""
    open(path) do file
        line = readline(file)
    end

    floor = count(c -> c == '(', line) - count(c -> c == ')', line)
    println(floor)
end

solve("input-test.txt")
solve("input.txt")
