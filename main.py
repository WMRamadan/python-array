array = [1, 2, 3, 4, 5, 6]

number_of_elements = 4
iterations = 7

iterations_groups = []
elements_group = []

for y in range(iterations):
    for i, x in enumerate(array):
        if len(iterations_groups) == iterations:
            break
        if len(elements_group) < number_of_elements:
            elements_group.append(x)
        else:
            iterations_groups.append(elements_group)
            elements_group = []
            elements_group.append(x)

for group in iterations_groups:
    print(group)
