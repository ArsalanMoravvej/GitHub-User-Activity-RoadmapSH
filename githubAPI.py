import requests
import argparse



def print_output(data):
    pass

def get_GitHub_data(username):
    response = requests.get(f'https://api.github.com/users/{username}/events')
    print(response.status_code)
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        print(f'Username "{username}" was ot found!')
        return None
    

def main():    
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
    results = get_GitHub_data(args.userName)

    # terminate if not valid
    if not results: return

    # iterating results
    for i,item in enumerate(results):
        print(i, item['created_at'].split('T'), item['type'], item['repo']['name'].split('/')[1])


if __name__ == '__main__':
    main()