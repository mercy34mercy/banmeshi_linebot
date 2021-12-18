import requests
import json

def get_recipe(postdata):

    for i in range(1,3):
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

    #json文字列を辞書に変換
        data_ = json.loads(data)

        returndata = data_["data"][i]["foodImageUrl"]

        print(returndata)

        return returndata
