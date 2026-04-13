# A Proof-of-Concept Method for Logical Inconclusiveness-based Abstention

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.

**Motivation for my work on this topic is based on my thought experiment on logic, and a bunch of facts and evidences:** No matter how many new carefully designed lies to force a lie to become true are added, the query to assert that the lie is not a lie, will continue to remain logically inconclusive. But on the contrary, no matter how many times a fact is denied, fact remains a grounded atom irrespective of how many ever lies are introduced to make that fact into a lie.

__Bat is a mammal. Bat is used in baseball. Bats have a barrel. Bat flies with wings. Wings are not barrels. Barrels are not wings. Bats can fly. There is a brown bat. Brown bat flew. Query: Brown bat is a mammal.__

Note: This work originally developed by me in January 2025 and underwent a metamorphosis through five stages: (1) independent research expanded during CS 830 (Spring 2025, UNH) with two very rough word document drafts reviewed by Prof. Wheeler Ruml; (2) submitted to the workshop on "Application of LLM Explainability to Reasoning and Planning" at COLM (June 2025, no feedback received); (3) fully revised following significant changes in LLM behavior across newer model versions; (4) resubmitted to the "Logical and Symbolic Reasoning in Language Models" Bridge Program at AAAI 2026 (Fall 2025, feedback received but not yet incorporated); (5) the current version employs a different method, an updated toy dataset, and reflects some of the recent developments in logical reasoning under abstention. Scripts to generate the example dataset: <a href="https://tinyurl.com/inconclusive-data-repo">https://tinyurl.com/inconclusive-data-repo</a> and <a href="https://tinyurl.com/inconclusive-sub2">https://tinyurl.com/inconclusive-sub2</a>. Preprint: <a href="https://beta.dpid.org/1076">https://beta.dpid.org/1076</a>.

As of February 6, 2026, the author is no longer affiliated with the University of New Hampshire and University of Arizona (May 2024), unfortunately it is not possible to work with either. I wish both institutions and their research communities well. This work reflects the author's (my) independent research direction, currently focused on Representational Alignment and Brain-AI alignment. Prior no-contact directives prevented continuation of this work within a fellowship context before during Fall 2025. The author continues to develop this work independently and welcomes collaboration from researchers outside of prior no-contact arrangements. For collaboration inquiries, contact: sushma.ananda13@gmail.com.

The author maintains strict boundaries between personal and professional life. Declining to collaborate with specific individuals due to prior no-contact directives reflects a mature exercise of professional boundaries and **does not indicate hatred, bias, or discrimination against any groups/categories those individuals belong to/identify with**. The author welcomes professional and mentorship connections with early-career researchers and students. **My/Author's pronouns: she/her/hers**. Any mischaracterization of these boundaries — including misgendering — will not be tolerated!!!

            
**Commercial Use:** This work is licensed for non-commercial use only. 
For any commercial use, licensing inquiries, or permissions beyond the 
scope of this license, please note that additional legal restrictions may 
apply. Any commercial use inquiry must be directed solely to the author at 
sushma.ananda13@gmail.com. Prior commercial use inquiries received before 
April 2026 are subject to pre-existing legal restrictions and are not 
applicable. Any further use or adaptation of this work remains solely under 
the copyright of the author and requires consultation with her, as well as 
her reviewers and participating mentors accordingly. All required additional supporting documentation and relevant verification can be provided accordingly.

**Copyright © 2025 Sushma Anand Akoju. All rights reserved.**

## PROMPT

1. Select a polysemy noun. Each one of the polysemy noun keywords in - bat, head, nail, paper- that have two different meanings in the noun forms and with real world references. Example: bat. Add this to json key: "KB".

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

12. Now combine the resulting KB in this format: {"key": "Bat", "kb": "Bat is a mammal. Bat is used in baseball. Bats have a barrel. Bat flies with wings. Wings are not barrels. Barrels are not wings. Bats can fly. There is a brown bat. Brown bat flew." "inconclusive": ["query": "Brown bat is a mammal.", "mcq": "For the query: Brown bat is a mammal, select the Correct Ans from following choices: 1. True, 2. False, 3. Inconclusive, 4. True if brown bat is a mammal and Inconclusive i.e. undecidable if brown bat could have accidentally thrown by a baseball player.", "Reasoning": "Brown bat can be a mammal or baseball bat when a baseball player may have thrown the brown bat."]}

13. For each generated KB, generate a conclusive query, mcq, reasoning format and add a "conclusive" list with query, mcq, reasoning items and add it to the array.

14. Repeat all the steps for remaining polysemy noun keywords listed in step 1.

15. Generate other polysemy noun keywords. And repeat steps 1 to 10 for each new polysemy noun.

16. Place all generated results in a json array format.

### Update API keys

```
echo "GEMINI_API_KEY=your_gemini_api_key" > .env
echo "ANTHROPIC_API_KEY=your_anthropic_api_key" > .env
```

To generate examples:

```
uv sync
uv run --env-file .env -- python generate_data.py

OR

uv sync
uv run generate_data.py
```


<!-- <img src="img/bat-wk-wumpus-2.png"  width="500px" height="400px" ></img> -->
