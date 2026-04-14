def validate_ticket(code): 
    if type(code) != str:
        raise ValueError("The code must be a string!")
    if len(code) != 8:
        return False
    if code[0] != "T" and code[1] != "K":
        return False
    else:
        return True

def get_ticket_tier(code):
    if validate_ticket(code) != True:
        raise ValueError("The code must be a valid!")
    if code[2] in [0, 1, 2, 3]:
        return "General"
    elif code[2] in [4, 5, 6]:
        return "VIP"
    elif code[2] in [7, 8, 9]:
        return "Platinum"

def calculate_total(prices, discount=0):
    if prices == []:
        raise ValueError("cant be empty")
    if discount not in range(0.0, 1.0):
        raise ValueError("out of range")
    if price not in prices:
        raise TypeError("not in list")
    total = sum(prices) * discount 
    return total 

