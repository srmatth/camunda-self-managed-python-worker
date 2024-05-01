from pyzeebe import ZeebeWorker, create_insecure_channel, Job
import asyncio
import logging
import grpc

def main():
    print("Starting worker")
    grpc_channel = grpc.aio._channel.insecure_channel("http://localhost:26500")
    worker = ZeebeWorker(grpc_channel)
    print(grpc_channel)
    print(worker)

    @worker.task(task_type="task_helloWorld")
    def task_helloWorld(job: Job):
        return {"message": "Hello World!"}
    
    print("about to start the loop")
    loop = asyncio.get_event_loop()
    try:
        print("in the try catch thing")
        loop.run_until_complete(worker.work())
    finally:
        print("about to close")
        loop.close()

if __name__ == "__main__":
    logging.log(logging.INFO, "Starting main function")
    main()
