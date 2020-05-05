# The following method should take a strand as an argument and
# return a complementary strand

def complementary(strand):
    base =['A','T','C','G']
    complement  =['T','A','G','C']
    dna=""
    for i in (strand):
        dna=dna+(complement[base.index(i)]) 
        
    return dna