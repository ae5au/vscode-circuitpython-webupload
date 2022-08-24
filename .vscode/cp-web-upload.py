import sys
import requests

baseURL = "http://cpy-daa7a1.local/fs/"
password = "webpassword"

workspaceFolder = sys.argv[1]
relativeFile = sys.argv[2]

def create_parent_directory(relative_path):
    relative_path = relative_path.removesuffix("/")
    print("Creating parent directory for:",relative_path)
    directory = relative_path.replace(relative_path.split("/")[-1],"")
    dir_response = requests.put(baseURL + directory, auth=("",password))
    if(dir_response.status_code == 201):
        print("Directory created:", directory)
    else:
        print(dir_response.status_code, dir_response.reason)

response = requests.put(baseURL + relativeFile, data=open(workspaceFolder + "/" + relativeFile,"rb"), auth=("",password))
if(response.status_code ==  201):
    print("Created file:", relativeFile)
elif(response.status_code == 204):
    print("Overwrote file:", relativeFile)
elif(response.status_code == 401):
    print("Incorrect password")
elif(response.status_code == 403):
    print("CIRCUITPY_WEB_API_PASSWORD not set")
elif(response.status_code == 404):
    print("Missing parent directory")
    create_parent_directory(relativeFile)
    retry_response = requests.put(baseURL + relativeFile, data=open(workspaceFolder + "/" + relativeFile,"rb"), auth=("",password))
    if(retry_response.status_code ==  201):
        print("Created file:", relativeFile)
    else:
        print(retry_response.status_code, retry_response.reason)
elif(response.status_code == 409):
    print("USB is active and preventing file system modification")
else:
    print(response.status_code, response.reason)

