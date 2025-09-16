'''
    clients = []                        clients is just a list


    client = {'id':None,                client is just a dictionary
              'fname': None,
              'lname': None,              
              'positions': [],          but it also contains two lists
              'transactions': []}
    
    position = {'id': None,             position is just a dictionary
                'shares': None,         integer except for cash
                'symbol': None,         sp500 + $$$$
                'name': None,
                'avg_cost':None}
    
    transaction ={'id': None,           transaction is just a dictionary
                  'timestamp': None,   
                  'type': None,         BUY, SELL, CONTRIBUTION, WITHDRAWAL
                  'shares': None,       integer except for cash
                  'symbol': None,       sp500 + $$$$
                  'name': None,
                  'trn_price': None}

what do clients, positions and transactions contain? 

what design issues are we not handling?

How do we store our data?
'''


import json
import os
from datetime import datetime

CLIENTS_JSON_FILE = 'portfolio/clients.json'

# ---------- File Handling ----------
def load_clients():
    """Load clients from JSON file or return empty list."""
    if os.path.exists(CLIENTS_JSON_FILE):
        try:
            with open(CLIENTS_JSON_FILE, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            print('FATAL ERROR: Your clients.json file is corrupt 000')
            exit()
    return []



def save_clients(clients):
    """Save clients to JSON file."""
    #print(CLIENTS_JSON_FILE)
    with open(CLIENTS_JSON_FILE, "w") as file:
        json.dump(clients, file, indent=4)





# ---------- Client Handling ----------
def get_next_id(clients):
    """Get the next available client ID."""
    next_id = max((client["id"] for client in clients), default=0) + 1

    next_id = max([client["id"] for client in clients], default=0) + 1

    next_id = 0
    for client in clients:
        if client['id'] > next_id: next_id = client['id']
    next_id += 1


def create_transaction(next_id, type, shares,symbol, name, price):
    """Create a cash contribution transaction."""
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    return {
        'id': next_id,
        'timestamp': timestamp,
        'type': type,
        'shares': round(shares, 2) if type in ('CONTRIBUTION', 'WITHDRAWAL')  else shares,
        'symbol': symbol,
        'name': name,
        'trn_price': round(price, 2)
    }


def input_client(clients):
    """Gather client input (name + cash) and add to clients list."""
    fname = input('Please enter your first name: ')
    lname = input('Please enter your last name: ')

    if not fname or not lname:
        return None  # go back to menu

    # --- cash input now handled here ---
    txt = 'Please enter initial cash contribution: '
    while True:
        try:
            cash = float(input(txt).replace("$", ''))
        except ValueError:
            txt = 'Please enter a number for cash: '
        else:
            if cash > 0:
                break
            txt = 'Please enter a positive number for cash: '

    next_id = get_next_id(clients)

    client = {
        'id': next_id,
        'fname': fname,
        'lname': lname,
        'positions': [],
        'transactions': [create_transaction(next_id, 'CONTRIBUTION', cash, '$$$$', 'Cash', 1.00)]
    }

    clients.append(client)
    save_clients(clients)
    return client

def select_client(clients):


    if not clients:
        print('You have no clients, please create 1 first before selecting (select_client())')
        return None

    menu_items = []
    for client in clients:
        name = client['fname'] + ' ' + client['lname']
        menu_items.append(name)
        while True:
            choice = display_menu(menu_items)
            if choice == '':
                return None                
            else:
                return choice

# ---------- Menu Handling ----------
def display_menu(menu_items):
    """Display a menu and return a valid integer choice."""
    txt = 'Select menu item (display_menu()): '
    while True:
        print('\n\n\n')
        for idx, item in enumerate(menu_items, start=1):
            print(f'{idx}) {item}')
        print('\n\n')

        item_no = input(txt)
        try:
            item_no = int(item_no)
        except ValueError:
            if item_no == '':                
                return None
            txt = 'Please select an integer item (display_menu()): '
        else:
            if 1 <= item_no <= len(menu_items):
                return item_no
            else:
                txt = f'Enter an integer between 1 and {len(menu_items)} (display_menu()): '

# ---------- Main Flow ----------
def main():
    clients = load_clients()   
    
    while True:
        menu_items = ('Create client', 'Select client')
        choice = display_menu(menu_items)

        if choice == None:
            print('exit system 00')
            exit()
        elif choice == 1:  # Create client
            while True:
                choice = input_client(clients)
                if choice == None:
                    print('return to previous menu 1-00')
                    break
                else:
                    new_client = choice
                    print(f"Client {new_client['fname']} {new_client['lname']} created. 1-01")
                    break  # break now out of top loop but go to sc 1 later
        elif choice == 2:            
            while True:
                choice = select_client(clients)                
                if choice == None:
                    print('return to previous menu 2-00')
                    break
                else:
                    print('go to s1 2-01')
                    break  # break now out of top loop but go to sc 1 later

        


if __name__ == "__main__":
    main()
