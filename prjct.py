def trngl(n):
    for i in range(n):
        for j in range(n-i):
            print(' ', end=' ')
        for k in range(2*i+1):
            print('*',end=' ')
        print()
def stick(n):
    for i in range(n):
        for j in range(n-1):
            print(' ', end=' ')
        print('* * *')

trngl(5)
trngl(5)
trngl(5)
stick(5)
print("HAPPY CHRISTMAS")
print(".....AND.....")
print("HAPPY NEW YEAR")
print("  ")
print("CREATED BY: ")
print("     NAYOF K S")