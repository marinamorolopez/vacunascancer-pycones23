# vacunascancer-pycones23
This repository includes the slides of the public presentation 'Diseño de vacunas contra el cáncer con Python' of the PyConES23 and both the code and files used for the practical case.

## Installation
You simply have to download the .py and fasta files (or get your own fasta files from a database as [NCBI](https://www.ncbi.nlm.nih.gov/)).

## Usage
First you'll have to select the file of your gene of interest. Then introduce the mutation type (knock-in or knock-out) as in/out. If case of a knock-in, you'll have to specify if the DNA change is a single-base modification or a whole-gene insertion. In case of a knock-in of a single base, you'll have to introduce the position of the mutation (as a positive integer) and the new base in that position (as a single upper case letter among A/T/C/G). In case of a knock-in of a whole gene, you'll have to select the file of the gene of interest. When finished, you'll have three .txt files saved in the same folder of the .py file with the RNA guide, the DNA mold and the mutated sequence.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
