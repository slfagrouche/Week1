


# "Pooh"	"Oh bother!"
# "Tigger"	"TTFN: Ta-ta for now!"
# "Eeyore"	"Thanks for noticing me."
# "Christopher Robin"	"Silly old bear."


hashmap = {"Pooh": "Oh bother!",
            "Tigger":"TTFN: Ta-ta for now!"}

def print_catchphrase(character):
    if character == "Pooh":
        print("Oh bother!")
    elif character == "Tigger":
        print("TTFN: Ta-ta for now!")
    elif character == "Eeyore":
        print("Thanks for noticing me.")
    elif character == "Christopher Robin":
        print("Silly old bear.")
        
def print_catchphrase1(character):
    if character in hashmap :
        print(hashmap[character])
        

        
    
	
	
character1 = "Pooh"
print_catchphrase(character1) # "Oh bother!"
print_catchphrase1(character1)
