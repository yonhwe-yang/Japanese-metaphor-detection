from openai import OpenAI
import csv
# 初始化客户端
client = OpenAI(
    api_key="sk-0Obo6KWguHXjEMtU23A00e4e40F14901Ac65D02f86Bf6aBd", base_url="https://api.apiyi.com/v1"
)

# system prompt：定义模型角色和任务规则
system_prompt = """
You are a linguistic research assistant specializing in metaphor studies.
"""


# Read input file
with open(r"C:\Users\86159\Desktop\input01.txt", "r", encoding="utf-8") as file:
    lines = [line.strip() for line in file if line.strip()]

total = len(lines)
results = []

# Process each line
for idx, text in enumerate(lines, 1):
    print(f"Processing {idx}/{total}: {text}")

    user_prompt = f"""
Please analyze the following sentence and provide a answer.

Sentence: {text}

Please output in the following format:
Reasonable or make sense: Yes / No
Explanation: 

"""

    completion = client.chat.completions.create(
        model="gpt-5.4",
        temperature=0.1,
        reasoning_effort="none",
        stream=False,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )

    result = completion.choices[0].message.content.strip()
    print(f"Result: {result}\n")

    results.append([idx, text, result])

# Save as CSV
with open("outputsimiliarity.csv", "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.writer(file)
    writer.writerow(["ID", "TEXT", "RESULT"])
    writer.writerows(results)

print(f"Finished. Total processed: {total}")