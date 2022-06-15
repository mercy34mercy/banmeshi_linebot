import requests
import json


def get_recipe(postdata):


    #banmeshiAPIのURL
    url = "https://banmeshikun.azurewebsites.net/random_one_by_mate"

    #jsonの型宣言
    datas = ({
        "data":[]
    })

    for data in postdata.replace("　"," ").split(" "):
        #Lineから貰ってきたデータを配列に入れる
        datas["data"].append(str(data))



    #BanmeshiAPIにリクエスト
    data = requests.post(url,json = datas).text

    

#json文字列を辞書に変換
    data_ = json.loads(data)
    print(data_)
    # for i in range(0,2):
    #     returndata =[ data_["data"][0]["foodImageUrl"],data_["data"][1]["recipeUrl"]]
        
    returnlist=[]

    result_dict={
            "foodImageUrl":data_["data"][0]["foodImageUrl"],
            "url":data_["data"][0]["recipeUrl"]
    }
    returnlist.append(result_dict)
        # print(returndata)
        # print(returndata2)
        # print(data)
        # print(returndata[i])
    # print(data[:100])
    print(returnlist)
    return str(data_["data"][0]["recipeUrl"])