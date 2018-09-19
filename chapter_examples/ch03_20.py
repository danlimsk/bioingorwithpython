### Example 3-20: Reading FASTA descriptions using set comprehension

def get_FASTA_codes(filename):
    with open(filename) as file:
        return {line.split('|')[2] for line in file
                if line[0] == '>' and len(line.split('|')) > 2}

print(get_FASTA_codes('../data/BacillusSubtilisPlastmidP1414.fasta'))
