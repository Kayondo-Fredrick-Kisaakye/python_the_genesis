prompt = "\nWelcome, tell us what toppings you'd like on your Rolex!"
prompt += "\n(type 'quit' or 'done' to stop process)"
prompt += "\nEnter Here: "

stop_words = ['quit', 'done']

customer_input = ""
while customer_input != stop_words[0] and stop_words[1]:
    customer_input = input(prompt)
    
    if customer_input != stop_words[0] and stop_words[1]:
        print("i will add " + customer_input.title() + " to your rolex!")
        
# FAILED