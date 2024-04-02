#!/usr/bin/env python
import pandas as pd
from Bio import SeqIO

def parse_genbank(genbank_file):
    records = SeqIO.parse(genbank_file, "genbank")
    data = []
    for record in records:
        accession = record.id
        features_count = len(record.features)
        source = record.annotations.get('source', '')
        taxonomy = record.annotations.get('taxonomy', [])
        
        # Extract family, genus, and species from the taxonomic hierarchy
        family, genus, species = "", "", ""
        if len(taxonomy) >= 4:  # Ensure there are at least 4 taxonomic levels present
            genus = taxonomy[-1]  # Last element is always genus
            species = taxonomy[-2]  # Second last element is species
            if len(taxonomy) >= 5:  # Check if family information is present
                family = taxonomy[-3]  # Third last element is family
        
        data.append([accession, family, genus, species, features_count, source])
    return data

if __name__ == "__main__":
    genbank_file = input("Enter the path to the GenBank file: ")
    
    data = parse_genbank(genbank_file)
    df = pd.DataFrame(data, columns=["Accession", "Family", "Genus", "Species", "Num_Features", "Source"])
    df.to_csv("genbank_parse.csv", index=False)
