'''127.0.0.1:8001
'''
from fastapi import FastAPI
import threading
    

app = FastAPI()
access = threading.Lock()


@app.get("/fetch")
async def fetch(guid: str):
    '''Fetch the files required for a given sample GUID

    Args:
        guid (str): Sample GUID
    '''
    with access:
        return {'file': open(f"files/{guid}.fastq").read()}
    
