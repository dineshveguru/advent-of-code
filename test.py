# print(str(ord("a")) + " - 1") 97
# print(str(ord("A")) + " - 27") 65
small = {}
cap = {}
for i in range(97, 123):
    small[chr(i)] = i - 96

for i in range(65, 91):
    cap[chr(i)] = i - 38


