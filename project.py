import hashlib


password = "124aksdjflaksjdf"
hashed_password = hashlib.sha256(password.encode("utf-8")).hexdigest()
print(hashed_password)
