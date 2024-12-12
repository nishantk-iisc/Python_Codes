# The Equilibrium index of an array is an index where the sum of the elements on the left of the index is equal to the sum of right of the elements on the right side.

def find_equilibrium_index(arr):
    total_sum = sum(arr)
    left_sum = 0

    for i, num in enumerate(arr):
        total_sum -= num

        if left_sum == total_sum:
            return i

        left_sum += num

    return -1

# Example Usage
arr = [1, 3, 5, 2, 2]
equilibrium_index = find_equilibrium_index(arr)
print(f"Equilibrium Index: {equilibrium_index}")
