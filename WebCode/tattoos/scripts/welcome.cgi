#!/usr/bin/perl


my ($webpath);

$webpath = "http://semlab.bu.edu/tattoos/";

use CGI qw(:standard); print "Content-type: text/html\n\n";

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

print "<form method=post action=startsurvey.cgi><p>";

print "<h1>Welcome!</h1>\n";

print "<p>Thanks for participating in our study! Your participation will help us learn about how people understand words that describe parts of the body. </p>\n";

print "<p>You will see a series of pictures with tattoos, in pairs, 
accompanied by a sentence. We ask that you imagine that somebody said 
the sentence in reference to either the picture on the left or the picture 
on the right. Please click on the one you think the speaker was talking about.</p>\n";


print "<p>The information that you share on this page will be stored
  exclusively in a private location on a password-protected server
  maintained by Boston University, and it will not be shared with
  anyone outside the research team.</p>";

print "<p>Your participation in this research is voluntary. You may decline to answer any or all of the following questions. You may decline further participation at any time without adverse consequences. No personal or identifying information about you will be shared with anyone else.</p>";

print "<p>If you have any questions or concerns, please contact Elizabeth Coppock at ecoppock" . '@' . "bu.edu. If you have questions about your rights as a research subject or want to speak with someone independent of the research team, you may contact the Boston University IRB directly at 617-358-6115.</p>";

print "<p>By clicking \"I agree\" below you are indicating that you are at least 18 years old, have read and understood the information above and agree to participate in this research study.</p>";

print "<form method=post action=startsurvey.cgi><p>";

print "<p><input type=\"checkbox\" name=\"consent\"> I agree!</p>";

print "Prolific ID: <input type=\"text\" name=\"workerID\" required /><br><br>";

print "<input type=submit value=\"Continue\">";
print "</form>";


print "</div>";
print "</div>";
print "</div>";

print "<div id=\"preload\">";
print "</div>";


print "</body></html>";
