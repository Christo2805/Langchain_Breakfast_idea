import os
from langchain_openai import ChatOpenAI


# STEP 1: GET OPENAI API KEY

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError(
        "OPENAI_API_KEY not found. "
        "Please configure your OpenAI API key."
    )


# STEP 2: INITIALIZE OPENAI LANGUAGE MODEL

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=api_key,
    temperature=0
)


# STEP 3: CREATE THE PROMPT

prompt = """
You are a professional nutrition assistant.

Suggest exactly 5 healthy breakfast ideas.

Requirements:

1. Give exactly five breakfast ideas.
2. Include nutritious and balanced ingredients.
3. Include protein and fibre.
4. Prefer simple and affordable meals.
5. Include vegetarian breakfast options.
6. Use a numbered list.
7. Write only one idea per line.
8. Do not include any introduction.
9. Do not include explanations or conclusions.

Expected format:

1. Breakfast idea
2. Breakfast idea
3. Breakfast idea
4. Breakfast idea
5. Breakfast idea
"""


# STEP 4: SEND PROMPT TO OPENAI USING LANGCHAIN

reply = llm.invoke(prompt)


# STEP 5: PRINT ONLY THE GENERATED TEXT

print("\n===== 5 HEALTHY BREAKFAST IDEAS =====\n")

print(reply.content)


# STEP 6: END PROGRAM

print("\n===== PROGRAM COMPLETED =====")
