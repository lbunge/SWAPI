import requests
import argparse
from tabulate import tabulate

# Function to get starships from the StarWars API.
def get_starships(max_length, max_results):
    # API endpoint.
    url = 'https://swapi.dev/api/starships/'
    # List to store the starships.
    starships = []

    # Loop through all pages.
    while url:
        # Make a GET request to the API.
        response = requests.get(url)
        
        # If the request was not successful, print an error message and break the loop.
        if response.status_code != 200:
            print("Failed to get data from StarWars API")
            break
        
        # Parse the JSON response.
        data = response.json()

        # Loop through all starships on this page.
        for starship in data['results']:
            # Ignore starships with unknown length.
            if starship['length'] == 'unknown':
                continue

            # Convert the length to a float after removing commas. Necessary as length value is type string and some values had a comma/decimal point
            length = float(starship['length'].replace(',', ''))

            # If the starship is shorter than max_length, add it to the list.
            if length < max_length:
                starships.append((starship['name'], length))
        
        # Get the next page.
        url = data['next']

        # If we have enough results, break the loop.
        if len(starships) == max_results:
            break

    # Sort the list of starships by length.
    starships.sort(key=lambda x: x[1])
    
    return starships

# Function to parse command-line arguments.
def parse_arguments():
    # Create an argument parser.
    parser = argparse.ArgumentParser(description='Get Star Wars starships less than a certain length.')
    # Add an argument for the maximum length.
    parser.add_argument('--max_length', type=float, default=25.0, help='Maximum length of starships')
    # Add an argument for the maximum number of results.
    parser.add_argument('--max_results', type=int, default=11, help='Maximum number of results to display')
    return parser.parse_args()

# If this script is run directly, parse arguments and get the starships.
if __name__ == '__main__':
    # Parse the command-line arguments.
    args = parse_arguments()

    # Get the starships from the StarWars API.
    starships = get_starships(args.max_length, args.max_results)

    # Print the starships in a nice table.
    print(tabulate(starships, headers=["Starship Name", "Length (m)"], tablefmt="grid"))
    # Print the total number of starships found.
    print(f"\nTotal starships found: {len(starships)}")
