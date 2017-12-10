with open('day1.txt', 'r') as f:
    data = f.read().strip()

length = len(data)
digits = [int(d) for d in list(data) + [data[0]]]
total = 0


for i,  d in enumerate(digits):
    if i + 1 > length:
        continue
    if d == digits[i + 1]:
        total += d

print total
