# crt.sh Subdomain Finder

A Python script that queries the [crt.sh](https://crt.sh) website for certificate transparency data, extracts the unique list of subdomains for a given domain, and writes the results to a file.

## Features

- **Subdomain Enumeration:** Fetches subdomains related to a specified domain using crt.sh.
- **Unique Results:** Eliminates duplicate subdomains from the output.
- **Command-Line Interface:** Specify the target domain and output file directly via CLI arguments.

## Requirements

- Python 3.x
- [requests](https://pypi.org/project/requests/) library

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/ishan-saha/crt.sh.git
   cd crt.sh
   pip install -r requirements.txt
   ```

2. **Usage**

   ```python3 crt_subdomain.py -d example.com -o output.txt```

   
