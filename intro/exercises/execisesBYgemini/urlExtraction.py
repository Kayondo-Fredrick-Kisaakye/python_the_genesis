full_url = "https://github.com"
print(f"{full_url.removeprefix('https://')}")

full_url = full_url.removeprefix('https://') #ive reaasigned the string back to variable so it becomes permanent
print(full_url)