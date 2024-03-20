def main():
    """
    Prompts the user to input an amount in US dollars and converts it to various global currencies.

    This function serves as the entry point for a currency conversion application. 
    It asks the user to enter an amount in US dollars and then displays the 
    equivalent amount in a range of different currencies including GBP, EUR, JPY, 
    AUD, CAD, CHF, CNY, SEK, and NZD using predefined conversion rates.

    Parameters:
    None

    Returns:
    None: This function prints the converted amounts to the console.
    """
        
    print()
    print("Currency Converter: USD to Various Global Currencies")
    print()

    dollars = float(input("Enter amount in US dollars: $"))

    print()
    print("Converted amount: ", convert_to_pounds(dollars), "Pounds Sterling (GBP).")
    print("Converted amount: ", convert_to_euro(dollars), "Euro (EUR).")
    print("Converted amount: ", convert_to_yen(dollars), "Japanese Yen (JPY).")
    print("Converted amount: ", convert_to_aud(dollars), "Australian Dollars (AUD).")
    print("Converted amount: ", convert_to_cad(dollars), "Canadian Dollars (CAD).")
    print("Converted amount: ", convert_to_chf(dollars), "Swiss Francs (CHF).")
    print("Converted amount: ", convert_to_cny(dollars), "Chinese Yuan Renminbi (CNY).")
    print("Converted amount: ", convert_to_sek(dollars), "Swedish Krona (SEK).")
    print("Converted amount: ", convert_to_nzd(dollars), "New Zealand Dollars (NZD).")
    print()

convert_to_pounds = lambda dollars: dollars * 0.79  # 1 United States Dollar equals 0.79 Pound sterling Feb 4, 12:06 PM UTC
convert_to_euro = lambda dollars: dollars * 0.93  # 1 United States Dollar equals 0.93 Euro Feb 4, 9:52 AM UTC   
convert_to_yen = lambda dollars: dollars * 148.38 # 1 United States Dollar equals 148.38 Japanese Yen Feb 4, 9:52 AM UTC       
convert_to_aud = lambda dollars: dollars * 1.53 # 1 United States Dollar equals 1.53 Australian Dollar Feb 3, 10:04 PM UTC     
convert_to_cad = lambda dollars: dollars * 1.35 # 1 United States Dollar equals 1.35 Canadian Dollar Feb 4, 9:52 AM UTC       
convert_to_chf = lambda dollars: dollars * 0.87 # 1 United States Dollar equals 0.87 Swiss Franc Feb 4, 12:08 PM UTC       
convert_to_cny = lambda dollars: dollars * 7.12 # 1 United States Dollar equals 7.12 Chinese Yuan Feb 4, 10:50 AM UTC     
convert_to_sek = lambda dollars: dollars * 10.58 # 1 United States Dollar equals 10.58 Swedish Krona Feb 4, 9:52 AM UTC      
convert_to_nzd = lambda dollars: dollars * 1.65 # 1 United States Dollar equals 1.65 New Zealand Dollar Feb 4, 12:10 PM UTC      

main()