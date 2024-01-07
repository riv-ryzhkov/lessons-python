import csv


# with open('db_table.csv', 'r') as file:
#     reader = csv.reader(file)
#     print('reader', reader, type(reader))
#     for i in reader:
#         # print(*i, sep='\t')
#         print(i)

import numpy as np
import pandas as pd

s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)

dates = pd.date_range("20130101", periods=6)
print(*dates, sep='\n')

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
print(df)

df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)
print(df2)
print(df2.dtypes)
print(df2.head(2))
print(df2.tail(2))
print(df.index)
print(df.describe())
print(df.T)
print(df.sort_index(axis=1, ascending=False))
print(df.sort_values(by="B"))

print(df["A"])
k = df["A"]
print(df[0:3])
print(k[0:3])

print(df.loc[dates[1]])
print(df.loc[:, ["A", "B"]])
print(df.loc["20130102":"20130104", ["A", "B"]])
print(df.loc["20130102", ["A", "B"]])
print(df.loc[dates[0], "A"])
print(df.loc["20130102", "A"])

print(df.iloc[3])
print(df.iloc[3:5, 0:2])
print(df.iloc[[1, 2, 4], [0, 2]])
print(df.iloc[1:3, :])
print(df.iloc[1, 1])

# Для получения быстрого доступа к скаляру (эквивалентно предыдущему методу):
print(df.iat[1, 1])
print('='*80)
# Логическое индексирование
print(df[df["A"] > 0])
print(df[df > 0])

df2 = df.copy()
df2["E"] = ["one", "one", "two", "three", "four", "three"]
print(df2)
print(df2[df2["E"].isin(["two", "four"])])
print(df2["E"].isin(["two", "four"]))

# Установка нового столбца автоматически выравнивает данные по индексам:
s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range("20130102", periods=6))
print(s1)
df["F"] = s1
print(df)
df.at[dates[0], "A"] = 0
df.at["2013-01-04", "A"] = 0

df.iat[0, 1] = 0
print(df)

df.loc[:, "D"] = np.array([5] * len(df))
print(df)

df2 = df.copy()
df2[df2 > 0] = -df2
print(df2)

# Отсутствующие данные
df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ["E"])
df1.loc[dates[0] : dates[1], "E"] = 1
print(df1)

# Чтобы удалить все строки с отсутствующими данными:
print(df1.dropna(how="any"))
# Заполнение недостающих данных:
print(df1.fillna(value=8))
# Чтобы получить логическую маску, где значения nan:
print(pd.isna(df1))

# Статистика
# реднее
print(df.mean())
# Та же операция на другой оси:
print(df.mean(1))

# сдвиг данных по индексу
s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates).shift(2)
print(s)
# фильтрация одной таблицы через другую
print(df.sub(s, axis="index"))

# Применение функций к данным:
print(df.apply(np.cumsum)) # накапливает сумму по столбцам
print(df.apply(lambda x: x.max() - x.min()))

# гистограмма
s = pd.Series(np.random.randint(0, 7, size=10))
print(s)
print(s.value_counts()) # подсчет сколько раз встречается

# Строковые методы
s = pd.Series(["A", "B", "C", "Aaba", "Baca", np.nan, "CABA", "dog", "cat"])
print(s.str.lower())

# нарезание построчно и слияние в один
# Добавление столбца в a DataFrame происходит относительно быстро.
# Однако для добавления строки требуется копия, и это может быть дорого.
# Мы рекомендуем передавать в конструктор предварительно созданный
# список записей, а не DataFrame создавать DataFrame
# путем итеративного добавления к нему записей.
df = pd.DataFrame(np.random.randn(10, 4))
pieces = [df[:5], df[3:8], df[7:]]
print('='*80)
print(df)
print('='*80)
print(pieces)
print(pd.concat(pieces))

# Слияния в стиле SQL.
left = pd.DataFrame({"key": ["foo", "foo"], "lval": [1, 2]})
right = pd.DataFrame({"key": ["foo", "foo"], "rval": [4, 5]})
print(pd.merge(left, right, on="key"))
#    key  lval  rval
# 0  foo     1     4
# 1  foo     1     5
# 2  foo     2     4
# 3  foo     2     5
print(pd.merge(left, right, on="key")) # аналогично

# Группировка ¶
# Под «группировкой по» мы имеем в виду процесс, включающий один или несколько следующих шагов:
# Разделение данных на группы по некоторым критериям
# Применение функции к каждой группе независимо
# Объединение результатов в структуру данных

df = pd.DataFrame(
    {
        "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
        "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
        "C": np.random.randn(8),
        "D": np.random.randn(8),
    }
)
print(df)

print(df.groupby("A").sum())
print(df.groupby(["A", "B"]).sum())
# tuples = list(zip(*[["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
#                     ["one", "two", "one", "two", "one", "two", "one", "two"],]))
tuples = list(zip(["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
                    ["one", "two", "one", "two", "one", "two", "one", "two"]))
print(tuples)
index = pd.MultiIndex.from_tuples(tuples, names=["first", "second"])
print(index)
df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=["A", "B"])
print(df)
df2 = df[:4]
stacked = df2.stack()
print(stacked)
print(stacked.unstack())
print(stacked.unstack(1))
print(stacked.unstack(0))

# Сводные таблицы
df = pd.DataFrame(
    {
        "A": ["one", "one", "two", "three"] * 3,
        "B": ["A", "B", "C"] * 4,
        "C": ["foo", "foo", "foo", "bar", "bar", "bar"] * 2,
        "D": np.random.randn(12),
        "E": np.random.randn(12),
    }
)

print(df)
print(pd.pivot_table(df, values="D", index=["A", "B"], columns=["C"]))

# Временные ряды
rng = pd.date_range("1/1/2012", periods=100, freq="S")
ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)
print(rng)
print(ts)
print(ts.resample("5Min").sum())

rng = pd.date_range("3/6/2012 00:00", periods=5, freq="D")
ts = pd.Series(np.random.randn(len(rng)), rng)
ts_utc = ts.tz_localize("UTC")
print(ts_utc)
print(ts_utc.tz_convert("US/Eastern"))

rng = pd.date_range("1/1/2012", periods=5, freq="M")
ts = pd.Series(np.random.randn(len(rng)), index=rng)
ps = ts.to_period()
print(ps)
print(ps.to_timestamp())

prng = pd.period_range("1990Q1", "2000Q4", freq="Q-NOV")
ts = pd.Series(np.random.randn(len(prng)), prng)
ts.index = (prng.asfreq("M", "e") + 1).asfreq("H", "s") + 9
print(ts.index)
print(ts.head())

df = pd.DataFrame(
    {"id": [1, 2, 3, 4, 5, 6], "raw_grade": ["a", "b", "b", "a", "a", "e"]}
)
df["grade"] = df["raw_grade"].astype("category")

print(df["grade"])
df["grade"].cat.categories = ["very good", "good", "very bad"]
print(df["grade"])
df["grade"] = df["grade"].cat.set_categories(
    ["very bad", "bad", "medium", "good", "very good"]
)
print(df)
print(df.sort_values(by="grade"))
print(df.groupby("grade").size())

# Построение

import matplotlib.pyplot as plt


# plt.close("all")
ts = pd.Series(np.random.randn(1000), index=pd.date_range("1/1/2000", periods=1000))
ts = ts.cumsum()
ts.plot();
plt.show();

df = pd.DataFrame(
    np.random.randn(1000, 4), index=ts.index, columns=["A", "B", "C", "D"]
)
df = df.cumsum()
plt.figure();
df.plot();
plt.legend(loc='best');
plt.show();

# Работа с файлами
df.to_csv("foo.csv")

print(pd.read_csv("foo.csv"))

df.to_hdf("foo.h5", "df")
pd.read_hdf("foo.h5", "df")

df.to_excel("foo.xlsx", sheet_name="Sheet1")
pd.read_excel("foo.xlsx", "Sheet1", index_col=None, na_values=["NA"])