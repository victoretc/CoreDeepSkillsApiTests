import requests 
import json
import jsonpath
baseUrl = 'http://51.250.23.16:8090'

def test_succeful_execute() :
    file = open('Tests/TestData/helloworld.json',"r")
    inputData = json.loads(file.read())
    path1 = "/shell/startKernel/44" 
    response1 = requests.post(url=baseUrl+path1)
    responseJson = json.loads(response1.text)
    data = (jsonpath.jsonpath(responseJson,'$.output'))
    a = ("".join(data))
    path2 = ("/shell/execute/" + a + "?exerciseId=44&isGraphRequired=false")
    response2 = requests.post(url = baseUrl + path2, json= inputData)
    assert response2.status_code == 200
    assert jsonpath.jsonpath(responseJson,'$.status')[0] == "success"
    assert jsonpath.jsonpath(responseJson,'$.error')[0] == ""
    assert jsonpath.jsonpath(responseJson,'$.bytePayload')[0] == None
    
    
def test_execute_unsuccefulbody():
    path1 = "/shell/startKernel/44" 
    response1 = requests.post(url=baseUrl+path1)
    responseJson = json.loads(response1.text)
    data = (jsonpath.jsonpath(responseJson,'$.output'))
    a = ("".join(data))
    path2 = ("/shell/execute/" + a + "?exerciseId=44&isGraphRequired=false")
    response2 = requests.post(url = baseUrl + path2)
    assert response2.status_code == 400







