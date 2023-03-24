import openai

openai.api_key = "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"



while True:
    models = "gpt-4-0314"

    user = input("Please enter your question here: ")
    print("Please wait for 5 seconds!")
    
    if "exit" in user:
        break
    
    
    completion = openai.Completion.create(model= "text-davinci-003",
      prompt = user,
      max_tokens =  1000,
      temperature =  0.5,
      n = 1,  
      stop = None)

    response = completion.choices[0].text
    print(response)