import ipaddress

def subnet_calculator():
    ip_input = input("Enter your IP address with CIDR (e.g., 192.168.1.0/24): ")
    num_subnets = int(input("Enter desired number of subnets: "))
    print("\nCalculating subnets...\n")
'''
    try:
        network = ipaddress.ip_network(ip_input, strict=False)
    except ValueError:
        print("Invalid IP address or CIDR notation.")
        return

    # Calculate new prefix length
    total_hosts = network.num_addresses
    bits_needed = (num_subnets - 1).bit_length()
    new_prefix = network.prefixlen + bits_needed


    if new_prefix > network.max_prefixlen:
        print("Cannot create that many subnets from this network.")
        return

    subnets = list(network.subnets(new_prefix=new_prefix))
    print(f"\nSubnets ({len(subnets)}):")
    for i, subnet in enumerate(subnets[:num_subnets], 1):
        print(f"{i}: {subnet}")
'''

subnet_calculator()