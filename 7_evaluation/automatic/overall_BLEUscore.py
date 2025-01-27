from sacrebleu.metrics import BLEU, CHRF, TER
import pandas as pd

data_df = pd.read_csv('./resources/llama3.1_8b_finetuned_non_replace_inference.csv')
bleu = BLEU()

def calculate_score(turn_no):
    #there is a column called 'turns' create reference and n-shot answers for rows where turns == turn_no
    reference_answers = data_df[data_df['turns'] == turn_no]['answers'].tolist()
    zero_shot_answers = data_df[data_df['turns'] == turn_no]['zero_shot_responses'].tolist()
    # one_shot_answers = data_df[data_df['turns'] == turn_no]['one_shot_responses'].tolist()
    # three_shot_answers = data_df[data_df['turns'] == turn_no]['three_shot_responses'].tolist()
    # five_shot_answers = data_df[data_df['turns'] == turn_no]['five_shot_responses'].tolist()

    
    refs = [[ref] for ref in reference_answers]
    sys_zero = zero_shot_answers
    # sys_one = one_shot_answers
    # sys_three = three_shot_answers
    # sys_five = five_shot_answers

    score_zero = bleu.corpus_score(sys_zero, refs)
    # score_one = bleu.corpus_score(sys_one, refs)
    # score_three = bleu.corpus_score(sys_three, refs)
    # score_five = bleu.corpus_score(sys_five, refs)

    print(f"Average BLEU score for {turn_no} turn zero shot: {score_zero}")
    # print(f"Average BLEU score for {turn_no} turn one shot: {score_one}")
    # print(f"Average BLEU score for {turn_no} turn three shot: {score_three}")
    # print(f"Average BLEU score for {turn_no} turn five shot: {score_five}")


  



calculate_score(1)
calculate_score(2)
calculate_score(3)
calculate_score(4)





# for llama 3.1-8b

# Average BLEU score for 1 turn zero shot: BLEU = 19.93 49.3/24.9/14.2/9.0 (BP = 1.000 ratio = 1.523 hyp_len = 402 ref_len = 264)
# Average BLEU score for 1 turn one shot: BLEU = 23.75 64.5/28.7/15.3/11.2 (BP = 1.000 ratio = 1.062 hyp_len = 172 ref_len = 162) 
# Average BLEU score for 1 turn three shot: BLEU = 20.42 47.8/25.4/15.4/9.3 (BP = 1.000 ratio = 1.481 hyp_len = 391 ref_len = 264)
# Average BLEU score for 1 turn five shot: BLEU = 20.91 47.2/26.2/15.7/9.9 (BP = 1.000 ratio = 1.508 hyp_len = 398 ref_len = 264) 
# Average BLEU score for 1 turn finetuning: BLEU = 15.96 43.0/21.1/11.4/6.3 (BP = 1.000 ratio = 1.875 hyp_len = 495 ref_len = 264)

# Average BLEU score for 2 turn zero shot: BLEU = 23.08 75.3/34.9/15.9/7.0 (BP = 0.994 ratio = 0.994 hyp_len = 348 ref_len = 350)
# Average BLEU score for 2 turn one shot: BLEU = 26.04 77.3/38.5/19.0/9.0 (BP = 0.975 ratio = 0.975 hyp_len = 313 ref_len = 321)
# Average BLEU score for 2 turn three shot: BLEU = 29.89 78.8/38.4/20.9/13.6 (BP = 0.982 ratio = 0.982 hyp_len = 217 ref_len = 221)
# Average BLEU score for 2 turn five shot: BLEU = 27.35 78.9/38.3/19.0/9.7 (BP = 1.000 ratio = 1.031 hyp_len = 270 ref_len = 262)
# Average BLEU score for 2 turn finetuning: BLEU = 21.24 66.7/30.4/13.7/7.3 (BP = 1.000 ratio = 1.177 hyp_len = 412 ref_len = 350)

# Average BLEU score for 3 turn zero shot: BLEU = 27.21 76.5/39.2/19.8/10.7 (BP = 0.963 ratio = 0.964 hyp_len = 264 ref_len = 274)
# Average BLEU score for 3 turn one shot: BLEU = 32.61 79.3/42.7/24.2/13.8 (BP = 1.000 ratio = 1.025 hyp_len = 242 ref_len = 236)
# Average BLEU score for 3 turn three shot: BLEU = 26.27 75.9/37.6/18.4/10.0 (BP = 0.976 ratio = 0.976 hyp_len = 203 ref_len = 208)
# Average BLEU score for 3 turn five shot: BLEU = 27.38 76.8/39.6/19.4/10.5 (BP = 0.976 ratio = 0.976 hyp_len = 203 ref_len = 208)
# Average BLEU score for 3 turn finetuning: BLEU = 26.98 73.1/40.2/19.8/9.9 (BP = 0.980 ratio = 0.980 hyp_len = 245 ref_len = 250)

# Average BLEU score for 4 turn zero shot: BLEU = 23.48 77.2/31.8/17.3/9.7 (BP = 0.927 ratio = 0.929 hyp_len = 158 ref_len = 170)
# Average BLEU score for 4 turn one shot: BLEU = 29.37 84.1/43.1/22.5/9.1 (BP = 1.000 ratio = 1.112 hyp_len = 189 ref_len = 170)
# Average BLEU score for 4 turn three shot: BLEU = 29.23 78.8/39.1/20.8/11.4 (BP = 1.000 ratio = 1.000 hyp_len = 170 ref_len = 170)
# Average BLEU score for 4 turn five shot: BLEU = 29.92 81.5/43.3/23.8/14.1 (BP = 0.907 ratio = 0.911 hyp_len = 195 ref_len = 214)
# Average BLEU score for 4 turn finetuning: BLEU = 31.65 81.2/42.9/23.7/12.4 (BP = 0.995 ratio = 0.995 hyp_len = 213 ref_len = 214)





# for llama 3.2-3b

# Average BLEU score for 1 turn zero shot: BLEU = 16.66 43.7/21.9/11.7/6.9 (BP = 1.000 ratio = 1.663 hyp_len = 439 ref_len = 264)
# Average BLEU score for 1 turn one shot: BLEU = 14.97 48.4/19.5/10.0/6.4 (BP = 0.953 ratio = 0.955 hyp_len = 252 ref_len = 264)
# Average BLEU score for 1 turn three shot: BLEU = 23.47 51.5/27.6/18.3/11.7 (BP = 1.000 ratio = 1.375 hyp_len = 363 ref_len = 264)
# Average BLEU score for 1 turn five shot: BLEU = 20.93 48.2/26.3/15.2/9.9 (BP = 1.000 ratio = 1.500 hyp_len = 396 ref_len = 264)
# Average BLEU score for 1 turn finetuning: BLEU = 18.54 45.9/23.4/13.8/8.0 (BP = 1.000 ratio = 1.576 hyp_len = 416 ref_len = 264)

# Average BLEU score for 2 turn zero shot: BLEU = 23.16 70.8/33.9/14.7/8.2 (BP = 1.000 ratio = 1.057 hyp_len = 370 ref_len = 350)
# Average BLEU score for 2 turn one shot: BLEU = 23.21 73.1/35.3/15.9/7.0 (BP = 1.000 ratio = 1.063 hyp_len = 372 ref_len = 350)
# Average BLEU score for 2 turn three shot: BLEU = 28.13 76.2/39.2/19.0/11.0 (BP = 1.000 ratio = 1.045 hyp_len = 302 ref_len = 289)
# Average BLEU score for 2 turn five shot: BLEU = 28.03 78.9/40.1/19.8/11.2 (BP = 0.968 ratio = 0.969 hyp_len = 280 ref_len = 289)
# Average BLEU score for 2 turn finetuning: BLEU = 21.67 72.5/35.1/15.2/5.7 (BP = 1.000 ratio = 1.060 hyp_len = 371 ref_len = 350)
    
# Average BLEU score for 3 turn zero shot: BLEU = 22.74 65.7/30.2/15.4/8.8 (BP = 1.000 ratio = 1.033 hyp_len = 379 ref_len = 367)
# Average BLEU score for 3 turn one shot: BLEU = 25.50 71.4/36.5/17.5/9.3 (BP = 1.000 ratio = 1.039 hyp_len = 294 ref_len = 283)
# Average BLEU score for 3 turn three shot: BLEU = 28.81 73.2/38.6/21.0/11.8 (BP = 0.997 ratio = 0.997 hyp_len = 317 ref_len = 318)
# Average BLEU score for 3 turn five shot: BLEU = 24.30 71.1/38.0/17.9/7.2 (BP = 1.000 ratio = 1.027 hyp_len = 377 ref_len = 367)
# Average BLEU score for 3 turn finetuning: BLEU = 23.93 69.6/32.6/16.8/8.6 (BP = 1.000 ratio = 1.035 hyp_len = 329 ref_len = 318)

# Average BLEU score for 4 turn zero shot: BLEU = 25.99 78.4/37.6/17.3/9.1 (BP = 0.996 ratio = 0.996 hyp_len = 222 ref_len = 223)
# Average BLEU score for 4 turn one shot: BLEU = 27.75 78.5/42.2/21.2/11.2 (BP = 0.932 ratio = 0.935 hyp_len = 200 ref_len = 214)
# Average BLEU score for 4 turn three shot: BLEU = 26.57 78.3/38.5/19.1/8.6 (BP = 1.000 ratio = 1.012 hyp_len = 258 ref_len = 255)
# Average BLEU score for 4 turn five shot: BLEU = 26.52 75.8/39.1/18.2/10.0 (BP = 0.980 ratio = 0.980 hyp_len = 244 ref_len = 249)
# Average BLEU score for 4 turn finetuning: BLEU = 19.77 68.9/30.2/11.8/6.8 (BP = 0.980 ratio = 0.980 hyp_len = 299 ref_len = 305)








