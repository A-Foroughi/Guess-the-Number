print("Enter the start and the end of the period: ")
a, b = input().split()
a, b = int(a), int(b)
q = 0
print("Pick a number between the period you chose.")
print("If your number is larger than my guess enter l.")
print("If your number is smaller than mine enter s.")
print("and if i got your number right enter e.")
print("If you are ready press enter.")
enter = input()
while b >= a:
    m = (a + b) // 2
    print(f"My guess is {m}")
    q += 1
    g = input()
    if g == "l":
        a = m + 1
    elif g == "s":
        b = m - 1
    elif g == "e":
        print(f"I got it with {q} guesses.")
        break
    else:
        print(f"I said l, s or e not {g}")