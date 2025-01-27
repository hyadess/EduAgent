import pdfkit
import tempfile
from markdown2 import markdown
import re

#config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')


def html_start():
     # HTML header with CSS stylings
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
        <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
  <script type="text/javascript" id="MathJax-script" async
    src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
  </script>
        <style>
            body {
            font-family: 'Roboto', sans-serif;
            margin: 5%;
            font-size: 14px;
            text-align: justify;
            line-height: 1.5;
            }   

            .middle-form {
                margin-left: auto;
                margin-right: auto;
                width: 60%;
            }

            .assistant-header {
                padding: 15px;
                border-radius: 30px;
                text-align: center;
                color: white;
                background-color: #6bcd7b;
                text-transform: uppercase;
                font-weight: bold;
                margin-left: 5px;
                margin-right: 5px;
            }

            .chat-message {
                margin: 10px 0;
                padding: 10px;
                padding-left: 20px;
                padding-right: 20px;
                border-radius: 30px;
                display: flex;
                flex-direction: column;
            }

            .user-message {
                background-color: #6bcd7b;
                color: white;
                font-weight: bold;
            }

            .icon {
                margin-right: 10px;
                font-size: 1.5em;
            }

            .robot {
                color: orange;
            }

            .assistant-message {
                background-color: #f0f0f0;
            }

            .answers-table {
                width: 90%;
                border-collapse: collapse;
                margin: 30px auto;
                table-layout: fixed;
            }

            .answers-container {
                display: flex;
                flex-direction: column;
                gap: 10px;
            }

            .answer-container {
                width: 100%;
                box-sizing: border-box;
            }

            .answer-item {
                padding: 10px;
                border: 1px solid #ccc;
                border-radius: 20px;
                margin: 10px 10px;
            }

            .answer-item-2 {
                padding: 10px;
                border: none;
                margin: 10px 0;
            }

            .answer-item-3 {
                padding: 10px;
                border: none;
            }

            .image-td, .text-td {
                width: 100%;
                vertical-align: top;
            }

            .form-container {
                margin-top: 20px;
                text-align: center;
            }

            .convo-header {
                background-color: #3adfa0;
                margin-top: 50px;
                margin-bottom: 20px;
                border-radius: 30px;
                padding-top: 20px;
                padding-bottom: 20px;
                font-size: 24px;
                font-weight: bold;
                text-align: center;
                color: white;
            }

            @media (min-width: 768px) {
                body {
                    margin: 50px;
                }

                .middle-form {
                    width: 80%;
                }

                .chat-message {
                    margin-left: 100px;
                    margin-right: 100px;
                }

                .answers-container {
                    flex-direction: row;
                    justify-content: space-between;
                }

                .answer-container {
                    width: 33%;
                }

                .convo-header {
                    font-size: 30px;
                    padding-top: 40px;
                    padding-bottom: 40px;
                }
            }

            @media (min-width: 1200px) {
                body {
                    margin: 100px;
                }

                .chat-message {
                    margin-left: 300px;
                    margin-right: 300px;
                }
            }

        </style>
    </head>
    <body>
    """
    return html_content

def parse_text_with_table(text):
    # Regular expression to detect tables by checking lines with data separated by |
    table_pattern = re.compile(
        r'(?:\n|^)([|A-Za-z0-9\s]+\n(?:[|0-9\s]+\n)+)', re.MULTILINE
    )

    parsed_output = ""
    last_end = 0

    # Find each table in the text
    for match in table_pattern.finditer(text):
        # Add any text before the table as Markdown
        non_table_text = text[last_end:match.start()]
        if non_table_text.strip():
            parsed_output += markdown(non_table_text)
        
        # Process table text and replace "| |" with a newline
        table_text = match.group(0)
        table_text = re.sub(r'\|\s+\|', '|\n|', table_text)  # Insert newline between "| |"

        # Wrap the detected table in <pre> tags to preserve formatting
        parsed_output += f"<pre>{table_text.strip()}</pre>"
        
        # Update last position
        last_end = match.end()

    # Add any remaining text after the last table
    remaining_text = text[last_end:]
    if remaining_text.strip():
        parsed_output += markdown(remaining_text)
    
    return parsed_output


def write_A_convo_column(model_name, messages):
    content = ""
    content += f"""
        <td class="text-td">
        <div class="assistant-header">
            {model_name}
        </div>
        """
    for message in messages:
        text = parse_text_with_table(message.content)
        if message.role == 'user':
            content += f'<div class="answer-item user-message"><div><i class="fas fa-user icon"></i> </div><div>{text}</div></div>'
        else:
            content += f'<div class="answer-item assistant-message"><div><i class="fas fa-robot icon robot"></i></div> <div>{text}</div></div>'
        # text = markdown(message)
        # content += f'<div class="answer-item assistant-message"><div><i class="fas fa-robot icon robot"></i></div> <div>{text}</div></div>'
    # add the form here................................
    
    
    content += "</td>"
    return content

def write_An_image_column(model_name, messages,image_url,explanation):
    content = ""
    content += f"""
        <td class="image-td">
        <div class="assistant-header">
            {model_name}
        </div>
        """
    for message in messages:
        text = parse_text_with_table(message.content)
        if message.role == 'user':
            content += f'<div class="answer-item user-message"><div><i class="fas fa-user icon"></i> </div><div>{text}</div></div>'
        else:
            content += f'<div class="answer-item assistant-message"><div><i class="fas fa-robot icon robot"></i></div> <div>{text}</div></div>'
        # text = markdown(message)
        # content += f'<div class="answer-item assistant-message"><div><i class="fas fa-robot icon robot"></i></div> <div>{text}</div></div>'
    # add the form here................................

    # add an image
    content += f'<div><img src="{image_url}" alt="Image" style="width: 100%; border-radius: 20px;"></div>'
    text = parse_text_with_table(explanation)
    content += f'<div class="answer-item assistant-message"><div><i class="fas fa-robot icon robot"></i></div> <div>{text}</div></div>'
    
    
    content += "</td>"
    return content

def write_A_convo_table(conversation1,conversation2,conversation3,evaluator_no,question_no):
    content = ""

    content += f"""
        <table class="answers-table">
        <tr style="vertical-align: top;">
        """
    # the responses are just a string, convert them into an array of strings where the array will have only one element

    content += write_A_convo_column(conversation1.model_name, conversation1.messages)
    content += write_A_convo_column(conversation2.model_name, conversation2.messages)
    content += write_A_convo_column(conversation3.model_name, conversation3.messages)

    content += "</tr></table>"

    # the forms as table----------------------------------------------------------------------------------------------
    content += f"""
        <table class="answers-table">
        <tr>
        """
    code1 = f"{evaluator_no}_{question_no}_1"
    # the first column
    content += f"""
        <td>
        <div class="answer-item-2">
            <iframe src="https://docs.google.com/forms/d/e/1FAIpQLScrTvvoeXIpm2pVpRT2ZL1KK1zzvbmQik_fm6mvFDgeD4EPPA/viewform?embedded=true&usp=pp_url&entry.1311965315={code1}"
              width="600" height="1200" frameborder="0" marginheight="0" marginwidth="0"  style="transform: scale(0.8); transform-origin: top left; width: 570px; height: 1333px; border: none; padding: 0; margin: 0;">Loading…</iframe>
        </div>
        </td>
    """

    code2 = f"{evaluator_no}_{question_no}_2"
    # the second column
    content += f"""
        <td>
        <div class="answer-item-2">
            <iframe src="https://docs.google.com/forms/d/e/1FAIpQLScrTvvoeXIpm2pVpRT2ZL1KK1zzvbmQik_fm6mvFDgeD4EPPA/viewform?embedded=true&usp=pp_url&entry.1311965315={code2}" 
            width="600" height="1200" frameborder="0" marginheight="0" marginwidth="0"  style="transform: scale(0.8); transform-origin: top left; width: 570px; height: 1333px; border: none; padding: 0; margin: 0;">Loading…</iframe>
        </div>
        </td>
    """
    code3 = f"{evaluator_no}_{question_no}_3"
    # the third column
    content += f"""
        <td>
        <div class="answer-item-2">
            <iframe src="https://docs.google.com/forms/d/e/1FAIpQLScrTvvoeXIpm2pVpRT2ZL1KK1zzvbmQik_fm6mvFDgeD4EPPA/viewform?embedded=true&usp=pp_url&entry.1311965315={code3}" 
            width="600" height="1200" frameborder="0" marginheight="0" marginwidth="0"  style="transform: scale(0.8); transform-origin: top left; width: 570px; height: 1333px; border: none; padding: 0; margin: 0;">Loading…</iframe>
        </div>
        </td>
    """

    content += "</tr></table>"


    content += f"""
        <td>
        <div class="middle-form answer-item-3">
            <iframe src="https://docs.google.com/forms/d/e/1FAIpQLSdTROuWLempdBPa_AWB7jm8s8tsXiwKYXADdESy0WH4qpzAYQ/viewform?embedded=true&usp=pp_url&entry.788835600={evaluator_no}_{question_no}"
              width="800" height="1200" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>
        </div>
        </td>
    """
    return content

def write_A_image_table(conversation, image_url,explanation,imageNo,evaluator_no):
    content = ""
    
    content += f"""
        <table class="answers-table">
        <tr style="vertical-align: top;">
        """
    
    content += write_A_convo_column("Without Image", conversation.messages)
    content += write_An_image_column('With Image', conversation.messages, image_url, explanation)
    
    content += "</tr></table>"

    image_code = f"{evaluator_no}_{imageNo}"

    content+= f"""
        <div class="middle-form answer-item-3 ">
            <iframe src="https://docs.google.com/forms/d/e/1FAIpQLSco3XSolBOdzvfMDxXPc9Ob2QWPPMVc8H3ugk2XItsBkaqo1w/viewform?embedded=true&usp=pp_url&entry.1311965315={image_code}" 
            width="800" height="1000" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>
        </div>
    """

    return content
    



def generate_html(evaluation_units,image_units,evaluator_no):
    html_content = html_start()

    evaluator_code = f"{evaluator_no}"

    html_content+= f"""
        <div class="middle-form answer-item-3">
            <iframe src="https://docs.google.com/forms/d/e/1FAIpQLSdnr-ODYsDSvo7UVSvAR45tdQX6MoTtYyK--3YYuxxM7_xiRQ/viewform?embedded=true&usp=pp_url&entry.187720330={evaluator_code}" 
            width="800" height="800" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>
        </div>
    """


    for i, evaluation_unit in enumerate(evaluation_units):

        conversation1 = evaluation_unit.conversations[0]
        conversation2 = evaluation_unit.conversations[1]
        conversation3 = evaluation_unit.conversations[2]

        # a convo header
        html_content += f"""
            <div class="convo-header">
                CONVERSATION SET {i+1}
            </div>
        """

        html_content += write_A_convo_table(conversation1,conversation2,conversation3, evaluator_no,i+1)


    for i, image_evaluation_unit in enumerate(image_units):
        conversation = image_evaluation_unit.conversation
        image_url = image_evaluation_unit.image_url
        explanation = image_evaluation_unit.explanation

        html_content += f"""
            <div class="convo-header">
                IMAGE SET {i+1}
            </div>
        """

        html_content += write_A_image_table(conversation, image_url, explanation,i+1,evaluator_no)


    # model_names = [image_evaluation_unit.text_response.model_name, image_evaluation_unit.image_response.model_name]
    # imageConversation = [message.dict() for message in image_evaluation_unit.context.messages]
    # imageResponse1 = image_evaluation_unit.text_response.content
    # imageResponse2 = image_evaluation_unit.image_response.content
    # image_url = image_evaluation_unit.image_response.image_path
    # explanation = image_evaluation_unit.image_response.explanation


    # html_content += write_A_image_table(model_names,imageConversation, imageResponse1, image_url,explanation,imageResponse2)
    
    html_content += "</body></html>"

    return html_content



def save_html_to_file(html_content, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(html_content)
    print(f"HTML content saved to {filename}")


def generate_pdf(html_content):
    options = {
        'page-size': 'A4',
        'orientation': 'Landscape',  # Set the orientation to Landscape
        'margin-top': '0.5in',
        'margin-right': '0.5in',
        'margin-bottom': '0.5in',
        'margin-left': '0.5in',
        'encoding': "UTF-8",
        'no-outline': None,
    }
    
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        pdfkit.from_string(html_content, tmp_file.name, options=options)
        return tmp_file.name


