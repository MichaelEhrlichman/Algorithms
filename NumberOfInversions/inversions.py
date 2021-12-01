import sys

def leading_le_0(l,r):
    if len(l) > 0 and len(r) > 0:
        return 'l' if l[0] <= r[0] else 'r'
    elif len(l) > 0:
        return 'l'
    else:
        return 'r'

def merge_sort(a):
    if len(a) > 2:
        m = len(a)//2
        al,invsr = merge_sort(a[:m])
        ar,invsl = merge_sort(a[m:])
        i = 0
        merge_invs = 0
        while len(al)>0 or len(ar)>0:
            if leading_le_0(al,ar) == 'l':
                a[i] = al[0]
                del al[0]
            else:
                a[i] = ar[0]
                del ar[0]
                if len(al) > 0:
                    merge_invs += len(al)
            i += 1
        return a, merge_invs+invsr+invsl
    elif len(a) == 2:
        if a[0] <= a[1]:
            return a, 0
        else:
            return [a[1],a[0]], 1
    elif len(a) == 1:
        return a, 0
    else:
        print('bomb')
        print(1/0)

def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    #write your code here
    return number_of_inversions

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    #print(a)
    b, ninv = merge_sort(a)
    print(ninv)
    #print(get_number_of_inversions(a, b, 0, len(a)))
