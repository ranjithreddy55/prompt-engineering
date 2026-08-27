from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
# Reference text
reference = "The cat is sitting on the mat."
# Generated/Candidate text
candidate = "The cat is sitting on the rug."
# Tokenize the texts
reference_tokens = reference.lower().split()
candidate_tokens = candidate.lower().split()
# BLEU expects a list of reference sentences
references = [reference_tokens]
# Smoothing function
smoothing = SmoothingFunction().method1
# Calculate BLEU score
score = sentence_bleu(references,
candidate_tokens,
smoothing_function=smoothing
)
# Display result
print("BLEU Score:", score)