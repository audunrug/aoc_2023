# check if indice is at end
function is_not_end(t,i,j)
    (i ∉ [0, length(t[:,1])+1] && j ∉ [0, length(t[1,:])+1]) ? true : false
end

function look_around(t, i, j)
    res = false
    for i_1 in [i, i+1, i-1], j_1 in [j, j+1,j-1]
        if is_not_end(t,i_1,j_1)
            if t[i_1,j_1] ∉ [0, 1, 2, 3, 4 ,5 , 6, 7, 8, 9, raw"."]
                res = true
            end
        end
    end
    return res
end

function find_valid(t,n,m)
    vals, nums, adj = [], [], []
    for i in 1:n, j in 1:m
        p = t[i,j]
        if p isa Number
            push!(adj, look_around(t,i,j))
            push!(nums, string(p))
            if j==m || t[i,j+1] isa Char
                (sum(adj) > 0) && push!(vals, parse(Int, join(nums)))
                nums, adj = [], []
            end
        end        
    end
    return vals
end

function look_around_gear(t,i,j)
    vals, nums, visited = [], [], []
    for i_1 in [i, i+1, i-1], j_1 in [j, j+1,j-1]
        if is_not_end(t,i_1,j_1)
            if t[i_1, j_1] isa Number && (i_1, j_1) ∉ visited
                j_2 = j_1
                while is_not_end(t,i_1,j_2) && t[i_1, j_2] isa Number #chjeck backwards
                    pushfirst!(nums, string(t[i_1, j_2]))
                    push!(visited, (i_1, j_2))
                    j_2 -= 1
                end
                j_2 = j_1 + 1
                while is_not_end(t,i_1,j_2) && t[i_1, j_2] isa Number #check forwards
                    push!(nums, string(t[i_1, j_2]))
                    push!(visited, (i_1, j_2))
                    j_2 += 1
                end
                push!(vals, parse(Int, join(nums)))
                nums = []
            end
        end
    end
    return vals
end

function find_gear_ratios(t)
    sums = []
    for i in eachindex(t[:,1]), j in eachindex(t[1,:])
        if t[i,j] == '*'
            around = look_around_gear(t,i,j)
            if length(around) == 2
                push!(sums, around[1]*around[2])
            end
        end
    end
    sums
end

f = open("input_3.txt", "r")
lines = readlines(f) 
close(f)

# make matrix
n, m = length(lines), length(split(lines[1], ""))
t =  Array{Any}(undef, n, m)
for i in 1:n, j in 1:m
    c = split(lines[i], "")[j]
    c = only(c)
    isdigit(c) ? (t[i, j] = parse(Int, c)) : t[i, j] = c
end

# part 1
valid = find_valid(t,n,m)
println(sum(valid))

# part 2
gear_ratios = find_gear_ratios(t)
println(sum(gear_ratios))