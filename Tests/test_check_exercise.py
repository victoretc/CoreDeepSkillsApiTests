import requests 
import json
import jsonpath
baseUrl = 'http://51.250.23.16:8090'

def test_check_exercise_succeful() :
    file = open('Tests/TestData/helloworld.json',"r")
    inputData = json.loads(file.read()) 
    path = "/checkExercise/42?isGraphRequired=false&xp=0&userId=2"
    response = requests.post(url=baseUrl+path , json = inputData)
    responseJson = json.loads(response.text)
    assert response.status_code == 200 
    assert jsonpath.jsonpath(responseJson,'$.error')[0] == "Вы правильно создали переменную <code>children</code>? Должно быть <code>['Таня', 'Ваня', 'Маша', 'Андрей']</code>"
    assert jsonpath.jsonpath(responseJson,'$.status')[0] == "error" 
    assert jsonpath.jsonpath(responseJson,'$.output')[0] == ""
    assert jsonpath.jsonpath(responseJson,'$.bytePayload')[0] == None 

def test_unsucceful_check_exercise_body() :
    path = "/checkExercise/42?isGraphRequired=false&xp=0&userId=2"
    response = requests.post(url=baseUrl+path)
    assert response.status_code == 400


