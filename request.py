import requests

def get_recipe(postdata):
    url = "https://banmeshii.herokuapp.com/get_db_recipe_one"

    data = requests.post(url,postdata).json

    print(data)

    returndata = data["recipeTitle"]

    return returndata
