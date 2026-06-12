    #   0   1   2   3   4   5    6  7   8    9
bar = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# print(bar[0:3]) #원본을 건드리지 않는다 copy

i = 0
while i < 3:
    print(bar[i])
    i += 1  

# for i in range(3):
#     print(bar[i],end=" ")

# print(bar[1:5])
# print(bar[1:5:1])
# print(bar[1:5:2])


# bar = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# foo = bar[::-1]
# print(foo)
# print(bar[1::])
# for value in bar:
#     foo.append() 

# 뒤에서 5명
# foo = bar[:-6:-1]
# print(foo)

# 앞에서 3명
# foo = bar[:4:1]
# print(foo)

# 양쪽 끝 공백제거
# msg = " hello world "
# result = msg[1:-1]
# print(result)

# msg = " hello world "
# result = "".join(msg.split())
# print(result)

# pos = [1,2,3]
# foo = [4,5]
# print(pos + foo)

# bar = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# foo = bar[::]
# foo[:4] = [0]
# print(foo)

# bar[0] = 2000
# bar[:4] = [0,0,0,0]
# print(bar)

# bar = [10, 20, 30, 40, 50]
# bar[1:3] = [1000,2000,3000,4000,5000] # 1번부터 3번까지(2번) 1000 - 5000 집어넣기
# print(bar)

# bar = [1,2,3]
# foo = [1,3,2]
# list collection 
# opperator
# 1) +,*
# print(bar + foo)
# print("-"*10)
# 2) == , !=
# print(bar != foo) # false or True
# 3) > >= < <=
# print(bar >= foo) # True or false
# 4) in not in
# print(10 not in bar) # True or false
# 5) = 

# score_list = list(map(int, input().split()))

bar = [100,20,3,24,35,66,77,68]

bar.sort()

print(bar)

bar.sort(reverse=True)

print(bar)