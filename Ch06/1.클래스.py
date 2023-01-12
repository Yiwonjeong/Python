"""
날짜: 2023/01/11
이름: 이원정
내용: 파이썬 객체지향 class 실습하기
"""
# from package.py import class name 
from sub1.Car import Car
from sub1.Account import Account

sonata = Car('소나타', '흰색', 3000)
sonata.speedUp()
sonata.speedDown()
sonata.show()

bmw = Car('BMW', '검정', 5000)
bmw.speedUp()
bmw.speedDown()
bmw.show()

kb = Account('국민은행', '101-12-1110', '홍길동', 30000)
kb.deposit(20000)
kb.withdraw(5000)
# kb.balance += 10000 방지 -> 캡슐화(정보 은닉: __)
kb.show()

wr = Account('우리은행', '101-21-1110', '김유신', 10000)
wr.deposit(20000)
wr.withdraw(7000)
wr.show()