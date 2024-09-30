import requests
import argparse
import json



def print_output(data):
    pass

def get_GitHub_data(username):
    pass

if __name__ == '__main__':    
    """
    Main function to set up the command-line interface and handle user commands.
    """
    # Create the parser
    parser = argparse.ArgumentParser()

    # Add the argument
    parser.add_argument('userName', type=str)

    # Parse the argument
    args = parser.parse_args()

    # Use the argument
    print(f"You entered: {args.userName}")
