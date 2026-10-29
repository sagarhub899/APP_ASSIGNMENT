
# Experiment No. 8: File Handling

try:
    # Read the input file
    with open("input.txt", "r") as file:
        lines = file.readlines()

    # Count total lines
    line_count = len(lines)
    print("Total number of lines:", line_count)

    # Extract first two lines
    first_two_lines = lines[:2]

    print("\nFirst two lines:")
    for line in first_two_lines:
        print(line.strip())

    # Write the extracted lines to output.txt
    with open("output.txt", "w") as file:
        file.writelines(first_two_lines)

    print("\nFirst two lines have been written to output.txt")

except FileNotFoundError:
    print("Error: input.txt not found. Create it in the same folder as your Python program.")

except OSError as e:
    print("File handling error:", e)
