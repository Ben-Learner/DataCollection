#输入四国数据，转换成百分比，并按顺序排列
data = [4,7,3,4,5]
percent = []
for i in range(len(data)-1):
    percent.append(data[i]/data[4])
percent.sort()
final_output = []
for i in range(len(percent)):
    final_output.append(str(percent[i] * 100) + "%")
print(final_output)