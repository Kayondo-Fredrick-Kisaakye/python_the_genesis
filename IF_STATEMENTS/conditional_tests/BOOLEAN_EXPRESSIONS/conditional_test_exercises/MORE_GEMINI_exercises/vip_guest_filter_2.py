guests = ['jexi', 'ryson', 'domee', 'muha', 'mavol']  #a list of guests
vips = ('mark', 'herbat')              #a tuple of vips

print("---guest check in---")
for guest in guests[:4]:
    if guest in vips:
        print(f"Welcome, VIP {guest.title()}! your table is ready.")
    else:
        print(f"Hello, {guest.title()}, thanks for coming.")

#lemme  switch the tutor