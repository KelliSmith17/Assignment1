_16/6/2020_


_**Assignment 2 summary**_



**New reference sequence** 


The expected input from the previous task was a reference sequence in FASTA format, however, the new reference sequence is in GenBank format. The program has been modified to print an error message stating the reference sequence must be in FASTA format. 
[Commit code: a5ed096e90b5c3480b86cdbc06aab6a507b3cdcf](https://github.com/kellismith17/assignment1/commit/a5ed096e90b5c3480b86cdbc06aab6a507b3cdcf)
 
 
**New read 1**


The quality score and read sequence differ in length, rendering it an invalid fastQ file. As the default BioPython error clearly states this issue, this was retained and no changes were made to the program. 


**New read 2**


The new sequence differed from the expected input of the last task by giving the read sequence in lowercase. As the reference sequence is given in uppercase, case differences were recorded as mutations. As a solution, the program has been modified to convert and compare sequences in uppercase.
[Commit code: fd6a22d6af9f5ab4f6d4b2d5a7afcc0fb31edc80](https://github.com/kellismith17/assignment1/commit/fd6a22d6af9f5ab4f6d4b2d5a7afcc0fb31edc80)


**New read 3**


Previously, the expected inputs harboured only one mutation. The new sequence has no mutations and is identical to the reference sequence. The programme was able to successfully output an empty list, thus, no changes were made to the program and documentation. 


**New read 4**


The read contained multiple base mutations. As the program was able to successfully find and record all mutations, no changes were made to the program or documentation. 


**New read 5**


The expected input of the previous task was reads and reference sequences of the same length. The new read differed in length to the new reference sequence, thus the program has been modified to raise a ValueError stating reference and read sequence must be the same length. 
[Commit code: 6891ef7f0cf67f3cf509716097d582bd14defca3](https://github.com/KelliSmith17/Assignment1/commit/6891ef7f0cf67f3cf509716097d582bd14defca3)

**New read 6**


This read differed from expected input as it harbours an ambiguous N base. The program has been modified to print a warning stating that the N base will be skipped. 
[Commit code: 524e7cb7330aa3d929b5f0df39882a93cbd6e49e](https://github.com/kellismith17/assignment1/commit/524e7cb7330aa3d929b5f0df39882a93cbd6e49e)
