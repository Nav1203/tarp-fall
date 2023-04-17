import heyoo
def send_whtsp_msg(body,number):
        messenger = heyoo.WhatsApp('<Enter API key from META developer',phone_number_id='<Enter Id from META developer>')# For sending a Text messages
        messenger.send_message(body,number)
