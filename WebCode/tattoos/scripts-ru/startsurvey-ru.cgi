#!/usr/bin/perl

use CGI qw(:standard); print "Content-type: text/html\n\n";

use strict;
use CGI;
use CGI::Carp 'fatalsToBrowser', 'croak';

my ($query,$inputdata,@params,$num,$newnum,$itemID,%item,@randitems,$seed,@stims,@lines,@targets,@randtargets,@checks,@randchecks,@practice,@randpractice,@fillers,@randfillers,@blm,@randblm,@order,$writedir,$resourcedir,$webpath,$time);


#$writedir = "."; #for eecoppock.info 
$writedir = "/shared/tattoos/output-ru/";  #for semlab.bu.edu
$resourcedir = "/shared/tattoos/resources-ru/";

$webpath = "http://semlab.bu.edu/tattoos-ru/";

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

print "<h1>&#1044;&#1086;&#1073;&#1088;&#1086; &#1055;&#1086;&#1078;&#1072;&#1083;&#1086;&#1074;&#1072;&#1090;&#1100;!</h1>";

print "<p>&iexcl;&#1057;&#1087;&#1072;&#1089;&#1080;&#1073;&#1086; &#1079;&#1072; &#1042;&#1072;&#1096;&#1077; &#1091;&#1095;&#1072;&#1089;&#1090;&#1080;&#1077; &#1074; &#1085;&#1072;&#1096;&#1077;&#1084; &#1080;&#1089;&#1089;&#1083;&#1077;&#1076;&#1086;&#1074;&#1072;&#1085;&#1080;&#1080;!</p>";

print "<p><b>&#1047;&#1072;&#1084;&#1077;&#1090;&#1082;&#1072;</b>: &#1059; &#1101;&#1090;&#1086;&#1075;&#1086; &#1089;&#1077;&#1088;&#1074;&#1077;&#1088;&#1072; &#1073;&#1099;&#1074;&#1072;&#1077;&#1090;, &#1095;&#1090;&#1086; &#1089;&#1074;&#1103;&#1079;&#1100; &#1087;&#1088;&#1077;&#1088;&#1099;&#1074;&#1072;&#1077;&#1090;&#1089;&#1103;. &#1045;&#1089;&#1083;&#1080; &#1101;&#1090;&#1086; &#1089;&#1083;&#1091;&#1095;&#1080;&#1090;&#1089;&#1103;, &#1042;&#1099; &#1084;&#1086;&#1078;&#1077;&#1090;&#1077; &#1087;&#1088;&#1086;&#1089;&#1090;&#1086; &#1085;&#1072;&#1078;&#1072;&#1090;&#1100; &#1082;&#1085;&#1086;&#1087;&#1082;&#1091; &laquo;&#1053;&#1072;&#1079;&#1072;&#1076;&raquo; &#1074; &#1042;&#1072;&#1096;&#1077;&#1084; &#1073;&#1088;&#1072;&#1091;&#1079;&#1077;&#1088;&#1077;, &#1095;&#1090;&#1086;&#1073;&#1099; &#1074;&#1077;&#1088;&#1085;&#1091;&#1090;&#1100;&#1089;&#1103; &#1082; &#1087;&#1088;&#1077;&#1076;&#1099;&#1076;&#1091;&#1097;&#1077;&#1084;&#1091; &#1074;&#1086;&#1087;&#1088;&#1086;&#1089;&#1091; &#1080; &#1087;&#1086;&#1087;&#1088;&#1086;&#1073;&#1086;&#1074;&#1072;&#1090;&#1100; &#1089;&#1085;&#1086;&#1074;&#1072;. &#1069;&#1090;&#1086; &#1076;&#1086;&#1083;&#1078;&#1085;&#1086; &#1089;&#1088;&#1072;&#1073;&#1086;&#1090;&#1072;&#1090;&#1100;. &#1052;&#1099; &#1080;&#1079;&#1074;&#1080;&#1085;&#1103;&#1077;&#1084;&#1089;&#1103; &#1079;&#1072; &#1085;&#1077;&#1091;&#1076;&#1086;&#1073;&#1089;&#1090;&#1074;&#1086; &#1077;&#1089;&#1083;&#1080; &#1101;&#1090;&#1086; &#1087;&#1088;&#1086;&#1080;&#1079;&#1086;&#1081;&#1076;&#1077;&#1090;.</p>";


print "<form method=post action=\"display-question-ru.cgi\">
<input type=hidden name=usernum value=$num>
<input type=hidden name=qnum value=0>
<input type=submit value=\"&#1053;&#1072;&#1095;&#1080;&#1085;&#1072;&#1081;&#1090;&#1077;\">
</form>";

close (USERDATAFILE);

open (STIMFILE,"$resourcedir" . "items-ru.csv") or print "Can't find items-ru.csv";

@lines = <STIMFILE>;


foreach my $line (@lines) {
    chomp;
    my ($type,$condition,@rest) = split(/,/,$line);
    push(@stims,"$condition");
  }

close (STIMFILE);

@order = randarray(@stims);

open (ORDERFILE,">>$resourcedir" . "order-ru.txt") or print "Can't find $resourcedir" . "order-ru.txt";

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

