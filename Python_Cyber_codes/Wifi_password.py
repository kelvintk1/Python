import subprocess

# Fetch all Wi-Fi profiles
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')

# Extract profile names
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

# Print header
print("\n{:<30} | {}".format("Wi-Fi Name", "Password"))
print("-" * 46)

# Fetch and print passwords for each profile
for i in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    try:
        print("{:<30} | {}".format(i, results[0]))
    except IndexError:
        print("{:<30} | {}".format(i, ""))