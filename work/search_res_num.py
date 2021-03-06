#!/usr/bin/python2.7

import time, os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

# Load browser
driver = webdriver.Firefox()

# Open Database file to read
try:
    dbase = file('database.txt')
except IOError:
    print 'Unable to open file', dbase

# Create new Database file to write
file = open("NewDatabase.txt", 'a')

# Init line count and read in first line
lnum = 0
line = dbase.readline()

#Sign In

def login():
	driver.get("https://www.linkedin.com/uas/login")
	time.sleep(20)
    # During the sleep time, you must use your own credentials in the login window that appears

	wait = WebDriverWait(driver, 5)

	print "signed in"



login()

# Begin timing the program
start = time.time()


# This loop parses the file, reads in the web page, retrieves the info,
# and then writes the info to the file
while 1:


    line = line.rstrip('\r\n')
    lntok = line.split()
    try :
        link = lntok[2]
    except IndexError:
        break

    site = driver.get(link)
    elem = driver.find_element_by_xpath("//*")
    source_code = elem.get_attribute("outerHTML")
    soup = BeautifulSoup(source_code)
    rescount = soup.find("div", {"class" : "mod results_count"})

# If I encounter a sign in timeout:
    if rescount is not None:
        count = rescount.p.strong.string
    else:
        time.sleep(60) # Give me time to enter in user/password and reCaptcha
        continue # rerun the line
    print("\n"+count+"\n")
    file.write(lntok[0] + "\t" + lntok[1] + "\t" + count + "\n")
    lnum += 1
    print lnum
    time.sleep(2.5)
    

    line = dbase.readline()


end = time.time()
print ("Finished")
print ("Time elapsed: "+ str(end - start))
print ("Number of URLs read: " + str(lnum))

file.close()
dbase.close()
driver.quit()

