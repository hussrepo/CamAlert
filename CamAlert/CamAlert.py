import os
import smtplib, ssl
from datetime import date

unformatted_today = date.today()
today = unformatted_today.strftime("%m/%d/%y")

ip_list = []
bad_cameras = []
cam_count = 0
cam_check_count = 0


def import_camlist():
    global total_lines
    global cam_count
    global ip_list
    data_file = open("camlist.txt", "r")
    for each_line in data_file:
        striped_data = each_line.strip("\n")
        ip_list.append(striped_data)
        cam_count +=1
    data_file.close()
    print("Cameras Imported: " + str(cam_count))

def check_camlist():
    global bad_cameras
    global ip_list
    global cam_count
    global cam_check_count
    while cam_check_count != cam_count:
        response = os.system("ping -n 1 -w 1000 " + ip_list[cam_check_count])
        if response == 0:
            print("Camera Responded")
        else:
            print("Camera Did Not Respond")
            bad_cameras.append(ip_list[cam_check_count])
        cam_check_count +=1
    

def email_badcams():
    global bad_cameras
    port = 465
    scriptmail = "scriptmail@domain.com"
    password = "scriptmail@domain.com pass"
    recipients = ['john@doe.com', 'jane@doe.com']
    bad_cameras_email = ""
    for ele in bad_cameras:
        bad_cameras_email += ele +"\n"
    message = "Subject: CamAlert Report " + today + "\n\n" + "Cameras Unreachable:\n\n" + bad_cameras_email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(scriptmail, password)
        server.sendmail(scriptmail, recipients, message)
    
    
    

import_camlist()

check_camlist()

email_badcams()

