from openai import OpenAI

client = OpenAI()

update = input("Enter your project update:\n")

response = client.responses.create(
    model="gpt-5",
    input=f"""
You are an AI Technical Program Manager.

Analyze the following project update:

{update}

Produce a structured program assessment with these sections:

1. PROGRAM HEALTH
   - Green, Amber, or Red
   - Explain why

2. TOP RISKS
   For each risk provide:
   - Risk
   - Impact
   - Mitigation
   - Owner

3. DEPENDENCIES
   Identify dependencies that could affect the schedule.

4. ISSUES
   Identify problems that require immediate action.

5. RECOMMENDED ACTIONS
   Provide specific actions and suggested owners.

6. EXECUTIVE SUMMARY
   Summarize the situation in 5 bullets.

Do not invent facts that are not supported by the project update.
Clearly identify assumptions.
"""
)

print("\nAI TPM PROGRAM ASSESSMENT:\n")
print(response.output_text)