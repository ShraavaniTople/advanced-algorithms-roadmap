import sys
import platform
from datetime import datetime

print("Python version:", sys.version)
print("Platform:", platform.platform())
print("Current date and time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

arr = [2, 4, 1, 3, 5]
inversions = sum(1 for i in range(len(arr)) for j in range(i+1, len(arr)) if arr[i] > arr[j])
print("Sample array:", arr)
print("Inversion count:", inversions)
