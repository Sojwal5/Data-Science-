import numpy as np
import matplotlib.pyplot as plt

# Function to take a 4x4 binary matrix input from the user
def get_matrix_input():
    print("Enter elements of a 4x4 binary matrix (0s and 1s):")
    matrix = []
    for i in range(4):
        while True:
            try:
                row = list(map(int, input().split()))  # Splitting user input by space and converting to integers
                if len(row) != 4:  # Checking if the row has exactly 4 elements
                    raise ValueError("Please enter 4 binary numbers (0 or 1) separated by space for each row.")
                if not all(num in [0, 1] for num in row):  # Checking if all elements are either 0 or 1
                    raise ValueError("Please enter valid binary values (0 or 1) separated by space for each row.")
                matrix.append(row)  # Appending the valid row to the matrix
                break
            except ValueError as e:
                print(f"Error: {e}")
                print("Please enter valid binary values (0 or 1) separated by space for each row.")
    return np.array(matrix)  # Converting the matrix list into a numpy array

# Get the input binary matrix from the user
binary_matrix = get_matrix_input()

# Compute the 2D DFT
dft_matrix = np.fft.fft2(binary_matrix)  # Calculating the 2D DFT of the binary matrix
# Print the result
print("2D DFT of the binary matrix:")
print(dft_matrix)

# Plotting the binary image
plt.subplot(1, 2, 1)
plt.imshow(binary_matrix, cmap='gray')
plt.title('Binary Image')
plt.axis('off')  # Removing axis for better visualization

# Plotting the magnitude spectrum of the DFT
plt.subplot(1, 2, 2)
plt.imshow(np.abs(dft_matrix), cmap='gray')
plt.title('Magnitude Spectrum of 2D DFT')
plt.axis('off')  # Removing axis for better visualization

# Displaying the plots
plt.tight_layout()  # Adjusting layout to prevent overlap
plt.show()
