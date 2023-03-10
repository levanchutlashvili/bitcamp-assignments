  
filetype = input("file name: ")
match filetype:
    case "cat.gif":
        print("image/gif")
    case "cat.jpg":
        print("image/jpeg")
    case "dog.png":
        print("image/png")
    case "rat.pdf":
        print("application/pdf")
    case _:
      print("application/octet-stream")