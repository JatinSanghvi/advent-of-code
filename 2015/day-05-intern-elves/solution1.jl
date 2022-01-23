function solve(path)
    lines = nothing
    open(path) do file
        lines = readlines(file)
    end

    function isNice(str)
        count(c -> c in "aeiou", str) >= 3 &&
            match(r"([a-z])\1", str) !== nothing &&
            match(r"(?:ab)|(?:cd)|(?:pq)|(?:xy)", str) === nothing
    end

    println(count([isNice(line) for line in lines]))
end

solve("input-test1.txt")
solve("input.txt")
