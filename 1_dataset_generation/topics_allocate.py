import openai
import os
import re
import json
from dotenv import load_dotenv
import pandas as pd
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

topics = {
    "Logic Gates": [
        "AND Gate", "OR Gate", "NAND Gate (Not AND Gate)", "NOR Gate (Not OR Gate)", 
        "XOR Gate (Exclusive OR Gate)", "NOT Gate", "AND Gate Using Transistors", 
        "OR Gate Using Transistors"
    ],
    "Adders": [
        "Half Adder", "Full Adder", "Implementation of Full Adder Using Half Adder"
    ],
    "Power Electronics": [
        "SCR (Silicon Controlled Rectifier)", "Forward Conducting Mode of SCR", 
        "Reverse Blocking Mode of SCR", "SCR as Inverter", "SCR as Contractor", 
        "SCR in Rectifiers", "TRIAC (Triode for Alternating Current) Application", 
        "DIAC (Diode for Alternating Current)", "IGBT (Insulated Gate Bipolar Transistor)", 
        "IGBT as Inverter", "GTO (Gate Turn-Off Thyristor)", 
        "LSCR (Light-Triggered Silicon Controlled Rectifier)", 
        "SCS (Silicon Controlled Switch)", "Thyristor"
    ],
    "Transistors": [
        "BJT (Bipolar Junction Transistor)", "FET (Field-Effect Transistor)", 
        "JFET (Junction Field-Effect Transistor)", "MOSFET (Metal-Oxide-Semiconductor Field-Effect Transistor)", 
        "UMOS (U-shaped Metal-Oxide-Semiconductor)", "VMOS (V-shaped Metal-Oxide-Semiconductor)", 
        "PMOS (P-type Metal-Oxide-Semiconductor)", "NMOS (N-type Metal-Oxide-Semiconductor)", 
        "UJT (Unijunction Transistor)", "Load Line Shift for Transistor",
    ],
    "Rectification and Diode Circuits": [
        "Diode", "Bridge Rectifier", "Center Tapped Transformer", "Rectification", 
        "Ripples", "Clipper and Clamper Circuits", "SCR in Rectifiers", "Biasing (DC, AC)"
    ],
    "Electronic Instruments": [
        "Multimeter", "VTVM (Vacuum Tube Voltmeter)", "CRT (Cathode Ray Tube)", 
        "Cathode Ray Oscilloscope", "Sawtooth Generator", "Electronic Instruments"
    ],
    "Amplifiers and Oscillators": [
        "OP AMP (Operational Amplifier)", "Voltage Buffer, Subtraction (Using OP AMP)", 
        "Power Transistor", "Amplifier", "Comparator", "Oscillator", "Astable Multivibrator"
    ],
    "Digital Electronics": [
        "RTL (Resistor-Transistor Logic)", "DTL (Diode-Transistor Logic)", 
        "TTL (Transistor-Transistor Logic)"
    ],
    "Electronic Components and Applications": [
        "Capacitor", "Photodiodes", "Photoconductive Cells", "LED (Light Emitting Diode)", 
        "LCD (Liquid Crystal Display)", "555 Timer", "RLC Circuit (Resistor, Inductor, Capacitor Circuit)", 
        "RC Circuit (Resistor, Capacitor Circuit)"
    ],
    "Miscellaneous Topics": [
        "Shockley’s Equation", 
        "Miller Effect Capacitance",  
        "Thevenin Voltage and Norton Current"
    ]
}


def get_topics():
    # Print out the structure
    full_string = ""
    for major_topic, sub_topics in topics.items():
        # print(f"{major_topic} ({len(sub_topics)} topics):")
        # for topic in sub_topics:
        #     print(f"  - {topic}")
        # every thing in one string
        full_string += f"Area:  {major_topic} ({len(sub_topics)} topics):\n"
        i=1
        for topic in sub_topics:
            full_string += f"{i}:  {topic}\n"
            i+=1

    #print(full_string)
    return full_string



def topic_fixing_using_openai(question):
    topics_text = get_topics()
    reply_json_format = """
    {
        "area": "Area 1",
        "topic": "Topic 1"
    }
    """

    # Prompt to guide the model response
    prompt = (
        f"Here is a list of major EEE areas and topics under each of the areas:\n\n"
        f"{topics_text}\n\n"
        f"Please find the topic and corresponding area for the following question in this exact format:\n\n"
        f"{reply_json_format}\n"
        f"Only respond in JSON format as shown above.\n\n"
        f"Question: {question}\n"
    )

    messages = [
        {
            "role": "system",
            "content": prompt
        },
        {
            "role": "user",
            "content": question
        },
    ]

    try:
        chat_completion = openai.chat.completions.create(
            messages=messages,
            model="gpt-3.5-turbo",
        )
        reply = chat_completion.choices[0].message.content.strip()

        # Remove code block delimiters if present
        if reply.startswith("```") and reply.endswith("```"):
            reply = re.sub(r"^```(?:json)?|```$", "", reply, flags=re.DOTALL).strip()

        reply_json = json.loads(reply)
        area = reply_json.get("area")
        topic = reply_json.get("topic")
        return area, topic
    except json.JSONDecodeError:
        print(f"Error: JSON response not in expected format.\nResponse: {reply}")
        return None, None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None, None

# topics=get_topics()
# print(topics)

df = pd.read_csv('resources/questions.csv')
questions = df['questions']

# area,topic = topic_fixing_using_openai(questions[0])
# print(area,topic)

# -------   

# for each question, find the area and topic and create two new columns in the dataframe
areadf = []
topicdf = []
for index,question in enumerate(questions):
    area, topic = topic_fixing_using_openai(question)
    areadf.append(area)
    topicdf.append(topic)

df['area'] = areadf
df['topic'] = topicdf

df.to_csv('resources/questions_with_topic.csv', index=False)



