from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from ftplib import FTP
from time import sleep, gmtime, strftime
import os


def upload_to_ftp(ip, user, pw, file, file_name):
    ftp = FTP(ip)
    ftp.login(user, pw)
    file = open(file_name, 'rb')  # 'r' for reading, 'w' for writing 'a' for appending 'b' open the file in binary mode,
    ftp.storbinary('STOR ' + file_name, file)   # upload file
    ftp.close()


folder_id = '1V4nq7ZV6RdxmGwiH_qyaTzvs0FqK8eSE'  # folder ID  you can easily get the ID from browser URL
download_folder = 'download/'


gauth = GoogleAuth()

auth_url = gauth.GetAuthUrl()  # Create authentication url user needs to visit

if gauth.access_token_expired:
    gauth.LocalWebserverAuth()  # Creates local webserver and auto handles authentication.

drive = GoogleDrive(gauth)

while True:
    file_list = []

    try:
        file_list = drive.ListFile({'q': "'%s' in parents and title contains '.jpg'  and trashed=false " % (
            folder_id)}).GetList()  # Get file list from the folder
    except:
        pass

    ### List all:
    # file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
    # q refernce https://developers.google.com/drive/api/v2/search-parameters

    if len(file_list) ==  0: 
        print('No file found')

    for file in file_list:

        ### display file list information
        file_id = file['id']
        file_name = file['title']
        print('title: %s, id: %s' % (file['title'], file['id']))

        ### download file
        download_filepath = download_folder + file_name
        filedownload = drive.CreateFile({'id': file_id})
        filedownload.GetContentFile(download_filepath)

        ### delete file
        # os.remove(file['title'])  # delete from current file
        # file.Trash()  # Move file to trash from google drive.
        # file.UnTrash()  # Move file out of trash from google drive
        # file.Delete()  # Permanently delete the file from google drive

    print('Wait 60s for next run. Current time: ' + strftime("%Y-%m-%d %H:%M:%S", gmtime()))
    sleep(60)

    if gauth.access_token_expired:
        gauth.Refresh()
        print('Access Token expired, gauth refresh' + strftime("%Y-%m-%d %H:%M:%S", gmtime()))
