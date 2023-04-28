import hashlib
print("**************PASSWORD CRACKER ******************")

pass_found = 0
input_hash = input("Enter the hashed password:")
pass_doc = input("\nEnter passwords filename including path(root / home/):")
try:
 pass_file = open(pass_doc, 'r')
 
except:

 print("Error:")
 
 print(pass_doc, "is not found.\nPlease give the path of file correctly.")
 quit()
for word in pass_file:
 #print(word)
 enc_word = word.encode('utf-8')
 hash_word = hashlib.md5(enc_word.strip())
 digest = hash_word.hexdigest()
 #print(digest)
 if digest == input_hash:
     print("Password found.\nThe password is:", word)
 pass_found = 1

