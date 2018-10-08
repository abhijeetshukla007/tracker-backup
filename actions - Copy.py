import requests
import json
import logging
import datetime

def main():
		listname="temp"       
		taskName ="task1"
		url = "http://localhost:8080/api/v1/addTaskToList"
		now = datetime.datetime.now()
		print(now)
		payload = {
				"name": listname,
				"taskList": [
					{
						"taskName": taskName,
						"date":str(now)			
					}
				]
		}
		response = requests.post(url, data=None, json=payload)
		

		if response.status_code != 200:
			print("Errorr",format(response.status_code))
		else:
			print("Success")
		logging.info(type(response))

		jsonResponse=response.json()
		print(jsonResponse["message"])

if __name__== "__main__":
  main()