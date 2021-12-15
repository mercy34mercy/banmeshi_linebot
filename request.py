import requests
import json

def get_recipe(postdata):
    url = "https://banmeshii.herokuapp.com/get_db_recipe_one"

    datas = ({
        "data":["豚肉"]
    })

    

    # datas["data"].append(str(postdata))


    data = requests.post(url,json = datas).text


    returndata = data[0]

    print(returndata)

    return returndata
