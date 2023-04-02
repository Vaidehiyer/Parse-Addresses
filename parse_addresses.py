from argparse import ArgumentParser
import re
import sys


def parse_address(address_string):
    """
    Parses a single address string and returns a dictionary containing the parts of the address.

    Args:
    address_string (str): A string containing an address in the format "house_number street, city state zip".

    Returns:
    dict: A dictionary with the keys "house_number", "street", "city", "state", and "zip", and the corresponding
    values from the address string. If the address string cannot be parsed, returns None.
    """
    pattern = r'(\S+)\s+(.*),\s+(.*)\s+([A-Z]{2})\s+(\d{5})'
    match = re.search(pattern, address_string)
    if match:
        return {
            "house_number": match.group(1),
            "street": match.group(2),
            "city": match.group(3),
            "state": match.group(4),
            "zip": match.group(5)
        }
    else:
        return None


def parse_addresses(file_path):
    """
    Parses a file containing addresses and returns a list of dictionaries.

    Args:
    file_path (str): A string containing the path to the file to be parsed.

    Returns:
    list: A list of dictionaries, where each dictionary contains the keys "house_number", "street", "city",
    "state", and "zip", and the corresponding values from the addresses in the file. If an address cannot be parsed,
    the corresponding dictionary will be None.
    """
    with open(file_path, 'r') as file:
        addresses = [parse_address(line.strip()) for line in file]
    return addresses


def parse_args(arglist):
    """ Parse command-line arguments. """
    parser = ArgumentParser()
    parser.add_argument("file",
                        help="file containing one address per line")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    for address in parse_addresses(args.file):
        print(address)
