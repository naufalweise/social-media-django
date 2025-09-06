fst = 0
snd = 1
n_raw = input("Barisan ke: ")
n = int(n_raw)

if n == 1:
    ans = fst
elif n == 2:
    ans = snd
else:
    sisa_n = n - 2
    for i in range(sisa_n):
        fst_old = fst
        fst = snd
        snd = fst_old + snd
    ans = snd

print(ans)
