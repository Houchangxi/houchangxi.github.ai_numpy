import pandas as pd

food_info = pd.read_csv("food_info.csv")
# print(type(food_info))
# print(food_info.dtypes)
# print(help(pd.read_csv))
# print(food_info.head())
# print(food_info.head())
# print(food_info.tail())
# print(food_info.columns)
# print(food_info.shape)
# print(food_info.loc[1])
# print(food_info.loc[3:8])  # 打印行
# print(food_info["NDB_No"])   # 打印列
# columns = ["Zinc_(mg)","Copper_(mg)"]
# print(food_info[columns])

# 根据列名对数据进行分类  通过重量进行分类
columns_all = food_info.columns.tolist()
# print("len all is ",len(columns_all))
gram_columns = []
mgram_columns = []
other_columns = []
# 找出不同单位的数据
for cell in columns_all:
    if cell.endswith("(g)"):
        gram_columns.append(cell)
    elif cell.endswith("(mg)"):
        mgram_columns.append(cell)
    else:
        other_columns.append(cell)


if len(gram_columns) == 0:
    print("No find g")
else:
    gram_df = food_info[gram_columns]
    # print(gram_df.shape)

if len(mgram_columns) == 0:
    print("No find mg")
else:
    mgram_df = food_info[mgram_columns]
    # print(mgram_df.shape)

if len(other_columns) == 0:
    print("No find mg")
else:
    other_df = food_info[other_columns]
    # print(other_df.shape)
    # print(other_columns)

# 单独一列进行数学运算
mgram_tansfer_g = mgram_df/1000
# print(mgram_df.head())
# print(mgram_tansfer_g.head())

# 列数据可以进行 + - * / 操作
water_energy = food_info["Water_(g)"]*food_info["Energ_Kcal"]
print("----")
print(food_info["Water_(g)"].head())
print(food_info["Energ_Kcal"].head())
print(water_energy.head())
