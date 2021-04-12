#!/usr/bin/perl

use CGI qw(:standard); print "Content-type: text/html\n\n";

use strict;
use CGI;
use CGI::Carp 'fatalsToBrowser', 'croak';

my ($query,$inputdata,@params,$num,$newnum,$itemID,%item,@randitems,$seed,@stims,@lines,@targets,@randtargets,@checks,@randchecks,@practice,@randpractice,@fillers,@randfillers,@blm,@randblm,@order,$writedir,$resourcedir,$webpath,$time);


#$writedir = "."; #for eecoppock.info 
$writedir = "/shared/tattoos/output/";  #for semlab.bu.edu
$resourcedir = "/shared/tattoos/resources/";

$webpath = "http://semlab.bu.edu/tattoos/";

$query=CGI->new;  

print start_html(-title=>'Survey',
                 -style => { -src => "$webpath" . 'survey.css',
                             -type => 'text/css',
                             -media => 'screen' },
                 );
print "<div id=\"shade\">";
print "<p>&nbsp;</p>";
print "<p>&nbsp;</p>";
print "<div id=\"squarecontent\">";
print "<div id=\"pub\">";

@params = $query->param;


#read old usernum
open (USERNUMFILE, "$resourcedir" . "usernum.txt");
while (<USERNUMFILE>) {
    chomp;
    if (/([0-9]+)/) {
	$num = $1;
      } else {
	$num = 0;
      }
}
$newnum = $num + 1;
close (USERNUMFILE);

#update it
open (USERNUMFILE, ">$resourcedir" . "usernum.txt") or print "WARNING: Can't open usernum.txt";
print USERNUMFILE $newnum;
close (USERNUMFILE);

#print user data

open (USERDATAFILE, ">$writedir" . "userdata/userdata-$num.txt") or print "WARNING: Cannot open $writedir" . "userdata/userdata-$num.txt";

foreach my $paramKey (@params) {
    $inputdata = $query->param($paramKey);
    print USERDATAFILE "$num\t$paramKey\t$inputdata\n";
  }

foreach my $key ("REMOTE_ADDR","REMOTE_PORT","UNIQUE_ID","HTTP_USER_AGENT") {
   print USERDATAFILE "$num\t$key\t$ENV{$key}\n";
}

$time = localtime;

print USERDATAFILE "$num\tstarttime\t$time\n";

close (USERDATAFILE);



print "<p>&nbsp;</p>";

print "<h1>Welcome!</h1>";

print "<p>Thanks for participating!</p>
<p>Let's get started.</p>";

print "<p><b>Note</b>: There is sometimes a tendency for the server to drop the connection. If this happens, just <i>press the 'Back' button on your browser to go to the previous question</i>, and try again. It should work. Apologies for this inconvenience if it happens.</p>";


print "<form method=post action=\"display-question.cgi\">
<input type=hidden name=usernum value=$num>
<input type=hidden name=qnum value=0>
<input type=submit value=\"Begin\">
</form>";

close (USERDATAFILE);

open (STIMFILE,"$resourcedir" . "items.csv") or print "Can't find items.csv";

@lines = <STIMFILE>;


foreach my $line (@lines) {
    chomp;
    my ($type,$condition,@rest) = split(/,/,$line);
    push(@stims,"$condition");
  }

close (STIMFILE);

@order = randarray(@stims);

open (ORDERFILE,">>$resourcedir" . "order.txt") or print "Can't find $resourcedir" . "order.txt";

print ORDERFILE "$num @order\n";


close(ORDERFILE);


print "</div>";
print "</div>";
print "</div>"; 

print "</body></html>";

sub randarray {
        my @array = @_;
        my @rand = undef;
        $seed = $#array + 1;
        my $randnum = int(rand($seed));
        $rand[$randnum] = shift(@array);
        while (1) {
                my $randnum = int(rand($seed));
                if ($rand[$randnum] eq undef) {
                        $rand[$randnum] = shift(@array);
                }
                last if ($#array == -1);
        }
        return @rand;
}

