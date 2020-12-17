import requests
import json
BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT= 'api/'

# def get_resources(id=None):
#     data={}
#     if id is not None:
#         data={
#             'id':id
#         }
#     resp=requests.get(BASE_URL+ENDPOINT,data=json.dumps(data))
#     print(resp.status_code)
#     print(resp.json())
# get_resources()


# def create_resource():
#     new_std={
#         'name':'Dhoni',
#         'rollno': 77,
#         'marks': 99,
#         'gf':'Dipika',
#         'bf':'Yuvraj'
#     }
#     resp=requests.post(BASE_URL+ENDPOINT,data=json.dumps(new_std))
#     print(resp.status_code)
#     print(resp.json())
# create_resource()


# def update_resource(id):
#     new_data={
#         'id':id,
#         'gf':'Sakshi',
#     }
#     resp=requests.put(BASE_URL+ENDPOINT,data=json.dumps(new_data))
#     print(resp.status_code)
#     print(resp.json())
# update_resource(4)

# def delete_resource(id):
#     data={
#         'id':id
#     }
#     resp=requests.delete(BASE_URL+ENDPOINT,data=json.dumps(data))
#     print(resp.status_code)
#     print(resp.json())
# delete_resource()