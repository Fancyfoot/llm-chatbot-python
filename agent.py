from langchain.agents import AgentExecutor, create_react_agent
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain.tools import Tool
from langchain import hub
from llm import llm


memory = ConversationBufferWindowMemory(
    memory_key='chat_history',
    k=5,
    return_messages=True,
)


tools = [
    Tool.from_function(
        name="Chat Général",
        description="pour les échanges autour des sujets juridiques algériens",
        func=llm.invoke,
        return_direct=True
    )
]

agent_prompt = hub.pull("wessini/legal-search-agent")
agent = create_react_agent(llm, tools, agent_prompt)
agent_executor = AgentExecutor(
    agents=agent,
    tools=tools,
    memory=memory,
    verbose=True
)


def generate_response(prompt):
    """
    Create Handler That Calls the conversational agent
    and returns response to be rendered in the UI

    """

    response = agent_executor.invoke({"input": prompt})
    return response['output']
