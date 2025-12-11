# Description
```
Statement
Your goal is to hack this photo galery by uploading PHP code.
```

# Exploit 

- We have an upload form that accepts jpeg, gif, or png files. The title of the challenge also tells us that it’s a Null byte file upload, meaning we should upload a file using the pattern: ``test.php%00jpeg``
- We inject malicious code into our PHP file:

```php
<?php
        system('pwd && cat /challenge/web-serveur/ch22/.passwd');
?>
```
- When we upload this, we get the path where our PHP file is stored. But when we try to access it, we get a 400 Bad Request error — this is because the Nginx server blocks any request containing %00.

- So in our GET request, we remove ``%00jpeg``, and then we can retrieve our flag.