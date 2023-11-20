from langchain.agents import load_tools, initialize_agent, AgentType
from tools.config import init_open_ai


def wikipedia_agent(prompt_input):
    llm = init_open_ai(0.5)
    tools = load_tools(["wikipedia",], llm=llm)
    agent = initialize_agent(
        tools=tools, llm=llm,
        agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )
    return agent.run(prompt_input)


if __name__ == "__main__":
    # example input: How many presidents has Ghana had? Provide the names of each president and the number of years they served into a json object.
    text_input = input("\nWhat would you like to know?")
    print(wikipedia_agent(text_input))
