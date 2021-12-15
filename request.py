import requests
import json

def get_recipe(postdata):

    #banmeshiAPIのURL
    url = "https://banmeshii.herokuapp.com/get_db_recipe_one"

    #jsonの型宣言
    datas = ({
        "data":[]
    })

    #Lineから貰ってきたデータを配列に入れる
    datas["data"].append(str(postdata))

    #BanmeshiAPIにリクエスト
    data = requests.post(url,json = datas).text


    data_ = json.loads(data)

    returndata = data_["data"][0]["foodImageUrl"]

    print(returndata)

    return returndata
