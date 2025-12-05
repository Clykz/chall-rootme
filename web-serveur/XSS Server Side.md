# Description
```
Statement
Challenge created during the "HackDay 2023" CTF
This platform for issuing certificates of participation has just gone live. The developers assure you that they have followed best practices and escaped all user inputs before using them in their code...

The flag is located in the `/flag.txt` file.$
```
# Exploit
- The statement tells us that this is a server‑side XSS, so we are going to test the user input fields.

- First, we test the first user input (not the login). It is not vulnerable.

- We log in and then test the second user input, which is also not vulnerable, so the only ones left       are the inputs used to create an account.

- We inject this payload — which allows reading a file — into the First Name field:
```
<script>
x=new XMLHttpRequest;
x.onload=function(){document.write(btoa(this.responseText))};
x.open("GET","file:///flag.txt");x.send();
</script> 
```
- Bingo! When we download the PDF, we get our flag in Base64, which we can decode:
```
czNydjNyX3MxZDNfeHNzXzFzX3c0eV9tMHIzX2Z1bg==
```