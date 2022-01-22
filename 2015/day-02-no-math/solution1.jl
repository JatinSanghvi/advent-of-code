function solve(path)
    lines = nothing
    open(path) do file
        lines = readlines(file)
    end

    boxes = [[parse(Int64, c) for c in match(r"^(\d+)x(\d+)x(\d+)$", line).captures] for line in lines]
    face_areas = [[box[1] * box[2], box[2] * box[3], box[3] * box[1]] for box in boxes]
    paper_areas = [2 * (area[1] + area[2] + area[3]) + minimum(area) for area in face_areas]
    println(sum(paper_areas))
end

solve("input-test.txt")
solve("input.txt")
