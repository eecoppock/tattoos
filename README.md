# tattoos
Data and code for "Differences in implicature across languages stem from differences in salience of alternatives"

Data for the project is divided by language. There are five data folders. Each contains both production and comprehension data.

/Data_eng (English) -- this folder also contains example pre-processing scripts (make-r-data-file.pl and remove-nonfinal-answers.pl) that were used to convert the raw data into the data file that was imported into R. Similar scripts were used for all five languages.

/Data_spa (Spanish)

/Data_ru (Russian)

/Data_per (Persian)

/Data_ar (Arabic)

All data is anonymized. The participant IDs in the production data are encrypted.

The R analysis code is in

/R-Code/tattoo_crosslx.R

The WebPPL code for the RSA models is in 

/Modelling/model.wppl

The HTML/Perl-CGI code for running the comprehension experiments is under:

/WebCode

This directory contains the Perl/CGI scripts and associated resources that were used to run the comprehension studies in all five languages. The scripts directories contain CGI scripts and associated files that were placed in a web-readable directory on the server. The resources directories contain files that the scripts reference. The output directories are not included in the public repository.

Warning: There are some server-specific pathnames in this code.

This directory also contains the images that were used in the production studies.
