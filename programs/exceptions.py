try:
    n = "12.25"
    l = int(n)
    out = l / 0
except ValueError as e:
    print("Value error")
    print(e)
except Exception as e:
    print("Global error")
    print(e)


l = ["12", "10", "12.25", "25"]
res = []

for item in l:
    try:
        res.append(int(item))
    except Exception as e:
        print(item, e)
        continue
    print(res)


