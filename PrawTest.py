import praw
import datetime
import shelve
import re
import traceback
import time
import pyimgur
from selenium import webdriver
import os

CLIENT_ID = "ImgurClientIdHere"
im = pyimgur.Imgur(CLIENT_ID)

user_agent ='For Those On Mobile Bot by /u/anthoneyk123'
r = praw.Reddit(user_agent=user_agent)
submission = r.get_submission(submission_id='11v36o')
r.login('ForThoseOnMobileBot','PasswordRemoved')
files = shelve.open("PrawTest4.dat", writeback=True)
print "Opened!"
#already_done = {} 
#files["already_done"] = ["a","b"]
#x = files["x"]
#files["x"] = x
files.close()
done = set()
print "Running"
blacklist = ['demobilizer','AutoModerator','NightMirrorMoon','ApiContraption','LocationBot']
while True:
    #subreddit = r.get_subreddit('mobilebot')
    #all_comments = subreddit.get_comments()
    all_comments = r.get_comments('all')
    files = shelve.open("PrawTest4.dat", writeback=True)
    already_done = files["already_done"]
    files.close()
    for comment in all_comments:
        try:
            regex = re.compile('\|:-')
            if (comment.id not in already_done) and (comment.author not in blacklist) and (regex.search(comment.body)):
                
                a = datetime.datetime.now()
                htime = a.hour
                mtime = a.minute
                stime = a.second
                if (mtime<=9):
                    m=str(mtime)
                    m= "0" + m
                else:
                    m = str(mtime)
                if (stime<=9):
                    s=str(stime)
                    s= "0" + s
                else:
                    s=str(stime)

                h = str(htime)


                b = "%s:%s:%s" % (h,m,s)

                
                
                files = shelve.open("PrawTest4.dat", writeback=True)

                link = comment.permalink
                browser = webdriver.Firefox()
                browser.get(link)
                browser.save_screenshot(comment.id +'.png')
                browser.quit()
                PATH = 'C:\Users\Jacob\Desktop\Table Pictures\\' + comment.id + '.png'
                uploaded_image = im.upload_image(PATH, title="Uploaded by /u/ForThoseOnMobileBot")
                link = (uploaded_image.link)
                



                print link
                os.remove('C:\Users\Jacob\Desktop\Table Pictures\\'+comment.id+'.png')
                print "Image deleted"



                comment.reply("[For those on mobile, here is a picture of the table above:]" + "(" + link + ")" + "\n\n -----------------------------------------\n^^I'm ^^a ^^bot, ^^if ^^you ^^have ^^any ^^questions ^^or ^^concerns ^^message ^^/u/anthoneyk123")

                



                





                #comment.reply(comment.permalink)







                
                print "["+b+"]"+" Comment sent!"
                already_done = files["already_done"]
                already_done.append(comment.id)
        
                files["already_done"] = already_done
                

                
                
                files.sync()
                files.close()
        except:
            files = shelve.open("PrawTest4.dat", writeback=True)
            already_done = files["already_done"]
            already_done.append(comment.id)
            files["already_done"] = already_done
            files.sync()
            files.close()

            a = datetime.datetime.now()
            htime = a.hour
            mtime = a.minute
            stime = a.second
            if (mtime<=9):
                m=str(mtime)
                m= "0" + m
            else:
                m = str(mtime)
            if (stime<=9):
                s=str(stime)
                s= "0" + s
            else:
                s=str(stime)

            h = str(htime)

            b = "%s:%s:%s" % (h,m,s)
            print "["+b+"]"+" Error found! Skipping comment..."
            print traceback.format_exc()
            continue
