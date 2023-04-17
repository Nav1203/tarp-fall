import whatsappdemo
import telegramdemo
import geocoder
def send(img_url):
    number='''Phone Number the message is to be sent to'''
    g=geocoder.ip('me')
    msg_str="Fall Detected at Location "+"http://maps.google.com/maps?q="+str(g.latlng[0])+","+str(g.latlng[1])+" Image: "+img_url
    print(msg_str)
    whatsappdemo.send_whtsp_msg(msg_str,number)
    telegramdemo.tel_bot_send_msg(msg_str)
