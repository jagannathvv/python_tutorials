#JSON - Javascript Object Notation. Used for data exchange
# Eg:
# {
#     "name": "tom"
#     "address": "1 Green st, NY"
#     "phone": 111222333
# }
import json

#write JSON object into a file
add_book ={} #create an empty dictionary object
add_book["tom"] = {
    'name' : 'tom',
    'address' : '1 red st, ny',
    'phone' : 111222333
}
add_book["joe"] = {
    'name' : 'joe',
    'address' : '1 green st, ny',
    'phone' : 333444555
}


s=json.dumps(add_book)
print(s)
with open("/home/training/Documents/python_tutorial/data/json_txt.txt","w") as f:
    f.write(s)

with open("/home/training/Documents/python_tutorial/data/json_txt.txt","r") as f:
    s = f.read() # read the json file as string
    add_book_r = json.loads(s) #load string into a json object(dictionary object)
    print(add_book_r)
    print(type(add_book_r)) # type of add_book_r is dictionary
    print(add_book_r['joe']) # print joes record
    print(add_book_r['joe']['phone'])# print joes phone

    #print all records in the address book
    for rec in add_book_r:
        print(add_book_r[rec]) # print entire record
        print(add_book_r[rec]['phone']) # print phone number

