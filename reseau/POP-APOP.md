# Description 
```
Statement
Find the user password in this network frame.
```

# Exploit
- Opened in wireshark with filter **pop**
```
+OK Hello little hackers. <1755.1.5f403625.BcWGgpKzUPRC8vscWn0wuA==@vps-7e2f5a72>
APOP bsmith 4ddd4137b84ff2db7291b568289717f0
+OK Logged in.
LIST
+OK 2 messages:
1 6
2 76
.
RETR 1
+OK 6 octets
lutz
.
quit
+OK Logging out.
```
- The hash is the hash is **4ddd4137b84ff2db7291b568289717f0**
- The shared secret is **<1755.1.5f403625.BcWGgpKzUPRC8vscWn0wuA==@vps-7e2f5a72>**
- I used Hashcat along with rockyou.txt, and I created a .txt file in this format : **4ddd4137b84ff2db7291b568289717f0:<1755.1.5f403625.BcWGgpKzUPRC8vscWn0wuA==@vps-7e2f5a72>**
```
hashcat -a 0 -m 20 hashtest.txt rockyou.txt
```