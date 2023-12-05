function sort_game(game)
    result = Dict()
    for r in split(game, "; "), draw in split(r, ", ")
        n, c = split(draw, " ")
        n = parse(Int, n)
        (c in keys(result)) ? push!(result[c], n) : result[c] = [n]
    end
    result
end

function eval_game(line, thr)
    res, game  = true, sort_game(line)
    for col in keys(thr)
        (maximum(game[col]) > thr[col]) && (res = false)
    end
    res
end

get_power(gm) = prod([maximum(gm[col]) for col in keys(gm)])

f = open("input_2.txt", "r")
lines = readlines(f) 
close(f)

# part 1
threshold = Dict("blue"=>14,"red"=>12,"green"=>13)
println(sum([(eval_game(g[2], threshold)) && parse(Int, split(g[1], " ")[end]) for g in [split(l, ": ") for l in lines]]))

# part 2
println(sum([get_power(sort_game(g)) for g in [split(l, ": ")[end] for l in lines]]))