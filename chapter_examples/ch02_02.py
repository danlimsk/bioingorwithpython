### Example 02-02: Some function definition details

def validate_base_sequence(base_sequence): 
    seq = base_sequence.upper() 
    return len(seq) == (seq.count('T') + seq.count('C') + 
                        seq.count('A') + seq.count('G')) 
