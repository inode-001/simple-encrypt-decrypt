key = 3
count = 0
unecryptedText = "CAT HELLO"
def encrypter(key,text):
      count = 0
      letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ '
      encrypt = ''
      for let in text:
          print(f"count{count} : {let}")
          if let in text :
            value = letters.find(let)
            newValue = value + key
            if newValue > 26 or newValue == 26:
              newValue = newValue - 26
              encrypt+=letters[newValue]
            else:
                encrypt+=letters[newValue]
          else:
               print("test")
               encrypt+=let
          count+=1
          
    
      return encrypt
print(encrypter(key,unecryptedText))
