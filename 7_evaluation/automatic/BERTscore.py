import pandas as pd
from bert_score import BERTScorer



data_df = pd.read_csv('./resources/llama3.1_8b_finetuned_non_replace_inference.csv')
scorer = BERTScorer(lang="en",model_type='bert-base-uncased')

def calculate_score(turn_no):
    #there is a column called 'turns' create reference and n-shot answers for rows where turns == turn_no
    reference_answers = data_df[data_df['turns'] == turn_no]['answers'].tolist()
    zero_shot_answers = data_df[data_df['turns'] == turn_no]['zero_shot_responses'].tolist()
    # one_shot_answers = data_df[data_df['turns'] == turn_no]['one_shot_responses'].tolist()
    # three_shot_answers = data_df[data_df['turns'] == turn_no]['three_shot_responses'].tolist()
    # five_shot_answers = data_df[data_df['turns'] == turn_no]['five_shot_responses'].tolist()

    # for i in range(len(reference_answers)):
    #     print("=======================================================================================")
    #     print(reference_answers[i])
    #     print('\n')

    #calculate bert score for each answer and average them
    #scorer = BERTScorer(lang="en",model_type='bert-base-uncased')
    
    p_zero, r_zero, f_zero = scorer.score(zero_shot_answers, reference_answers, verbose=False)
    # p_one, r_one, f_one = scorer.score(one_shot_answers, reference_answers, verbose=False)
    # p_three, r_three, f_three = scorer.score(three_shot_answers, reference_answers, verbose=False)
    # p_five, r_five, f_five = scorer.score(five_shot_answers, reference_answers, verbose=False)

    # average f1 score for each shot
    avg_f_zero = sum(f_zero)/len(f_zero)
    # avg_f_one = sum(f_one)/len(f_one)
    # avg_f_three = sum(f_three)/len(f_three)
    # avg_f_five = sum(f_five)/len(f_five)

    print(f"Average F1 score for {turn_no} turn zero shot: {avg_f_zero}")
    # print(f"Average F1 score for {turn_no} turn one shot: {avg_f_one}")
    # print(f"Average F1 score for {turn_no} turn three shot: {avg_f_three}")
    # print(f"Average F1 score for {turn_no} turn five shot: {avg_f_five}")




    





calculate_score(1)
calculate_score(2)
calculate_score(3)
calculate_score(4)



#llama 3.1-8b


# Average F1 score for 1 turn zero shot: 0.6481858491897583
# Average F1 score for 1 turn one shot: 0.6571285724639893  
# Average F1 score for 1 turn three shot: 0.6683547496795654
# Average F1 score for 1 turn five shot: 0.6648956537246704
# Average F1 score for 1 turn finetuning: 0.6489388942718506

# Average F1 score for 2 turn zero shot: 0.6850128769874573
# Average F1 score for 2 turn one shot: 0.6935856938362122
# Average F1 score for 2 turn three shot: 0.6993510723114014
# Average F1 score for 2 turn five shot: 0.7067257165908813
# Average F1 score for 2 turn finetuning: 0.6865230798721313

# Average F1 score for 3 turn zero shot: 0.7202037572860718
# Average F1 score for 3 turn one shot: 0.7248534560203552
# Average F1 score for 3 turn three shot: 0.7371817827224731
# Average F1 score for 3 turn five shot: 0.7328383922576904
# Average F1 score for 3 turn finetuning: 0.7170572280883789


# Average F1 score for 4 turn zero shot: 0.7270632982254028
# Average F1 score for 4 turn one shot: 0.745261013507843
# Average F1 score for 4 turn three shot: 0.7425607442855835
# Average F1 score for 4 turn five shot: 0.7414880990982056
# Average F1 score for 4 turn finetuning: 0.7292957901954651


# llama 3.2-3b

# Average F1 score for 1 turn zero shot: 0.6374279260635376
# Average F1 score for 1 turn one shot: 0.6495440602302551  
# Average F1 score for 1 turn three shot: 0.6742061376571655
# Average F1 score for 1 turn five shot: 0.6695732474327087 
# Average F1 score for 1 turn finetuning: 0.6239755749702454


# Average F1 score for 2 turn zero shot: 0.6865768432617188
# Average F1 score for 2 turn one shot: 0.6901763677597046  
# Average F1 score for 2 turn three shot: 0.7024420499801636
# Average F1 score for 2 turn five shot: 0.7000901699066162 
# Average F1 score for 2 turn finetuning: 0.6884478330612183

# Average F1 score for 3 turn zero shot: 0.6993675231933594
# Average F1 score for 3 turn one shot: 0.7130678296089172  
# Average F1 score for 3 turn three shot: 0.7182721495628357
# Average F1 score for 3 turn five shot: 0.7093568444252014
# Average F1 score for 3 turn finetuning: 0.7055696249008179

# Average F1 score for 4 turn zero shot: 0.7176064252853394
# Average F1 score for 4 turn one shot: 0.7245118021965027
# Average F1 score for 4 turn three shot: 0.7357481122016907
# Average F1 score for 4 turn five shot: 0.7290328145027161
# Average F1 score for 4 turn finetuning: 0.7143821120262146
