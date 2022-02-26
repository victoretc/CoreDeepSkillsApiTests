import requests 
import json
import jsonpath
baseUrl = 'http://51.250.23.16:8090'

def test_succeful_execute() :
    file = open('Tests/TestData/helloworld.json',"r")
    inputData = json.loads(file.read()) 
    path = "/execute"
    response = requests.post(url=baseUrl+path , json = inputData)
    responseJson = json.loads(response.text)
    assert response.status_code == 200 
    assert jsonpath.jsonpath(responseJson,'$.error')[0] == ""
    assert jsonpath.jsonpath(responseJson,'$.status')[0] == "success" 
    assert jsonpath.jsonpath(responseJson,'$.output')[0] == "Hello, world!"
    assert jsonpath.jsonpath(responseJson,'$.bytePayload')[0] == None 

def test_unsucceful_execute_body() :
    path = "/execute"
    response = requests.post(url=baseUrl+path)
    assert response.status_code == 400
    
  