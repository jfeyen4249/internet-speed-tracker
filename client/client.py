import os
import time
import requests


print(" ")
print("    ******************************************************")
print("    ****             Speed Test Client                ****")
print("    ****                ver 2.2.1                     ****")
print("    ****                                              ****")
print("    ******************************************************")
print(" ")
print(" ")




store = "33"

url = "" # Server
# api=wired = Office computer
# api=wifi  = Secure Wireless
# api=guest = Guest Wireless

test_type = "speedtest"
# speedtest = Speedtest.net CLI test
# fast      = Fast.com test ** Node.js must be installed to run **




if test_type == "speedtest":
    print(" - Starting SpeedTest_CLI ")
    myCmd = 'speedtest-cli --simple > speed.txt'
    os.system(myCmd)
    print(" ")
    print(" ")
    print("  - Speed Test Complete! - ")
    print("  - Formatting Data - ")

    f = open("speed.txt", "r")
    ping = (f.readline())
    download = (f.readline())
    upload = (f.readline())

    download = download[:-7]
    upload = upload[:-7]
    speed = "Mbps"

    down = download.replace('Download:', '', 1) + speed
    upload = upload.replace('Upload:', '', 1) + speed

    f.close()


    payload = {"upload": upload, "download": down, "store": store}
    r = requests.post(url, json=payload)

    servertext = r.text
    if servertext == "Thank You":
        print("  - Speed Test data was saved to server! - ")
        print(" ")
        print(" ")
    else:
        print(servertext)
        print("  - Speed Test data was not saved to server! - ")
        print(" ")
        print(" ")
elif test_type == "fast":
    print(" - Starting Fast Test ")
    myCmd1 = 'fast -u > speed.txt'
    os.system(myCmd1)
    print(" ")
    print(" ")
    print("  - Speed Test Complete! - ")
    print("  -   Formatting Data    - ")
    f1 = open("speed.txt", "r")
    down = (f1.readline())
    upload = (f1.readline())

    f1.close()

    payload = {"upload": upload, "download": down, "store": store}
    r = requests.post(url, json=payload)

    servertext1 = r.text

    if servertext1 == "Thank You":
        print("  - Speed Test data was saved to server! - ")
        print(" ")
        print(" ")
    else:
        print (servertext1)
        print("  - Speed Test data was not saved to server! - ")
        print(" ")
        print(" ")
else:
    print("Error")

