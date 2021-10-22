#!/usr/bin/perl
system("echo \"usernum\tcond\ttimestamp\tleftright\torder\texpected\tchoice\" > data-eng-comp.txt");
system("cat data/data-*.txt >> data-eng-comp.txt");

