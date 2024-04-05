#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 10:29:23 2024

@author: surangijayasinghe
"""

#!/usr/bin/env python
import csv
from Bio import SeqIO

def count_cysteines(sequence):
    return sequence.count('C')

def extract_protein_info(fasta_file):
    protein_info = []
    for record in SeqIO.parse(fasta_file, "fasta"):
        fasta_id = record.id
        sequence = str(record.seq)
        first_10_aa = sequence[:10]
        length = len(sequence)
        cysteines = count_cysteines(sequence)
        protein_info.append([fasta_id, first_10_aa, length, cysteines])
    return protein_info

def write_to_csv(data, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["ID", "First_10_AA", "Length", "Num_Cysteines"])
        writer.writerows(data)

if __name__ == "__main__":
    fasta_files = ["AGI40145.1.fasta", "AGJ87295.1.fasta", "WVV45440.1.fasta", "WVS05366.1.fasta"]
    output_file = "protein_info.csv"
    all_protein_info = []

    for fasta_file in fasta_files:
        protein_info = extract_protein_info(fasta_file)
        all_protein_info.extend(protein_info)

    write_to_csv(all_protein_info, output_file)
