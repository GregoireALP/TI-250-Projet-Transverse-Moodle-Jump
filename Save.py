def save_score(score):

    score_file = "score.txt"
    best_score_file = "best_score.txt"
    with open(score_file, "r") as f:
        old_score = f.read()

    with open (score_file, "w") as f :
        f.write(str(score))

    with open (best_score_file, "r") as f :
        best_score = int(f.read())

    if score > best_score :
        best_score = score
        with open ("best_score.txt", "w") as f :
            f.write(str(best_score))
    print("Ancien score :", old_score,"\nNouveau score :", score, "\nMeilleur score :", best_score)

if __name__ == "__main__":
    save_score(8)