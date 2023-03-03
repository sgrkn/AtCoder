t = int(input())

#引数：x, 返り値：x^2+2x+3
def f(x):
    return x**2+2*x+3

ans = f(f(f(t)+t)+f(f(t)))

print(ans)