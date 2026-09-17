#🚀 Advanced Prompt Engineering & LLM Evaluation

A practical repository for exploring Prompt Engineering, Large Language Models (LLMs), text generation, and automated NLP evaluation.

This project demonstrates different prompting strategies and provides evaluation scripts to measure the quality and semantic similarity of generated text.

#📌 Overview

Prompt engineering plays an important role in improving the quality, consistency, and controllability of Large Language Model outputs.

This repository contains examples of:

Zero-shot prompting

One-shot prompting

Few-shot prompting

Open-ended prompting

Closed-ended prompting

Prompt templates

Text embeddings

Multilingual story generation

Adversarial prompting

Automated NLP evaluation

The repository also includes implementations of commonly used evaluation metrics such as BLEU, ROUGE, METEOR, and BERTScore.

#📂 Project Structure
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
├── prompttemplate.py     # Reusable prompt templates
├── embeddings.py         # Text embedding examples
├── storygenerator.py     # Multilingual story generation
│
└── README.md

#🧠 Prompt Engineering Techniques
##1. Zero-Shot Prompting

Zero-shot prompting asks the model to perform a task without providing examples.

Example:

Classify the following text as positive, negative, or neutral:

"I really enjoyed this movie."


This technique is useful for testing a model's baseline capabilities.

##2. One-Shot Prompting

One-shot prompting provides the model with a single example before asking it to perform the task.

Example:
Text: "I love this product."
Sentiment: Positive

Now classify:
Text: "The product is excellent."


One-shot prompting can help establish the expected format and behavior.

##3. Few-Shot Prompting

Few-shot prompting provides multiple examples to guide the model.

Text: "I love this phone."
Sentiment: Positive

Text: "This product is terrible."
Sentiment: Negative

Text: "The phone is okay."
Sentiment: Neutral

Now classify:
Text: "The camera quality is excellent."


This approach is useful when a task requires more precise formatting or behavior.

##4. Open-Ended Prompting

Open-ended prompts allow the model to generate flexible responses.

Typical applications include:

Creative writing

Brainstorming

Explanation

Summarization

Content generation

Research assistance

##5. Closed-Ended Prompting

Closed-ended prompts constrain the model's response to a predefined format or set of choices.

Typical applications include:

Classification

Sentiment analysis

Binary decisions

Information extraction

#🌍 Multilingual Story Generation

The repository includes a multilingual story generation example.

The story generator demonstrates how prompts can be structured to generate narratives in different languages while specifying requirements such as:

Story theme

Characters

Language

Tone

Length

Narrative style

This demonstrates how prompt structure can be used to control creative LLM outputs.

#📊 LLM Evaluation

Generating text is only one part of working with LLMs. Evaluating the generated output is also important.

This repository includes several NLP evaluation metrics.

##BLEU

BLEU (Bilingual Evaluation Understudy) evaluates generated text by comparing n-gram overlap between the generated output and a reference text.

File:

BLEUscore.py

##ROUGE

ROUGE (Recall-Oriented Understudy for Gisting Evaluation) measures overlap between generated and reference text and is commonly used for summarization evaluation.

File:

ROUGEscore.py

##METEOR

METEOR evaluates generated text using word-level matching while also considering factors such as stemming and synonyms.

File:

METEOR.PY

##BERTScore

BERTScore uses contextual embeddings to compare the semantic similarity between generated text and reference text.

File:

BERTscore.py


Unlike simple lexical-overlap metrics, BERTScore can capture semantic similarities between different wordings.

#🔄 Evaluation Workflow

A typical workflow using this repository is:

Prompt Design
     ↓
LLM Generation
     ↓
Generated Output
     ↓
Reference Output
     ↓
Evaluation Metrics
     ↓
Quality Analysis
     ↓
Prompt Optimization


This allows prompts to be iteratively improved based on measurable results.

#🛠️ Technologies

The project is primarily implemented using:

Python

Large Language Models

Natural Language Processing

Prompt Engineering

Text Embeddings

BLEU

ROUGE

METEOR

BERTScore

#🚀 Getting Started
##1. Clone the Repository
git clone https://github.com/ranjithreddy55/prompt-engineering.git
cd prompt-engineering

##2. Create a Virtual Environment
python -m venv venv


Activate it on Windows:

venv\Scripts\activate


On Linux/macOS:

source venv/bin/activate

##3. Install Dependencies

Install the required Python packages according to the imports used by the individual scripts.

For example:

pip install nltk rouge-score bert-score sentence-transformers


Additional dependencies may be required depending on the LLM or API used by a particular script.

##4. Run an Example

For example:

python openended.py


or:

python storygenerator.py


Evaluation scripts can be executed similarly:

python BLEUscore.py
python ROUGEscore.py
python METEOR.PY
python BERTscore.py

#🎯 Learning Objectives

This repository can be used to learn:

How prompt structure affects LLM outputs

Differences between zero-shot, one-shot, and few-shot prompting

How to design reusable prompt templates

How to control LLM-generated content

How embeddings represent text semantically

How to evaluate generated text

How lexical and semantic evaluation metrics differ

How to iteratively improve prompts using evaluation results

#🔬 Future Improvements

Potential extensions include:

Add Chain-of-Thought prompting examples

Add Role-Based prompting

Add ReAct prompting

Add structured JSON output examples

Add function/tool calling examples

Add prompt comparison experiments

Add automated prompt evaluation

Add visualization of evaluation scores

Add a requirements.txt file

Add sample datasets

Add unit tests

Add experiment tracking

Add support for additional LLM providers

#📄 License

This project is licensed under the MIT License.

#👨‍💻 Author

Ranjith Reddy

GitHub:
https://github.com/ranjithreddy55

#⭐ Support

If you find this repository useful for learning Prompt Engineering and LLM evaluation, consider giving it a ⭐ on GitHub.
