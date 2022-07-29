import pwd

users = pwd.getpwall()
for user in users:
    print(f"USER: {user.pw_name}  SHELL:  {user.pw_shell}")
