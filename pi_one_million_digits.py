import mpmath
from pathlib import Path

filename = "one_million_digits.txt"

# Set the precision (number of digits)
mpmath.mp.dps = 1000000  # 1 million digits after the decimal point

# Calculate pi
pi = mpmath.pi
# Print the first 10 digits as a quick check
print(str(pi)[:10])

# Convert π to a string
pi_str = str(pi)

Path(filename).write_text(pi_str)