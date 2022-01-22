using MD5

function solve(path)
    key = nothing
    open(path) do file
        key = readline(file)
    end

    for suffix in 1:2000000
        hash = bytes2hex(md5(key * string(suffix)))
        if startswith(hash, "00000")
            println(suffix)
            return
        end
    end
end

solve("input-test1.txt")
solve("input-test2.txt")
solve("input.txt")
