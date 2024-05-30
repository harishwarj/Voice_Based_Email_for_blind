import speech_recognition as sr  # Import the speech recognition library
import smtplib  # Import the smtplib library for sending emails
import pyaudio  # Import the pyaudio library for accessing the microphone
import platform  # Import the platform library for system-related functions
import sys  # Import the sys library for system-related parameters and functions
from bs4 import BeautifulSoup  # Import BeautifulSoup for parsing HTML content
import email  # Import the email library for handling email messages
import imaplib  # Import the imaplib library for receiving emails
from gtts import gTTS  # Import the gTTS library for text-to-speech conversion
import pyglet  # Import the pyglet library for playing audio
import os  # Import the os library for interacting with the operating system
import time  # Import the time library for managing time-related tasks

# Define the function to play text as speech
def play_text(text):
    tts = gTTS(text=text, lang='en')  # Convert the given text to speech
    ttsname = "temp.mp3"  # Temporary filename for the speech file
    tts.save(ttsname)  # Save the speech to the file
    music = pyglet.media.load(ttsname, streaming=False)  # Load the speech file with pyglet
    music.play()  # Play the speech file
    time.sleep(music.duration)  # Wait for the speech to finish
    os.remove(ttsname)  # Remove the temporary file

# Announce project name
play_text("Project: Voice based Email for blind")  # Announce the project name

# Get login username
login = os.getlogin()  # Get the username of the current system login
print("You are logging from : " + login)  # Print the login username
play_text("You are logging from : " + login)  # Announce the login username

# Announce choices to the user
choices = ["1. Compose a mail.", "2. Check your inbox"]  # Define the choices
for choice in choices:
    print(choice)  # Print each choice
    play_text("Option " + choice)  # Announce each choice

# Get user choice using voice recognition
def get_voice_input(prompt):
    play_text(prompt)  # Announce the prompt to the user
    r = sr.Recognizer()  # Create a Recognizer object
    with sr.Microphone() as source:  # Use the microphone as the source
        print(prompt)  # Print the prompt
        audio = r.listen(source)  # Listen to the user's input
    try:
        text = r.recognize_google(audio)  # Use Google Speech Recognition to recognize the input
        print("You said: " + text)  # Print the recognized text
        return text  # Return the recognized text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")  # Print an error message if the audio is not understood
        play_text("I could not understand. Please try again.")  # Announce an error message
        return None  # Return None if there is an error
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))  # Print an error message if there is a request error
        play_text("Error with the speech recognition service.")  # Announce an error message
        return None  # Return None if there is an error

# Prompt user for their choice
choice = get_voice_input("Your choice")  # Prompt the user for their choice

# If user chooses to compose an email
if choice and choice.lower() in ['1', 'one', 'good morning', 'my choice is one', 'first one', 'option one']:
    subject_text = get_voice_input("Please speak your subject.")  # Prompt the user for the email subject
    body_text = get_voice_input("Please speak your message.")  # Prompt the user for the email body
    
    if subject_text and body_text:
        FROM_EMAIL = "miniyamini2525@outlook.com"  # Sender email address
        TO_EMAIL = "harichselvamc@gmail.com"  # Receiver email address
        PASSWORD = "Qwerty@123456" # Email password

        # Create the email message
        email_message = f"Subject: {subject_text}\n\n{body_text}"  # Format the email message

        try:
            smtp = smtplib.SMTP('smtp-mail.outlook.com', 587)  # Connect to the SMTP server
            smtp.ehlo()  # Send the EHLO command to the SMTP server
            smtp.starttls()  # Start TLS for security
            smtp.ehlo()  # Send the EHLO command again to the SMTP server
            smtp.login(FROM_EMAIL, PASSWORD)  # Log in to the SMTP server
            smtp.sendmail(FROM_EMAIL, TO_EMAIL, email_message)  # Send the email
            smtp.quit()  # Quit the SMTP server
            play_text("Congratulations! Your email has been sent.")  # Announce that the email has been sent
        except smtplib.SMTPAuthenticationError:
            play_text("Authentication failed. Please check your email and password.")  # Announce an authentication error
        except Exception as e:
            print(f"Failed to send email: {e}")  # Print an error message if the email could not be sent
            play_text("Failed to send email. Please try again later.")  # Announce an error message

# If user chooses to check their inbox
elif choice and choice.lower() in ['2', 'two', 'tu', 'to', 'good night', 'second option', 'check inbox', 'read emails', 'read my emails', 'read my messages', 'show my messages', 'inbox', 'check my inbox', 'option two', 'second one', 'my choice is two', 'good evening', 'check messages', 'view inbox', 'view messages', 'view my emails','option']:
    try:
        FROM_EMAIL = "miniyamini2525@outlook.com"  # Sender email address
        PASSWORD = "Qwerty@123456"  # Email password
        
        mail = imaplib.IMAP4_SSL('outlook.office365.com', 993)  # Connect to the IMAP server
        mail.login(FROM_EMAIL, PASSWORD)  # Log in to the IMAP server
        mail.select('inbox')  # Select the inbox

        # Fetch all email IDs in the inbox
        status, email_ids = mail.search(None, 'ALL')  # Search for all emails in the inbox
        email_ids = email_ids[0].split()  # Split the email IDs
        total_emails = len(email_ids)  # Count the total number of emails
        print("Number of emails in your inbox: " + str(total_emails))  # Print the total number of emails
        play_text("Total emails are: " + str(total_emails))  # Announce the total number of emails
        
        # Fetch all unseen email IDs in the inbox
        status, unseen_email_ids = mail.search(None, 'UNSEEN')  # Search for unseen emails in the inbox
        unseen_email_ids = unseen_email_ids[0].split()  # Split the unseen email IDs
        unseen_emails = len(unseen_email_ids)  # Count the number of unseen emails
        print("Number of unseen emails: " + str(unseen_emails))  # Print the number of unseen emails
        play_text("Your unseen emails are: " + str(unseen_emails))  # Announce the number of unseen emails
        
        if unseen_emails > 0:
            latest_email_id = unseen_email_ids[-1]  # Get the latest unseen email ID
            status, data = mail.fetch(latest_email_id, '(RFC822)')  # Fetch the latest unseen email
            raw_email = data[0][1].decode('utf-8')  # Decode the email content
            email_message = email.message_from_string(raw_email)  # Create an email message object
            sender = email_message['From']  # Get the sender's email address
            subject = email_message['Subject']  # Get the email subject
            print(f"From: {sender}")  # Print the sender's email address
            print(f"Subject: {subject}")  # Print the email subject
            play_text(f"From: {sender} And Your subject: {subject}")  # Announce the sender and subject

            if email_message.is_multipart():
                for part in email_message.walk():
                    if part.get_content_type() == "text/plain":
                        body = part.get_payload(decode=True).decode('utf-8')  # Decode the email body
                        print(f"Body: {body}")  # Print the email body
                        play_text(f"Body: {body}")  # Announce the email body
            else:
                body = email_message.get_payload(decode=True).decode('utf-8')  # Decode the email body
                print(f"Body: {body}")  # Print the email body
                play_text(f"Body: {body}")  # Announce the email body

        mail.logout()  # Log out from the IMAP server
    except smtplib.SMTPAuthenticationError:
        play_text("Authentication failed. Please check your email and password.")  # Announce an authentication error
    except Exception as e:
        print(f"Failed to check inbox: {e}")  # Print an error message if the inbox could not be checked
        play_text("Failed to check inbox. Please try again later.")  # Announce an error message

# Instructions for each section
"""
1. Play Text-to-Speech:
    - The function 'play_text' converts text to speech using gTTS and plays the audio using pyglet.

2. Announce Project Name:
    - Use the 'play_text' function to announce the project name.

3. Get Login Username:
    - Use os.getlogin() to fetch the current system login name and announce it.

4. Announce Choices:
    - Loop through a list of choices, print and announce each one.

5. Get Voice Input:
    - Function 'get_voice_input' prompts the user to speak their choice, listens using the microphone, and uses Google's speech recognition to interpret the command.

6. Compose and Send Email:
    - If the user chooses to compose an email, prompt them to speak their subject and message, then send the email using SMTP with a properly formatted message.

7. Check Inbox:
    - If the user chooses to check their inbox, fetch the number of total and unseen emails using IMAP, then fetch and announce details of the latest email.
"""

