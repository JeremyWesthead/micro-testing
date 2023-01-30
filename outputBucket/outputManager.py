'''127.0.0.1:8002
'''
import base64
import json
import os
import threading
from fastapi import FastAPI
    

app = FastAPI()
access = threading.Lock()



@app.post("/put")
async def put(guid: str, files: str):
    '''Save the files required for a given sample GUID

    Args:
        guid (str): Sample GUID
        files (str): JSON mapping filename->base64 encoded contents
    '''
    if not os.path.exists(f"files/{guid}"):
        os.mkdir(f"files/{guid}")
    print("|"+guid+"|"+files+"|")
    files = json.loads(files)
    for filename in files.keys():
        with access:
            with open(f"files/{guid}/{filename}", "w") as f:
                f.write(base64.b64decode(files[filename]).decode("utf-8"))
