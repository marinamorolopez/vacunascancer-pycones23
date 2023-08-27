# -*- coding: utf-8 -*-

"""

Created on Tue Feb 28 20:20:55 2023
@author: Marina Moro López

"""

from tkinter.filedialog import askopenfile

def main():
    
    print('Select the FASTA file of the gene of interest for CRISPR.')
    gene_file = askopenfile(mode='r')
    gene_seq = gene_file.readlines()[1:]
    gene_seq = ''.join(gene_seq).replace('\n', '')

    mutation_type = input("Introduce mutation type (in/out): ")
    
    while mutation_type != 'in' and mutation_type != 'out':
        print('Invalid input.')
        mutation_type = input("Introduce mutation type (in/out): ")
    
    if mutation_type == "in":
        
        knockin_type = input("Introduce the knock-in position in the gene (single/gene): ")
        while knockin_type != 'single' and knockin_type != 'gene':
            print('Invalid input.')
            knockin_type = input("Introduce the knock-in position in the gene (single/gene): ")
            
        if knockin_type == "single":
            DNA_guide, mutated_gene_seq, mold = knock_in_single(gene_seq)
        elif knockin_type == "gene":
            DNA_guide, mutated_gene_seq, mold = knock_in_gene(gene_seq)
            
    else:
        DNA_guide, mutated_gene_seq, mold = knock_out(gene_seq)

    mutated_gene_file = open('MUTATED_SEQUENCE.txt', 'w')
    mutated_gene_file.write(mutated_gene_seq)
    mutated_gene_file.close()

    guide_file = open('GUIDE.txt', 'w')
    guide_file.write(DNA_to_RNA(DNA_guide))
    guide_file.close()

    mold_file = open('MOLD.txt', 'w')
    mold_file.write(mold)
    mold_file.close()


def knock_in_single(gene_seq):
    
    mutation_position = int(input("Introduce the numeric position of the knock-in base (e.g. 1, 25, 203): "))
    while mutation_position <= 0:
        print('Invalid input. Introduce positive integer. ')
        mutation_position = int(input("Introduce the numeric position of the knock-in base (e.g. 1, 25, 203): "))
    
    mutation_base = input("Introduce the new base corresponding to the defined knock-in position in upper case (A/T/G/C): ")
    while mutation_base != 'A' and mutation_base != 'T' and mutation_base != 'G' and mutation_base != 'C':
        print('Invalid input. ')
        mutation_base = input("Introduce the new base corresponding to the defined knock-in position (A/T/G/C): ")
            
    DNA_guide = gene_seq[mutation_position-25:mutation_position+25]
    mutated_gene_seq = gene_seq[:mutation_position-1] + mutation_base + gene_seq[mutation_position:]
    mold = mutated_gene_seq[mutation_position-25:mutation_position+25]
    
    return DNA_guide, mutated_gene_seq, mold


def knock_in_gene(gene_seq):

    mutation_position = int(input("Introduce the numeric position of the knock-in base (e.g. 1, 25, 203): "))
    while mutation_position <= 0:
        print('Invalid input. Introduce positive integer. ')
        mutation_position = int(input("Introduce the numeric position of the knock-in base (e.g. 1, 25, 203): "))
            
    print('Select the FASTA file of the knock-in gene.')
    gene_add_file = askopenfile(mode='r')
    gene_add_seq = gene_add_file.readlines()[1:]
    gene_add_seq = ''.join(gene_add_seq).replace('\n', '')
    
    DNA_guide = gene_seq[mutation_position-10:mutation_position+10]
    mold = DNA_guide[:10] + gene_add_seq + DNA_guide[10:]
    mutated_gene_seq = gene_seq[:mutation_position] + gene_add_seq + gene_seq[mutation_position:]
    
    return DNA_guide, mutated_gene_seq, mold


def knock_out(gene_seq):
    
    mutation_position_ini = int(input("Introduce the numeric position of the initial knock-out base (e.g. 1, 25, 203): "))
    while mutation_position_ini <= 0:
        print('Invalid input. Introduce positive integer. ')
        mutation_position_ini = int(input("Introduce the numeric position of the initial knock-out base (e.g. 1, 25, 203): "))
    
    mutation_position_fin = int(input("Introduce the numeric position of the final knock-out base (e.g. 1, 25, 203): "))
    while mutation_position_fin <= 0:
        print('Invalid input. Introduce positive integer. ')
        mutation_position_fin = int(input("Introduce the numeric position of the final knock-out base (e.g. 1, 25, 203): "))
            
    DNA_guide = gene_seq[mutation_position_ini-1:mutation_position_fin]
    mutated_gene_seq = gene_seq[:mutation_position_ini-1] + gene_seq[mutation_position_fin:]
    mold = ""
    
    return DNA_guide, mutated_gene_seq, mold


def DNA_to_RNA(DNA_guide):
    
    RNA_guide = ""
    for base in DNA_guide:
        if base == "T":
            RNA_guide += "A"
        elif base == "A":
            RNA_guide += "U"
        elif base == "C":
            RNA_guide += "G"
        elif base == "G":
            RNA_guide += "C"
    
    return RNA_guide


main()