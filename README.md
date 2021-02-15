# BarabasiAlbert
# Language: Python
# Input: TXT
# Output: PREFIX
# Tested with: PluMA 1.1, Python 3.6
# Dependency: Networkx 2.2

PluMA plugin that takes as input a TXT file of tab-delimited keyword-value pairs:
faa1: FASTA file of sequences
faa2: Another FASTA file of sequences
ortholog: Tab-delimited file of mutual orthologs between faa1 and faa2

The plugin expects as output a prefix, it will then return two output files:
prefix.[argument passed to faa1]: faa1 file, with all non-orthologs removed
prefix.[argument passed to faa2]: faa2 file, with all non-orthologs removed
