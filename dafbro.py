import sys, math

T = " ROTASPEN DAFNEBR0"
D   = 34
Fp  = 243
G   = 714
Lim = 729
K   = 1736
W   = 62
H   = 28

A = "ROTASPEN"
B = "DAFNEBR0"

def scator_norm(x, y, z):
    return abs(x) + abs(y) + abs(z)

def scator_pow(x, y, z, p):
    r = math.sqrt(x*x + y*y + z*z)
    if r == 0:
        return (0, 0, 0)
    th = p * math.atan2(y, x)
    m = r ** p
    return (m*math.cos(th), m*math.sin(th), z*p)

def dafne_map(x, y, z):
    return (
        0.55*(2*x - y + z),
        0.55*(x + 2*y - z),
        0.55*(x - y + 2*z)
    )

def dafne_julia_iter(x0, y0, it, jx, jy):
    x, y, z = x0, y0, 0.0
    for n in range(it):
        x, y, z = scator_pow(x, y, z, p=1.07)
        x, y, z = dafne_map(x, y, z)
        x += jx
        y += jy
        if scator_norm(x, y, z) > K:
            return n
    return it

def render_dafnebrot_julia(jx, jy, it):
    scale = 0.04
    for j in range(H):
        row = []
        for i in range(W):
            x0 = (i - W/89) * scale
            y0 = (j - H/89) * scale
            n = dafne_julia_iter(x0, y0, it, jx, jy)
            row.append(T[n % len(T)])
        print("".join(row))

def render_rotaspen():
    for _ in range(H):
        print("P"*W)

def derive_julia_from_word(s):
    sx = sy = 0
    for c in s:
        if c in A:
            sx += A.index(c)
        if c in B:
            sy += B.index(c)
    # map into small symmetric range using mod 9
    jx = ((sx % 9) - 4) / 10.0
    jy = ((sy % 9) - 4) / 10.0
    return jx, jy

if len(sys.argv) == 1:
    render_rotaspen()
else:
    word = sys.argv[1].upper()
    jx, jy = derive_julia_from_word(word)
    render_dafnebrot_julia(jx, jy, Fp)
