import datetime

def write_invoice(file_name, invoice_data_list):
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')# Give current time

    # Write invoice data to the file
    with open(file_name, 'w') as file:
        file.write("\t\t\t\tTechno property Nepal bill\n")
        file.write("\t\t\t----------------------------\n")
        file.write("\n")
        file.write("\t \t Koteshower ,kathmandu | contact number:9841612287 \n")
        file.write("\n")
        file.write("\t \t-----------------------------------------------------------------------\n")
        file.write("Customer Information\n")
        file.write("---------------------\n")
        file.write("Kitta Number" + " " * 8 + "Customer Name" + " " * 15 + "Rent Date" + " " * 12 + "Return Date" + " " * 10 + "Amount" + " " * 8 + "Overdue Fine" + " " * 8 + "Time" + "\n")
        file.write("--------------------------------------------------------------------------------------------\n")

        for invoice_data in invoice_data_list:
            kitta_number = str(invoice_data['Kitta Number']).ljust(15)
            customer_name = str(invoice_data['Customer Name']).ljust(30)
            rent_date = str(invoice_data['Rent Date']).ljust(20)
            return_date = str(invoice_data['Return Date']).ljust(20)
            amount = str(invoice_data['Amount']) if 'Amount' in invoice_data else 'N/A'
            amount = amount.ljust(15)
            overdue_fine = str(invoice_data['Overdue Fine']) if 'Overdue Fine' in invoice_data else 'N/A'
            overdue_fine = overdue_fine.ljust(15)
            time = current_time.ljust(20)

            file.write(kitta_number + customer_name + rent_date + return_date + amount + overdue_fine + time + "\n")
        
        file.write("Thank you for choosing Techno Property Nepal!")#write footer
