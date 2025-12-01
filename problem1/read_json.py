import json
 
def read_interface_data(file_path):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
 
        iface = data.get("data", {}) \
                    .get("openconfig-interfaces:interfaces", {}) \
                    .get("interface", [{}])[0]
 
        name = iface.get("name", "Key not found")
        intf_type = iface.get("state", {}).get("type", "Key not found")
 
        subif = iface.get("subinterfaces", {}) \
                     .get("subinterface", [{}])[0]
 
        ipv4_data = subif.get("openconfig-if-ip:ipv4", {}) \
                         .get("addresses", {}) \
                         .get("address", [{}])[0]
 
        ipv4_addr = ipv4_data.get("ip", "Key not found")
        prefix_len = ipv4_data.get("state", {}).get("prefix-length", "Key not found")
 
        counters = iface.get("state", {}).get("counters", {})
 
        in_octets = counters.get("in-octets", "Key not found")
        in_unicast = counters.get("in-unicast-pkts", "Key not found")
        out_octets = counters.get("out-octets", "Key not found")
        out_unicast = counters.get("out-unicast-pkts", "Key not found")
 
        print(f"name : {name}")
        print(f"type: {intf_type}")
        print(f"Ipv4 address: {ipv4_addr}")
        print(f"Prefix length: {prefix_len}")
        print(f"in octets: {in_octets}")
        print(f"in unicast pkts: {in_unicast}")
        print(f"out octets: {out_octets}")
        print(f"out unicast pkts: {out_unicast}")
 
    except FileNotFoundError:
        print("Error: JSON file not found.")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")
    except Exception as e:
        print(f"Unexpected error: {e}")
 
read_interface_data("intf.json")
 