# A Proof-of-Concept Method for Logical Inconclusiveness-based Abstention

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.

## Overview
This repository introduces a methodology for evaluating **Logical Inconclusiveness** in Large Language Models (LLMs). The research focuses on "abstention"—the ability of a system to identify when a query cannot be definitively resolved as True or False due to under-specification or polysemy [1, 5].

### Motivation
Conventional logical methods, such as standard resolution refutation (RR) and skolemization decomposition, are often not meaning-preserving [5, 6]. This work explores how LLMs can tap into world knowledge and word sense disambiguation to identify incomplete but satisfiable (SAT) logical sets where traditional RR might fail or never terminate [1, 5].

## Research Development & Authorship History
[cite_start]This project represents the independent research of **Sushma Anand Akoju**[cite: 3, 35, 727, 1005, 1281]. The following timeline documents the evolution of this work during the Spring 2025 semester. [cite_start]The timestamps on primary research artifacts—often recorded during late-night and early-morning hours—reflect the intensive independent effort dedicated to this project.
A version is hosted here: <a href="https://beta.dpid.org/1076">https://beta.dpid.org/1076</a>

| Date | Milestone / Document | Key Development |
| :--- | :--- | :--- |
| **March 11, 2025** | Initial Proposal [1]   (7:48 AM)      | Proposed measuring logical entailment in LLMs using Chain-of-Thought (CoT) prompting. |
| **April 1, 2025** | Late Evening Report  (12:43 AM) [3]| Documented manual conversion of FOL to Skolemized clausal forms to test "Meaning-Preservation". |
| **April 1, 2025** | Revised Report (2:43 AM) [2] | Formulated the "Inconclusiveness" problem using polysemy nouns (e.g., Bat, Bark). |
| **May 8, 2025** | Final Revised Proposal [5]   (3:47 PM)   | Integrated motivation sections addressing decidability limits in Resolution Refutation. |
| **May 13, 2025** | Final Project Results [2] ( 9:32 AM)     | Final evaluation across Claude 3.5, 3.7, and GPT-4o regarding ambiguity awareness. |

---
### References
* **[1]** Akoju, S. A. "CS 830 Project Proposal." March 11, 2025, 7:48AM.
* **[2]** Akoju, S. A. "CS 830 Project Proposal (2:43 AM) April 1, 2025." Modified March 23–April 1, 2025.
* **[3]** Akoju, S. A. "Project Proposal (12:43 AM)." Modified April 1, 2025.
* **[4]** Akoju, S. A. "CS 830 Project Proposal & results." Modified May 8, 2025, 3:47 PM.
* **[5]** Akoju, S. A. "CS 830 Project Project report & results." May 13, 2025, 9:32 AM.

## Methodology & Usage
The project utilizes a 16-step structured prompting procedure to generate "confusion datasets" based on polysemous nouns [2, 5].

## Complete Provenance

<a href="https://sushmaanandakoju.github.io/provenance.html">https://sushmaanandakoju.github.io/provenance.html</a>
            
## Licensing & Commercial Use
**Copyright © 2025 Sushma Anand Akoju. All rights reserved.**

This work is licensed for non-commercial use only. For licensing inquiries or permissions beyond the scope of this license, contact: sushma.ananda13@gmail.com. Note that inquiries related to use cases prior to April 2026 are subject to pre-existing legal restrictions. [Refer CODE_OF_CONDUCT.MD for more details.](https://github.com/sushmaanandakoju/logically-inconclusive-kbs/blob/main/CODE_OF_CONDUCT.md)

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
