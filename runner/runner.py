'''127.0.0.1:8004
'''
import subprocess
import shlex
import time
import requests

    
def run(guid: str):
    '''Given a batch GUID, run the nextflow pipeline

    Args:
        guid (str): GUID of a batch
    '''
    #Run the pipeline
    print(subprocess.check_output(shlex.split(f"nextflow run . --guid {guid}")).decode("utf-8").strip())
    print()

if __name__ == "__main__":
    #Loop infinitely, checking the queue and processing as requried
    while True:
        #Check the queue
        item = requests.get("http://127.0.0.1:8000/fetch").json().get("item")
        if item is None:
            print("Queue is empty, sleeping", flush=True)
            time.sleep(20)
        else:
            print(f"Found new batch: {item}", flush=True)
            run(item)