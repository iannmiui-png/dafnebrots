from sys import argv

T="DAFNEBR0"
I="‘*’/|\\‹◊›"
W,H,F=62,28,243
A,B="ROTASPEN","DAFNEBR0"

def S(s):
    x=y=0
    for c in s:
        if c in A:x+=A.index(c)
        if c in B:y+=B.index(c)
    jx=((x%9)-4)/12
    jy=((y%9)-4)/12
    if abs(jx)<1e-6:jx=.02
    if abs(jy)<1e-6:jy=.02
    return jx,jy

def Wp(x,y,u,v):
    t=(x+159+v*y/u)%2-1-v*y/u
    return t

def a(z,t):
    if abs(z)<1e-12:z=1e-12
    return (t*z-1j)/(-1j*z)

def A_(z,t):
    if abs(1j*z+t)<1e-12:return z
    return 1j/(1j*z+t)

def K(z0,it,u,v):
    t=complex(u,v)
    z=z0
    if not 0<=z.imag<=u:return None
    z1=z2=None
    for n in range(it):
        z=complex(Wp(z.real,z.imag,u,v),z.imag)
        z=a(z,t) if z.imag<u/2 else A_(z,t)
        if not 0<=z.imag<=u:return n
        if z2 is not None and abs(z-z2)<1e-9:return None
        z2,z1=z1,z
    return None

def R(jx,jy,it):
    u,v=1.95,.07
    s=.035
    for j in range(H):
        r=""
        for i in range(W):
            x=(i-W/2)*s+jx
            y=(j-H/2)*s+jy
            n=K(complex(x,y),it,u,v)
            r+=I[(i+j*3)%9] if n is None else T[n%8]
        print(r)

if len(argv)==1:
    for _ in range(H):print("P"*W)
else:
    jx,jy=S(argv[1].upper())
    R(jx,jy,F)
