# Rule-Based Troubleshooting Assistant
# 

print("Welcome to the Troubleshooting Assistant!")
print("Describe your computer issue and I will suggest a possible solution.")
print("Example: no power, no display, slow computer, internet issue, overheating, or blue screen")

while True:

# User input
    problem = input("\nWhat problem are you having? ")

# Convert input to lowercase
    problem = problem.lower()

# Rule 1: Power-related problems
# If the user's input contains keywords that indicate the computer
# is not receiving power, recommend checking power connections.
    if "no power" in problem or "won't turn on" in problem or "dead" in problem:
        print("\nRecommendation:")
        print("Check the power cable, wall outlet, power supply switch, and power button connection.")
        break

# Rule 2: Display-related problems
# If the user's input contains keywords related to a missing display
# or black screen, recommend checking monitor and display connections.
    elif "no display" in problem or "black screen" in problem or "no signal" in problem:
        print("\nRecommendation:")
        print("Check the monitor input, display cable, and GPU/display connection.")
        break

# Rule 3: Performance-related problems
# If the user's input contains keywords indicating slow performance
# or freezing, recommend basic performance troubleshooting steps.
    elif "slow" in problem or "laggy" in problem or "freezing" in problem:
        print("\nRecommendation:")
        print("Close background programs, restart the computer, check Task Manager, and scan for updates or malware.")
        break

# Rule 4: Internet-related problems
# If the user's input contains keywords related to internet or Wi-Fi
# issues, recommend checking the network connection and router.
    elif "internet" in problem or "wifi" in problem or "connection" in problem:
        print("\nRecommendation:")
        print("Restart the router, check your Wi-Fi connection, test Ethernet, or run the Windows network troubleshooter.")
        break

# Rule 5: Temperature-related problems
# If the user's input contains keywords indicating overheating
# or unexpected shutdowns, recommend checking cooling and airflow.
    elif "overheating" in problem or "hot" in problem or "shutting down" in problem:
        print("\nRecommendation:")
        print("Check that fans are spinning, clean dust from the case, improve airflow, and monitor CPU/GPU temperatures.")
        break

# Rule 6: Crash-related problems
# If the user's input contains keywords related to crashes,
# blue screens, or restarts, recommend diagnostic steps.
    elif "blue screen" in problem or "crash" in problem or "restart" in problem:
        print("\nRecommendation:")
        print("Write down the error code, check recent driver updates, remove newly installed software, or run system diagnostics.")
        break

# Rule 7: Mouse input lag related problems
# If the user's input contains keywords describing delayed,
# floaty, or laggy mouse movement, recommend checking mouse
# software, power settings, and wireless interference.
    elif "mouse floaty" in problem or "mouse laggy" in problem or "mouse input lag" in problem or "cursor feels delayed" in problem:
        print("\nRecommendation:")
        print("Try uninstalling mouse software, disabling power saving features, or eliminating wireless interference from other devices.")
        break

# Rule 8: No sound or audio issues
# If the user's input contains keywords related to missing
# or distorted audio, recommend checking audio settings,
# device connections, and playback devices.
    elif "no audio" in problem or "choppy sound" in problem or "audio" in problem or "sound" in problem:
        print("\nRecommendation:")
        print("Try disconnecting and reconnecting your device, checking sound settings, verifying cables are plugged in, and ensuring the correct playback device is selected")
        break

# Default rule if no keywords match
# If none of the defined keywords are found in the user's input,
# provide a generic troubleshooting response and ask for more details.
    else:
        print("\nRecommendation:")
        print("I am not sure what the issue is. Try restarting the computer or describe the problem with different keywords.")

print("\nThank you for using the Troubleshooting Assistant!")