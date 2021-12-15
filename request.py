import requests

def get_recipe(postdata):
    url = "https://banmeshii.herokuapp.com/get_db_recipe_one"

    print("postdata : "+postdata)

    data = requests.post(url,postdata)

    print(data)

    returndata = data["recipeTitle"]

    return returndata
