import subprocess

def get_current_wifi_password():
    try:
        # Get the name of the currently connected Wi-Fi network
        current_network = subprocess.check_output(['netsh', 'wlan', 'show', 'interfaces']).decode('utf-8').split('\n')
        current_network = [line.split(":")[1].strip() for line in current_network if "SSID" in line][0]

        # Get the password for the currently connected network
        password_info = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', current_network, 'key=clear']).decode('utf-8').split('\n')
        password = [line.split(":")[1].strip() for line in password_info if "Key Content" in line][0]

        print(f"Currently connected to: {current_network}")
        print(f"Password: {password}")
    except IndexError:
        print("No Wi-Fi network is currently connected, or the password is not available.")
    except subprocess.CalledProcessError:
        print("Failed to retrieve Wi-Fi information. Make sure you are running this script as an administrator.")

# Run the function
get_current_wifi_password()