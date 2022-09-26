import os
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator


# 读入数据
path = 'E:\system\desktop\python'
FileName = 'CR3000_flux.dat'
fullfilename = os.path.join(path,FileName)
file = open(fullfilename,encoding = 'ISO-8859-1')
file_data = file.readlines()
file.close()
data = file_data[4:]

time_s = []

temprature_1 = []
wind_speed_1 = []
humidity_1 = []
pressure_1 = []
Rn_avg_1 = []
Rs_downwell_Avg_1 = []
Rs_upwell_Avg_1 = []
Rl_downwell_Avg_1 = []
Rl_upwell_Avg_1 = []
Hc_1 = []
LE_wpl_1 = []
Fc_wpl_1 = []

temprature_8 = []
wind_speed_8 = []
humidity_8 = []
pressure_8 = []
Rn_avg_8 = []
Rs_downwell_Avg_8 = []
Rs_upwell_Avg_8 = []
Rl_downwell_Avg_8 = []
Rl_upwell_Avg_8 = []
Hc_8 = []
LE_wpl_8 = []
Fc_wpl_8 = []

for m in data:
    lis = m.split(',') #分割每行数据
    if (lis[0][0:11]=='"2015-01-01'):
        #float(lis = )[float(lis[i]) for i in range(1,len(lis))]
        time_s.append(lis[0][12:17])
        temprature_1.append(float(lis[2]))
        wind_speed_1.append(float(lis[11]))
        humidity_1.append(float(lis[5]))
        pressure_1.append(float(lis[8]))
        Rn_avg_1.append(float(lis[-12]))
        Rs_downwell_Avg_1.append(float(lis[-10]))
        Rs_upwell_Avg_1.append(float(lis[-9]))
        Rl_downwell_Avg_1.append(float(lis[-8]))
        Rl_upwell_Avg_1.append(float(lis[-7]))
        Hc_1.append(float(lis[54]))
        LE_wpl_1.append(float(lis[53]))
        Fc_wpl_1.append(float(lis[52]))
        # print("*****************")
    
    if (lis[0][0:11]=='"2015-08-01'):
        #float(lis = )[float(lis[i]) for i in range(1,len(lis))]
        temprature_8.append(float(lis[2]))
        wind_speed_8.append(float(lis[11]))
        humidity_8.append(float(lis[5]))
        pressure_8.append(float(lis[8]))
        Rn_avg_8.append(float(lis[-12]))
        Rs_downwell_Avg_8.append(float(lis[-10]))
        Rs_upwell_Avg_8.append(float(lis[-9]))
        Rl_downwell_Avg_8.append(float(lis[-8]))
        Rl_upwell_Avg_8.append(float(lis[-7]))
        Hc_8.append(float(lis[54]))
        LE_wpl_8.append(float(lis[53]))
        Fc_wpl_8.append(float(lis[52]))
        # print("8**********************")

# 计算波文比 = 显热/潜热
bowen_1 = [Hc_1[i]/LE_wpl_1[i] for i in range(len(Hc_1))]
bowen_8 = [Hc_8[i]/LE_wpl_8[i] for i in range(len(Hc_8))]

#画图
x_axis_data = time_s # x轴数据
y_axis_data = bowen_8 # y轴数据
plt.rc('font',family='Times New Roman') # 设置字体
plt.figure(figsize = [17,8]) # 设置画布大小
plt.plot(x_axis_data, y_axis_data, alpha=0.8, linewidth=3)
plt.tick_params(labelsize=23) # 设置坐标轴字体大小
plt.title('Bowen  Ratio  of  2015-08-01',fontsize = 27) #设置标题
# plt.ylabel('W/m^2',fontsize = 23) #设置y轴单位与字体大小
plt.xlabel('time',fontsize = 23) #设置x轴单位与字体大小
plt.grid(b = True, linestyle='--', linewidth=1) #设置背景网格
# plt.ylim(2.6,3.2) #设置y轴范围
x_major_locator = MultipleLocator(6) #设置x轴坐标间距
ax = plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
