import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

df=pd.read_csv('/content/electric_train.csv')

#2020년 월별 분할
# CSV 파일에서 데이터를 불러옵니다. 파일 경로를 적절히 수정하세요.
df = pd.read_csv("/content/electric_train.csv")

# 'e_tm' 열을 날짜 형식으로 변환합니다.
df['e_tm'] = pd.to_datetime(df['e_tm'])

# 2020년 데이터만 추출합니다.
data_2020 = df[(df['e_tm'].dt.year == 2020)]

# 각 월별 데이터를 추출하고 Excel 파일로 저장합니다.
for month in range(1, 13):
    # 해당 월의 데이터를 추출합니다.
    data_month = data_2020[(data_2020['e_tm'].dt.month == month)]

    # Excel 파일로 저장합니다.
    file_name = f"2020_data_{month:02d}.xlsx"  # 월별 파일 이름
    data_month.to_excel(file_name, index=False)

    print(f"{month}월 데이터가 {file_name} 파일로 저장되었습니다.")

#2021년 월별 분할
# 'e_tm' 열을 날짜 형식으로 변환합니다.
df['e_tm'] = pd.to_datetime(df['e_tm'])

# 2021년 데이터만 추출합니다.
data_2021 = df[(df['e_tm'].dt.year == 2021)]

# 각 월별 데이터를 추출하고 Excel 파일로 저장합니다.
for month in range(1, 13):
    # 해당 월의 데이터를 추출합니다.
    data_month = data_2021[(data_2021['e_tm'].dt.month == month)]

    # Excel 파일로 저장합니다.
    file_name = f"2021_data_{month:02d}.xlsx"  # 월별 파일 이름
    data_month.to_excel(file_name, index=False)

    print(f"{month}월 데이터가 {file_name} 파일로 저장되었습니다.")

#2022년 월별 분할
import pandas as pd

# CSV 파일에서 데이터를 불러옵니다. 파일 경로를 적절히 수정하세요.
df = pd.read_csv("/content/electric_train.csv")

# 'e_tm' 열을 날짜 형식으로 변환합니다.
df['e_tm'] = pd.to_datetime(df['e_tm'])

# 2022년 데이터만 추출합니다.
data_2022 = df[(df['e_tm'].dt.year == 2022)]

# 각 월별 데이터를 추출하고 Excel 파일로 저장합니다.
for month in range(1, 13):
    # 해당 월의 데이터를 추출합니다.
    data_month = data_2022[(data_2022['e_tm'].dt.month == month)]

    # Excel 파일로 저장합니다.
    file_name = f"2022_data_{month:02d}.xlsx"  # 월별 파일 이름
    data_month.to_excel(file_name, index=False)

    print(f"{month}월 데이터가 {file_name} 파일로 저장되었습니다.")
