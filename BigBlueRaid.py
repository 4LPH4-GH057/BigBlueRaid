from os import system
from os.path import isfile
from platform import system as platform
from sys import argv
from time import sleep

from selenium import webdriver


def clear():
    if platform() == "Windows":
        system("cls")
    elif platform() == "Linux":
        system("clear")
    else:
        print("ERROR: not supported os")


def banner():
    clear()
    print("")
    print("")
    print("     ██████╗ ██╗ ██████╗ ██████╗ ██╗     ██╗   ██╗███████╗")
    print("     ██╔══██╗██║██╔════╝ ██╔══██╗██║     ██║   ██║██╔════╝")
    print("     ██████╔╝██║██║  ███╗██████╔╝██║     ██║   ██║█████╗  ")
    print("     ██╔══██╗██║██║   ██║██╔══██╗██║     ██║   ██║██╔══╝  ")
    print("     ██████╔╝██║╚██████╔╝██████╔╝███████╗╚██████╔╝███████╗")
    print("     ╚═════╝ ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚══════╝")

    print("             ██████╗  █████╗ ██╗██████╗   ")
    print("             ██╔══██╗██╔══██╗██║██╔══██╗  ")
    print("             ██████╔╝███████║██║██║  ██║  ")
    print("             ██╔══██╗██╔══██║██║██║  ██║  ")
    print("             ██║  ██║██║  ██║██║██████╔╝  ")
    print("             ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═════╝   ")
    print("")
    print("")



meeting_set = False
name_set = False
custom_file = False
delay = 2
file = "names.txt"

args = argv
if __name__ == '__main__':
    banner()

    if len(args) ==1:
        print("ERROR: pls give required arguments")
        exit()

    if "-m" in args:  # meeting link
        place = args.index("-m") + 1
        meeting_set = True
        bbb_meeting = args[place]
        if not "http" in bbb_meeting:
            print("ERROR: missing http(s)")
            exit()
        try:
            link = bbb_meeting.split("://")[1]
            parts = link.split(".")
            subdomain = parts[0]
            domain_name = parts[1]
            toplevel_domain = parts[2].split("/")[0]
        except:
            print("ERROR: something is wrong with the link")
            print("link: " + bbb_meeting)
            exit()

    if "-u" in args:  # single user (use "-" for space)
        place = args.index("-u") + 1
        name_set = True
        name = args[place]
        name = name.replace("-", " ")

    if "-d" in args:  # delay in seconds (default is 3 seconds)
        place = args.index("-d") + 1
        if args[place].isdigit():
            delay = int(args[place])
        else:
            print("ERROR: not a valid delay")
            exit()

    if "-f" in args:  # set file to read names from (default is "names.txt")
        place = args.index("-f") + 1
        if isfile(args[place]):
            file = args[place]
            custom_file = True
        else:
            print("ERROR: file does not exist")
            exit()
        if len(open(file, "r").readlines()) == 0:
            print("WARNING: file is empty")
            exit()

    opts = webdriver.FirefoxOptions()
    opts.set_preference("dom.popup_maximum", len(open(file, "r").readlines()))
    driver = webdriver.Firefox(options=opts)

    room_id = bbb_meeting.split(domain_name + "." + toplevel_domain)[1]
    if not name_set:
        if isfile(file):
            names = open(file, "r").readlines()
            x = 0
            for i in names:
                try:
                    name = i.strip()
                    driver.get(bbb_meeting)
                    html = driver.page_source

                    if not "404" in html:
                        #sleep(delay)
                        enter_name = driver.find_element_by_name(room_id + "[join_name]")
                        enter_name.clear()
                        enter_name.send_keys(name)
                        enter_name.submit()

                        if not x + 1 == len(names):
                            x += 1
                            sleep(delay)
                            driver.execute_script("window.open('');")
                            driver.switch_to.window(driver.window_handles[x])

                        print("request sent as " + name + ", " + str(x + 1) + ". request")

                    elif "404" in html:
                        print("ERROR: invalid link/meeting")
                        exit()

                except KeyboardInterrupt:
                    print("")
                    print("interrupted by Keyboardevent")
                    exit()
    else:
        # single user request
        html = driver.page_source

        if not "404" in html:
            driver.get(bbb_meeting)
            #sleep(delay)
            enter_name = driver.find_element_by_name(room_id + "[join_name]")
            enter_name.send_keys(name)
            enter_name.submit()
            print("request sent as " + name)
            exit()
        elif "404" in html:
            print("ERROR: invalid link/meeting")
            exit()
