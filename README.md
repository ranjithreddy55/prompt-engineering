# Advanced Prompt Engineering & LLM Evaluation

A production-ready repository dedicated to structured prompt engineering methodologies and automated evaluation metrics. This project contains highly optimized prompt templates ranging from foundational classification tasks to complex multilingual generation, paired with rigorous NLP evaluation frameworks.

## Core Prompt Engineering Categories

* **Zero-Shot Prompts:** Direct task execution without prior examples to test baseline model capability.
* **One-Shot Prompts:** Single-example provisioning to establish target formatting, tone, and constraints.
* **Few-Shot Prompts:** Multi-example in-context learning to guide complex reasoning and deterministic outputs.
* **Closed-Ended Prompts:** Structural constraints designed for classification, sentiment analysis, and binary extraction.
* **Open-Ended Prompts:** Expansive, creative instructions optimized for brainstorming, analysis, and synthesis.

## Specialized Applications

* **Multilingual Story Generator:** Advanced dynamic prompts engineered to generate high-coherence creative narratives across multiple target languages while maintaining cultural nuances and idiomatic accuracy.

## Automated Evaluation Metrics

To quantitatively measure prompt performance, generation quality, and model drift, this project integrates the following text-generation evaluation frameworks:

* **BLEU (Bilingual Evaluation Understudy):** Measures precision by matching n-grams between the generated text and reference text.
* **ROUGE (Recall-Oriented Understudy for Gisting Evaluation):** Focuses on recall, measuring overlapping n-grams to evaluate summarization and content retention.
* **METEOR:** Evaluates translation and generation quality by incorporating synonymy, stemming, and exact word matches.
* **BERTScore:** Utilizes contextual embeddings from BERT to calculate semantic similarity between generations and references, moving beyond exact keyword matching.

## How to Use This Project

1. **Select a Technique:** Choose the appropriate prompting directory based on your evaluation or generation goals.
2. **Populate Placeholders:** Inject your specific data into the bracketed input variables inside each template.
3. **Run Evaluation:** Use the metric scripts to score the model's output against your ground-truth reference datasets.

## Contributing

Contributions are welcome! Please submit a pull request with your optimized prompt templates or metric implementation updates.

## License

This project is licensed under the MIT License.
