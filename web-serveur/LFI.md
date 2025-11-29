# 🧩Challenge : File Upload - Double extensions

# 🔍 Description
- The main goal of this challenge, as mentioned in the title, is to exploit a Local File Inclusion (LFI) vulnerability.



# ⚙️ Exploitation
- While navigating through the website, we notice that the application uses a URL parameter called ``file=``.
This parameter is used to include pages dynamically, which immediately suggests a potential LFI vector.

- When we modify the ``file=`` parameter, we observe that the page content changes accordingly.
This confirms that the server is including files directly based on user input.
- ``file=../`` we see a admin file 
- ``file=../admin``  wee a index.php with the flag