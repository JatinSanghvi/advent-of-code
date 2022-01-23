function solve(path)
    lines = nothing
    open(path) do file
        lines = readlines(file)
    end

    function isNice(str)
        match(r"([a-z])([a-z])[a-z]*\1\2", str) !== nothing && match(r"([a-z])[a-z]\1", str) !== nothing
    end

    println(count([isNice(line) for line in lines]))
end

solve("input-test2.txt")
solve("input.txt")
