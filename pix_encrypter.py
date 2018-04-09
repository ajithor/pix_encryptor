import imageio
print("Enter path with image name (default  = current working dir)")
path = input()
print("Enter private key")
prk = int(input())
print("Enter public key")
puk = int(input())
img = imageio.imread(path)
img = img ^ prk

img = img ^ puk

print("Encrypted as per request")
print("Enter destination address with name (default  = current working dir)")
dest = input()
print("Saving...")
imageio.imwrite(dest, img)

print("Decrypt ?")
ch = int(input())
if ch == 1:
	img = img ^ puk
	img = img ^ prk
	print("Decrypted")
	imageio.imwrite("Decrypted.jpg", img)