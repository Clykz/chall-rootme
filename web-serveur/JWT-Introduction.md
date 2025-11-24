# 🧩Challenge : JWT-Introduction

# 🔍 Description
- The main goal of this challenge is to authenticate as the admin user.

- To achieve this, we first need to understand how the JWT (JSON Web Token) is constructed.

# ⚙️ Exploitation
- When we log in as guest, we receive a JWT containing a header, a payload, and a signature.
    The first step is to decode the token from Base64.
- After decoding, we obtain :
````
{"typ":"JWT","alg":"HS256"}
{"username":"guest"}
<binary signature>
````
- And by checking the documentation, we understand that it is possible to bypass this verification.
To do so, we simply need to modify the JWT header by replacing the algorithm with ``none``, and change the payload by setting the username to ``admin`` instead of ``guest``.

- JWT:``eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0=.eyJ1c2VybmFtZSI6ImFkbWluIn0=.OnuZnYMdetcg7AWGV6WURn8CFSfas6AQej4V9M13nsk``