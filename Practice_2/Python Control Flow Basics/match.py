#match
day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")
#output: Thursday

#My example
month = 7
match month:
    case 1:
        print("January")
    case 2:
        print("February")
    case 3:
        print("March")
    case 4:
        print("April")
    case 5:
        print("May")
    case 6:
        print("June")
    case 7:
        print("July")
    case 8:
        print("August")
    case 9:
        print("September")
    case 10:
        print("October")
    case 11:
        print("November")
    case 12:
        print("December") #output: July



#Another example
fruit = "apple"
match fruit:
    case "apple":
        print("This is an apple.")
    case "banana":
        print("This is a banana.")
    case "cherry":
        print("This is a cherry.")
    case _:
        print("Unknown fruit.") #output: This is an apple.
    
    
day = 4
match day:
  case 6:
    print("Today is Saturday")
  case 7:
    print("Today is Sunday")
  case _:
    print("Looking forward to the Weekend")

#my example
month = 10
match month: 
    case 12 | 1 | 2:
        print("It's Winter")
    case 3 | 4 | 5:
        print("It's Spring")
    case 6 | 7 | 8:
        print("It's Summer")
    case 9 | 10 | 11:
        print("It's Autumn") #output: It's Autumn 
        