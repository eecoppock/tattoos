#!/usr/bin/perl
system("echo \"usernum\tcond\ttimestamp\tleftright\torder\texpected\tchoice\" > data-spa-comp.txt");
system("cat data/data-*.txt >> data-spa-comp.txt");

