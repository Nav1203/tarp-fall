import requests
def tel_bot_send_msg(body):
    chat_id='fall_det'
    str='''Your API link for telegram bot'''+chat_id+'&text='+body
    x = requests.get(str)

if __name__=="__main__":
    for i in range(0,9):
        tel_bot_send_msg(str(i))
