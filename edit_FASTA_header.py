import re

if __name__ == '__main__':
    ## the infile name goes here, as a string in open()
    infile = open('Ta_Ef1a_complete_genbank.fasta', 'r')

    # for every line with a '>', we want to get the ID and store that as the key.
    # for every line after that line,
    # if it DOES NOT have '>', then we want to append that line to the value.
    # if it does have '>', we want to stop.

    fasta_dict = {}

    # while the file still has lines:
    # look at the next line
    # does this line have a carrot?
    # get the ID out of the line
    # store in the dictionary as the key
    # while the file still has lines
    # look at the next line
    # does this line not have a carrot?
    # tack on line to the value associated with the key
    # else stop

    # currentLine = next(infile, "STOP").strip()
    # while currentLine != "STOP":
    #     if currentLine.startswith('>'):
    #         fastaHeader = currentLine[1:]
    #         fasta_dict[fastaHeader] = ''
    #         currentLine = next(infile, "STOP").strip()
    #         while currentLine != "STOP":
    #             if not currentLine.startswith('>'):
    #                 fasta_dict[fastaHeader] = fasta_dict[fastaHeader] + currentLine
    #                 #print(fasta_dict)
    #                 currentLine = next(infile, "STOP").strip()
    #                 #print(currentLine)
    #             else:
    #                 break

    previous_key = ''
    for current_line in infile.readlines():
        if current_line.startswith('>'):
            previous_key = current_line.strip()
            fasta_dict[previous_key] = ''
        else:
            fasta_dict[previous_key] += current_line.strip()

    out_fasta_dict = {}
    index = 1
    for key, value in fasta_dict.items():
        # alternate method
        # key = fasta_tuple[0]
        # value = fasta_tuple[1]
        key = key.replace('-', '')
        key = key.replace('>', '')
        # key = key.replace('|revcompl', '')
        match = re.search(r'[A-Za-z]+(?P<WiW>[0-9]{7})', key)
        if match is not None:
            print(match)
        key = key.replace(key, '[organism=Trachymyrmex arizonensis]' + ' wingless (wnt-1) gene, partial cds')
        key = '>Seq' + str(index) + ' ' + key
        index = index + 1

        # my first two lines by myself
        # char_position = key.find('T')
        # key = key[0:char_position]
        out_fasta_dict[key] = value
        # new_key = key.split('_')[0]

    # for key, value in out_fasta_dict.items():
    #    if 'ITS' in key:
    #        continue
    #    else:
    #        key = key + 'ITS'

    new_file_name = 'Ta_Ef1a_complete_genbank_upload.fasta'
    outfile = open(new_file_name, 'w')
    # for key, value in out_fasta_dict:
    #    outfile.write(key)

    # same as above, less 'pythonic'
    for key, value in out_fasta_dict.items():
        outfile.write(key)
        outfile.write('\n')
        outfile.write(value)
        outfile.write('\n')
