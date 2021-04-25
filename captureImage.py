import cv2
import dropbox
import time
import random

start_time = time.time()

def take_snapshot():
    number = random.randint(0, 100)
    videoCaptureObject = cv2.VideoCapture(0)
    res = True
    while (res):
        ret, frame = videoCaptureObject.read()
        img_name = "img" + str(number) + ".png"

        cv2.imwrite(img_name, frame)
        start_time = time.time()
        res = False
        
    return img_name
    print("Snapshot taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token = "3xK4-zIywnsAAAAAAAAAAQWzMlFC4JefQNOBpsNTxLrgn3rvEPyZqTajGLmkLjQK"
    file = img_name
    file_from = file
    file_to = "/NewFolder1/" + img_name

    dbx = dropbox.Dropbox(access_token)
    with open(file_from, "rb") as f:
        dbx.files_upload(f.read(), file_to, mode = dropbox.files.WriteMode.overwrite)
        print("File uploaded")

def main():
    while (True):
        if ((time.time() - start_time) >= 30):
            name = take_snapshot()
            upload_file(name)

main()