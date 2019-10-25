import logging
import os
import twilio

from os import getenv
from twilio.rest import Client

TWILIO_ACCOUNT_SID = getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = getenv('TWILIO_AUTH_TOKEN')
TWILIO_NUMBER = getenv('TWILIO_NUMBER')

BUCKET = getenv('BUCKET', 'sms-input')

def send_sms(data,context):

    theBody = "Item added to Cloud Storage bucket '" + BUCKET + "'.\n" + "Item added: " + data['name']

    client = twilio.rest.Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    rv = client.messages.create(
         to= TWILIO_NUMBER,
         from_= TWILIO_NUMBER,
         body= theBody
     )
    return str(rv)
