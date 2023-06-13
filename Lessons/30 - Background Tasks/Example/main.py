import time

from fastapi import BackgroundTasks, FastAPI, Depends

app = FastAPI()


def send_message(email: str, message: str):
    time.sleep(5)
    with open("email_message.txt", "w") as email_file:
        email_file.write(f"{email}: {message}")
        print("Message was sent")


def dependency(background_tasks: BackgroundTasks):
    background_tasks.add_task(send_message, "logging@service.com", "Logging is going alright")
    print("Logging is going on")


@app.post("/send_it_to/{email}", dependencies=[Depends(dependency)])
def send_message_to_email(email: str, message: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(send_message, email, message)
    return {"message": "Message is going to be sent"}
