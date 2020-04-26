import requests
import urllib3
import json
import time
from xml.etree import ElementTree

urllib3.disable_warnings()

if  __name__ == "__main__":
    url_checkin = 'https://api.cloud.189.cn/mkt/userSign.action?' 
    url_drawprize = 'https://m.cloud.189.cn/v2/drawPrizeMarketDetails.action?taskId=TASK_SIGNIN'
    url_drawprize1 = 'https://m.cloud.189.cn/v2/drawPrizeMarketDetails.action?taskId=TASK_SIGNIN_PHOTOS'
    headers = {
        'Host': 'api.cloud.189.cn',
        'Accept-Language': 'zh-cn',
        'Cookie': '',
        'Connection': 'Keep-Alive',
        'Signature': '',
        'Date': '',
        'Accept': '*/*',
        'User-Agent': '',
        'sessionKey': '',                            
        'Accept-Encoding': 'gzip',
        'X-Request-ID': '',
    }
    
    headers_drawprize = {
        'Host': 'm.cloud.189.cn',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Accept': '*/*',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': '',
        'Referer': 'https://m.cloud.189.cn/zhuanti/2016/sign/index.jsp?albumBackupOpened=0',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en,en-US;q=0.8',
        'Cookie': ''
    }
    
    headers_drawprize1 = {
        'Host': 'm.cloud.189.cn',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Accept': '*/*',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': '',
        'Referer': 'https://m.cloud.189.cn/zhuanti/2016/sign/index.jsp?albumBackupOpened=1',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en,en-US;q=0.8',
        'Cookie': ''

    }
    
    session = requests.session()
    response_checkin = session.get(url_checkin,headers=headers,verify=False) #关闭校验ssl证书
    checkin_unicode = response_checkin.content.decode("utf-8")
    tree = ElementTree.fromstring(checkin_unicode)
    box = tree.find('resultTip')
    response_drawprize = session.get(url_drawprize,headers=headers_drawprize,verify=False)
    drawprize_unicode = response_drawprize.content.decode("utf-8")
    response_drawprize1 = session.get(url_drawprize1,headers=headers_drawprize1,verify=False)
    drawprize1_unicode = response_drawprize1.content.decode("utf-8")
    #drawprize_unicode ='{"activityId":"ACT_SIGNIN","description":"天翼云盘50M空间","isUsed":1,"listId":64559600,"prizeGrade":1,"prizeId":"SIGNIN_CLOUD_50M","prizeName":"天翼云盘50M空间","prizeStatus":1,"prizeType":4,"useDate":"2020-03-05T10:31:27","userId":376673451}'
    result_drawprize = json.loads(drawprize_unicode)
    result_drawprize1 = json.loads(drawprize1_unicode)
    if 'activityId' in result_drawprize:
        result = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '  签到:' + box.text + '  一次抽奖获得:' + str(result_drawprize['description']) + '  二次抽奖获得:' + str(result_drawprize1['description'])
    else :
        result = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "  签到抽奖失败/已签到抽奖"
    f = open("log.txt", "a+")
    f.write(result)
    f.write('\n') 
    f.close()
