from app.agent import agent

def main() -> None:
    result = agent.run("Hi! How are you doing today?")
    print(result.content)
    agent.serve(enable_server=True, port=8001)

if __name__ == "__main__":
    main()
