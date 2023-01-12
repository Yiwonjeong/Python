"""
날짜: 2023/01/12
이름: 이원정
내용: 파이썬 외부 패키지 모듈 실습하기
"""

from openpyxl import Workbook

# 새로운 엑셀파일 생성
workbook = Workbook()

# 첫 번째 시트 활성화
sheet = workbook.active

# 데이터 입력
sheet['A1'] = "파이썬 엑셀 실습"
sheet.append(['a101','김유신','010-1111-1111',25,'김해시'])
sheet.append(['a102','김춘추','010-1111-2222',23,'원주시'])
sheet.append(['a103','이순신','010-1111-3333',45,'진주시'])
sheet.append(['a104','장보고','010-1111-4444',15,'부산시'])
sheet.append(['a105','강감찬','010-1111-5555',55,'청주시'])

# 저장 닫기
workbook.save('/Users/iilhwan/Desktop/Member.xlsx')
workbook.close()