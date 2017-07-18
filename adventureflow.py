print("You wake up in a small cabin.")
print("You can either *explore the cabin*, or *exit* it to see where you are.")
user_input = input()
if user_input == "explore the cabin":
    print("You walk around for a few minutes until you begin to hear a strange noise coming from one of the rooms.")
    print("*open the room door*, or *leave the cabin*?")
    user_input = input()
if user_input == "open the room door":
    print("There appears to be a jewlery box playing music so relaxing that it lulls you to sleep.")
    print("You wake up after a couple hours confused and still sleepy. *keep exploring*, or *leave the cabin*?")
    user_input = input()
if user_input == "keep exploring":
    print("Once was enough. You died of boredom after exploring for so long. (YOU LOSEEEEEEEEEEEEE)")
    user_input = input()
if user_input == "leave the cabin" or user_input == "exit":
    print("You left the cabin only to find four starving wolves begging for food.")
    print("*run away* so they don't maul you, or *throw whatever you have* in your pockets at them in high hopes they'll leave you alone.")
    user_input = input()
if user_input == "run away":
    print("You get away safely and find some donuts. (YOU WINNNNNNNNNNNNN)")
if user_input == "throw whatever you have":
    print("You only had coins. The noise of the coins frightens the wolves, and they all take turns feasting on you. You died. (YOU LOSEEEEEEEEEEEEE)")
