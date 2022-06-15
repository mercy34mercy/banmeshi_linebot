import requests
import json


def get_recipe(postdata):


    #banmeshiAPIのURL
    url = "https://banmeshikun.azurewebsites.net/get_recipe"

    #jsonの型宣言
    datas = ({
        "data":[]
    })

    #Lineから貰ってきたデータを配列に入れる
    datas["data"].append(str(postdata))

    #BanmeshiAPIにリクエスト
    data = requests.post(url,json = datas).text

#json文字列を辞書に変換
    data_ = json.loads(data)
    # for i in range(0,2):
    #     returndata =[ data_["data"][0]["foodImageUrl"],data_["data"][1]["recipeUrl"]]
        
    returnlist=[]
    for i in range(0,3):
        result_dict={
            "foodImageUrl":data_[data][i]["foodImageUrl"],
            "url":data_[data][i]["recipeUrl"]
        }
        returnlist.append(result_dict)
        # print(returndata)
        # print(returndata2)
        # print(data)
        # print(returndata[i])
    # print(data[:100])
    print(returnlist)
    # return returndata
