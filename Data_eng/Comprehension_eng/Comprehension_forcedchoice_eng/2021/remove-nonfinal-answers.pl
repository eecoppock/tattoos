#!/usr/bin/perl

$file = $ARGV[0];

open (FILE,$file);

while (<FILE>) {
  ($usernum,$cond,@vals) = split(/\t/);
  unless ($data{$usernum}{$cond}==1) {
    print $_;
  }
  $data{$usernum}{$cond} = 1;
}
close(FILE);
