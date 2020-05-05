# The following function should take a string and a sub-string and return 
# a list of starting positions for the substring

def get_sub_position(search_string, needle):
    index=[]
    for i in range(len(search_string)):
        if search_string.startswith(needle, i) :
            index.append(i)

    return index