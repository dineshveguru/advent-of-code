# part one

x = [i.strip() for i in open("day_one.in")]
x = "\n".join(x)
x = x.split("\n\n")
x = list(map(lambda x: x.split("\n"), x))
for i in range(len(x)):
    x[i] = list(map(lambda x: int(x), x[i]))
res = max(list(map(lambda x: sum(x), x)))
print(res)


# part two

data = list(map(lambda x: sum(x), x))
data = sorted(data, reverse=True)
print(sum(data[:3]))
