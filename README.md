# CasualCoding

放一点日常写的（实际用了）的东西。有的可能会顺便在 GitHub Pages 那边写详细的说明。

为什么 coding 本身是高兴做的，po 上来或者是整理思路就那么不情愿呢（

## 语言和依赖的说明

- Python：3.10。requirements.txt 没做。看 import 里的东西对着 pip 请。

## countdown/countdown.py

一个用命令行写的下班倒计时。由于几百年没碰过 Python，完完全全的面向搜索引擎编程。

用到了在命令行固定位置打印的模块 **reprint**。

## PickImageByRatio/PickImageByRatio.py

给两个参数：路径、长宽比（浮点数或形似16/9的表达式），会筛选出文件夹（不含子文件夹）内位于该长宽比前后10%范围内的图像并复制到新文件夹中。

给三个参数：路径、长宽比1、长宽比2，会筛选指定长宽比范围的图像。

用途是从一大堆图里筛出适合作为壁纸的图。

## bdf_to_sfd.py

用于转换BDF格式点阵字体为点阵风格矢量字体的脚本。

由 [中文像素字体制作  | indienova](https://ldt.indienova.com/u/hata/blogread/26923) 中的脚本修改而来。

详细请见 [提取TTF中内嵌的点阵字模并转换为点阵风格的TrueType字体 | HasukaPoi.github.io](https://hasukapoi.github.io/2022/05/08/bdf2truetype/)。


