from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate

# Initialize Ollama Model
model = ChatOllama(
    model="llama3.1",
    temperature=0.2
)

# Closed-Ended Prompt Template
closedEndedPromptTemplate = PromptTemplate(
    input_variables=["question"],
    template="""
Answer the following question with only "Yes" or "No".

Question:
{question}

Do not provide any explanation.
"""
)

# Create Final Prompt
final_prompt = closedEndedPromptTemplate.format(
    question="Is Python a programming language?"
)

print("Sending prompt...")

# Generate Response
response = model.invoke(final_prompt)

print("Response:")
print(response.content)