def dna_to_rna(dna):
    """
    Ribonucleic acid, RNA, is the primary messenger molecule 
    in cells. RNA differs slightly from DNA its chemical 
    structure and contains no Thymine. In RNA Thymine is 
    replaced by another nucleic acid Uracil ('U').
    
    Create a function which translates a given DNA string into RNA.
    For example: "GCAT"  =>  "GCAU"
    """
    result = ""
    for i in dna:
        if 'T' in i:
            result += 'U'
        else:
            result += i
    return result

print(dna_to_rna("TTTT"))