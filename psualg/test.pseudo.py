# Lists are of length N, storing it in a variable helps keep track
N = length[A]
# Carry is 0 or 1 for each bit based on the previous
carry = 0
# Start at last bit (1s place), work towards first bit (2^(N-1)s place)
# (Loop step is -1 rather than the standard +1)
for i in range(N-1,0):
    # Add the two bits and any carry from the previous addition
    do  C[i+1] = A[i] + B[i] + carry
        # If a single bits value is greater than 1, add 1 to carry on to the
        # next addition, and subtract 2 from the bit. (value won't exceed 3)
        if C[i+1] > 1
            do  carry = 1
                C[i+1] = C[i+1] - 2
        # If the added bit is 0 or 1, no need to carry. Reset carry to 0.
        else
            do  carry = 0
# Assign the first bit the remaining carry value
C[0] = carry
