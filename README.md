# Auth Smasher

Auth Smasher is a penetration testing tool available as open-source software. Its primary function is to automate tasks related to penetration testing, specifically focusing on the identification and exploitation of SQL injection vulnerabilities, as well as executing brute-force attacks. This tool is designed to facilitate the process of bypassing the login pages of web applications.

## Screenshot

![authsmasher-banner](/images/screenshot.png)

## Requirements

* Python
* pip packaga installer

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

`pip install requests termcolor twilio`

## SMS notification feature

If you wish to use the SMS authentication feature, register and create account on Twilio. (https://www.twilio.com/try-twilio). 

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
