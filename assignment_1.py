
import argparse
import sys
from Bio import SeqIO

parser = argparse.ArgumentParser(
    description = "Convert fastq sequencing reads to fasta and generate a .vcf file which records positions of bases in reads that do not match the corresponding position in the reference sequence."
)
##following arguments will be stored for use when parse_args() is employed.
#parse args will later refer to the command line and convert each file to the appropriate object
parser.add_argument("--reads", dest = "reads", help = "sequencing reads aligned to reference genome (fastq)", required = True)#required = True requires files to be specified before use of the code
parser.add_argument("--reference", dest = "reference", help = "reference genome (fasta)", required = True)
parser.add_argument("--outstem",  dest= "outstem", help = "name specified for output files", required = True)

#Defining the function:
def find_differences(reference, read):
    """This function will create a list containing information on bases in read sequences that do not match the
    corresponding base in the reference sequence. It will list the position, the name of the sequence at which
    the variation occurs, the base in the reference genome, and the base in the sequencing read"""
    results = list() #empty list is created to append results of following code
    #if bases in the read sequence do not match the reference genome, location and base changes will be recorded
    for i, base in enumerate(reference):
        if base.upper() != read[i].upper():#finding bases in reads that do not match base of reference at the corresponding position
            #code abive ensures sequences are compared in uppercase
            results.append([i, read.id, base, read[i].upper()])#bases will be recorded as uppercase
            #results will show location of the base mismatch, the bases, and read id of the sequence harbouring the mismatch,
    return(results) #ends execution of the function

if __name__ == "__main__": #when reading the source file, "__main__" will be assigned as __name__ variable
    #assigning files to be used in the function above
    args = parser.parse_args()
    reads = SeqIO.parse(args.reads, "fastq")
    try:
        ref = SeqIO.read(args.reference, "fasta")
    except ValueError:
        print("Reference sequence must be in FASTA format")
        sys.exit(1) #ValueError will be raised if reference sequence is not in correct format.   
    differences = list() #empty list created to append results.
    for read in reads:
        differences += find_differences(ref, read) # a list of a list is created to avoid nesting of results

##Generating the output files:
    with open(args.outstem + ".vcf",  "w") as outstem: #write outstem as a vcf file
        outstem.write("CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\n") #generating .vcf format headings
        diff = sorted(differences) # differences in bases are sorted in ascending order by location of base
        for res in diff: 
            outstem.write("{}\t{}\t.\t{}\t{}\t.\t.\n".format(ref.id, res[0], res[2], res[3])) #data from input files will be assigned to their relevant position in output files
        SeqIO.convert(args.reads, "fastq", args.outstem + ".fna", "fasta") #convert fastq read sequences to fasta and save as an output file.
    sys.exit(0) #exit without errors
