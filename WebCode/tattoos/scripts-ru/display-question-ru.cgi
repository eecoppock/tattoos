#!/usr/bin/perl

use CGI qw(:standard); print "Content-type: text/html\n\n";
use strict;
use CGI;
use CGI::Carp 'fatalsToBrowser', 'croak';

use Time::HiRes qw(time);
use POSIX qw(strftime);

my ($query,       # CGI query object
    @params,      # array of all fields sent
    $usernum, $qnum, $answer,
    $type, $stimnum, $total,
    @order, $question,
    %item,$condition,
    $time,
    $writedir,$resourcedir,$webpath
   );

$query=CGI->new;           # get CGI object

$writedir = "/shared/tattoos/output-ru/"; 
$resourcedir = "/shared/tattoos/resources-ru/";
$webpath = "http://semlab.bu.edu/tattoos-ru/";

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

#first print data from previous question

$usernum = $query->param("usernum");
$qnum = $query->param("qnum");
$condition = $query->param("condition");
$answer = $query->param("answer");

my $t = time;
$time = strftime "%m/%d/%Y %H:%M:%S", localtime $t;
$time .= sprintf ".%03d", ($t-int($t))*1000;

open (STIMFILE,"$resourcedir" . "items-ru.csv") or die "Can't find items-ru.csv";


while (<STIMFILE>) {
   $_ =~ s/"//g;
   chomp;
   my ($type,$condition,$word, $word_ru, $expected,$image1,$image2) = split(/,/);
   
   $item{"$condition"}{"type"} = "$type";
   $item{"$condition"}{"word"} = "$word";
   $item{"$condition"}{"expected"} = "$expected";
   $item{"$condition"}{"word_ru"} = "$word_ru";
   $item{"$condition"}{"image1"} = "$image1";
   $item{"$condition"}{"image2"} = "$image2";
 }

 close (STIMFILE);



open (ORDERFILE, "$resourcedir" ."order-ru.txt") or die "Can't open order-ru.txt";

while (<ORDERFILE>) {
     chomp;
     my ($subject,@stims) = split(/ /);
     if ($subject eq $usernum) {
 	@order = @stims;
     }
 }
close (ORDERFILE);

$total = scalar(@order);

if ($qnum > 0) {
  
   open (DATAFILE, ">>$writedir" . "data/data-$usernum.txt") or print "Can't open data/data-$usernum.txt<br>\n";
   $condition = $order[$qnum-1];
   print DATAFILE join("\t", ("$usernum","$condition","$time",
			      $query->param("leftrightorder"),
			      $query->param("qnum"),
			      $query->param("expected"),
 			     $query->param("answer")));
   print DATAFILE "\n";
   close (DATAFILE);
  
 } else {
   open (USERDATAFILE, ">>$writedir" . "userdata/userdata-$usernum.txt");
   print USERDATAFILE "$usernum\tstarttime\t$time\n";
   close (USERDATAFILE);
}


#then print next question



 $qnum = $qnum+1;

 if ($qnum>$total) {
  
   print "<br><br><br><h1>&#1057;&#1087;&#1072;&#1089;&#1080;&#1073;&#1086;!</h1>\n";
  
   print "<p>&#1057;&#1089;&#1099;&#1083;&#1082;&#1072; &#1086;&#1073;&#1086;&#1079;&#1085;&#1072;&#1095;&#1072;&#1102;&#1097;&#1072;&#1103; &#1086;&#1082;&#1086;&#1085;&#1095;&#1072;&#1085;&#1080;&#1077;: https://app.prolific.co/submissions/complete?cc=6EAC8AA7</p>"

    
 } else {
  
   print "\n<p id=\"progress-indicator-position\">$qnum/$total</p>\n";

   $condition = $order[$qnum-1];

   my $type = $item{$condition}{"type"};
   my $word_ru = $item{$condition}{"word_ru"};
   my $image1 = $item{$condition}{"image1"};
   my $image2 = $item{$condition}{"image2"};
   my $expected = $item{$condition}{"expected"};
   my $leftrightorder = rand(1);

   print "\n\n<form method=\"post\" action=\"display-question-ru.cgi\" autocomplete=\"off\">\n";
 
   print "<div align=center>";

   print "\n<p>&#1059; &#1085;&#1077;&#1077; &#1090;&#1072;&#1090;&#1091;&#1080;&#1088;&#1086;&#1074;&#1082;&#1072; &#1085;&#1072; $word_ru.</p>\n";

   if ($leftrightorder==1) {
     

#     print "<p><input type=\"radio\" name=\"answer\" value=\"$image1\" required> Left <br>\n
 #<input type=\"radio\" name=\"answer\" value=\"$image2\"> Right</p>\n";

     print "

<label for=\"answerleft\"><img src=\"images/single_$image1.jpg\" height=250><input id=\"answerleft\" type=\"radio\" name=\"answer\" value=\"$image1\" onclick=\"this.form.submit();\"></label>
<label for=\"answerright\"><img src=\"images/single_$image2.jpg\" height=250><input id=\"answerright\" type=\"radio\" name=\"answer\" value=\"$image2\" onclick=\"this.form.submit();\">
</label>";

     
    
   } else {

     print "
<label for=\"answerleft\">
<input id=\"answerleft\" type=\"radio\" name=\"answer\" value=\"$image2\" onclick=\"this.form.submit();\">
<img src=\"images/single_$image2.jpg\" height=250>
</input>
</label>
<label for=\"answerright\">
<input id=\"answerright\" type=\"radio\" name=\"answer\" value=\"$image1\" onclick=\"this.form.submit();\">
<img src=\"images/single_$image1.jpg\" height=250>
</input>
</label>
";
     
     #print "<p><input type=\"radio\" name=\"answer\" value=\"$image2\" required> Left <br>\n
# <input type=\"radio\" name=\"answer\" value=\"$image1\"> Right</p>\n";
    
   }
  
   print "<input type=hidden name=usernum value=\"$usernum\">\n";
   print "<input type=hidden name=condition value=\"$condition\">\n";
   print "<input type=hidden name=qnum value=\"$qnum\">\n";
   print "<input type=hidden name=leftrightorder value=\"$leftrightorder\">\n";
   print "<input type=hidden name=expected value=\"$expected\">\n";
   print "</form>\n";   
  
}

print "</div>";

print "</div>";
print "</div>";
print "</div>"; 

    
print "</body></html>";
    

