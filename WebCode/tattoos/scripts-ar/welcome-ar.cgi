#!/usr/bin/perl
#use utf8::all;
#use CGI qw(-utf8);

my ($webpath);

$webpath = "http://semlab.bu.edu/tattoos-ar/";

use CGI qw(:standard); print "Content-type: text/html\n\n";

print "<meta charset=\"utf_8\">";

# print start_html(-title=>'استبيان',
#                  -style => { -src => "$webpath" . 'survey.css',
#                              -type => 'text/css',
#                              -media => 'screen' },
# 		 -lang => 'fa-IR'
#                  );

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



print "<h1 style= \"text-align:right;\">!أهلا و سهلا</h1>\n";

print "<p style= \"text-align:right;\">شكرا لمشاركتك في بحثنا! ستساعدنا مشاركتك في تعلم كيف يفهم الناس الكلمات  التي تصف الأجزاء المختلفة من الجسم</p>\n";

print "<p style= \"text-align:right;\">سنعرض لك سلسلة من صور الوشوم في أزواج مع  جملة. نطلب منك أن تتخيل أن أحدهم قال هذه الجملة إما عن الصورة على اليسار أو الصورة على اليمين. الرجاء الضغط على الصورة التي تناسب الجملة بشكل أفضل</p>\n"; 


print "<p style= \"text-align:right;\">سيتم تخزين المعلومات التي تشاركها معنا على خادم جامعة بوسطن الإلكتروني المحمي بكلمة مرور. لن يتم مشاركة هذه المعلومات مع أي شخص خارج فريق البحث لدينا </p>";

print "<p style= \"text-align:right;\">مشارکت شمامشاركتك فى هذا البحث اختياري. يمكنك رفض الإجابة على أي من الأسئلة التالية أو جميعها. يمكنك الانسحاب من المشاركة في البحث  في أي وقت دون عواقب سلبية. لن يتم مشاركة أي معلومات تعريفية أو معلومات شخصية مع أي شخص خارج فريق البحث</p>";

print "<p style= \"text-align:right;\"> ecoppock" . '@' . 
"bu.edu :إذا كانت لديك أسئلة أو شكاوى ، يرجى مراسلة هذا العنوان </p>";



print "<p style=\"text-align:right;\"> إذا كانت لديك أسئلة حول حقوقك كمشارك في هذا البحث ، أو ترغب في التحدث إلى شخص خارج فريق البحث ، فيمكنك الاتصال بـمجلس المراجعة المؤسسية على 617.358.6115 مباشرة</p>";

print "<p style= \"text-align:right;\"> بالنقر على \'أوافق\' أدناه ، فإنك تؤكد أن عمرك لا يقل عن 18 عامًا ، وأنك قد قرأت وفهمت جميع المعلومات الواردة مسبقا ، وأنك توافق على المشاركة في هذه الدراسة</p>";

print "<form method=post action=startsurvey-ar.cgi><p>";

print "<p style= \"text-align:right;\"><input type=\"checkbox\" name=\"consent\"> أوافق </p>";

print "<p style= \"text-align:right;\"> <input type=\"text\" name=\"workerID\" required /> :Prolific رقم تعريف </p><br><br>";

#style:\"float:right\" 

print "<input type=submit value=\"تقدم\" style=\"float:right\">";

print "</form>";


print "</div>";
print "</div>";
print "</div>";

print "<div id=\"preload\">";
print "</div>";


print "</body></html>";
