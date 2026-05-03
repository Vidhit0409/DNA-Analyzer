
dna = input("Enter DNA sequence: ").upper()

# Validate input
if not all(base in "ATGC" for base in dna):
    print("Invalid DNA sequence!")
    exit()

print("\n--- DNA ANALYSIS REPORT ---")

# Basic analysis
print("Length:", len(dna))
print("A:", dna.count("A"), "| T:", dna.count("T"), "| G:", dna.count("G"), "| C:", dna.count("C"))

gc = dna.count("G") + dna.count("C")
gc_content = (gc / len(dna)) * 100
print("GC Content: {:.2f}%".format(gc_content))

# RNA conversion
rna = dna.replace("T", "U")
print("RNA Sequence:", rna)

# Reverse complement
complement = {"A":"T", "T":"A", "G":"C", "C":"G"}
reverse_complement = "".join([complement[base] for base in dna[::-1]])
print("Reverse Complement:", reverse_complement)

# Codon splitting
codons = [dna[i:i+3] for i in range(0, len(dna), 3)]
print("Codons:", codons)
