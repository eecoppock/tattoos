#!/usr/bin/perl

use CGI qw(:standard); print "Content-type: text/html\n\n";

use strict;
use CGI;
use CGI::Carp 'fatalsToBrowser', 'croak';

my ($query,$inputdata,@params,$num,$newnum,$itemID,%item,@randitems,$seed,@stims,@lines,@targets,@randtargets,@checks,@randchecks,@practice,@randpractice,@fillers,@randfillers,@blm,@randblm,@order,$writedir,$resourcedir,$webpath,$time);


$writedir = "/shared/tattoos/output-ar/";
$resourcedir = "/shared/tattoos/resources-ar/";
$webpath = "http://semlab.bu.edu/tattoos-ar/";

$query=CGI->new;  

print "<meta charset=\"utf_8\">"; 

print "<html lang=\"ar\">
<head>
    <title>استبيان</title>
    <link rel=\"stylesheet\" type=\"text/css\" href=\"survey.css\" media=\"screen\"/>
  <meta http-equiv=\"content-type\" content=\"text-html; charset=utf-8\">
</head>
<body>
";

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


print "<p style= \"text-align:right;\">!شكرا لمشاركتك في بحثنا</p>";
print "<p style= \"text-align:right;\">.حان الوقت للبدء</p>";

print "<p style= \"text-align:right;\"><b> ملاحظة</b> ينقطع الاتصال عن هذا الخادم أحيانًا. إذا حدث هذا ، يمكنك النقر فوق زر الرجوع في متصفحك للعودة إلى الصفحة السابقة. هذا قد يساعدك. شكرا لك. إذا حدث هذا نعتذر عن أي إزعاج</p>";


print "<form method=post action=\"display-question-ar.cgi\">
<input type=hidden name=usernum value=$num>
<input type=hidden name=qnum value=0>
<input type=submit value=\"ابدأ\" style=\"float:right\">

</form>";
 
close (USERDATAFILE);

open (STIMFILE,"$resourcedir" . "items-ar.csv") or print "Can't find items-ar.csv";

@lines = <STIMFILE>;


foreach my $line (@lines) {
    chomp;
    my ($type,$condition,@rest) = split(/,/,$line);
    push(@stims,"$condition");
  }

close (STIMFILE);

@order = randarray(@stims);

open (ORDERFILE,">>$resourcedir" . "order-ar.txt") or print "Can't find $resourcedir" . "order-ar.txt";

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

