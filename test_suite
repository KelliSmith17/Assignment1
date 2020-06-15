from assignment_2 import find_differences
from Bio import SeqIO
import warnings
import pytest

ref = SeqIO.read("test/reference.fna", format = "fasta")

class TestVariants:
    def test_call_one(self):
        read = SeqIO.read("test/one_mutation.fq", "fastq")
        res = find_differences(ref, read)
        assert res == [[70, 'agoPnkEt', 'A', 'T']] #this is the expected output of the function using one_mutation.fq.  
        #if the output differs, the test will fail. 
        
    
    def test_call_none(self):
        read = SeqIO.read("test/none.fq", "fastq")
        res = find_differences(ref, read)
        assert res == [] #empty list expected, and is required to pass the test
        
    def test_lengths_match(self):
        read = SeqIO.read("test/lengths_match.fq", "fastq")
        with pytest.raises(ValueError, match = "length of read sequence*"): 
            res = find_differences(ref, read) #expects an error starting with "length of read sequence" when unmatched lengths are used in function
        
    def test_warn_on_N(self):

        read = SeqIO.read("test/warn_on_N.fq", "fastq")
        with pytest.warns(None) as warnings: #create object called warnings using code below. 
            find_differences(ref, read)
        assert len(warnings) == 1 #expects one warning. 

        
