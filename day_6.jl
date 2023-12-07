function find_win_combos(race)
    t, d = race
    wins = 0
    for i in 1:t
        if i*(t-i) >= d
            wins += 1 end end
    return wins end

f = open("input_6.txt", "r")
lines = readlines(f) 
close(f)
races = zip([parse(Int,t) for t in split(lines[1], "     ")[2:end]], [parse(Int,r) for r in split(lines[2], "   ")[2:end]])

# part 1
println(prod([find_win_combos(r) for r in races]))

# part 2
println(find_win_combos((parse(Int, join([string(r[1]) for r in races])), parse(Int, join([string(r[2]) for r in races])))))