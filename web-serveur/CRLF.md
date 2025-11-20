# 🧩Challenge : CRLF%0d%0aInjection

# 🔍 Description
- The main goal of this challenge is to inject entries into the authentication log.

- We observe a login form, and below it we can see the authentication log.

- Each time we try to log in, the application appends a new line to the log, showing the username we entered followed by either “authenticated” or “failed to authenticate”.

# ⚙️ Exploitation
- To do this, we will compose a request including the newline characters `cr` and `lf` in the `username` parameter. In URI encoding, they are written as `%0d%0a`.
- First we see user admin exist and when we submit a login when have this URL
```
http://challenge01.root-me.org/web-serveur/ch14/?username=test&password=test
```
- So we try injection CRL ``http://challenge01.root-me.org//web-serveur/ch14/index.php?username=admin%0D%0Aadmin&password=test``
- and we have this : 
```
admin
admin failed to authenticate.
````
- We are now going to make the admin believe that he tried to log in but was unsuccessful.
![alt text](/img/image-14.png)