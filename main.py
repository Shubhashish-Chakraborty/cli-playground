from dotenv import load_dotenv
import os
import requests

# Loading environment variables from .env file in the root directory 
load_dotenv()

BACKEND_URL = os.getenv("BACKEND_URL")

if not BACKEND_URL:
    raise ValueError("❌ BACKEND_URL not found in .env file!")

def SIGNUP():

    print("\n--- User Sign Up ---")
    
    username = input("Enter Your Username: ")
    email = input("Enter Your Email: ")
    contactNumber = input("Enter Your Contact Number: ")
    password = input("Enter Your Password: ")

    print("🔄 Processing your request, Please Wait...")

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

        print("✅ Signup successful!")
        print("Response:", data)

    except:
        print("❌ Something Went Wrong, Please Try Again Later!:" )
    # except requests.exceptions.RequestException as e:
    #     print("❌ Error during signup:", e)
    # except ValueError:
    #     print("❌ Response is not valid JSON.")
    print()



def main():
    while True:
        print("\nOptions:")
        print("1 -> SignUp")
        print("2 -> Exit")
        choice = input("Enter Your Choice: ")

        if choice == '1':
            SIGNUP()
        elif choice == '2':
            print("👋 Exiting...")
            break
        else:
            print("⚠️ Invalid Choice! Please try again.")

main()