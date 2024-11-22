def all_variants(text):
    for i in range(1, len(text)+1):
        a = 0
        b = i
        while a <= len(text)-b:
            yield text[a:i]
            a += 1
            i += 1

a = all_variants("abc")
for i in a:
    print(i)