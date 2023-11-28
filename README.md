# Auth Smasher

Auth Smasher is a penetration testing tool available as open-source software. Its primary function is to automate tasks related to penetration testing, specifically focusing on the identification and exploitation of SQL injection vulnerabilities, as well as executing brute-force attacks. This tool is designed to facilitate the process of bypassing the login pages of web applications.

## Screenshot

![authsmasher-banner](/images/screenshot.png)

## Requirements

* Python
* pip package installer

## Python modules required

* requests
* termcolor import colored
* os
* time
* twilio
* datetime

## Installation

Download and install the latest version of Python (https://www.python.org/downloads/)

Clone the repository to your computer by typing the following commands on your shell,

`git clone https://github.com/zafarfast/authsmasher.git`

`cd authsmasher`

`pip3 install requests termcolor twilio` or `pip install requests termcolor twilio`

## Run the program

To run the app, type the following command in your shell,

`python3 main.py` or `python main.py`

## SMS notification feature

If you wish to use the SMS notification feature, register and create account on Twilio. (https://www.twilio.com/try-twilio). 

You will get the following after registering a trial account on Twilio,

* SID
* Token
* Account mobile number
* Limited free messages

Once you have the above, open main.py file and copy their values in the variables below,

`account_sid = "" `

`auth_token = "" `

`USER_PHONE_NUMBER = ""`

`TWILIO_ACCOUNT_MOBILE_NUMBER = ""#Enter the Twilio account mobile number here`

## Report feature

All the password and SQL injections attempts are recorded in report.txt file.
