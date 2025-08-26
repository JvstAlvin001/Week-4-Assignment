# Step 1: Read from input.txt
with open("input.txt", "r") as infile:
    content = infile.read()

# Step 2: Count the number of words
word_count = len(content.split())

# Step 3: Convert text to uppercase
processed_text = content.upper()

# Step 4: Write results to output.txt
with open("output.txt", "w") as outfile:
    outfile.write("Processed Text:\n")
    outfile.write(processed_text + "\n\n")
    outfile.write(f"Word Count: {word_count}\n")

# Step 5: Print success message
print("✅ Processing complete! 'output.txt' has been created successfully.")
