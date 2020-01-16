import requests
import base64
import json

ai_list = {'植物':'/v1/plant','动物':'/v1/animal','其他':'/v2/advanced_general'}

def baidu(type,path):
    if type in ai_list:
        url="https://aip.baidubce.com/rest/2.0/image-classify%s?access_token=24.01416a9e46ef6dc97bb99ffd00e10fd9.2592000.1580090240.282335-17874022"%(ai_list[type])
    else:
        return None

    header = {
        'Content-Type':'application/x-www-form-urlencoded'
    }

    data = {}
    with open(path,'rb') as f:
        image=base64.b64encode(f.read())
        data['image'] = str(image,'utf-8')
        res = requests.post(url=url,data=data,headers=header).text
        return json.loads(res).get('result','Error')

if __name__ == '__main__':
    print(baidu('其他','pyy.jpeg'))