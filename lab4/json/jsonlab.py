import json

with open("sample-data.json", "r") as file:
    data = json.load(file)

print("Interface Status")
print("=" * 80)
print(f"{'DN':<50}{'Desсription':<20}{'Speed':<8}{'MTU':<6}")
print("-"*84)

for item in data["imdata"]:
    attributes = item['l1PhysIf']['attributes']
    dn = attributes.get("dn", "")
    description = attributes.get("descr", "")
    speed = attributes.get("speed", "")
    mtu = attributes.get("mtu", "N/A")
    print(f"{dn:<50}{description:<20}{speed:<8}{mtu:<6}")
