studen = {'a', 'b', 'c', 'd', 'a'}

print(studen)

if 'a' in studen:
    print('a在那里面')
else:
    print('a不在里面')

child = {'e', 'f', 'a'}

print(studen - child)  # 差集
print(studen | child)  # 并集
print(studen & child)  # 交集
print(studen ^ child)  # 不同时存在的元素
