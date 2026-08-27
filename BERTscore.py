from bert_score import score
#reference text
reference=["the cat is sitting on the mat"]
#candidate text
candidate=["the cat is sitting on the rug."]
#compute BERTScore
P, R, F1 = score(candidate, reference, lang="en", verbose=True)
#RESULT
print("BERTScore Precision: ",P[0].item())
print("BERTScore Recall: ",R[0].item())
print("BERTScore F1: ",F1[0].item())