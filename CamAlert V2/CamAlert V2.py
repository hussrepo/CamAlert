import os
import smtplib, ssl
from datetime import date

ip_list = []
bad_cameras = []
cam_count = 0
cam_check_count = 0



def import_camlist(ip_list, cam_count):
    data_file = open("camlist.txt", "r")
    for eachline in data_file:
        striped_data = eachline.strip("\n")
        print(striped_data)
        ip_list.append(striped_data)
        cam_count += 1
    data_file.close()

def check_camlist(cam_check_count, cam_count, bad_cameras, ip_list):
    while cam_check_count != cam_count:
        response = os.system("ping -n 1 -w 1000 " + ip_list[cam_check_count])
        if response == 0:
            print("Camera Online")
        else:
            print("Camera Offline")
            bad_cameras.append(ip_list[cam_check_count])
        cam_check_count += 1

def send_email(bad_cameras):
    unformatted_today = date.today()
    today = unformatted_today.strftime("%m/%d/%y")
    port = 465
    scriptmail = "scriptmail@domain.com"
    password = "scriptmail@domain.com pass"
    recipients = ['john@doe.com', 'jane@doe.com']
    bad_cameras_email = ""
    for ele in bad_cameras:
        bad_cameras_email += ele + "\n"
    message = "Subject: CamAlert Report " + today + "\n\n" + "Cameras Unreachable:\n\n" + bad_cameras_email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(scriptmail, password)
        server.sendmail(scriptmail, recipients, message)


def cam_alert(): #Host function that calls all other functions
    import_camlist(ip_list, cam_count)
    print("Cameras Imported: " + str(cam_count))
    check_camlist(cam_check_count, cam_count, bad_cameras, ip_list)
    print("Cameras Checked: " + str(cam_check_count))
    send_email(bad_cameras)

cam_alert()