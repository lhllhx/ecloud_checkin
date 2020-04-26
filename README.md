# 天翼云签到
一个自动完成天翼云签到的脚本
                
        
## 使用说明
此脚本需要使用者有一定的移动端抓包能力  
iOS用户建议使用免费的stream，需启用https抓包模块  
具体初始化步骤不在此详述

需抓包链接：  

https://api.cloud.189.cn/mkt/userSign.action  

https://m.cloud.189.cn/v2/drawPrizeMarketDetails.action?taskId=TASK_SIGNIN 

https://m.cloud.189.cn/v2/drawPrizeMarketDetails.action?taskId=TASK_SIGNIN_PHOTOS 

然后将抓包后的数据**替换掉脚本内所有**请求头和链接参数 确保脚本里的内容和与抓包内容保持一致

运行后会将日志记录到同目录log.txt上
## 开发相关

使用python3.7编写

## 感谢
部分项目代码来源于此项目  
https://github.com/liuqitoday/checkin-helper