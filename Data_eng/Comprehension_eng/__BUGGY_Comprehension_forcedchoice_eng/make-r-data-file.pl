#!/usr/bin/perl
system("echo \"usernum\tcond\ttimestamp\tchoice\" > data-eng-comp.txt");
system("cat data/data-*.txt | grep -v condition >> data-eng-comp.txt");

