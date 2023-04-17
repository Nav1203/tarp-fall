import whatsappdemo
import telegramdemo
import geocoder
def send_img():
    phone_numbers=['919188590190','917907779230','918618841325','917034209186']
    for i in phone_numbers:
        whatsappdemo.send_whtsp_img('temp.jpg',i)
def send(img_url):
    phone_numbers=['919188590190','917907779230','918618841325','917034209186']
    g=geocoder.ip('me')
    msg_str="Fall Detected at Location "+"http://maps.google.com/maps?q="+str(g.latlng[0])+","+str(g.latlng[1])+" Image: "+img_url
    print(msg_str)
    for i in phone_numbers:
        whatsappdemo.send_whtsp_msg(msg_str,i)
    telegramdemo.tel_bot_send_msg(msg_str)
if __name__=='__main__':
    send()
