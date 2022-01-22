function solve(path)
    lines = nothing
    open(path) do file
        lines = readlines(file)
    end

    boxes = [[parse(Int64, c) for c in match(r"^(\d+)x(\d+)x(\d+)$", line).captures] for line in lines]
    ribbon_lengths = [2 * (box[1] + box[2] + box[3] - maximum(box)) + box[1] * box[2] * box[3] for box in boxes]
    println(sum(ribbon_lengths))
end

solve("input-test.txt")
solve("input.txt")
