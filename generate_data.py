# Logically Conclusive and Inconclusive KBs

import json
import os
import time
import datetime
from google import genai
import anthropic

PROMPT = """
1.  Select a polysemy noun. Each one of the polysemy noun keywords in - bat, head, nail, paper- that have two different meanings in the noun forms and with real world references. Example: bat. Add this to json key: "KB".
2. Select one fact each for each one of the two meanings for the each one of the keywords. Example: "Bat is a mammal. Bat is used in baseball." where this information is valid in real world. Add this to json key: "KB".
3. Select two distinct features of two different meanings of a given keyword and generate two new facts using "have" or "contain" depending on reference. Example: "Bats have a barrel. Bat flies with wings". Add this to json key: "KB".
4. Generate two equivalence clauses for two distinct features selected in previous step, for the two meanings of a given keyword. \textbf{(for ensuring meaning preservation by common sense, not refutation)}. Example: "Wings are not barrels. Barrels are not wings.".  Add this to json key: "KB".
5. Introduce a repeated re-assertion of a fact generated in step 3 with "can" or other relevant forms. Add this to json key: "KB".
6. Select a random color. Prepend the color to new instance of keyword and generate a query using this new colored instance to construct an introduction. For the query, use one of the two facts to replace the keyword with colored keyword instance $\textit{color} \in \textit{black, white, brown, red, yellow, blue, green, pink} $. Example: "There is a Brown bat" or "There is a pink nail" and so on. Add this to json key: "KB".
7. Add an action or negated action sentence based on step 2, replacing the noun with colored keyword instance (Ex: brown bat). The idea is to add confusion such that the action/property that could distinguish two meanings of the polysemy noun is absent, leading to inconclusiveness. Examples: "There is a brown bat. Brown bat flew." or "There is a pink nail. Pink nail did not fasten the object." Add this to json key: "KB".
8. Using the facts in step 1 such as containment or $\exists$ assertions from facts, generate a query as a statement. Example: "Query: Brown bat is a mammal", or "Query: Pink nail is part of the finger". The resulting query "Is the statement "Brown bat is a mammal" true or false or inconclusive?".
9. Generate a question with multiple choices can be framed as: "For the statement: Brown bat is a mammal, select the Correct Ans from following choices: 1. True, 2. False, 3. Inconclusive, 4. True if brown bat is a mammal and Inconclusive i.e. undecidable if brown bat could have accidentally thrown by a baseball player.".
10. Place results from steps 8 and 9 into a json list with key: "Inconclusive".
11. Generate reasoning why this KB is "Inconclusive".
12. Now combine the resulting KB in this format: {"key": "Bat", "kb": "Bat is a mammal. Bat is used in baseball. Bats have a barrel. Bat flies with wings. Wings are not barrels. Barrels are not wings. Bats can fly. There is a brown bat. Brown bat flew." "inconclusive": ["query": "Brown bat is a mammal.", "mcq": "For the statement: Brown bat is a mammal, select the Correct Ans from following choices: 1. True, 2. False, 3. Inconclusive, 4. True if brown bat is a mammal and Inconclusive i.e. undecidable if brown bat could have accidentally thrown by a baseball player.", "Reasoning": "Brown bat can be a mammal or baseball bat when a baseball player may have thrown the brown bat."]}
13. For each generated KB, generate a conclusive query, mcq, reasoning format and add a "conclusive" list with query, mcq, reasoning items and add it to the array.
14. Repeat all the steps for remaining polysemy noun keywords listed in step 1.
15. Generate other polysemy noun keywords. And repeat steps 1 to 10 for each new polysemy noun.
16. Place all generated results in a json array format.
"""
output_dir = "out"

"""## Gemini Pro 2.5 Flash KB Generation for Conclusive and Inconclusive"""

def generate_data():
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
    if GEMINI_API_KEY is None:
        raise ValueError("GEMINI_API_KEY environment variable is not set.")



    client = genai.Client(api_key = GEMINI_API_KEY)

    MODEL_ID = "gemini-2.5-flash"

    model_info = client.models.get(model=MODEL_ID)
    # print(model_info)

    response = client.models.generate_content(
        model = MODEL_ID,
        contents=PROMPT,
        config = genai.types.GenerateContentConfig(temperature=0.7)
    )
    result = response.text

    response

    results = result.replace("```json","").replace('\\"',"'").replace('\\"',"'").replace("```","")


    json_list = json.loads(results)

    filename = "gemini_generated_kbs.jsonl"

    try:
        os.makedirs(output_dir, exist_ok=True)
    except OSError as e:
        print(f"Error creating directory {output_dir}:{e}")

    file_path = os.path.join('out/', filename)

    with open(file_path, "w", encoding="utf-8") as output_file:
        json.dump(json_list, output_file, indent=4)

    assert os.path.exists(file_path), "File does not exist!"

    """## Claude KB Generation for Conclusive and Inconclusive"""

    ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')
    if ANTHROPIC_API_KEY is None:
        raise ValueError("ANTHROPIC_API_KEY environment variable is not set.")


    client = anthropic.Anthropic(api_key = ANTHROPIC_API_KEY)
    # print(client)

    message = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens = 10000,
        messages=[
            {
                "role": "user",
                "content": PROMPT,
            }
        ],
    )
    # print(message.content)

    result = message.content[0].text.replace("```json","").replace("```","")

    result

    json_list = json.loads(result)

    filename = "claude_generated_kbs.jsonl"

    try:
        os.makedirs(output_dir, exist_ok=True)
    except OSError as e:
        print(f"Error creating directory {output_dir}:{e}")

    file_path = os.path.join('out/', filename)

    with open(file_path, "w", encoding="utf-8") as output_file:
        json.dump(json_list, output_file, indent=4)

    assert os.path.exists(file_path), "File does not exist!"

def main():
    generate_data()

if __name__ == "__main__":
    main()