import requests 
import json
import jsonpath
baseUrl = 'http://51.250.23.16:8090'

def test_succeful_execute_with_exercise() :
    file1 = open('Tests/TestData/helloworld.json',"r")
    inputData1 = json.loads(file1.read()) 
    file2 = open('Tests/TestData/ex.json',"r")
    inputData2 = json.loads(file2.read())
    a = (inputData2['exercises'])
    for i in a:
        s = i['id']
        path = ("/executeWithExercise/" + str(s) + "?isGraphRequired=false")
        response = requests.post(url=baseUrl + path , json = inputData1)
        responseJson = json.loads(response.text)
        assert response.status_code == 200 
        assert jsonpath.jsonpath(responseJson,'$.bytePayload')[0] == None


def test_unsucceful_execute_with_exercise_body() :
    file2 = open('Tests/TestData/ex.json',"r")
    inputData2 = json.loads(file2.read())
    a = (inputData2['exercises'])
    for i in a:
        s = i['id']
        path = ("/executeWithExercise/" + str(s) + "?isGraphRequired=false")
        response = requests.post(url=baseUrl + path)
        assert response.status_code == 400
