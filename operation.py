import datetime
import write

def display_lands(land_data):
    # Display header
    print("-----------------------------------------------------------------------------------------------------------------")
    print("Kitta Number      City        Direction        Anna              Price          Status         ")
    print("-----------------------------------------------------------------------------------------------------------------")
    
    # Display land data
    for land in land_data:
        kitta_number = str(land['kitta']).ljust(16)
        city = land['city'].ljust(13)
        direction = land['direction'].ljust(15)
        area = str(land['area']).ljust(18)
        price = str(land['price']).ljust(14)
        status = land['status']
        print(kitta_number + city + direction + area + price + status)
    
    # Display footer
    print("-----------------------------------------------------------------------------------------------------------------")

def rent_land(land_data, rented_lands):
    # Get current date and time
    current_date = datetime.datetime.now()
    all_invoice_data = []

    # Loop for renting land
    while True:
        try:
            # Display available lands
            display_lands(land_data)
            
            # Input customer details
            customer_name = input("Enter customer name: ")
            print("------------------------------------")
            if any(char.isdigit() for char in customer_name):
                print("Error: Customer name cannot contain numbers.")
                continue
            customer_number = int(input("Enter customer number: "))
            print("------------------------------------")
            customer_email = input("Enter customer email: ")
            print("------------------------------------")

            # Input kitta numbers to rent
            print("Enter the Kitta numbers you want to rent (separated by commas):")
            kitta_numbers = [int(x) for x in input().split(',')]
            total_available_anna = sum(land['area'] for land in land_data if land['status'] == 'Available')

            # Confirm renting all available anna
            print("Total Available Anna: " + str(total_available_anna))
            confirmation = input("Do you want to rent all available anna? (yes/no): ").lower()
            print("------------------------------------")

            if confirmation != 'yes':
                print("Error: You must rent all the available anna.")
                continue

            # Input duration of rent
            duration_months = int(input("Enter the duration of rent (in months): "))
            if duration_months <= 0:
                print("Error: Duration must be a positive integer.")
                continue
            print("Thanks for Renting land from Techno Property  Nepal.Invoice generated.")

            # Generate invoice data for each rented land
            invoice_data_list = []
            for kitta_number in kitta_numbers:
                land = next((land for land in land_data if land['kitta'] == kitta_number and land['status'] == 'Available'), None)
                if land:
                    land['status'] = 'NotAvailable'
                    land['customer_name'] = customer_name
                    return_date = current_date + datetime.timedelta(days=duration_months * 30)
                    invoice_data = {
                        'Kitta Number': kitta_number,
                        'Customer Name': customer_name,
                        'Customer Number': customer_number,
                        'Customer Email': customer_email,
                        'Rent Date': current_date.strftime('%Y-%m-%d'),
                        'Return Date': return_date.strftime('%Y-%m-%d'),
                        'Amount': land['price'] * duration_months
                    }
                    invoice_data_list.append(invoice_data)
                    rented_lands[kitta_number] = {'customer_name': customer_name, 'customer_number': customer_number, 'customer_email': customer_email}
                else:
                    print("Error: Land with Kitta Number " + str(kitta_number) + " is not available for rent.")

            all_invoice_data.extend(invoice_data_list)

            more = input("Do you want to rent more land? (yes/no): ")
            if more.lower() != 'yes':
                break
        except ValueError:
            print("Error: Invalid input data.")

    # Write invoice data to file
    invoice_file = str(customer_name) + "_rent_invoice.txt"
    write.write_invoice(invoice_file, all_invoice_data)

    # Update land data file
    write_land_data(land_data)
    return all_invoice_data

def return_land(land_data, rented_lands):
    # Get current date and time
    current_date = datetime.datetime.now()
    all_invoice_data = []

    # Loop for returning land
    while True:
        try:
            # Display available lands
            display_lands(land_data)
            
            # Input customer details
            customer_name = input("Enter customer name: ")
            print("------------------------------------")
            if any(char.isdigit() for char in customer_name):
                print("Error: Customer name cannot contain numbers.")
                continue
            customer_number = int(input("Enter customer number: "))
            print("------------------------------------")
            customer_email = input("Enter customer email: ")
            print("------------------------------------")

            # Input kitta numbers to return
            print("Enter the Kitta numbers you want to return (separated by commas):")
            kitta_numbers = [int(x) for x in input().split(',')]
            return_duration_months = int(input("Enter the duration of return (in months): "))
            if return_duration_months <= 0:
                print("Error: Duration must be a positive integer.")
                continue
            print("Your land has been returned succesfully.Invoice generated")

            # Generate invoice data for each returned land
            invoice_data_list = []
            for kitta_number in kitta_numbers:
                if kitta_number in rented_lands:
                    rented_info = rented_lands[kitta_number]
                    if rented_info['customer_name'] == customer_name and rented_info['customer_number'] == customer_number and rented_info['customer_email'] == customer_email:
                        land = next((land for land in land_data if land['kitta'] == kitta_number and land['status'] == 'NotAvailable'), None)
                        if land:
                            land['status'] = 'Available'
                            del land['customer_name']
                            return_date = current_date + datetime.timedelta(days=return_duration_months * 30)
                            invoice_data = {
                                'Kitta Number': kitta_number,
                                'Rent Date': '',
                                'Return Date': return_date.strftime('%Y-%m-%d'),
                                'Amount': land['price'] * return_duration_months,
                                'Customer Name': customer_name,
                                'Customer Number': customer_number,
                                'Customer Email': customer_email
                            }
                            invoice_data_list.append(invoice_data)
                        else:
                            print("Error: Land with Kitta Number " + str(kitta_number) + " is not rented by any customer.")
                    else:
                        print("Error: Customer details do not match the rented land's details.")
                else:
                    print("Error: Land with Kitta Number " + str(kitta_number) + " is not rented by any customer.")

            all_invoice_data.extend(invoice_data_list)

            more = input("Do you want to return more land? (yes/no): ")
            if more.lower() != 'yes':
                break
        except ValueError:
            print("Error: Invalid input data.")

    # Write invoice data to file
    invoice_file = str(customer_name) + "_return_invoice.txt"
    write.write_invoice(invoice_file, all_invoice_data)

    # Update land data file
    write_land_data(land_data)
    return all_invoice_data

def write_land_data(land_data):
    # Write land data to file
    with open('land_data.txt', 'w') as file:
        for land in land_data:
            status = 'NotAvailable' if land['status'] == 'NotAvailable' else land['status']
            file.write(str(land['kitta']) + ',' + land['city'] + ',' + land['direction'] + ',' + str(land['area']) + ',' + str(land['price']) + ',' + status + '\n')

if __name__ == "__main__":
    # Test the functions if required
    pass
