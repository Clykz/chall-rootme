# 🧩Challenge : Bluetooth-Unknow File

# 🔍 Description
- The main goal of this challenge is to find the hash of the MAC address and the phone name.

- To achieve this, we use Wireshark to obtain the MAC address and the phone name, then we compute the SHA‑1 hash.

⚙️ Exploitation
- We retrieved the MAC address and the device name in Wireshark (Wireless → Bluetooth devices).
![alt text](/img/image12.png)
- After that, we formatted the data correctly (MAC address in uppercase concatenated with the phone name) and computed the SHA‑1 hash, which gives us the flag.
![alt text](/img/image13.png)