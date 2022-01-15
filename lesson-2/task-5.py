
s = ""
for i in range(127 - 32 + 1):
    code = i + 32
    s += f"Код: {code}, символ: {chr(code)}; "
    if i % 10 == 0 or code == 127:
        print(s)
        s = ""
