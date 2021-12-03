num = int(input())

nops_lst = [0,1,1]
seq_lst = [[1],[1],[1,2]]

while len(nops_lst) < num:
    new_num = len(nops_lst)+1
    nops_a,nops_b = float('inf'),float('inf')

    if new_num%2 == 0:
        nops_a = nops_lst[new_num//2-1]+1
    if new_num%3 == 0:
        nops_b = nops_lst[new_num//3-1]+1

    nops_c = nops_lst[-1]+1

    if nops_a <= nops_b and nops_a <= nops_c:
        nops_lst.append(nops_a)
        seq_lst.append(seq_lst[new_num//2-1]+[new_num])
    elif nops_b <= nops_a and nops_b <= nops_c:
        nops_lst.append(nops_b)
        seq_lst.append(seq_lst[new_num//3]-1+[new_num])
    elif nops_c <= nops_a and nops_c <= nops_b:
        nops_lst.append(nops_c)
        seq_lst.append(seq_lst[-1]+[new_num])

print(nops_lst[num-1])
print(*seq_lst[num-1])
