# # list
# bar =  [1,2,3,4,5]
# # index 0 1 2 3 4 
# print(bar[4])

# bar = [10, 20, 30, 40, 50]

# foo = list(range(200))

# print(foo[len(foo) - 1])
# print(foo[-1])
#    -5   -4  -3  -2  -1 
bar = [10, 20, 30, 40, 50]
# #     0   1   2   3   4
bar.append(70)
bar.append(100)
bar.append(120)
print(bar)
print(bar[-5])

# insert
# print(bar)
# bar.insert(0, 99)
# print(bar)
# bar.insert(-2,999)
# print(bar)
# bar[2] = 1000
# print(bar)

# x = [1, 2, 3, 4]
# rev = x[2::] 
# print(rev)

# a = [3, 1, 4, 1, 5, 9, 2, 6]
# # 추가
# a.extend([8, 9])
# a.append(7)
# a.insert(1, 99)
# print(a)

# bar = [10, 20, 30, 40, 50]
# bar.remove(100)
# print(bar)

# print(bar)
# del bar[1] #index를 이용해 삭제
# print(bar)

# bar = [10, 20, 30, 40, 50]
# print(bar.pop())
# print(bar)

# bar = []

# bar.append(10)
# bar.append(30)
# bar.append(20)
# print(bar)

# print(bar.pop())
# print(bar.pop())
# print(bar.pop())
# print(bar)

# bar = []
# 초기화 CRUD
# 초기화 -> literal, function
# create -> append,insert
# read -> ref var [index]
# update -> 

# bar = [list(range(1_000_000))]
# print(len(bar))
# bar.clear()
# print(bar)

# indexing -> slice indexing
# bar = [10, 20, 30, 40, 50]
# foo = bar[-4:]

# print(f"bar: {bar}")
# print(f"foo: {foo}")

# foo[0] = 100
# print(bar)
# print(foo)

# #      0   1   2   3   4
# bar = [10, 20, 30, 40, 50]
# #     -5  -4  -3  -2  -1 
# foo = bar[-3::-1]
# print(f"foo: {foo}")

bar = [10, 20, 30, 40, 50, 60, 70, 80]
