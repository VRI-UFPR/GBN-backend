import numpy as np
def levenshteinDistance(str1, str2):
    n = len(str1)
    m = len(str2)

    if n == 0:
        return m
    if m == 0:
        return n

    # cria duas listas de tamanho n+1, onde cada elemento é i
    tam = max(n, m)
    v0 = np.arange(tam + 1, dtype=np.uint64)
    v1 = np.zeros(tam + 1, dtype=np.uint64)

    # t é a maior string, s é a menor
    s = str1
    t = str2

    if m < n:
        aux = t
        t = s
        s = aux
        aux = m
        m = n
        n = aux

    for i in range(0, n):
        v1[0] = i + 1
        for j in range(0, m):
            if s[i] == t[j]:
                cost = 0
            else:
                cost = 1

            a = v1[j] + 1
            b = v0[j + 1] + 1
            c = v0[j] + cost

            if a <= b and a <= c:
                v1[j + 1] = a
            elif b <= a and b <= c:
                v1[j + 1] = b
            else:
                v1[j + 1] = c
            
            # a mesma coisa que:
            # v1[j+1] = min(v1[j] + 1, v0[j + 1] + 1, v0[j] + cost)
        v0 = v1.copy()

    return v1[m]