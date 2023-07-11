def allocation_calculator(num_ppl):
    
    num_classes = max(2, (num_ppl + 29) // 30)   # Ensure at least 2 classes

    # Calculate the number of ppl in each class
    ppl_per_class = num_ppl // num_classes
    remaining_ppl = num_ppl % num_classes

    # Create the class allocation
    allocation = {}
    for i in range(1, num_classes + 1):
        if i <= remaining_ppl:
            allocation[f'Class {i}'] = ppl_per_class + 1
        else:
            allocation[f'Class {i}'] = ppl_per_class

    # Print the proposed allocation
    print(f"Proposed Allocation: {num_classes} classes")
    print(allocation)

allocation_calculator(77)
allocation_calculator(5)
allocation_calculator(35)
