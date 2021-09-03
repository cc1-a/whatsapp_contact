from twilio.rest import Client
def send_message(body, to_phone_number):

    account_sid = "AC259ad0659f45d2f1f21838520c4c6c61"

    auth_token  = "4679a6d2cc5e49acebcc1a60726159cf"

    client= Client(account_sid, auth_token)

    whatsapp_no='whatsapp:+14155238886'
    to_whatsapp_no='whatsapp:'+str(to_phone_number)

    client.messages.create(body=body, from_=whatsapp_no, to=to_whatsapp_no)