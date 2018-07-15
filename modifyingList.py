# Program to takes some actions on a list
# and then puts those items in another list

# Start with some designs that need to be printed
unprinted_designs = ['item1', 'item2', 'item3']
completed_models = []

# Simulate printing each design, until none are left.
# Move each design to completed_design after printing
while unprinted_designs:
    current_design = unprinted_designs.pop()

    # Simulate creating a 3D print from the design.
    print("Printing model: " + current_design)
    completed_models.append(current_design)

# Display all completed models.
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
