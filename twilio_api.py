from twilio.rest import Client
def send_message(body, to_phone_number):

    account_sid = "your sid"

    auth_token  = "youe auth token"

    client= Client(account_sid, auth_token)

    whatsapp_no='whatsapp:+14155238886'
    to_whatsapp_no='whatsapp:'+str(to_phone_number)

    client.messages.create(body=body, from_=whatsapp_no, to=to_whatsapp_no)
