
filename = input("Filename:  ").strip().lower()
new_filename = filename
    #if gif or png or jpg or jpeg, print "image/type"

if '.gif' in new_filename:
    print("image/gif")

elif '.jpg' in new_filename:
    print("image/jpeg")

elif 'jpeg' in new_filename:
    print("image/jpeg")

elif '.png' in new_filename:
    print("image/png")

    #if pdf or zip, print "application/type"
elif '.pdf' in new_filename:
    print("application/pdf")

elif '.zip' in new_filename:
    print("application/zip")

    # if txt, print "text/plain"
elif '.txt' in new_filename:
    print("text/plain")

else:
    print(f"application/octet-stream")


