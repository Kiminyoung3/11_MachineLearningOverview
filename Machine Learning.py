import numpy
import pandas as pd
import sklearn

data = {
    '학번': range(2000, 2010),
    '성적': [85, 95, 75, 70, 100, 100, 95, 85, 80, 85]
}

print(data['성적'])
print(pd.DataFrame(data)) #pandas의 DataFrame 기능이용해 딕셔너리를 출력
print("-"*30)
print(pd.DataFrame(data, columns=['성적', '학번'])) #프레임 컬럼 순서 변경
print("-"*30)
print(pd.DataFrame(data, columns=['성적', '학번'], index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])) #인덱스추가
