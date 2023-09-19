import yaml

# List of VMs
#vms = ["ussouth.com", "westus.com", "eastus.com", "central.com"]

with open('/var/tmp/vm.txt', 'r') as file:
    # Read the lines and store them in a list
    vms = [line.strip() for line in file]

# Create a dictionary to hold the structure
vm_hierarchy = {}

# Populate the dictionary with VMs and their relationships
for vm in vms:
    other_vms = [other_vm for other_vm in vms if other_vm != vm]
    vm_hierarchy[vm] = other_vms

# Create a dictionary for the final YAML structure
yaml_data = {"vm_hierarchy": vm_hierarchy}

# Write the data to a YAML file
with open("vm_hierarchy.yaml", "w") as yaml_file:
    yaml.dump(yaml_data, yaml_file, default_flow_style=False)

print("YAML VM hierarchy file 'vm_hierarchy.yaml' generated successfully.")
