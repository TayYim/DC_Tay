# DC_Tay

数据处理 by 严宋扬

## 第一题:SVM_BASED_ON_API_USAGE

### api_name 统计

`CollectApiNames.py`:统计用到的所有 api

`MakeApiNameTable.py`:生成 csv 表格，体现每个样本调用每个 api 次数的信息

### 统计结果

`black_usage.csv`:黑样本的统计结果

`white_usage.csv`:白样本的统计结果

`test_usage.csv`:测试样本的统计结果

### Jupyter Notebook

`SVM_BASED_ON_API_USAGE-Demo.ipynb`:只用 train 数据，测试用

`SVM_BASED_ON_API_USAGE.ipynb`:用所有 train 数据训练模型，输出 test 数据的预测结果

### 预测结果

`result_svm_by_ysy.csv`

## 第二题:Kmeans_BASED_ON_API_USAGE

api_usage.csv 是用第一题的脚本生成的 api 使用情况统计。

由于`AnalyzeStart`的调用数量全是 1，故去除。

使用 KMeans 聚类算法
