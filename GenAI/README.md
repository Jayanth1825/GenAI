# Day 1 — LLM Foundations

## Objective
Learn tokens, prompt basics, and API integration.

## What I built
- Connected to OpenRouter API
- Used an LLM model (nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free)
- Generated responses using prompts

## Concepts learned
- Tokens
- Prompting
- API calls
- Environment variables

## Sample prompt
"Explain tokens in simple words"

## Tech stack
- Python
- PyCharm
- OpenRouter

## What I Learned
- Given different types of prompts to the model and observed the difference in output
- API Connections


# Day 2 - Prompt Engineering Basics
- Zero shot Prompting
- Few shot Prompting

# Day 3 - System Prompts vs User Prompts
- Learned difference between System prompt and user prompt
- Given different scenarios to the model and observed the difference in output.

# Day 4 - Structured Outputs and JSON Format
- Learned what is JSON.
- Tested on a resume to extract key values from the resume in JSON Format.

# Day 5 - Function/Tool Calling Basics
- Learned how LLMs uses external tool calling when required
- LLMs can decide when to use external tools.

# Day 6 - Built first version of Resume Analyzer
- Extracted skills, projects and Experience sections from Resume and given feedback accordingly
- Suggested improvements to make resume ATS friendly.

# Day 7 - Built basic Streamlit UI for Resume Analyzer
- Given input skills, projects, experience.
- Done JSON Parsing.
- Given Score based on skills, projects and experience.

# Day 8 - Cost and Token Optimization
- Given Long Prompt and Short Prompt to the model
# Long Prompt
Prompt Tokens: 59
Completion Tokens: 1795
Total Tokens: 1854
# Short Prompt
Prompt Tokens: 36
Completion Tokens: 180
Total Tokens: 216
- Shorter prompts reduced token usage by 88% while maintaining useful output

# Day 9 - Context Window Limitations
- Learned about context window limitations.
- Given long inputs to the model and observed that latency is higher than shot inputs.