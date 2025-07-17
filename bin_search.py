# This script demonstrates the algorithm for binary search function

target_array1 = [2, 4, 6, 8, 15, 20, 25]
target_array2 = [1, 3, 5, 7, 9, 11, 13]
target_array3 = [10, 20, 30, 40, 50, 60, 70]

def binary_search(arr, target):
    # Initialize low and high pointers
    low = 0
    high = len(arr) - 1 
    
    while low <= high:
        median = (low + high) // 2
        
        if arr[median] == target:
            return True
        
        if arr[median] < target:
            low = median + 1
        else:
            high = median - 1
    return False

def main(): 
    target_num = 8
    print(f"Is {target_num} in the array {target_array1}? {binary_search(target_array1, target_num)}")
    
    target_num = 9
    print(f"Is {target_num} in the array {target_array2}? {binary_search(target_array2, target_num)}")
    
    target_num = 35
    print(f"Is {target_num} in the array {target_array3}? {binary_search(target_array3, target_num)}")

if __name__ == "__main__":
    main()
