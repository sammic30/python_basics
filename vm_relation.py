import yaml

# Define the VMs
vms = ["VM1", "VM2", "VM3"]

# Create a dictionary to represent the relationships
relationships = {}
for vm in vms:
    other_vms = [other_vm for other_vm in vms if other_vm != vm]
    relationships[vm] = other_vms

# Write the data to a YAML file
with open("vm_relationships.yaml", "w") as yaml_file:
    yaml.dump(relationships, yaml_file, default_flow_style=False)

print("YAML file 'vm_relationships.yaml' has been created.")

