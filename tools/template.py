"""
    本代码用于: XXXX
    创建时间: 2022 年 04 月 25 日
    创建人: MorningStar
    最后一次修改时间: 2022 年 04 月 25 日
"""
# ==================== 导入必要的包 ==================== #
# ----- 系统操作相关的包 ----- #
import time
import sys
import os 

# ----- 数据处理相关的包 ----- #
import numpy as np 


# ==================== 设置常量参数 ==================== #


# ==================== 函数实现 ==================== #


# ==================== 主函数运行 ==================== #
if __name__ == '__main__':
    # ----- 开始计时 ----- #
    T_Start = time.time()
    print("程序开始运行 ! \n")
    print("系统运行环境: ", sys.executable)
    print("")


    # ----- 结束计时 ----- #
    T_End = time.time()
    T_Sum = T_End  - T_Start
    T_Hour = int(T_Sum/3600)
    T_Minute = int((T_Sum%3600)/60)
    T_Second = round((T_Sum%3600)%60, 2)
    print("程序运行时间: {}时{}分{}秒".format(T_Hour, T_Minute, T_Second))
    print("程序已结束 !")