#This is a dummy database to demonstrate the concept of mocking
#Mocking is a way to replace parts of your system under test and make assertions about how they have been used.
#In this case, we will mock the database call to return a specific user without actually querying
#This is extra helpful https://jsonplaceholder.typicode.com/users for get requests

import requests

database = {
    1: "Alpha",
    2: "Bravo",
    3: "Charlie",
}

#We will create a function which will get the user from DB
def get_user_from_db(user_id):
    return database.get(user_id)

def get_users():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    if response.status_code == 200: #if the request is successful
        return response.json()
    
    raise requests.HTTPError