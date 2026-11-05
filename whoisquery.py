import whois
from tabulate import tabulate

def get_whois_info(domain):
    try:
        w = whois.whois(domain)
        if isinstance(w.creation_date, list):
            creation_date = w.creation_date[0]
        else:
            creation_date = w.creation_date
        
        if isinstance(w.expiration_date, list):
            expiration_date = w.expiration_date[0]
        else:
            expiration_date = w.expiration_date
        
        if isinstance(w.updated_date, list):
            updated_date = w.updated_date[0]
        else:
            updated_date = w.updated_date
        
        data = [
            ["Domain Name", w.domain_name],
            ["Registrar", w.registrar],
            ["Registered On", creation_date],
            ["Expires On", expiration_date],
            ["Updated On", updated_date]
        ]
        print(tabulate(data, headers=["Field", "Value"], tablefmt="grid"))
    except Exception as e:
        print(f"Error fetching WHOIS data: {e}")

if __name__ == "__main__":
    domain = input("Enter domain name: ")
    get_whois_info(domain)
