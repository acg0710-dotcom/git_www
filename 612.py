# bar = [100,20,3,24,35,66,77,68]

# # bar.sort() #오름차순 정렬

# # print(bar)

# #bar.sort(reverse=True)#리버스 = 트루로 내림차순 정렬

# # foo = bar[:3]#복사
# # foo[0] = 1
# # print(bar[0])

# bar.sort(reverse=True)
# print(bar)

# bar[:3] = [100, 100, 100]
# print(bar)

# del bar[:3]
# print(bar)
# # 슬라이싱 인덱스 자유롭게 쓰게 연습

# bar = [100,20,3,24,35,66,77,68]
# print(sum(bar)/len(bar)) #평균
# print(max(bar)) #최고점
# print(min(bar)) #최저점
# # bar.sort(reverse=True)
# print(bar)

# idx = bar.index(99)

# bar[idx]
# print(idx)

# bar = [x for x in range(10)]
# foo = {x for x in range(10) if x % 2 == 0}
# print(bar, f"bar type: {type(bar)}")
# print(foo, f"foo type: {type(foo)}")

# bar = [7] * 100
# print(bar)

# bar = [7 for _ in range(100)]
# print(bar)

# bar = [표현식 반복(요소의 개수) 선택(필터링)]
# bar = [1 for _ in range(3)]
# print(bar)
# bar = [x for x in range(3)]
# print(bar)
# bar = [(x + 1) for x in range(3)]
# print(bar)

# squares = []
# for i in range(5):
#     squares.append(i ** 2)
# print(squares)

# squares = [i**2 for i in range(5)]
# print(squares)

# items = [900,700,600] # 세전
# items_tax = [price * 1.1 for price in items ] # 세후, + vat 10%
# print(items_tax)

# # 2의 1승부터 2의 10승까지
# num = [2**exp for exp in range(1,11)]
# print(num)

# 1 -> 10 정수중 3의배수인 list
# bar = [x for x in range (1,11) if x % 3 == 0]
# print(bar)

# foo = [90,70,20,30,40,10]
# pos = [score 
#        for score in foo
#        if score >= 60
#        ]
# print(pos)

# name_list = [" kim"," lee   ","so      ","      ","soo"]
# # title -> kim lee so soo
# # 좌우 공백은 삭제 공백만 있을 경우 제거
# title = [name for name in name_list]
#             #공백제거  #대문자로 변환           # 이름이 있으면 true 
# title = [name.strip().title() for name in name_list if name.strip()]

# print(title)

matrix = [[1,2], 
       [3,4]]
foo = [x for row in matrix
       for x in row]
print(foo) # 1,2,3,4 벡터로 변환
print(matrix[0]) # 1,2
print(matrix[1]) # 3,4
# 단어 하나짜리 입력('abc')은 정확히 통과했지만, 여러 단어가 있는 경우 순서가 뒤집혀 출력되는 문제가 있습니다.
# 핵심 원인은 두 가지입니다. 첫째, 공백 감지 조건이 char == "" (빈 문자열)로 되어 있어 실제로 공백 문자 ' '를 검출하지 못합니다. 둘째, 단어를 뒤집는 방식으로 word = char + word를 사용했는데,
# 이렇게 하면 문자를 앞에 계속 붙여 나가므로 단어 자체는 뒤집히지만 단어들이 result에 역순으로 쌓이게 됩니다.

# 예를 들어 'hello world'를 처리할 때 공백을 만나지 못하므로 전체 문자열이 하나의 word로 쌓이고, 결국 'dlrow olleh'가 출력됩니다. 올바른 접근은 word += char로 문자를 뒤에 붙여 단어를 모은 뒤, 공백을 만났을 때 word[::-1]로 뒤집거나 별도 슬라이싱으로 처리하는 방식입니다. 주석으로 흐름을 설명하려는 노력은 좋았습니다!