#!/bin/python

# Import libraries
import re

################## MAIN ###################

if __name__ == '__main__':


    # INPUT FILE
    # the infile name goes here, as a string in open()
    infile = open('Ta_Ef1a_complete_genbank.fasta', 'r')


    # COLLECT HEADERS
    # make a dictionary (ID will be keys and sequences will be values)
    fasta_dict = {}

    # Collect header lines in the FASTA file
    original_key = ''
    for current_line in infile.readlines():
        # if the line starts with '>'
        if current_line.startswith('>'):
            # key is the line, with leading and trailing chars removed
            original_key = current_line.strip()
            # store key in dictionary
            fasta_dict[original_key] = ''
        # if the line does not start with '>'
        else:
            # remove trailing and leading whitespace, store as value for preceding line
            fasta_dict[original_key] += current_line.strip()


    # MAKE CHANGES / REPLACEMENTS TO HEADERS; OUTPUT EDITED HEADERS
    # initialize a dictionary to store the output (edited) headers
    out_fasta_dict = {}

    # start index
    index = 1 # use this if you want to number headers sequentially in file

    # for each key-value pair in dictionary, do replacements,
    # loop has some options for replacements (can use all or some)
    for key, value in fasta_dict.items():
        
        # 1. use specify strings to replace and replacements
        key = key.replace('-', '')
        key = key.replace('text_to_remove', '')

        # 2. use to specify regex pattern to find
        match = re.search(r'[A-Za-z]+(?P<WiW>[0-9]{7})', key)
        # if regex pattern is found
        if match is not None:
            # update key with replacement string
            key = key.replace(key, 'additional_text_to_add')
            # update key to have 
            key = 'Seq' + str(index) + '_' + key # elements can be reordered 
            index += 1 # increment index (use if you want to add numbers)

        # 3. remove everything after a certain character
        char_position = key.find('C') # find first instance of char in line
        # update key to be string from beginnning to searched char
        key = key[0:char_position]

        # output the updated keys to output dict 
        # (using value (sequence) from previous dict)
        out_fasta_dict[key] = value


    # WRITE TO A NEW FILE
    # specify a new file name
    new_file_name = 'Ta_Ef1a_complete_genbank_upload.fasta'


    # write a new file using the new file name
    outfile = open(new_file_name, 'w')
     for key, value in out_fasta_dict:
        outfile.write(key)