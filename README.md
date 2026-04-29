# A Proof-of-Concept Method for Logical Inconclusiveness-based Abstention

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.

## Overview
[cite_start] This repository introduces a methodology for evaluating **Logical Inconclusiveness** in Large Language Models (LLMs)[cite: 47, 120]. [cite_start]The research focuses on "abstention"—the ability of a system to identify when a query cannot be definitively resolved as True or False due to under-specification or polysemy[cite: 52, 55, 119].


**Motivation for my work on this topic is based on my thought experiment on logic, and a bunch of facts and evidences:** No matter how many new carefully designed lies to force a lie to become true are added, the query to assert that the lie is not a lie, will continue to remain logically inconclusive. But on the contrary, no matter how many times a fact is denied, fact remains a grounded atom irrespective of how many ever lies are introduced to make that fact into a lie. A simple answer for someone asked to verify a set of facts/evidences, given query, would require someone to identify when there is not enough information to conclude. Analogous to how most human-generated responses do not abstain under incomplete but satisfiable (SAT) logical set (by conventional skolemization decomposition). Conventional skolemization decomposition is not meaning-preserving and do not align with inherent logical inconclusiveness. Traditional resolution refutation may not resolve this. This may be challenging when the problem of evaluating logical (in)conclusiveness is configured with world knowledge and commonsense reasoning. But there are other directions to verify this by tapping into the other capabilities of LLMs. 

[cite_start]Conventional logical methods, such as standard resolution refutation and skolemization decomposition, are often not meaning-preserving and can fail to align with inherent logical inconclusiveness in natural language[cite: 64, 65, 106]. [cite_start]This work explores how LLMs can tap into world knowledge and word sense disambiguation to identify incomplete but satisfiable (SAT) logical sets[cite: 115, 117].

__Bat is a mammal. Bat is used in baseball. Bats have a barrel. Bat flies with wings. Wings are not barrels. Barrels are not wings. Bats can fly. There is a brown bat. Brown bat flew. Query: Brown bat is a mammal.__

**Example Case: Polysemy Confusion**
> *Bat is a mammal. Bat is used in baseball. Bats have a barrel. Bat flies with wings. Wings are not barrels. Barrels are not wings. Bats can fly. There is a brown bat. Brown bat flew.* [cite: 155, 156]  
> [cite_start]**Query:** *Brown bat is a mammal.* [cite: 157]  
> [cite_start]**Result:** *Inconclusive* (The context does not specify if this "brown bat" is the animal or a brown-colored baseball bat)[cite: 247, 248].

## Research Development & Authorship History
This project represents the independent research of **Sushma Anand Akoju**. The following timeline documents the evolution of this work during the Spring 2025 semester. The timestamps on primary research artifacts—often recorded during late-night and early-morning hours—reflect the intensive independent effort dedicated to this project.

| Date | Milestone / Document | Key Development |
| :--- | :--- | :--- |
| **March 11, 2025** | [cite_start][Initial Proposal] [cite: 3] | [cite_start]Proposed measuring logical entailment in LLMs using Chain-of-Thought (CoT) prompting[cite: 15]. |
| **March 31, 2025** | [cite_start][Revised Report (2:43 AM)] [cite: 1002, 1004] | [cite_start]Introduced the "Inconclusiveness" problem using polysemy nouns (e.g., Bat, Bark)[cite: 1012, 1014]. |
| **April 1, 2025** | [cite_start][Nite Report (12:43 AM)] [cite: 1726, 1729] | [cite_start]Documented manual conversion of FOL to Skolemized clausal forms to test "Meaning-Preservation"[cite: 1739, 1807]. |
| **May 8, 2025** | [cite_start][Final Revised Proposal] [cite: 1282, 1284] | [cite_start]Integrated motivation sections addressing decidability limits in Resolution Refutation[cite: 1298, 1302]. |
| **May 13, 2025** | [cite_start][Final Project Results] [cite: 36, 38] | [cite_start]Final evaluation across Claude 3.5, 3.7, and GPT-4o regarding ambiguity awareness[cite: 138, 237]. |


## Methodology & Usage
[cite_start]The project utilizes a structured prompting procedure to generate "confusion datasets" based on polysemous nouns[cite: 119, 179].
            
## Licensing & Commercial Use
**Copyright © 2025 Sushma Anand Akoju. All rights reserved.**

This work is licensed for non-commercial use only. For licensing inquiries or permissions beyond the scope of this license, contact: sushma.ananda13@gmail.com. Note that inquiries related to use cases prior to April 2026 are subject to pre-existing legal restrictions.

## Methodology & Dataset Generation
The project includes a 16-step structured prompting procedure to generate "confusion datasets" based on polysemous nouns.

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
