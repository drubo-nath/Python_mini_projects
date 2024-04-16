import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_info():
    try:
        with sr.Microphone() as source:
            print('I am listening you')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Make sure to give app access in your Google account
    server.login('email_of_the_sender', 'password_of_the_sender')
    email = EmailMessage()
    email['From'] = 'email_of_the_sender'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {
    'drubo': 'drubo.nath.official@gmail.com',

}


def get_email_info():
    talk('Tell the name of the person to whom you want to send email!')
    name = get_info()
    receiver = email_list[name]
    talk('What will be the subject of your email?')
    subject = get_info()
    talk('Tell inside text of your email')
    message = get_info()
    send_email(receiver, subject, message)
    talk('Successful! Your email is sent')
    talk('Do you want to send more email right now?')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()


get_email_info()