from dotenv import load_dotenv
import os
import requests
from utils.speak import speak



# Loading environment variables from .env file in the root directory 
load_dotenv()

BACKEND_URL = os.getenv("BACKEND_URL")
try:
    if not BACKEND_URL:
        raise ValueError("BACKEND_URL not found in .env file!")
except:
    print("❌ BACKEND_URL not found in .env file!")


def SIGNUP():

    print("\n--- User Sign Up ---")
    
    username = input("Enter Your Username: ")
    email = input("Enter Your Email: ")
    contactNumber = input("Enter Your Contact Number: ")
    password = input("Enter Your Password: ")

    print("🔄 Processing your request, Please Wait...")
    speak("Processing your request, Please Wait...")

    try:
        response = requests.post(
            f"{BACKEND_URL}/api/v1/auth/user/signup",
            json={
                "username": username,
                "email": email,
                "contactNumber": contactNumber,
                "password": password
            }
        )

        response.raise_for_status()  # Raises error if status code is not 2xx

        data = response.json()

        print(f"✅ {data['message']}")
        speak(f"{data['message']}")
        # print("Response:", data)

    except:
        print("❌ Something Went Wrong, Please Try Again Later!:" )
    # except requests.exceptions.RequestException as e:
    #     print("❌ Error during signup:", e)
    # except ValueError:
    #     print("❌ Response is not valid JSON.")
    print()


def SHOW_ALL_USERS():
    print("\n🔎 Searching...")
    
    try:
        response = requests.get(f"{BACKEND_URL}/api/v1/auth/user")

        response.raise_for_status()  # Raises error if status code is not 2xx

        data = response.json()

        print("✅ --- All the Users in the Database --- ✅\n")

        if (len(data['finalUserArray']) == 0):
            print("⚠️ No Users Found!")
            speak("No Users Found!")
            return
        
        # col_widths = {
        #     "Sno": 5,
        #     "username": 20,
        #     "email": 30,
        #     "contactNumber": 15
        # }

        col_widths = {
            "Sno": 5,
            "username": 28,
            "email": 35,
            "contactNumber": 15
        }
        
        # Printing the header
        header = f"{'Sno'.ljust(col_widths['Sno'])}  {'Username'.ljust(col_widths['username'])}  {'Email'.ljust(col_widths['email'])}  {'Contact Number'.ljust(col_widths['contactNumber'])}"
        print(header)
        print("-" * len(header))

        # Print the user's data
        for index, user in enumerate(data['finalUserArray'], start=1):
            row = f"{str(index).ljust(col_widths['Sno'])}  {user['username'].ljust(col_widths['username'])}  {user['email'].ljust(col_widths['email'])}  {user['contactNumber'].ljust(col_widths['contactNumber'])}"
            print(row)

        # print("Sno\t\tusername\t\temail\t\tcontactNumber")
        # print("-------------------------------------------------------------------------")
        
        # for index, user in enumerate(data['finalUserArray'], start=1):
        #     print(f"{index}\t\t{user['username']}\t\t{user['email']}\t\t{user['contactNumber']}")
        # print()

        
    except:
        print("❌ Something Went Wrong, Please Try Again Later!:" )


def main():
    if not BACKEND_URL:
        speak("Create a .env file in the root directory and add your backend url in it.")
        return
    
    while True:
        print("\nOptions:")

        options = ["1-> SignUp" , "2-> Display All Users" , "3-> EXIT\n"]

        for option in options:
            print(option)

        choice = input("Enter Your Choice: ")

        if choice == '1':
            SIGNUP()
            
        elif choice == '2':
            SHOW_ALL_USERS()

        elif choice == '3':
            print("👋 Byee bye, See You Sooon...")
            speak("Byee bye, See You Sooon...")
            break
        else:
            print("⚠️ Invalid Choice! Please try again.")
    print()

main()