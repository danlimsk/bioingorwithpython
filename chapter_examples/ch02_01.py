### Example 02-01: A simple function for recognizing a binding site

def recognition_site(base_seq, recognition_seq):
    return base_seq.find(recognition_seq)
    
