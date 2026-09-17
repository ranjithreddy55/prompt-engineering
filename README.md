🚀 Advanced Prompt Engineering & LLM Evaluation

A practical repository for exploring Prompt Engineering, Large Language Models (LLMs), text generation, embeddings, and automated NLP evaluation.

This project demonstrates different prompting techniques and evaluation methods for understanding and improving the quality of Large Language Model outputs.

📌 Overview

Prompt Engineering is the process of designing and optimizing prompts to guide Large Language Models toward producing useful, accurate, and consistent responses.

This repository contains practical examples covering:

Zero-shot prompting

One-shot prompting

Few-shot prompting

Open-ended prompting

Closed-ended prompting

Prompt templates

Text embeddings

Multilingual story generation

Adversarial prompting

LLM output evaluation

The repository also includes implementations of popular NLP evaluation metrics such as:

BLEU

ROUGE

METEOR

BERTScore

📂 Project Structure
prompt-engineering/
│
├── BERTscore.py          # BERTScore evaluation
├── BLEUscore.py          # BLEU score evaluation
├── METEOR.PY             # METEOR evaluation
├── ROUGEscore.py         # ROUGE score evaluation
│
├── adversial.py          # Adversarial prompting examples
├── closedended.py        # Closed-ended prompting
├── openended.py          # Open-ended prompting
├── prompttemplate.py     # Prompt template examples
├── embeddings.py         # Text embedding examples
├── storygenerator.py     # Multilingual story generation
│
└── README.md             # Project documentation

🧠 Prompt Engineering Techniques
1. Zero-Shot Prompting

Zero-shot prompting asks an LLM to perform a task without providing any examples.

Example:

Classify the following text as Positive, Negative, or Neutral:

"I really enjoyed this movie."


The model needs to understand the task based only on the instructions provided.

Use cases:

Text classification

Sentiment analysis

Summarization

Question answering

Information extraction

2. One-Shot Prompting

One-shot prompting provides the model with a single example before asking it to perform the task.

Example:

Example:

Text: "I love this product."
Sentiment: Positive

Now classify:

Text: "The product is excellent."


The example helps the model understand the expected task and output format.

3. Few-Shot Prompting

Few-shot prompting provides multiple examples to guide the model.

Example:

Text: "I love this phone."
Sentiment: Positive

Text: "This product is terrible."
Sentiment: Negative

Text: "The phone is okay."
Sentiment: Neutral

Now classify:

Text: "The camera quality is excellent."


Few-shot prompting is useful when the task requires a specific format or behavior.

4. Open-Ended Prompting

Open-ended prompts allow the LLM to generate flexible responses without restricting the answer to predefined options.

Examples include:

Creative writing

Story generation

Brainstorming

Explanations

Summarization

Content generation

Question answering

Example:

Write a short story about a student who discovers an ancient technology.

5. Closed-Ended Prompting

Closed-ended prompting restricts the model's response to a specific format, category, or set of choices.

Example:

Is the following statement true or false?

"Python is a programming language."

Answer only with True or False.


This approach is useful for:

Classification

Binary decisions

Sentiment analysis

Multiple-choice questions

Information extraction

📝 Prompt Templates

Prompt templates allow reusable instructions to be created for different tasks.

Instead of writing a complete prompt every time, variables can be inserted into a predefined structure.

Example:

You are an expert in {topic}.

Explain {concept} in simple terms
for a {audience} audience.


This makes prompts easier to reuse, maintain, and modify.

The repository contains examples demonstrating prompt template usage.

🌍 Multilingual Story Generation

The project includes a multilingual story-generation example demonstrating how prompts can be used to generate stories in different languages.

The prompt can be structured around parameters such as:

Language

Story theme

Characters

Tone

Length

Narrative style

Example concept:

Generate a short story in Telugu.

Theme: Artificial Intelligence
Characters: Student and AI Assistant
Tone: Inspirational
Length: 500 words


This demonstrates how prompt instructions can be used to control the characteristics of generated content.

🔤 Text Embeddings

The repository also contains an example related to text embeddings.

Text embeddings represent text as numerical vectors that capture aspects of its semantic meaning.

Embeddings can be used for applications such as:

Semantic similarity

Text clustering

Search

Recommendation systems

Document comparison

Retrieval-Aug
