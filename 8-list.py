# l = [1, 2, 3, 4, 5]

# print(l[0])
# print(l[1: 2])
# print(l[-2: -1])
# print(l[:])

# print(l[0:5:2])

l = [1, 2, 1, 1, 3, 4, 5, -1]

l2 = [7, 8, 9]
print(l[-1:])     # [5]
print(l[-1::-1])  # [5, 4, 3, 2, 1]

print(len(l))
print(max(l))
print(min(l))
print(l.count(1))

l.append(88)
print(l)
l.pop()
print(l)

l.remove(5)
print(l)

l.reverse()
print(l)

l.sort(reverse=False)
print(l)

l.index(-1)
print(l, 12)
