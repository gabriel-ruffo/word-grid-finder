# word-grid-finder
A small program that finds all possible words within any n*n grid of letters.

Store file containing comma separated letters in a grid in src/main/files/ and run src/main/python/runner.py.

Example file:  
a,b,c  
d,e,f  
g,h,i  

Program will output list of found words along with their lengths ordered from greatest to least amount of letters.

Example output:  
badge|5, abed|4, bade|4, bead|4, defi|4, fied|4, head|4, hied|4, abc|3, abd|3, abe|3, ade|3, bad|3, bae|3, bcf|3, bde|3,  
bea|3, bec|3, bed|3, bef|3, beg|3, cfh|3, cfi|3, dab|3, dae|3, dea|3, deb|3, dec|3, def|3, deg|3, dei|3, ead|3, ecb|3,  
edh|3, fec|3, fed|3, feh|3, fei|3, fie|3, geb|3, ged|3, ghi|3, hed|3, hei|3, hie|3, ife|3  

NOTE: Uses words from dwyl's word dictionary: https://github.com/dwyl/english-words/blob/master/words_dictionary.json
