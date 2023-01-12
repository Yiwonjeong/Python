"""
날짜: 2023/01/11
이름: 이원정
내용: 파이썬 모듈 실습하기
"""
# 방법1
from sub2.calc import plus, minus

# 방법2
import sub2.calc as c 

r1= plus(1,2)
r2 = minus(4,3)

r3 = c.multi(4,2)
r4 = c.div(10,5)

print('r1: ', + r1)
print('r2: ', + r2)
print('r3: ', + r3)
print('r4: ', + r4)