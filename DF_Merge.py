import pandas as pd

left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})
left1 = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                      'key2': ['K0', 'K1', 'K0', 'K1'],
                      'A': ['A0', 'A1', 'A2', 'A3'],
                      'B': ['B0', 'B1', 'B2', 'B3']})
right1 = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                      'key2': ['K0', 'K0', 'K0', 'K0'],
                       'C': ['C0', 'C1', 'C2', 'C3'],
                       'D': ['D0', 'D1', 'D2', 'D3']})

print('----------------- Begin def + keys--------------------')
result = pd.merge(left, right, on='key')
print(result)
print('----------------- + key1 + key2 --------------------')
print(left1)
print(right1)
result1 = pd.merge(left1, right1, on=['key1', 'key2'])
print(result1)
print('----------------- + how = left --------------------')
result2 = pd.merge(left1, right1, how='left', on=['key1', 'key2'])
print(result2)
print('----------------- + how = right --------------------')
result3 = pd.merge(left1, right1, how='right', on=['key1', 'key2'])
print(result3)
print('----------------- + how = outer --------------------')
result4 = pd.merge(left1, right1, how='outer', on=['key1', 'key2'])
print(result4)
print('----------------- + how = inner --------------------')
result5 = pd.merge(left1, right1, how='inner', on=['key1', 'key2'])
print(result5)
print('--------------------------------------------------------------------------------------------')
df = pd.DataFrame({"Let": ["A", "B", "C"], "Num": [1, 2, 3]})
ser = pd.Series(["aaa", "bbb", "ccc", "ddd", "eee", "fff"],
                index=pd.MultiIndex.from_arrays([["A", "B", "C"] * 2, [1, 2, 3, 4, 5, 6]], names=["Let", "Num"]),
                )
print(df)
print(ser)
result6 = pd.merge(df, ser.reset_index(), on=['Let', 'Num'])
print(result6)
print('--------------------------------------------------------------------------------------------')
left2 = pd.DataFrame({'A': [1, 2], 'B': [2, 2]})
right2 = pd.DataFrame({'A': [4, 5, 6], 'B': [2, 2, 2]})
result7 = pd.merge(left2, right2, on='B', how='outer')
print(result7)
print('-----------------------------------validate = one_to_one---------------------------------')
left3 = pd.DataFrame({'A' : [1,2], 'B' : [1, 2]})
right3 = pd.DataFrame({'A' : [4,5,6], 'B': [2, 2, 2]})
# result8 = pd.merge(left3, right3, on='B', how='outer', validate="one_to_one") --> error
result8 = pd.merge(left3, right3, on='B', how='outer', validate="one_to_many")
print(left3)
print(right3)
print(result8)