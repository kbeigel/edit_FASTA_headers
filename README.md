# edit_FASTA_headers

## Description
Searches for a string in FASTA header lines (lines that begin withg '>') and replaces instances substrings with new substrings / replaces string within a regex format / finds character and removes following characters in the FASTA header lines. Outputs a new FASTA file with new FASTA headers.

## Dependencies
  re

## Pseudocode outline

    # for every line with a '>', we want to get the ID and store that as the key.
    # for every line after that line,
    # if it DOES NOT have '>', then we want to append that line to the value.
    build a dictionary
    while the file still has lines:
        look at the next line
        does this line have a carrot?
          get the ID out of the line
          store in the dictionary as the key
    while the file still has lines:
      look at the next line
      does this line not have a carrot?
        tack on line to the value associated with the key
    else stop