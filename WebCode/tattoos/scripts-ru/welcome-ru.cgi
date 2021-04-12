#!/usr/bin/perl


my ($webpath);

$webpath = "http://semlab.bu.edu/tattoos-ru/";

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


print "<h1>&#1044;&#1086;&#1073;&#1088;&#1086; &#1087;&#1086;&#1078;&#1072;&#1083;&#1086;&#1074;&#1072;&#1090;&#1100;</h1>\n";

print "<p>&#1057;&#1087;&#1072;&#1089;&#1080;&#1073;&#1086; &#1079;&#1072; &#1042;&#1072;&#1096;&#1077; &#1091;&#1095;&#1072;&#1089;&#1090;&#1080;&#1077; &#1074; &#1085;&#1072;&#1096;&#1077;&#1084; &#1080;&#1089;&#1089;&#1083;&#1077;&#1076;&#1086;&#1074;&#1072;&#1085;&#1080;&#1080;! &#1042;&#1072;&#1096;&#1077; &#1091;&#1095;&#1072;&#1089;&#1090;&#1080;&#1077; &#1085;&#1072;&#1084; &#1087;&#1086;&#1084;&#1086;&#1078;&#1077;&#1090; &#1087;&#1086;&#1085;&#1103;&#1090;&#1100;, &#1082;&#1072;&#1082; &#1080;&#1084;&#1077;&#1085;&#1085;&#1086; &#1083;&#1102;&#1076;&#1080; &#1074;&#1086;&#1089;&#1087;&#1088;&#1080;&#1085;&#1080;&#1084;&#1072;&#1102;&#1090; &#1089;&#1083;&#1086;&#1074;&#1072;, &#1082;&#1086;&#1090;&#1086;&#1088;&#1099;&#1084;&#1080; &#1086;&#1087;&#1080;&#1089;&#1099;&#1074;&#1072;&#1102;&#1090;&#1089;&#1103; &#1095;&#1072;&#1089;&#1090;&#1080; &#1090;&#1077;&#1083;&#1072;.</p>\n";

print "<p>&#1042;&#1072;&#1084; &#1073;&#1091;&#1076;&#1091;&#1090; &#1087;&#1086;&#1082;&#1072;&#1079;&#1072;&#1085;&#1099; &#1092;&#1086;&#1090;&#1086;&#1075;&#1088;&#1072;&#1092;&#1080;&#1080; &#1090;&#1072;&#1090;&#1091;&#1080;&#1088;&#1086;&#1074;&#1086;&#1082;, &#1076;&#1074;&#1077; &#1089;&#1088;&#1072;&#1079;&#1091;, &#1074;&#1084;&#1077;&#1089;&#1090;&#1077; &#1089; &#1086;&#1087;&#1080;&#1089;&#1099;&#1074;&#1072;&#1102;&#1097;&#1077;&#1081; &#1080;&#1093; &#1092;&#1088;&#1072;&#1079;&#1086;&#1081;. &#1052;&#1099; &#1042;&#1072;&#1089; &#1087;&#1088;&#1086;&#1089;&#1080;&#1084; &#1087;&#1088;&#1077;&#1076;&#1089;&#1090;&#1072;&#1074;&#1080;&#1090;&#1100; &#1089;&#1077;&#1073;&#1077;, &#1095;&#1090;&#1086; &#1082;&#1090;&#1086;-&#1090;&#1086; &#1080;&#1089;&#1087;&#1086;&#1083;&#1100;&#1079;&#1086;&#1074;&#1072;&#1083; &#1101;&#1090;&#1091; &#1092;&#1088;&#1072;&#1079;&#1091; &#1074; &#1086;&#1090;&#1085;&#1086;&#1096;&#1077;&#1085;&#1080;&#1080; &#1082; &#1086;&#1076;&#1085;&#1086;&#1081; &#1080;&#1079; &#1101;&#1090;&#1080;&#1093; &#1076;&#1074;&#1091;&#1093; &#1092;&#1086;&#1090;&#1086;&#1075;&#1088;&#1072;&#1092;&#1080;&#1081;. &#1055;&#1086;&#1078;&#1072;&#1083;&#1091;&#1081;&#1089;&#1090;&#1072; &#1082;&#1083;&#1080;&#1082;&#1085;&#1080;&#1090;&#1077; &#1085;&#1072; &#1090;&#1091; &#1092;&#1086;&#1090;&#1086;&#1075;&#1088;&#1072;&#1092;&#1080;&#1102;, &#1082;&#1086;&#1090;&#1086;&#1088;&#1072;&#1103; &#1087;&#1086; &#1042;&#1072;&#1096;&#1077;&#1084;&#1091; &#1084;&#1085;&#1077;&#1085;&#1080;&#1102; &#1073;&#1086;&#1083;&#1077;&#1077; &#1089;&#1086;&#1086;&#1090;&#1074;&#1077;&#1090;&#1089;&#1090;&#1074;&#1091;&#1077;&#1090; &#1076;&#1072;&#1085;&#1085;&#1086;&#1081; &#1092;&#1088;&#1072;&#1079;&#1077;.</p>\n";


print "<p>&#1048;&#1085;&#1092;&#1086;&#1088;&#1084;&#1072;&#1094;&#1080;&#1103;, &#1082;&#1086;&#1090;&#1086;&#1088;&#1086;&#1081; &#1042;&#1099; &#1089; &#1085;&#1072;&#1084;&#1080; &#1087;&#1086;&#1076;&#1077;&#1083;&#1080;&#1090;&#1077;&#1089;&#1100; &#1073;&#1091;&#1076;&#1077;&#1090; &#1089;&#1086;&#1093;&#1088;&#1072;&#1085;&#1077;&#1085;&#1072; &#1074; &#1073;&#1077;&#1079;&#1086;&#1087;&#1072;&#1089;&#1085;&#1086;&#1084; &#1084;&#1077;&#1089;&#1090;&#1077;, &#1074; &#1089;&#1077;&#1088;&#1074;&#1077;&#1088;&#1077; &#1079;&#1072;&#1097;&#1080;&#1097;&#1077;&#1085;&#1085;&#1099;&#1084; &#1087;&#1072;&#1088;&#1086;&#1083;&#1077;&#1084; &#1080; &#1087;&#1086;&#1076;&#1076;&#1077;&#1088;&#1078;&#1072;&#1085;&#1085;&#1099;&#1084; &#1059;&#1085;&#1080;&#1074;&#1077;&#1088;&#1089;&#1080;&#1090;&#1077;&#1090;&#1086;&#1084; &#1041;&#1086;&#1089;&#1090;&#1086;&#1085;&#1072;, &#1080; &#1086;&#1085;&#1072; &#1085;&#1077; &#1073;&#1091;&#1076;&#1077;&#1090; &#1088;&#1072;&#1089;&#1087;&#1088;&#1086;&#1089;&#1090;&#1088;&#1072;&#1085;&#1077;&#1085;&#1072; &#1085;&#1080;&#1075;&#1076;&#1077; &#1082;&#1088;&#1086;&#1084;&#1077; &#1085;&#1072;&#1096;&#1077;&#1075;&#1086; &#1080;&#1089;&#1089;&#1083;&#1077;&#1076;&#1086;&#1074;&#1072;&#1085;&#1080;&#1103;.</p>";

print "<p>&#1042;&#1072;&#1096;&#1077; &#1091;&#1095;&#1072;&#1089;&#1090;&#1080;&#1077; &#1074; &#1101;&#1090;&#1086;&#1084; &#1080;&#1089;&#1089;&#1083;&#1077;&#1076;&#1086;&#1074;&#1072;&#1085;&#1080;&#1080; &#1076;&#1086;&#1073;&#1088;&#1086;&#1074;&#1086;&#1083;&#1100;&#1085;&#1086;. &#1042;&#1099; &#1084;&#1086;&#1078;&#1077;&#1090;&#1077; &#1086;&#1090;&#1082;&#1072;&#1079;&#1072;&#1090;&#1100;&#1089;&#1103; &#1086;&#1090;&#1074;&#1077;&#1090;&#1080;&#1090;&#1100; &#1085;&#1072; &#1086;&#1076;&#1080;&#1085; &#1080;&#1083;&#1080; &#1074;&#1089;&#1077; &#1074;&#1086;&#1087;&#1088;&#1086;&#1089;&#1099;. &#1042;&#1099; &#1084;&#1086;&#1078;&#1077;&#1090;&#1077; &#1087;&#1088;&#1077;&#1082;&#1088;&#1072;&#1090;&#1080;&#1090;&#1100; &#1074;&#1072;&#1096;&#1077; &#1091;&#1095;&#1072;&#1089;&#1090;&#1080;&#1077; &#1074; &#1083;&#1102;&#1073;&#1086;&#1081; &#1084;&#1086;&#1084;&#1077;&#1085;&#1090; &#1073;&#1077;&#1079; &#1082;&#1072;&#1082;&#1080;&#1093;-&#1083;&#1080;&#1073;&#1086; &#1086;&#1090;&#1088;&#1080;&#1094;&#1072;&#1090;&#1077;&#1083;&#1100;&#1085;&#1099;&#1093; &#1087;&#1086;&#1089;&#1083;&#1077;&#1076;&#1089;&#1090;&#1074;&#1080;&#1081;. &#1053;&#1080;&#1082;&#1072;&#1082;&#1072;&#1103; &#1083;&#1080;&#1095;&#1085;&#1072;&#1103; &#1080;&#1083;&#1080; &#1080;&#1076;&#1077;&#1085;&#1090;&#1080;&#1092;&#1080;&#1094;&#1080;&#1088;&#1091;&#1102;&#1097;&#1072;&#1103; &#1080;&#1085;&#1092;&#1086;&#1088;&#1084;&#1072;&#1094;&#1080;&#1103; &#1085;&#1080;&#1082;&#1086;&#1084;&#1091; &#1085;&#1077; &#1073;&#1091;&#1076;&#1077;&#1090; &#1087;&#1077;&#1088;&#1077;&#1076;&#1072;&#1085;&#1072;.</p>";

print "<p>&#1045;&#1089;&#1083;&#1080; &#1091; &#1042;&#1072;&#1089; &#1077;&#1089;&#1090;&#1100; &#1082;&#1072;&#1082;&#1080;&#1077;-&#1083;&#1080;&#1073;&#1086; &#1074;&#1086;&#1087;&#1088;&#1086;&#1089;&#1099; &#1080;&#1083;&#1080; &#1079;&#1072;&#1073;&#1086;&#1090;&#1099;, &#1087;&#1086;&#1078;&#1072;&#1083;&#1091;&#1081;&#1089;&#1090;&#1072; &#1089;&#1074;&#1103;&#1078;&#1080;&#1090;&#1077;&#1089;&#1100; &#1089; &#1069;&#1083;&#1080;&#1079;&#1072;&#1073;&#1077;&#1090; &#1050;&#1086;&#1087;&#1087;&#1086;&#1082;: ecoppock.edu. &#1045;&#1089;&#1083;&#1080; &#1091; &#1042;&#1072;&#1089; &#1074;&#1086;&#1087;&#1088;&#1086;&#1089;&#1099; &#1087;&#1086; &#1087;&#1086;&#1074;&#1086;&#1076;&#1099; &#1042;&#1072;&#1096;&#1080;&#1093; &#1087;&#1088;&#1072;&#1074; &#1082;&#1072;&#1082; &#1091;&#1095;&#1072;&#1089;&#1090;&#1085;&#1080;&#1082;&#1072; &#1074; &#1080;&#1089;&#1089;&#1083;&#1077;&#1076;&#1086;&#1074;&#1072;&#1085;&#1080;&#1080; &#1080;&#1083;&#1080; &#1042;&#1072;&#1084; &#1093;&#1086;&#1095;&#1077;&#1090;&#1089;&#1103; &#1089;&#1074;&#1103;&#1079;&#1072;&#1090;&#1100;&#1089;&#1103; &#1089; &#1082;&#1077;&#1084;-&#1090;&#1086; &#1074;&#1085;&#1077; &#1082;&#1086;&#1084;&#1072;&#1085;&#1076;&#1099; &#1080;&#1089;&#1089;&#1083;&#1077;&#1076;&#1086;&#1074;&#1072;&#1090;&#1077;&#1083;&#1077;&#1081;, &#1042;&#1099; &#1084;&#1086;&#1078;&#1077;&#1090;&#1077; &#1089;&#1074;&#1103;&#1079;&#1072;&#1090;&#1100;&#1089;&#1103; &#1085;&#1072;&#1087;&#1088;&#1103;&#1084;&#1091;&#1102; &#1089; IRB &#1059;&#1085;&#1080;&#1074;&#1077;&#1088;&#1089;&#1080;&#1090;&#1077;&#1090;&#1072; &#1041;&#1086;&#1089;&#1090;&#1086;&#1085;&#1072; &#1087;&#1086; &#1085;&#1086;&#1084;&#1077;&#1088;&#1091; 617-358-6115.</p>";

print "<p>&#1053;&#1072;&#1078;&#1080;&#1084;&#1072;&#1103; \&ldquo;&#1071; &#1089;&#1086;&#1075;&#1083;&#1072;&#1089;&#1077;&#1085;/&#1085;&#1072;\&rdquo; &#1042;&#1099; &#1087;&#1086;&#1082;&#1072;&#1079;&#1099;&#1074;&#1072;&#1077;&#1090;&#1077;, &#1095;&#1090;&#1086; &#1042;&#1072;&#1084; &#1085;&#1077; &#1084;&#1077;&#1085;&#1100;&#1096;&#1077; 18&#1080; &#1083;&#1077;&#1090;, &#1095;&#1090;&#1086; &#1074;&#1099; &#1087;&#1088;&#1086;&#1095;&#1080;&#1090;&#1072;&#1083;&#1080; &#1080; &#1087;&#1086;&#1085;&#1103;&#1083;&#1080; &#1080;&#1085;&#1092;&#1086;&#1088;&#1084;&#1072;&#1094;&#1080;&#1102;, &#1085;&#1072;&#1087;&#1080;&#1089;&#1072;&#1085;&#1085;&#1091;&#1102; &#1074;&#1099;&#1096;&#1077;, &#1080; &#1089;&#1086;&#1075;&#1083;&#1072;&#1096;&#1072;&#1077;&#1090;&#1077;&#1089;&#1100; &#1091;&#1095;&#1072;&#1089;&#1090;&#1074;&#1086;&#1074;&#1072;&#1090;&#1100; &#1074; &#1101;&#1090;&#1086;&#1084; &#1080;&#1089;&#1089;&#1083;&#1077;&#1076;&#1086;&#1074;&#1072;&#1085;&#1080;&#1080;.</p>";

print "<form method=post action=startsurvey-ru.cgi><p>";

print "<p><input type=\"checkbox\" name=\"consent\"> &#1071; &#1089;&#1086;&#1075;&#1083;&#1072;&#1089;&#1077;&#1085;/&#1085;&#1072;!</p>";

print "&#1048;&#1076;&#1077;&#1085;&#1090;&#1080;&#1092;&#1080;&#1082;&#1072;&#1094;&#1080;&#1086;&#1085;&#1085;&#1099;&#1081; &#1085;&#1086;&#1084;&#1077;&#1088; Prolific: <input type=\"text\" name=\"workerID\" required /><br><br>";

print "<input type=submit value=\"&#1055;&#1088;&#1086;&#1076;&#1086;&#1083;&#1078;&#1072;&#1081;&#1090;&#1077;\">";
print "</form>";


print "</div>";
print "</div>";
print "</div>";

print "<div id=\"preload\">";
print "</div>";


print "</body></html>";
