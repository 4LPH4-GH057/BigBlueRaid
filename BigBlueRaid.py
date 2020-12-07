from os import system
from os.path import isfile
from sys import argv
from time import sleep

from selenium import webdriver


def banner():
    print("██████╗ ██╗ ██████╗ ██████╗ ██╗     ██╗   ██╗███████╗")
    print("██╔══██╗██║██╔════╝ ██╔══██╗██║     ██║   ██║██╔════╝")
    print("██████╔╝██║██║  ███╗██████╔╝██║     ██║   ██║█████╗  ")
    print("██╔══██╗██║██║   ██║██╔══██╗██║     ██║   ██║██╔══╝  ")
    print("██████╔╝██║╚██████╔╝██████╔╝███████╗╚██████╔╝███████╗")
    print("╚═════╝ ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚══════╝")

    print("         ██████╗  █████╗ ██╗██████╗   ")
    print("         ██╔══██╗██╔══██╗██║██╔══██╗  ")
    print("         ██████╔╝███████║██║██║  ██║  ")
    print("         ██╔══██╗██╔══██║██║██║  ██║  ")
    print("         ██║  ██║██║  ██║██║██████╔╝  ")
    print("         ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═════╝   ")
    print("")
    print("")


meeting_set = False
name_set = False
delay = 1

args = argv
if __name__ == '__main__':

    if "-m" in args:
        place = args.index("-m") + 1
        meeting_set = True
        bbb_meeting = args[place]

    if "-meeting" in args:
        place = args.index("-meetings") + 1
        meeting_set = True
        bbb_meeting = args[place]

    if "-u" in args:
        place = args.index("-u") + 1
        name_set = True
        name = args[place]
    if "-user" in args:
        place = args.index("-user") + 1
        name_set = True
        name = args[place]
    system("cls")
    banner()
    driver = webdriver.Firefox()
    room_id = bbb_meeting.split(".de")[1]
    if not name_set:
        if isfile("names.txt"):
            names = open("names.txt", "r").readlines()
            x = 0
            for i in names:
                name = i.strip()
                driver.get(bbb_meeting)
                sleep(delay)

                enter_code = driver.find_element_by_id("room_access_code")
                enter_code.clear()
                enter_code.send_keys("498794")
                enter_code.submit()
                sleep(delay)
                enter_name = driver.find_element_by_name(room_id + "[join_name]")
                enter_name.clear()
                enter_name.send_keys(name)
                enter_name.submit()
                x += 1
                if not x == len(names):
                    driver.execute_script("window.open('');")
                    driver.switch_to.window(driver.window_handles[x])
                print("Anfrage als " + name + " gesendet")

    else:
        driver.get(bbb_meeting)
        sleep(delay)
        enter_name = driver.find_element_by_name(room_id + "[join_name]")
        enter_name.send_keys(name)
        enter_name.submit()
        print("Anfrage als " + name + " gesendet")
