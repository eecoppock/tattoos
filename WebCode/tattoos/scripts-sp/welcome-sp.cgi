#!/usr/bin/perl


my ($webpath);

$webpath = "http://semlab.bu.edu/tattoos-sp/";

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

print "<form method=post action=startsurvey-sp.cgi><p>";

print "<h1>&iexcl;Bienvenida/o!</h1>\n";

print "<p>&iexcl;Gracias por participar en nuestro estudio! Su participaci&oacute;n nos ayudar&aacute; a aprender sobre c&oacute;mo las personas entienden a 
las palabras que describen partes del cuerpo.</p>\n";

print "<p>Usted ver&aacute; una serie de imagines de tatuajes, de a pares, acompa&ntilde;adas
 por una frase. Le pedimos que imagine que alguien dijo la frase en referencia a 
 una de las dos im&aacute;genes. Por favor haga click en la que piensa que corresponde con 
 lo dicho por el hablante.</p>\n";


print "<p>La informaci&oacute;n que usted comparta en esta p&aacute;gina ser&aacute; guardada 
exclusivamente en una ubicaci&oacute;n privada, en un servidor protegido con contrase&ntilde;a 
y mantenido por Boston University, y no ser&aacute; compartido con nadie por fuera del 
equipo de investigaci&oacute;n.</p>";

print "<p> Su participaci&oacute;n en esta investigaci&oacute;n es voluntaria. 
Puede negarse a contestar una o todas las preguntas. Puede terminar 
su participaci&oacute;n en cualquier momento sin consecuencias negativas. 
Ninguna informaci&oacute;n personal o identificatoria suya ser&aacute; compartida con nadie m&aacute;s.</p>";

print "<p>Si tiene preguntas o inquietudes, por favor 
contacte a Elizabeth Coppock: ecoppock@bu.edu. Si tiene alguna pregunta si 
te sus derechos como sujeto de investigaci&oacute;n o si quiere hablar con alguien 
ajeno al equipo de investigaci&oacute;n, puede contactarse directamente con el IRB 
de Boston University al 617-358-6115</p>";

print "<p>Al clickear \"Estoy de acuerdo\" usted est&aacute; indicando que tiene al menos 
18 a&ntilde;os de edad, que ley&oacute; y comprendi&oacute; la informaci&oacute;n de arriba y que acuerda participar 
en participar en este estudio.</p>";

print "<form method=post action=startsurvey-sp.cgi><p>";

print "<p><input type=\"checkbox\" name=\"consent\"> Estoy de acuerdo!</p>";

print "Prolific ID: <input type=\"text\" name=\"workerID\" required /><br><br>";

print "<input type=submit value=\"Contin&uacute;e\">";
print "</form>";


print "</div>";
print "</div>";
print "</div>";

print "<div id=\"preload\">";
print "</div>";


print "</body></html>";
