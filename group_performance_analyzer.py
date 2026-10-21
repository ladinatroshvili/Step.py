scores=[]
max_num=None
min_num=None
while True:
    userinput = input("Enter a score (or type 'stop' to finish):\n")
    if userinput == 'stop':    
        break
    try:
        score = int(userinput)
        if 0  <= score <= 10:
            scores.append(score)
            if max_num is None or score > max_num:
                max_num = score
            if min_num is None or score < min_num:
                min_num = score
        else:
            print("Score must be between 0 and 10. Please try again.")
            continue
    except ValueError:
        print("Invalid input. Please enter a valid integer score or type 'stop' to finish.")        
    
    
if len(scores) > 0:
    sum_scores = sum(scores)
    score_avarage= float(sum_scores)/len(scores)

    print(f"მიღებული ქულებია{scores},მაქსიმალური  {max_num}, მინიმალური{min_num},   საშუალო არითმეტუკული  {score_avarage}")
    