'''127.0.0.1:8003
'''
from fastapi import FastAPI
    

app = FastAPI()
    
@app.get("/batch")
async def batch(guid: str):
    '''Find the samples in the batch

    Args:
        guid (str): Batch guid
    '''
    if "1" in guid:
        return {'samples': ['sample1', 'sample2', 'sample3']}
    elif "2" in guid:
        return {'samples': ['sample2']}
    else:
        return {'samples': ['sample3']}
