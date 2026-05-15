from app.agent import agent

def main() -> None:
    result = agent.run("What pricing plans does Luumen offer?")
    print(result.content)
    agent.serve(enable_server=True)

if __name__ == "__main__":
    main()
