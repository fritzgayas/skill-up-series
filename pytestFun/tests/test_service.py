import pytest
import source.service as service
import unittest.mock as mock #import the mock library
import requests # import requests to fix "requests is not defined"
#When you want to use mocking, use it when tests are dependent on external systems that cannot guarantee the same result each time OR when you want to isolate the unit of code being tested.
#For example, if you are testing a function that makes an API call. An API can be down, or the data it returns can change. By mocking the API call, you can ensure that your tests are reliable and consistent.

@mock.patch("source.service.get_user_from_db") #mock the get_user_from_db function in service module
def test_get_user_from_db(mock_get_user_from_db): #the mock object is passed as an argument to the test function
    mock_get_user_from_db.return_value = "Mocked Alpha" #set the return value of the mock object
    user_name = service.get_user_from_db(1) #call the function which is being tested

    assert user_name == "Mocked Alpha" #assert that the return value is as expected

@mock.patch("requests.get") #mock the requests.get function in service module
def test_get_users(mock_get): #we want a certain response
    mock_response = mock.Mock() #create a mock response object
    mock_response.status_code = 200 #set the status code of the mock response. It is a property
    mock_response.json.return_value = [{"id": 1, "name": "Juan Dela Cruz"}] #json is a method, so we set its return value
    mock_get.return_value = mock_response #set the return value of the mock object
    data=service.get_users() #call the function which is being tested
    assert data == [{"id": 1, "name": "Juan Dela Cruz"}] #assert that the return value is as expected

@mock.patch("requests.get") #mock the requests.get function in service module
def test_get_users_error(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 400 #set the status code of the mock response to something other than 200
    mock_get.return_value = mock_response
    with pytest.raises(requests.HTTPError): #assert that the function raises an HTTPError
        service.get_users()


