'''127.0.0.1:8000
'''
from queue import Queue
import threading
from fastapi import FastAPI

class QueueAPI(FastAPI):
    '''An API for queue access
    '''
    def __init__(self):
        '''Constructor
        '''
        super().__init__()
        self.queue = Queue()
    

app = QueueAPI()
access = threading.Lock()


@app.get("/fetch")
async def fetch():
    '''Get an iten from the queue
    '''
    with access:
        if app.queue.qsize() > 0:
            return {'item': app.queue.get()}
        else:
            return {'item': None}

@app.post("/put")
async def put(guid: str):
    '''Put an item in the queue

    Args:
        guid (str): Batch GUID
    '''
    with access:
        app.queue.put(guid)
    
    
