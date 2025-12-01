import json

try:
    # Step 1: Open and read JSON file
    with open("intf.json", "r") as f:
        data = json.load(f)

    # Step 2: Extract interface block
    intf = data.get("interface", {})

    # Step 3: Extract values safely using .get()
    name = intf.get("name", "Key not found")
    type_ = intf.get("type", "Key not found")

    ipv4 = intf.get("ipv4", {})
    ipv4_addr = ipv4.get("address", "Key not found")
    prefix = ipv4.get("prefix_length", "Key not found")

    counters = intf.get("counters", {})
    in_octets = counters.get("in_octets", "Key not found")
    in_uni = counters.get("in_unicast_pkts", "Key not found")
    out_octets = counters.get("out_octets", "Key not found")
    out_uni = counters.get("out_unicast_pkts", "Key not found")

    # Step 4: Print output
    print("name :", name)
    print("type:", type_)
    print("Ipv4 address:", ipv4_addr)
    print("Prefix length:", prefix)
    print("in octets:", in_octets)
    print("in unicast pkts:", in_uni)
    print("out octets:", out_octets)
    print("out unicast pkts:", out_uni)

# Exception handling
except FileNotFoundError:
    print("Error: intf.json file not found.")

except json.JSONDecodeError:
    print("Error: JSON file format is invalid.")

except Exception as e:
    print("Unexpected error:", e)
