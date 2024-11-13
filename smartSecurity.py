'''
Challenge: "Smart Security System"


A security system for a building has five different sensors that help determine if the building is secure or if an alarm should be triggered. Each sensor represents a boolean value:

sensor_door_locked - True if all doors are locked, False if any door is unlocked.
sensor_windows_closed - True if all windows are closed, False if any window is open.
sensor_alarm_armed - True if the alarm is armed, False if it's disarmed.
sensor_motion_detected - True if there is any motion detected inside, False if there is no motion.
sensor_security_breach - True if any external security breach (like broken glass or forced entry) is detected, False if there is no breach.


HINT: To make sure a user input string is correctly formatted so that their input does not cause an error in your program, use the .strip( ).capitalize( ) methods to make the Input value either True or False, with proper casing and no extra spaces.



The building is considered "Secure" if all of the following conditions are met:

All doors are locked.
All windows are closed.
The alarm is armed.
No motion is detected inside.
No security breach is detected.


Write a function is_building_secure that takes five boolean arguments (representing the states of each sensor) and returns:

"Secure" if the building is secure.
"Warning: Alarm Triggered" if the building is not secure.


Additional Requirements:
Create inputs for each sensor using the input() function to allow the user to provide answers for each sensor's state.
Use these inputs to call the is_building_secure function.
'''
def isBuildingSecure(doorsLocked, windowsClosed, alarmArmed, motionDetected, securityBreac):
    # Test inputs
    if doorsLocked == "True" and windowsClosed == "True" and alarmArmed == "True" and motionDetected == "True" and securityBreach == "True":
    # if (doorsLocked and windowsClosed and alarmArmed and motionDetected and securityBreach):
        # print("The building is secure!!")
        return True
    else:
        return False

print("\n\n\n############################################################")
print("##                                                        ##")
print("##       Welcome to the Seaway Security System            ##")
print("##                                                        ##")
print("############################################################\n\n\n")


startQues = input("Do you need to make any changes to the system? Y or N: ").strip().capitalize()


if startQues == "Y":
    print("\n\n\nCheck the following systems:\n\n")
    doorsLocked = input("Are the doors locked? Type True or False: ").strip().capitalize()
    windowsClosed = input("Are the windows closed? Type True or False: ").strip().capitalize()
    alarmArmed = input("Is the alarm system armed? Type True of False: ").strip().capitalize()
    motionDetected = input("Has motion been detected? Type True of False: ").strip().capitalize()
    securityBreach = input("Has their been a security breach? Type True of False: ").strip().capitalize()

    buildingSecure = isBuildingSecure(doorsLocked, windowsClosed, alarmArmed, motionDetected, securityBreach)
    if buildingSecure == True:
        print("\n\n\n=========================================")
        print("=                                       =")
        print("=   The building is currently secure.   =")
        print("=                                       =")
        print("=========================================\n\n\n")
    else:
        print("\n\n\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("++                                                               ++")
        print("++     There is a warning alarm! Please recheck all systems.     ++")
        print("++                                                               ++")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n\n\n")   
        
elif startQues == "N":
    print("\n\n\n############################################################")
    print("##                                                        ##")
    print("##                  Have a Great Day                      ##")
    print("##                                                        ##")
    print("############################################################\n\n\n")
else:
    print("You input the wrong data. Please try again.")


