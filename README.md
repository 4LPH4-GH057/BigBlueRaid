# BigBlueRaid
This is a script for raiding BigBlueButton Meetings with Bots. 
 WARNING THIS IS A REAL TOOL!

## CMD Line Arguments
### Required 
* ``-m [meeting_link]``
* ``-p [meeting_pw]`` 			
			(if needed)
### Optional
* ``-f [file to read names from]``  
			(default "names.txt")
* ``-d [delay]``
			 (default 2secs)
* ``-u [single_user_name]``

## Usage

``python3 main.py -m https://www.example-meeting.com/b/abc-def-ghi-j12``


## Requirements

[Selenium](https://www.selenium.dev) `pip install selenium`
[Firefox](https://www.mozilla.org/de/firefox/new/)
[Gecko Webdriver](https://github.com/mozilla/geckodriver/releases)
