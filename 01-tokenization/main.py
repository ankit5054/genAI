import tiktoken 

enc = tiktoken.encoding_for_model("gpt-4o")
userInput= "Hi, I would love to go on world tour."
token=enc.encode(userInput)
print(token)

token=[12194, 11, 4843, 1652, 668, 13]
userInput=enc.decode(token)
print(userInput)