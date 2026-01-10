square_list = [i**2 for i in range(1,10) if i%2==0]
print(square_list)

two_d_list = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# one_d_list = [j for i in two_d_list for j in i]

one_d_list = [two_d_list[i][j] for i in range(len(two_d_list)) for j in range((len(two_d_list[i])))]


print(one_d_list)