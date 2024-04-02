#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 10:49:36 2024

@author: surangijayasinghe
"""

#!/usr/bin/env python
import csv
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

def count_occurrences(sequence, subsequence):
    return sequence.upper().count(subsequence.upper())

def reverse_complement(sequence):
    return sequence.reverse_complement()

def analyze_genome(fasta_file):
    for record in SeqIO.parse(fasta_file, "fasta"):
        length_of_genome = len(record.seq)
        gc_content = gc_fraction(record.seq)
        forward_strand_count = count_occurrences(record.seq, 'ATG')
        reverse_strand_count = count_occurrences(reverse_complement(record.seq), 'ATG')
        return length_of_genome, gc_content, forward_strand_count, reverse_strand_count

def write_to_csv(data, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Length_of_genome", "GC_content", "ATG_forward", "ATG_reverse"])
        writer.writerow(data)

if __name__ == "__main__":
    fasta_file = "GCA_000287275.1.fasta"
    output_file = "ruddi.csv"

    analysis_result = analyze_genome(fasta_file)
    write_to_csv(analysis_result, output_file)
