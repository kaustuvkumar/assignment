

def  keysData(Dict,keys):
    #Ensure no of keys is 3
 if (keys.count('/')==2):
    key1 , key2 , key3 = keys.split('/',3)
    #Check if key value is not empty
    if(len(key1)!=0 and len(key2)!=0 and len(key3)!=0):
        return (Dict[key1][key2][key3])
    else:
        return ("Check input key value")
 else:
     return ("Incorrect no of keys")

#Sample object1 
test_dict1={"a":{"b":{"c":"d"}}}

#Test for positive case
result=keysData(test_dict1,'a/b/c')
assert result =='d' ,"value mismatched"

#Test if no of keys is less than 3
result=keysData(test_dict1,'a/b')
assert result =='Incorrect no of keys',"value mismatched"

#Sample object2
test_dict2= {"Dict11":{"Dict1":{"name":"n1","age":"a1"},
                      "Dict2":{"name":"n2","age":"a2"}},
            "Dict12":{"Dict1":{"name":"n3","age":"a3"},
                      "Dict2":{"name":"n4","age":"a4"}}}

#Test positive case
result=keysData(test_dict2,"Dict11/Dict1/name")
assert result =='n1',"value mismatched"

#Test negative case, when one of the key is blank
result=keysData(test_dict2,"Dict12/Dict2/")
assert result =='Check input key value',"value mismatched"


 
