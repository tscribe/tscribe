from Bio import SeqIO

def contains_cpg(sequence):
    """
    Check if a sequence contains CpG dinucleotides.

    Parameters:
        sequence (str): Sequence to check.

    Returns:
        bool: True if CpG dinucleotides are present, False otherwise.
    """
    cpg_count = sequence.upper().count("CG")
    return cpg_count > 0

def mine_sequence(fasta_file, output_file, max_sequences=50):
    """
    Mine a fasta file for up to 50 23-nucleotide sequences that avoid CpG islands and save the results to a text file.

    Parameters:
        fasta_file (str): Path to the FASTA file.
        output_file (str): Path to the output text file.
        max_sequences (int): Maximum number of sequences to find.
    """
    sequences_found = 0
    with open(output_file, "w") as out_file:
        with open(fasta_file, "r") as handle:
            for record in SeqIO.parse(handle, "fasta"):
                sequence = str(record.seq)
                for i in range(len(sequence) - 22):
                    subseq = sequence[i:i+23]
                    if not contains_cpg(subseq):
                        out_file.write(f"{record.description}\t{i}\t{subseq}\n")
                        sequences_found += 1
                        if sequences_found >= max_sequences:
                            return

# Example usage:
fasta_file = "C:\\Users\\AntoinetteHayes\\OneDrive - QurAlis\\Desktop\\gene.fnaCFTR"  # Update with your FASTA file path
output_file = "mined_sequences.txt"  # Update with the desired output file path

mine_sequence(fasta_file, output_file)
print(f"Mined sequences saved to {output_file}.")

