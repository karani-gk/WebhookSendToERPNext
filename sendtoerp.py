import requests
import json

url = "http://127.0.0.1:8006/api/method/library_management.utils.receive_post_data"

data = {
	"job_title": "Software Engineer",
	"years_of_experience": "9 Years",
	"test": "This is a test"
}

request = requests.post( url, data=json.dumps(data), headers={"Authorization":"Token 623bcd74c96d52a:a0849c989781cbf"} )






#RECEIVE ON ERPNEXT
@frappe.whitelist()
def receive_post_data():
  data = frappe.request.data

  print(f"\n\n{data}\n\n")

  return
