from agent import run_agent

if __name__ == "__main__":
    user_input = input("Enter your problem: ")
    result = run_agent(user_input)
    print(result)
