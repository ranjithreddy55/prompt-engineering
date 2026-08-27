from rouge_score import rouge_scorer
# Reference text
reference = "The cat is sitting on the mat."
# Generated/Candidate text
candidate = "The cat is sitting on the rug."
# Create ROUGE scorer
scorer = rouge_scorer.RougeScorer(
["rouge1", "rouge2", "rougeL"],
use_stemmer=True
)
# Calculate ROUGE scores
scores = scorer.score(reference, candidate)
# Display ROUGE-1
print("ROUGE-1")
print("Precision:", scores["rouge1"].precision)
print("Recall:", scores["rouge1"].recall)
print("F1 Score:", scores["rouge1"].fmeasure)
# Display ROUGE-2
print("\nROUGE-2")
print("Precision:", scores["rouge2"].precision)
print("Recall:", scores["rouge2"].recall)
print("F1 Score:", scores["rouge2"].fmeasure)
# Display ROUGE-L
print("\nROUGE-L")
print("Precision:", scores["rougeL"].precision)
print("Recall:", scores["rougeL"].recall)
print("F1 Score:", scores["rougeL"].fmeasure)