import chardet # 인코딩
import pandas as pd
import numpy
import seaborn as sns
import matplotlib.pyplot as plt

path_train = r"C:\Users\이수진\Desktop\changed_dataframe_train.csv"
path_test = r"C:\Users\이수진\Desktop\changed_dataframe_test.csv"
df_train = pd.read_csv(path_train)
df_test = pd.read_csv(path_test)

c_num = pd.get_dummies(df_train['c_num']).astype('int')
c_num 

c_stn = pd.get_dummies(df_train['c_stn']).astype('int')
c_stn

df_train = pd.concat([df_train,c_num,c_stn], axis=1)
df_train

df_train.columns

nan_counts = df_train.isnull().sum()
nan_counts.value_counts()

from sklearn.preprocessing import MinMaxScaler
import pandas as pd

# 예제 데이터프레임 생성 (필요시 이 부분은 삭제하세요)
# df_train = pd.DataFrame({
#     'e_sum_qctr': [1, 2, 3],
#     'e_n': [4, 5, 6],
#     'e_sum_load': [7, 8, 9],
#     'e_n_mean_load': [10, 11, 12],
#     'feature_1': [13, 14, 15],
#     0: [16, 17, 18]  # 정수형 열 이름 예시
# })

# MinMaxScaler 선언 및 Fitting
mMscaler = MinMaxScaler()

# 데이터 프레임에서 열 삭제
df_train = df_train.drop(columns=['c_num','c_stn','e_sum_qctr', 'e_n', 'e_sum_load', 'e_n_mean_load'])

# 열 이름을 문자열로 변환
df_train.columns = df_train.columns.astype(str)

# 스케일러 피팅
mMscaler.fit(df_train)

# 데이터 변환
mMscaled_data = mMscaler.transform(df_train)

# 데이터 프레임으로 저장
mMscaled_data = pd.DataFrame(mMscaled_data, columns=df_train.columns)

# 변환된 데이터 확인
print(mMscaled_data.head())

n = 20000  # 저장할 행의 수
df_subset = df_train.iloc[:n]

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding, Conv1D, MaxPool1D, GlobalMaxPool1D, LSTM, Input
from tensorflow.keras.optimizers import Adam

model = Sequential()
model.add(Input(shape=(89,1)))  # Input layer 추가
model.add(Conv1D(32, 3, activation='relu'))
model.add(MaxPool1D(2))
model.add(Conv1D(32, 3, activation='relu'))
model.add(LSTM(32, dropout=0.2, recurrent_dropout=0.2))
model.add(Dense(1))

model.compile(optimizer=Adam(1e-4), loss='mse', metrics=['mae'])
x_train = df_train.drop(columns=['e_elec'])
y_train = df_train['e_elec']

history = model.fit(x_train, y_train,epochs=200, batch_size=32)
