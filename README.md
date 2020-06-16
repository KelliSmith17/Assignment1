# Assignment1
Code for Special Topic assignment 1

assignment_1.py can be used to assess base differences between a reference genome and aligned sequencing reads. The sequence name, variation location, and base changes will be recorded. 

## Prerequisites 

`Biopython` is required to run the software. 

The `pytest` module is required to run the set of tests that come with the software. 

## Usage:

assignment_1.py can be called from command line using the following script:

`python assignment_1.py --reads reads.fq --reference reference.fna --outstem outstem`
  
  where `reads.fq` and `reference.fna` are the user-specified sequencing reads and reference sequence in fastq and fasta format, respectively. The outstem specified in command line will be assigned as output file name. 
  
  ## Input:
  Input files specified at command line should be a reference genome sequence in fasta format, and sequencing reads aligned to the reference genome in fastq format.
  
  ## Output:
  Two output files will be created. An .fna file will contain the original sequencing reads that have been converted to fasta format. The VCF output file will provide information on the name of the sequence (CHROM) which harbours a variation between the reference sequence and read sequence, the position of the base at which the variation occurs (POS), the reference base (REF) and base of the new read at the corresponding position (ALT). 
  While the VCF output file will also contain QUAL, FILTER, and ID columns, due to the nature of the input data, this information will not be recorded. 
