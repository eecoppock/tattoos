#!/usr/bin/perl
#use utf8::all;
#use CGI qw(-utf8);

my ($webpath);

$webpath = "http://semlab.bu.edu/tattoos-per/";

use CGI qw(:standard); print "Content-type: text/html\n\n";

print "<meta charset=\"utf_8\">";

# print start_html(-title=>'نظرسنجی',
#                  -style => { -src => "$webpath" . 'survey.css',
#                              -type => 'text/css',
#                              -media => 'screen' },
# 		 -lang => 'fa-IR'
#                  );

print "<html lang=\"fa-IR\">
<head>
    <title>نظرسنجی</title>
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



print "<h1 style= \"text-align:right;\">!خوش آمدی</h1>\n";

print "<p style= \"text-align:right;\">ما از مشارکت شما در تحقیقاتمام سپاسگزار هستیم! مشارکت شما با ما کمک می کند بفهمیم چگونه مردم کلمات را برای قسمتهای بدن انتخاب می کنند </p>\n";

print "<p style= \"text-align:right;\">ما دو عکس خالکوبی و یک جمله که آنها را توصیف می کند به شما نشان خواهیم داد. ما از شما که می خواهیم تصور کنید که این بهنه برای کدام یک از این دو عکس استفاده شده است. اطفاً بر روی عکسی که شما فکر می کنید برای این جمله مناسب است کلیک کنید 
</p>\n";


print "<p style= \"text-align:right;\">اطلاعاتی که شما با ما اشتراک می کنید در یک سرور امن نگهداری می شود که توسط رمز عبور محافظت می شد و در دانشگاه بوسطن مدیریت می شد. اطلاعات شما فقط جز تحقیق ما برای هیچ چیز دیگری استفاده نخواهد شد </p>";

print "<p style= \"text-align:right;\">مشارکت شما در تحقیق ما دار طلبانه است. می توانید تصمیم بگیرید که به هر سوالی پاسخ ندهید. در هر زمان بدون عواقب منفی شما می توانید تصمیم بگیرید که شرکت نکنید. اطلاعات شما خصوصی است و شناسایی شما به کس دیگری اشتراک</p>";

print "<p style= \"text-align:right;\"> ecoppock" . '@' . 
"bu.edu :اگر سوال یا نگرانی دارید ، با الیزابت کوپوک در این لینک تماس بگیرید</p>";



print "<p style=\"text-align:right;\">اگر در راجع به حق خود به عنوان یک شرکت کننده در تحقیق سوال دارید و با شخص غیر از محقق می خواهید صحبت کنید، شما می توانید با هیئت بررسی نهادی در دانشگاه بوستون در 617.358.6115  مستقیماً تماس بگیرید </p>";

print "<p style= \"text-align:right;\">اگر گزینه موافقم را انتخاب کنید، تایید میکنید که عمر شما 18 سال یا بیشتر است، متن بالا را خوانده اید و موافقت می کنید که در این تحقیقات شرکت کنید</p>";

print "<form method=post action=startsurvey-per.cgi><p>";

print "<p style= \"text-align:right;\"><input type=\"checkbox\" name=\"consent\"> موافقم </p>";

print "<p style= \"text-align:right;\"> <input type=\"text\" name=\"workerID\" required /> :Prolific شماره شناسایی </p><br><br>";

#style:\"float:right\" 

print "<input type=submit value=\"ادامه بده\" style=\"float:right\">";

print "</form>";


print "</div>";
print "</div>";
print "</div>";

print "<div id=\"preload\">";
print "</div>";


print "</body></html>";
