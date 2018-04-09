# pix_encryptor
Python code to encrypt(simply XORs with a private key) images .

This program first XORs an image(preferably) with a user-defined private kay and XORs over it with another user defined Public key.
The code can be modified to keep the public key as an 'Arbitrary Constant' value for a given Network.

Prequisites
---
Python 3.x.(obviously)(preferably with pip ( pip within conda if any clashes of versions or the way  like for Deep-Learning)).
numpy (#pip install numpy)
imageio(# pip install imageio)
Simply google if any confusion(Prefer DuckDuckGo, if any privacy concerns).


This is created as an alternate solution against OpenCV
---

Reasons
---
- Tribute to Ajey Pai.
- Installing OpenCV on Windows is a time-consuming job.
- OpenCV itself has some dependencies.
- OpenCV doesn't work(official versions) with newer Python Versions(as of now)
- Demonstrate imageio and visvis as alternates for OpenCV.
- Promote "imprt imageio".

Note
---
People are free to condtribute or solve any of the issues.
Also, maybe write a javascript version of the code, just to rub it in a GUI.
In the js_encryptor repostory.
