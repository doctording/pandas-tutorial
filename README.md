## 个人整理

pandas官方文档：http://pandas.pydata.org/pandas-docs/stable/index.html

### 概念

#### Series

 Series is a one-dimensional labeled array capable of holding any data type (integers, strings, floating point numbers, Python objects, etc.).

Series是pandas中暴露给我们使用的基本对象，它是由相同元素类型构成的一维数据结构，同时具有列表和字典的属性（字典的属性由索引赋予）。

Series：有序，有索引

list：  有序，无索引
dict：  无序，有索引

#### DataFrame

http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html

DataFrame is a 2-dimensional labeled data structure with columns of potentially different types. You can think of it like a spreadsheet or SQL table, or a dict of Series objects. It is generally the most commonly used pandas object.

数据帧(DataFrame)是二维数据结构，即数据以行和列的表格方式排列。

数据帧(DataFrame)的功能特点：

1. 潜在的列是不同的类型
2. 大小可变
3. 标记轴(行和列)
4. 可以对行和列执行算术运算

##### DataFrame 查

* `DataFrame.at`

Access a single value for a row/column label pair

* `DataFrame.iloc`

Access group of rows and columns by integer position(s)

* `DataFrame.xs`

Returns a cross-section (row(s) or column(s)) from the Series/DataFrame.

* `Series.loc`

Access group of values using labels

http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.loc.html#pandas.DataFrame.loc

http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.xs.html#pandas.DataFrame.xs

##### DataFrame 增删改

http://pandas.pydata.org/pandas-docs/stable/dsintro.html#alternate-constructors


# pivot_table数据处理注意

* 不同的数值类型，做聚合操作，pandas会处理掉不符合规范的数据列 

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd
import numpy as np


def test_pivot_table():
    """
    test_pivot_table
    """
    data3 = {'A_column': {'a': 1, 'b': 4, 'c': 10}, 'B_metric': {'a': "a", 'b': "b", 'c': "c"}, 'C_metric': {'a': 3, 'b': 10.2, 'c': 10.5}}
    df = pd.DataFrame(data=data3)
    print(df)
    df2 = df.pivot_table(
        index=['A_column'],
        values=['B_metric', 'C_metric'],
        aggfunc=np.sum,
    )
    print(df2)
    df3 = df.pivot_table(
        index=['A_column'],
        values=['B_metric', 'C_metric'],
        aggfunc=np.max,
    )
    print(df3)

if __name__ == '__main__':
    test_pivot_table()

```

---

## 教程目录
<details>

        0. 配置环境
        1. Series和DataFrame对象的创建
        2. Series和DataFrame对象的查、改、增、删
        3. merge详解
        4. Index对象的创建，查、改、增、删和使用
        5. 普通列和行index的相互转化
        6. 数据结构总览
        7. 显示控制
        8. 快速查看整体信息
        9. 数值运算
        10. 数值统计运算
        11. mask与比较运算（待完成）
        12. Category型与离散化
        13. Object型的文本操作（待完成）
        14. groupby详解（待完成）
        15. ……

</details>

## 教程说明

当今最热的职业是数据科学，数据科学领域应用最广泛的编程语言是python，python这么火的原因就是其有一个功能强大的数据科学库：pandas。

## 为什么写这套教程
然而，作为一名数据科学行业从业者，即使在pandas中浸淫日久，我常常还需要去查询官方文档，这严重影响了我的工作效率；甚至有时候迫不得已还得写循环操作，非常不pandas，这我忍不了，所以我觉得我得做点什么。

经过多次通读官方文档后，我认为问题根因在于：
- 官方文档组织杂而乱，知识框架不够精炼一致；
- 面面俱到，高价值信息被为了完整性而稀释；
- 文档更新不及时，API功能有时与文档描述不符。

与此同时，我也通读了国内外各种pandas教程，不过总体而言这些教程多数浅尝辄止，不够实用。所以，我决定编写一套pandas教程，提高自己能力的同时，也能帮助大家少走弯路。

## 教程编写核心原则
这套教程编写的核心原则是：
- 首重知识体系逻辑，没有组织、不成体系的信息是无效信息，很难记住和使用；
- 知识粒度大小适中，即不流于表面也不深入过多细节;
- 示例精炼短小（能看出操作效果），方便手打练习；
- 在示例位置都会注上解释，辅助理解。

## 这套教程适合谁
这套教程包含从初级到进阶的内容，适合初学者和希望进阶建立知识体系的数据科学从业者阅读。为确保教程的高可用性和准确性，我花了大量时间精心准备，但仍难免有错漏，非常欢迎各位读者能够跟我反馈。

