def decorator(yskor):
    def wrapper():
        l=yskor()
        s=a*c+l*(c*c)/2
        print(l)
        print(s)
    return wrapper
try:
    a=int(input('V0='))
    b=int(input('V='))
    c=int(input('t='))
    @decorator
    def yskor():
        return((b-a)/c)
    yskor()
except ValueError:
    print("Нельзя вводить строки")
except ZeroDivisionError:
    print("Нельзя делить на ноль")
