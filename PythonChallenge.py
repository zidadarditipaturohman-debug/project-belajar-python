data = "968-maria (D@ta Engineer) ;; 27y"
data = (data.replace("968-", "name:").replace("@", "a").replace(";","").replace("(","| role: ").replace(")", " | age :").strip("y"))
print(data)