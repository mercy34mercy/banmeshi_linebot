import requests

def get_recipe(postdata):
    url = "https://banmeshii.herokuapp.com/get_db_recipe_one"

    datas = ({
        "data":[]
    })

    

    datas["data"].append(str(postdata))

    print(datas)


    data = requests.post(url,datas)

    print(data)

    returndata = data["recipeTitle"]

    return returndata
