import pandas as pd
import re

# 创建一个包含汉字的 DataFrame
df = pd.DataFrame({'A': ['一段序列中的汉字123', '另一段序列中的汉字456'], 'B': [1, 2]})

# 选择第3到5行（索引从0开始）
rows_to_remove = range(0, 2)  # 注意：这个范围是 [2, 3, 4]

# 对于这些行，使用正则表达式替换汉字
df.loc[rows_to_remove]['A'] = df.iloc[rows_to_remove]['A'].str.replace('[\u4e00-\u9fa5]+', '')

print(df)
