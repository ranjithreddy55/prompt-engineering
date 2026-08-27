from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate

# Initialize Ollama Model
model = ChatOllama(
    model="llama3.1",
    temperature=0.7
)

# Open-Ended Prompt Template
openEndedPromptTemplate = PromptTemplate(
    input_variables=[
        "role",
        "subject",
        "topic",
        "plagiarism",
        "grammar",
        "audience"
    ],
    template="""
Act like a professional {role}. Your goal is to write a long chapter on the topic "{topic}"
from the subject "{subject}" with plagiarism level {plagiarism}.

Throughout the chapter, maintain grammar at the {grammar} level
so that the {audience} audience can understand the concept easily.

Write only the chapter.
"""
)

# Create Final Prompt
final_prompt = openEndedPromptTemplate.format(
    role="university level professor",
    subject="Machine Learning",
    topic="Bias & Variance",
    plagiarism="0%",
    grammar="beginner",
    audience="beginner"
)

print("Sending prompt...")

# Generate Response
response = model.invoke(final_prompt)

print("Response:")
print(response.content)