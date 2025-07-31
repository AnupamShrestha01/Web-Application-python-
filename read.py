def read_land_data(file_path):
    land_data = []  # Initialize an empty list to store land data
    try:
        with open(file_path, 'r') as file:  # Open the file for reading
            for line in file:  # Iterate over each line in the file
                # Split the line by comma and assign values to variables
                kitta, city, direction, area, price, status = line.replace('\n', '').split(',')
                # Append a dictionary representing land data to the list
                land_data.append({
                    'kitta': int(kitta),  # Convert kitta to integer
                    'city': city.replace(' ', ''),  # Remove leading and trailing whitespaces from city
                    'direction': direction.replace(' ', ''),  # Remove leading and trailing whitespaces from direction
                    'area': int(area),  # Convert area to integer
                    'price': float(price),  # Convert price to float
                    'status': status.replace(' ', '')  
                })
    except FileNotFoundError:
        print("Error: Land data file not found.")  # Handle FileNotFoundError
    except ValueError:
        print("Error: Incorrect data format in the land data file.")  # Handle ValueError
    return land_data  # Return the list of land data
