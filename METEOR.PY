from nltk.translate.meteor_score import meteor_score
# Download required resources
import nltk
nltk.download("wordnet")
nltk.download("omw-1.4")
# Reference text
reference = "The cat is sitting on the mat."
# Generated/Candidate text
candidate = "The cat is sitting on the rug."
# Tokenize the texts
reference_tokens = reference.lower().split()
candidate_tokens = candidate.lower().split()
# Calculate METEOR score
score = meteor_score(
[reference_tokens],
candidate_tokens
)
# Display result
print("METEOR Score:", score)