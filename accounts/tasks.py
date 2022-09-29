from celery import shared_task
import requests

url = "https://api.mailgun.net/v3/lelionprofessionals.com/messages"
api = "117d9a71a610e3c2e4a9ec2878f673b4-20ebde82-d91d9532"
from_who = "Account Status <info@lelionprofessionals.com>"

lelion_prof_url = 'https://api.mailgun.net/v3/lelionprofessionals.com/messages'
lelion_prof_api = '117d9a71a610e3c2e4a9ec2878f673b4-20ebde82-d91d9532'

def sending_email(from_person,to,subject,text):
    return requests.post(
        lelion_prof_url,
        auth=("api", lelion_prof_api),
        data={"from": from_person,
            "to": f"{to}",
            "subject": f"{subject}",
            "text": f"You are receiving this email from {from_person}. The message is this {text}"})


def send_simple_message(to,subject,text):
    return requests.post(
        url,
        auth=("api", api),
        data={"from": from_who,
            "to": f"{to}",
            "subject": f"{subject}",
            "text": f"You can now change your password if you follow this link {text}"})

def send_simple_activation_email(to,subject,text):
    return requests.post(
        url,
        auth=("api", api),
        data={"from": from_who,
            "to": f"{to}",
            "subject": f"{subject}",
            "text": f"You can now activate your email by following this link {text}"})

def send_simple_activation_change_email(to,subject,text):
    return requests.post(
        url,
        auth=("api", api),
        data={"from": from_who,
            "to": f"{to}",
            "subject": f"{subject}",
            "text": f"You can now change your email by following this link {text}"})

def send_simple_username(to,subject,text):
    return requests.post(
        url,
        auth=("api", api),
        data={"from": from_who,
            "to": f"{to}",
            "subject": f"{subject}",
            "text": f"Your username is {text}"})

# You can see a record of this email in your logs: https://app.mailgun.com/app/logs.

# You can send up to 300 emails/day from this sandbox server.
# Next, you should add your own domain so you can send 10000 emails/month for free.

@shared_task
def send_email_activation_task(to,subject,text):
    send_simple_activation_email(to,subject,text)
    return None
@shared_task
def send_email_task(to,subject,text):
    send_simple_message(to,subject,text)
    return None

@shared_task
def send_activation_change_email_task():
    send_simple_activation_change_email(to,subject,text)
    return None

@shared_task
def send_username_task(email,subject,username):
    send_simple_username(email,subject,username)
    return None
@shared_task
def file_writer(user,uri):
    # Append-adds at last
    file1 = open("myfile.txt", "a")  # append mode
    file1.write(f"Today {user} , {uri} \n")
    file1.close()
    print("File Written successfully")
