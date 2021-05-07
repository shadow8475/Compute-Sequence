def not_invalid(a):
    for n in range(len(a)-1):
        if n+a[n+1] < len(a) and a[n+a[n+1]] != a[n] + a[n+1]:
            return False
    return True

def compute(a, m):
    '''computes m more terms and backtracks when necessary'''
    if m <= 0:
        return a
    # attempt to compute next term
    for k in range(1, len(a)+1):
        if not_invalid(a + [k]):
            seq = compute(a + [k], m-1)
            if seq:
                return seq
    else:
        # backtrack
        return

print(compute([0], 35))
