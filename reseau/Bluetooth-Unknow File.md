# Description
```
Statement
Your friend working at NSA recovered an unreadable file from a hacker’s computer. The only thing he knows is that it comes from a communication between a computer and a phone.

The answer is the sha-1 hash of the concatenation of the MAC address (uppercase) and the name of the phone.

Example:
AB:CD:EF:12:34:56myPhone -> 023cc433c380c2618ed961000a681f1d4c44f8f1
```

# Exploitation
- We retrieved the MAC address and the device name in Wireshark (Wireless → Bluetooth devices).
![alt text](/img/image12.png)
- After that, we formatted the data correctly (MAC address in uppercase concatenated with the phone name) and computed the SHA‑1 hash, which gives us the flag.
![alt text](/img/image13.png)