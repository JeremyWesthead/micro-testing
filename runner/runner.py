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
    try:
        print()
        print(subprocess.check_output(shlex.split(f"nextflow run . --guid {guid}")).decode("utf-8").strip())
    except Exception as e:
        print("Error!!!")
        print(e)
    print("---------------------------------")
    print()

if __name__ == "__main__":
    #Loop infinitely, checking the queue and processing as requried
    print()
    print()
    print("#################################")
    print("Starting to look in the queue...")

    #Because Kubernetes works with hostnames rather than localhost, figure out which it is
    try:
        requests.get("http://127.0.0.1:8000")
        HOST = "http://127.0.0.1"
        print("Using localhost")
    except:
        HOST = "http://queue"
        print("Using queue")
        
    while True:
        #Check the queue
        item = requests.get(f"{HOST}:8000/fetch").json().get("item")
        if item is None:
            print("Queue is empty, sleeping", flush=True)
            time.sleep(5)
        else:
            print(f"Found new batch: {item}", flush=True)
            run(item)