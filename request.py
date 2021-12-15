import requests
import json

def get_recipe(postdata):
    url = "https://banmeshii.herokuapp.com/get_db_recipe_one"

    datas = ({
        "data":[]
    })

    

    datas["data"].append(str(postdata))

    print(datas)


    data = requests.post(url,data = json.dumps(datas))

    print(data)

    returndata = data["recipeTitle"]

    return returndata
