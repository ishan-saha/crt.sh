#!/usr/bin/env python3
import argparse
import requests

def main():
    # Set up command-line arguments
    parser = argparse.ArgumentParser(description="Fetch unique subdomains from crt.sh")
    parser.add_argument("-d", "--domain", required=True, help="The domain to search (e.g., example.com)")
    parser.add_argument("-o", "--output", required=True, help="Output filename to write the subdomains")
    args = parser.parse_args()

    domain = args.domain
    output_file = args.output

    # Construct the URL. Note: '%25' is the URL-encoded '%' so that the query becomes %.example.com
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    print(f"[+] Fetching data from crt.sh for domain: {domain}")

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
    except requests.RequestException as e:
        print(f"[-] Error fetching data: {e}")
        return

    try:
        json_data = response.json()
    except ValueError as e:
        print(f"[-] Error parsing JSON: {e}")
        return

    # Use a set to avoid duplicates. The 'name_value' field sometimes contains multiple domains separated by newline.
    subdomains = set()
    for entry in json_data:
        names = entry.get("name_value", "")
        for subdomain in names.splitlines():
            subdomains.add(subdomain.strip())

    print(f"[+] Found {len(subdomains)} unique subdomains.")

    # Write the results to the specified output file
    try:
        with open(output_file, "w") as f:
            for sub in sorted(subdomains):
                f.write(sub + "\n")
        print(f"[+] Subdomains written to {output_file}")
    except IOError as e:
        print(f"[-] Error writing to file: {e}")

if __name__ == "__main__":
    main()
