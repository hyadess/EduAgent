import pandas as pd
import ast
import htmlGenerator
import convo_eval_models


evaluator_no=1
convo1=1
convo2=2
convo3=3
convo4=4


import sys
if len(sys.argv) > 5:
    evaluator_no = int(sys.argv[1])
    convo1 = int(sys.argv[2])
    convo2 = int(sys.argv[3])
    convo3 = int(sys.argv[4])
    convo4 = int(sys.argv[5])




# Load the CSV files
model1_df = pd.read_csv('../5_convo_human_evaluation_prep/test_conversations_shareGPT/gpt-4o-human_evaluation.csv')
model2_df = pd.read_csv('../5_convo_human_evaluation_prep/test_conversations_shareGPT/llama3.1_8b_finetuned.csv')
model3_df = pd.read_csv('../5_convo_human_evaluation_prep/test_conversations_shareGPT/llama3.1_8b_few_shot.csv')





def create_a_evaluation_convo(conversation_no,model_df,model_name):
    selected_conversation = model_df.iloc[conversation_no]['conversations']

    conversation_list = ast.literal_eval(selected_conversation)

    # create a conversation model for the conversation

    conversation = convo_eval_models.Conversation(messages=[], model_name=model_name)
    for item in conversation_list:
        # Map 'from' to 'role' and 'value' to 'content'
        role = item['from']
        content = item['value']

        if role == 'human':
            role = 'user'
        if role == 'gpt':
            role = 'assistant'
        # for every  item, create a message object
        message = convo_eval_models.Turn(role=role, content=content)
        # Append the formatted message to the list
        conversation.messages.append(message)
    
    # return the conversation model
    return conversation


def create_a_evaluation_unit(conversation_no):
    conversation1 = create_a_evaluation_convo(conversation_no,model1_df,'model 1')
    conversation2 = create_a_evaluation_convo(conversation_no,model2_df,'model 2')
    conversation3 = create_a_evaluation_convo(conversation_no,model3_df,'model 3')

    return convo_eval_models.EvaluationUnit(conversations=[conversation1, conversation2, conversation3])


def create_a_image_evaluation_unit(evaluator_no):
    df=pd.read_csv(f'./resources/images.csv')
    # select 2 images from index 2*evaluator_no and 2*evaluator_no-1
    image1 = df.iloc[2*evaluator_no-1]
    image2 = df.iloc[2*evaluator_no]

    # create 2 image evaluation units

    messages=[
        convo_eval_models.Turn(role='user',content=image1['question1']),
        convo_eval_models.Turn(role='assistant',content=image1['answer1']),
    ]
    conversation = convo_eval_models.Conversation(messages=messages, model_name='image model')
    image1_evaluation_unit = convo_eval_models.ImageEvaluationUnit(conversation=conversation, image_url=image1['image_url'], explanation=image1['explanation'])

    messages2=[
        convo_eval_models.Turn(role='user',content=image2['question1']),
        convo_eval_models.Turn(role='assistant',content=image2['answer1']),
    ]
    conversation2 = convo_eval_models.Conversation(messages=messages2, model_name='image model')
    image2_evaluation_unit = convo_eval_models.ImageEvaluationUnit(conversation=conversation2, image_url=image2['image_url'], explanation=image2['explanation'])

    return image1_evaluation_unit, image2_evaluation_unit







# def create_a_image_evaluation_unit(conversation_no,response_df):
#     selected_conversation = context_df.iloc[conversation_no]['conversations']

#     conversation_list = ast.literal_eval(selected_conversation)

#     # create a context model for the conversation

#     context = models.Context(messages=[])
#     for item in conversation_list:
#         # Map 'from' to 'role' and 'value' to 'content'
#         role = item['from']
#         content = item['value']

#         if role == 'human':
#             role = 'user'
#         if role == 'gpt':
#             role = 'assistant'
#         # for every  item, create a message object
#         message = models.Message(role=role, content=content)
#         # Append the formatted message to the list
#         context.messages.append(message)
    
#     # create text response
#     text_response = models.ModelResponse(model_name='text model', content=response_df.iloc[conversation_no]['fine_tune_responses'])

#     # create image response

#     # at first, do similarity search for the content of the previous text response
#     db = get_chroma_db()
#     # if the similarity score is lower than 0.6, don't show the image
    
#     fetched_images = db.similarity_search(text_response.content)
#     print("fetched images",text_response.content)
#     if len(fetched_images) == 0:
#         # image url and explanation are none
#         image_path = None
#         explanation = None
#     else:
#         # get the first image
#         image_path = fetched_images[0].metadata['image_url']
#         explanation = fetched_images[0].metadata['explanation']
#         print("image path",image_path)
#         print("explanation",explanation)




#     image_response = models.ImageResponse(model_name='image model', content=response_df.iloc[conversation_no]['fine_tune_responses'], image_path=image_path, explanation=explanation)

#     return models.ImageEvaluationUnit(context=context, text_response=text_response, image_response=image_response)

    



    


evaluation_unit1 = create_a_evaluation_unit(convo1)
evaluation_unit2 = create_a_evaluation_unit(convo2)
evaluation_unit3 = create_a_evaluation_unit(convo3)
evaluation_unit4 = create_a_evaluation_unit(convo4)
image_unit1, image_unit2 = create_a_image_evaluation_unit(evaluator_no)

# image_evaluation_unit1 = create_a_image_evaluation_unit(44,response1_df)


html_content = htmlGenerator.generate_html([evaluation_unit1, evaluation_unit2, evaluation_unit3, evaluation_unit4],[image_unit1,image_unit2],evaluator_no)


htmlGenerator.save_html_to_file(html_content, f'../convo_htmls/evaluator_{evaluator_no}.html')