import requests 
import json
import jsonpath
baseUrl = 'http://51.250.23.16:8090'

def test_succeful_create_core() :
    file2 = open('Tests/TestData/ex.json',"r")
    inputData2 = json.loads(file2.read())
    a = (inputData2['exercises'])
    for i in a:
        s = i['id']
        path = "/shell/startKernel/" + str(s)
        response = requests.post(url=baseUrl+path)
        responseJson = json.loads(response.text)
        assert response.status_code == 200 
        assert jsonpath.jsonpath(responseJson,'$.error')[0] == ""
        assert jsonpath.jsonpath(responseJson,'$.status')[0] == "success"
        assert jsonpath.jsonpath(responseJson,'$.bytePayload')[0] == None 

    
def test_unsucceful_create_core() :
    path = "/shell/startKernel/-100" 
    response = requests.post(url=baseUrl+path)
    responseJson = json.loads(response.text)
    assert response.status_code == 200 #нужно уточнить ок ли тут 200
    assert jsonpath.jsonpath(responseJson,'$.error')[0] == "Exercise with id: -100 wasn't found"
    assert jsonpath.jsonpath(responseJson,'$.status')[0] == "error" 
    assert jsonpath.jsonpath(responseJson,'$.output')[0] == ""
    assert jsonpath.jsonpath(responseJson,'$.bytePayload')[0] == None 
    
    
    







