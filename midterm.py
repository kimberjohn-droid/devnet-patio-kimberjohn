"""
Midterm Practical Exam — Network Device Inventory Tool
Student: Kimber John Patio
"""

devices = []  # starts empty — the user adds devices as the program runs

def display_menu():
    """Displays the menu options and returns the user's choice."""
    print("\n=== Network Device Inventory ===")
    print("1. Add a device")
    print("2. View all devices")
    print("3. Count active vs inactive devices")
    print("4. Find a device by name")
    print("5. Remove a device by name (Bonus)")
    print("6. Exit")
    choice = input("Choose an option: ")
    return choice

def add_device(device_list):
    # ask for name, IP, status — build the string, add to the list
    pass

def view_devices(device_list):
    # loop through and print every device — handle empty list
    pass

def count_active_inactive(device_list):
    # loop through, count Active vs Inactive, return both
    pass

def find_device(device_list):
    # ask for a name, search the list, print result or "not found"
    pass

# BONUS (optional)
def remove_device(device_list):
    # your code here
    pass

def main():
    running = True
    while running:
        choice = display_menu()
        # use if/elif to call the right function based on choice
        # set running = False when the user picks Exit

main()