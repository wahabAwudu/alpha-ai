from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from tools.config import init_open_ai


def generate_output(prompt_input):
    llm = init_open_ai()
    prompt = PromptTemplate(
        input_variables=["input"],
        template=f"{prompt_input}"
    )
    data_chain = LLMChain(llm=llm, prompt=prompt, output_key="data")
    response = data_chain({"input": prompt_input})
    return response


if __name__ == "__main__":
    input_text = input("\nGive me any request: ")
    print(generate_output(input_text.lower()))
