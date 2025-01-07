def areas(A, B, C):
    ret = A*B
    tri = (B*C)/2
    tra = ((C + B)*A)/2
    return int(ret), int(tri), int(tra)
