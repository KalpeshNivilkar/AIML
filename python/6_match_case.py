color = input("enter the color: ")
match color:
    case "green":
        print("go")
    case "yellow":
        print("look")
    case "red":
        print("stop")
    case _ :
        print("wrong color")