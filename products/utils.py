def get_currency_symbol(iso_code):
    # Define a mapping between ISO codes and symbols
    currency_symbols = {
        'USD': '$',
        'EUR': '€',
        'GBP': '£',
        # Add other currencies as needed
    }
    return currency_symbols.get(iso_code, iso_code) 