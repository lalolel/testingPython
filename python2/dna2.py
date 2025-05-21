# Step 1: The sample codons retrieved from the computer's keyboard
sample = ["GTA", "GGG", "CAG"]

# Step 3: Method to read DNA from a file and return it as a string
def read_dna(dna_file):
    # Step 4: Create an empty string to store the DNA data
    dna_data = ""
    
    # Step 5: Open the DNA file in read-only mode
    with open(dna_file, "r") as f:
        # Step 6: Iterate through each line in the file
        for line in f:
            # Step 7: Add each line to the dna_data string
            dna_data += line
    
    # Step 8: Return the complete DNA string
    return dna_data

# Step 10: Method to split a DNA string into codons (3-letter units)
def dna_codons(dna):
    # Step 11: Create an empty list to store the codons
    codons = []
    
    # Step 12: Iterate through the DNA string in increments of 3
    for i in range(0, len(dna), 3):
        # Step 13: Check if there are at least 3 more characters left in the DNA string
        if i + 3 <= len(dna):
            # Step 14: Add the current 3-letter codon to the list
            codons.append(dna[i:i+3])
    
    # Step 15: Return the list of codons
    return codons

# Step 16: Method to count matches between sample codons and suspect's DNA
def match_dna(dna):
    # Step 17: Initialize the match counter
    matches = 0
    
    # Step 18: Iterate through each codon in the suspect's DNA
    for codon in dna:
        # Step 19: Check if the current codon is in the sample list
        if codon in sample:
            # Step 20: If there's a match, increment the counter
            matches += 1
    
    # Step 21: Return the total number of matches
    return matches

# Step 22: Method to determine if a suspect is the criminal
def is_criminal(dna_sample):
    # Step 23: Read the DNA data from the file
    dna_data = read_dna(dna_sample)
    
    # Step 24: Convert the DNA string into a list of codons
    codons = dna_codons(dna_data)
    
    # Step 25: Count how many codons from the sample match the suspect's DNA
    num_matches = match_dna(codons)
    
    # Step 26: Check if the number of matches is significant (3 or more)
    if num_matches >= 3:
        # Step 27: Print the number of matches and indicate this suspect should be investigated
        print("%s matches found. Investigation should continue." % num_matches)
    else:
        # Step 28: Print the number of matches and indicate this suspect can be freed
        print("%s matches found. Suspect can be freed." % num_matches)

# Step 29: Call the is_criminal method on each suspect's DNA file
is_criminal("suspect1.txt")
is_criminal("suspect2.txt")
is_criminal("suspect3.txt")
