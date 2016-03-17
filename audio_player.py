local_directory = '/home/pi/Desktop/Audio_Files'

def get_files():

    global local_directory

    import os, shutil, fnmatch

    if os.path.exists(local_directory):
        shutil.rmtree(local_directory)

    if not os.path.exists(local_directory):
        os.makedirs(local_directory)

    from ftplib import FTP.
    
    ftp = FTP('thecharlieforce.com')
    ftp.login('', '')
    ftp.cwd('web/audio') 
    filenames = ftp.nlst()

    for filename in filenames:
        if fnmatch.fnmatch(filename, '*.mp3'):
            local_filename = os.path.join(local_directory, filename)
            file = open(local_filename, 'wb')
            ftp.retrbinary('RETR '+ filename, file.write)

            file.close()

    ftp.quit()


import os
import RPi.GPIO as GPIO
import random, time

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state18 = GPIO.input(18)
    if input_state18 == False:
        file_to_play = random.choice(os.listdir(local_directory))
        print(file_to_play)
        os.system('omxplayer ' + local_directory + '/' + file_to_play)
        time.sleep(2)
        
    input_state17 = GPIO.input(17)
    if input_state17 == False:
        get_files()
        time.sleep(10)    
