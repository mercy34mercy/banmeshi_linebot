import requests
import json

def get_recipe(postdata):
    url = "https://banmeshii.herokuapp.com/get_db_recipe_one"

    datas = ({
        "data":[]
    })

    

    datas["data"].append(str(postdata))


    data = requests.post(url,json = datas).text

    data_ = json.loads(data)



    returndata = data_["data"][0]["foodImageUrl"]

    print(returndata)

    return returndata
