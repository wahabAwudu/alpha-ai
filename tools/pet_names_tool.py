from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from tools.config import init_open_ai


def generate_pet_names(animal, color="black"):
    llm = init_open_ai()
    prompt = PromptTemplate(
        input_variables=["animal", "color"],
        template=f"I have {animal} pet and I want a cool name for it, it is {color} in color. Suggest me 5 cool names for my pet."
    )
    data_chain = LLMChain(llm=llm, prompt=prompt, output_key="data")
    response = data_chain({"animal": animal, "color": color})
    return response


if __name__ == "__main__":
    animal_type = input("\nEnter animal type (eg: horse, cat): ")
    animal_color = input(f"\nEnter color of your {animal_type}: ")
    print(generate_pet_names(animal_type.lower(), animal_color.lower()))
