dna = input("Enter DNA sequence: ").upper()

print("\n--- DNA Analysis ---")
print("Length:", len(dna))
print("A:", dna.count("A"))
print("T:", dna.count("T"))
print("G:", dna.count("G"))
print("C:", dna.count("C"))

gc = dna.count("G") + dna.count("C")
gc_content = (gc / len(dna)) * 100

print("GC Content: {:.2f}%".format(gc_content))