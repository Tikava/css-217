from handler import SoftwareSupportHandler, HardwareSupportHandler, NetworkSupportHandler
from enums import SupportType, Priority
from model import SupportTicket

def get_input(prompt, options):
    while True:
        try:
            value = int(input(prompt))
            if value not in options:
                raise ValueError(f"Invalid input. Please enter a number between {min(options)} and {max(options)}.")
            return value
        except ValueError as e:
            print(e)

def main():
    hardware_handler = HardwareSupportHandler()
    software_handler = SoftwareSupportHandler()
    network_handler = NetworkSupportHandler()
    
    hardware_handler.set_next_handler(software_handler)
    software_handler.set_next_handler(network_handler)

    print("Welcome to the support system!\nTo create a ticket, fill out the fields.\n")
    
    index = 1
    
    while True:
        description = input("Write a brief description of the issue: ")
        
        type_num = get_input("Enter type of issue:\n1. Hardware\n2. Software\n3. Network\n", [1, 2, 3])
        type = SupportType(type_num)
        
        priority_num = get_input("Enter priority:\n1. LOW\n2. MEDIUM\n3. HIGH\n", [1, 2, 3])
        priority = Priority(priority_num)
        
        ticket = SupportTicket(index, description, type, priority)
        hardware_handler.handle_request(ticket)
        index += 1
        
        cont = input("Do you want to create another ticket? (yes/no): ").lower()
        if cont != "yes":
            break

if __name__ == "__main__":
    main()
