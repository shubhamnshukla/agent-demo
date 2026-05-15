from app.agent import agent

def main() -> None:
    result = agent.run("Hi! How are you doing today?")
    print(result.content)
    agent.serve(enable_server=True)

if __name__ == "__main__":
    main()
