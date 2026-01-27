# Description
```
Statement
Find the "Enable" password.
```

# Exploit
- After the download of the file , we have line 

``
enable secret 5 $1$p8Y6$MCdRLBzuGlfOs9S.hXOp0.
``

```
username hub password 7 025017705B3907344E 
username admin privilege 15 password 7 10181A325528130F010D24
username guest password 7 124F163C42340B112F3830
```
- After reviewing how Cisco configuration files work, we can see that there are two different encryption types used for Cisco passwords. The first one is the enable password, which is encrypted using type 7 (easy to reverse), and the second one is the enable secret, which is hashed using MD5 or SHA1, offering strong security.
- In this case, we have both types of Cisco passwords. We start with the easy one to decrypt: the type 7 password. We can decode it using a Cisco Type 7 decryptor, and we obtain the following result:
```
6sK0_hub
6sK0_admin
6sK0_guest
```
- Here, we notice a common pattern: 6sK0_. Since we are looking for the enable password, we can deduce that the complete password is 6sK0_enable
