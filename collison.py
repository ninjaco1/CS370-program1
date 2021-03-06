import string
import random
import hashlib

# only need to check the first 24 bits
# use one way hash

#create random string
def ranstr():
    ranstring = "" 
    # make the string 10 other it will take forever
    for _ in range(10):
        # create random 
        ranstring += str(random.choice(string.ascii_letters ))
        # print ranstring
    return ranstring

def CR():
    print "Weak collision Resistant Test"
    test = 0
    total = 0
    for _ in range(3):
        trial = 0 # how many trials did it take
        test += 1
        #brute force
        while True:
            ranstr1 = ranstr()
            ranstr2 = ranstr()

            # don't want strings to be the same
            if ranstr1 == ranstr2:
                continue
            else:
                trial += 1
        
                # print "trial: ", trial
                # hash strings with md5
                # strings will be in hex
                hash1 = hashlib.md5(ranstr1.encode())
                hash2 = hashlib.md5(ranstr2.encode())

                #create strings
                hstring1 = hash1.hexdigest()
                hstring2 = hash2.hexdigest()    

                # see if 24 bits are the same
                if(hstring1[0:6] == hstring2[0:6]):
                    break

        print ("Test %s took %s trials" % (test,trial))
        total += trial
    avg = total / 3
    print("Average to break weak collision resistant: %s" % avg)

def CFR():
    print "Collision Free Resistant Tester"
    value = "142525" # random value
    total = 0
    test = 0
    for _ in range(3):
        trial = 0
        test += 1
        while True:
            trial += 1
            ranstr1 = ranstr()
            # hash with md5
            h = hashlib.md5(ranstr1.encode())
            # turn to hex
            hstring = h.hexdigest()
            if hstring[0:6] == value:
                break
        print ("Test %s took %s trials" % (test,trial))
        total += trial
    avg = total / 3
    print("Average to break collision free resistant: %s" % avg)
    

CR()
print "\n\n"
CFR()