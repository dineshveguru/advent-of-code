small = {}
cap = {}
for i in range(97, 123):
    small[chr(i)] = i - 96

for i in range(65, 91):
    cap[chr(i)] = i - 38

data = open("day_3.in")
data = [i.strip() for i in data]
score = 0
# for i in data:
#     res = set(i[:len(i) // 2]).intersection(set(i[(len(i) // 2):]))
#     for i in res:
#         if i in small.keys():
#             score += small[i]
#         else:
#             score += cap[i]
# print(score)

for i in range(0, 300, 3):
    res = set(data[i]).intersection(
        set(data[i + 1])).intersection(set(data[i + 2]))
    for i in res:
        if i in small.keys():
            score += small[i]
        else:
            score += cap[i]
print(score)
