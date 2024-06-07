# Write a simple login system where the user enters a username and password. Handle
# the KeyError by raising a custom exception if the username is not found in the users
# database(dictionary)
# CHHASKACA MICHEV VERJ
def sign_in(login,password):
    data_base = {"sipan":123456789,"dambldor":"avadagedaavra","Garry":"poter31"}
    try:
        for k,v in data_base.items():
            if k == login and v == password:
                return "login complite"
    except KeyError:
        return "Key is not found"
    
print(sign_in("sipan",123456789589989))