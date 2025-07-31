import datetime
import read
import operation
import write

def display_land_data(land_data):
    # Display available lands
    print("Available Lands:")
    for land in land_data:
        if land['status'] == 'Available':
            print("Kitta: ", land['kitta'], ", City: ", land['city'], ", Direction: ", land['direction'], ", Anna: ", land['area'], " annas, Price: ", land['price'], " NPR")        
    print("\nUnavailable Lands:")
    # Display unavailable lands
    for land in land_data:
        if land['status'] == 'NotAvailable':
            print("Kitta: ", land['kitta'], ", City: ", land['city'], ", Direction: ", land['direction'], ", Anna: ", land['area'], " annas, Price: ", land['price'], " NPR")

def main():
    land_data_file = 'land_data.txt'
    land_data = read.read_land_data(land_data_file)
    rented_lands = {}  # Dictionary to store rented lands with customer details
    all_invoice_data = []  # List to store invoice data for all transactions

    while True:
        print("                                    -----------------------")     
        print("                                    |Techno Property Nepal|")
        print("          ---------------------------------------------------------------")
        print("")
        print("                            Koteshower| Phone no: 9841612287")
        print("    ---------------------------------------------------------------------------")
        print("")
        print("                Welcome to the system. Hope you have a great day ahead.")
        print(" ------------------------------------------------------------------------------------")
        print("")
        print("           Given below are some of the key features of our operating system.")
        print("==================================================================================================================================================================")
        print("    ")

        # Display land data
        display_land_data(land_data)

        while True:
            print("######################################")
            print("#                                    #")
            print("#Land Rental System                  #")
            print("#1. Rent Land                        #")
            print("#--------------------                #")
            print("#2. Return Land                      #")
            print("#--------------------                #")
            print("#3. Exit                             #")
            print("#--------------------                #")
            print("######################################")
            choice = input("Hello sir/Miss, Enter your choice (1-3): ")

            if choice == '1':
                # Rent Land
                print("_______________________________________________________________")
                print("                                                               ")
                print("To create an invoice, kindly provide the required information: ")
                print("_______________________________________________________________")
                print("\n")
                invoice_data = operation.rent_land(land_data, rented_lands)
                all_invoice_data.extend(invoice_data)

            elif choice == '2':
                # Return Land
                print("_______________________________________________________________")
                print("                                                               ")
                print("To return land, please provide the required information: ")
                print("_______________________________________________________________")
                print("\n")
                invoice_data = operation.return_land(land_data, rented_lands)
                all_invoice_data.extend(invoice_data)

            elif choice == '3':
                # Exit
                print("\n")
                print("*********************************************")
                print("*                                           *")
                print("* Thank you for using Techno Property Nepal *")
                print("*                                           *")
                print("*********************************************")
                break

            else:
                print("Invalid choice! Please select a valid option (1-3).\n")

        exit_choice = input("Do you want to exit the program? (yes/no): ")
        if exit_choice.lower() == 'yes':
            break

    # Generate a single invoice for all transactions
    customer_name = input("Enter customer name for generating invoice: ")
    operation.generate_invoice(customer_name, all_invoice_data)

if __name__ == "__main__":
    main()
