def _update_position(active_client, transaction):
    # helper function to only be used inside create_transaction    

    if transaction['type'] == 'CONTRIBUTION':
        if active_client['positions']:
            for position in active_client['positions']:                
                if position['symbol'] == transaction['symbol']:
                    position['shares'] += transaction['shares']
        else:
            position = {'id': transaction['id'],            
            'shares': round(transaction['shares'], 2),
            'symbol': transaction['symbol'],
            'name': transaction['name'],
            'avg_cost': transaction['trn_price']}

            active_client['positions'].append(position)    # or client['positions].append(position)
    elif transaction['type'] == 'BUY':
        current_position = None
        for position in active_client['positions']:            
            if transaction['symbol'] == position['symbol']:                
                current_position = position
                break

        if current_position:
            
            old_total_cost = current_position['shares'] * current_position['avg_cost']
            new_total_cost = old_total_cost + transaction['shares'] * transaction['trn_price']
            
            current_position['shares'] += transaction['shares']
            current_position['avg_cost'] = new_total_cost / current_position['shares']
            
        else:
            position = {'id': transaction['id'],            
            'shares': round(transaction['shares'], 2),
            'symbol': transaction['symbol'],
            'name': transaction['name'],
            'avg_cost': transaction['trn_price']}
            active_client['positions'].append(position) 

        for position in active_client['positions']:
            if '$$$$' == position['symbol']:
                position['shares'] -= transaction['shares'] * transaction['trn_price']



        
    elif transaction['type'] == 'SELL':
        pass
    elif transaction['type'] == 'WITHDRAWAL':
        pass
    else:
        print('FATAL ERROR: we should never get here _update_postion')
        exit()
    return