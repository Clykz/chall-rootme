# 🧩Challenge : LDAP-Injection

# 🔍 Description
- The main goal of this challenge is to bypass the authentication.

- For bypass the authentification we use LDAP injection


# ⚙️ Exploitation
- The first step is to understand the LDAP query format. I tried entering the username: ``)t``.

- We get an invalid syntax error: ``(&(uid=)x)(userPassword=x))`` — this is expected.

- The entered login and password are inserted after "uid=" and "userPassword=" respectively. Let’s analyze this query:(&(x)(y)) returns true only if both x and y are true.

- Therefore, ``(&(uid=x)(userPassword=y))`` returns true only if the database contains a login x with password y.The test would succeed if it accepted any uid and userPassword:

    ``user=*`` and ``password=*``

- This does not work: ERROR: Bad characters in password

- So the attempt becomes:
``username=*``
``password=*)(&``