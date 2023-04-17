import heyoo
def send_whtsp_img(img,number):
        messenger = heyoo.WhatsApp('EAAHdhZCHB3vEBAMQoNdURk6BGpUZBy3qXGYTpdsfUx6BskKtK6JXeoQSmM28T3q4OzB7Yw2W6MeueAeF3eRK4uIPHCylJfVnKbpj7MbbSACZBOthcM3o1wIypuRa6lvYtQmpRgRwBuj3bfIdeZB6QHkzFQrlyfcTulU5TWKZAdQHIY7OFirIP0JZAX1pWRZB4nmJxZCwvLPHjAZDZD',phone_number_id='101431246218481')# For sending a Text messages
        #messenger.send_template("hello_world","918618841325")
        messenger.send_image(img,number)
def send_whtsp_msg(body,number):
        messenger = heyoo.WhatsApp('EAAHdhZCHB3vEBACZAcb6grD1l018DOsZCO2McMlfMG0BE0cf9GTTGt0bs9jElqf3wRc4RN5XRFY8Hq6rxhrSaWIyGrbFRbm8zEdMNF7RHt2cooPUlA2zLZBPLzW6XaPH7LeIjbqUp5IFIrZCfZBlJGGZBh3LZB2OMGrmCR5dPE5zgYj5PS85MzCwFKDNvlmKas8wVOEMypuVAgZDZD',phone_number_id='101431246218481')# For sending a Text messages
        #messenger.send_template("hello_world","918618841325")
        messenger.send_message(body,number)