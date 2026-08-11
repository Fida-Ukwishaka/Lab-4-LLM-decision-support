SUMMARY_PROMPT = """
You are a helpful assistant summarizing loan application letters for a microfinance loan officer.

Summarize the letter in a concise and factual way.

Include:
- Applicant name
- Amount requested
- Purpose of the loan
- Business or source of income
- Financial information mentioned
- Collateral or guarantor information
- Proposed repayment plan
- Any other important information relevant to the loan application

Only use information explicitly stated in the letter.
Do not guess or add information that is not provided.
Keep the summary brief and easy for a loan officer to understand.

LETTER:
{letter_text}
"""


EXTRACT_PROMPT = """
You are an information extraction assistant for a microfinance loan decision-support system.

Extract information ONLY from the letter provided.

Return ONLY a valid JSON object with EXACTLY these keys:

{
  "applicant_name": "string",
  "amount_ghs": number,
  "purpose": "string",
  "monthly_profit_ghs": number or null,
  "has_collateral_or_guarantor": boolean,
  "repayment_months": number or null
}

Rules:
- If a field is not stated in the letter, use null.
- Do not guess or infer missing information.
- amount_ghs must be a number.
- monthly_profit_ghs must be a number or null.
- repayment_months must be a number or null.
- has_collateral_or_guarantor must be true if collateral or a guarantor is explicitly mentioned, otherwise false.
- Return ONLY the JSON object.
- Do not include explanations.
- Do not include markdown or ```json fences.
- Do not add any extra keys.

Example:

Letter:
"My name is Ama Mensimah. I am requesting GHS 10,000 to buy equipment for my bakery.
The bakery makes GHS 1,200 profit per month. My brother will guarantee the loan.
I will repay the loan over 10 months."

Correct output:
{
  "applicant_name": "Ama Mensimah",
  "amount_ghs": 10000,
  "purpose": "buy equipment for bakery",
  "monthly_profit_ghs": 1200,
  "has_collateral_or_guarantor": true,
  "repayment_months": 10
}

Now extract the information from this letter:

{letter_text}
"""


BRIEF_PROMPT = """
You are assisting a microfinance loan officer.

Using the original loan application letter and the extracted JSON, produce a short decision-support brief.

Your response MUST contain exactly these four sections:

1. Strengths
- Use bullet points.
- Every strength must be grounded in information explicitly stated in the letter.

2. Risks / Red Flags
- Use bullet points.
- Identify concerns or risk factors based only on the letter and extracted information.
- Do not invent facts.

3. Missing Information
- Use bullet points.
- List information that the loan officer should request if it is missing or unclear.

4. Suggested Next Step
- Give a practical next step for the loan officer.
- Examples include "invite for interview", "request documents", or "flag for senior review".
- Do NOT say "approve" or "reject".

IMPORTANT:
- The final lending decision is made by a human loan officer.
- You are providing decision support only, not making the final decision.
- Do not invent or assume information that is not present.
- Keep the brief concise and clear.

ORIGINAL LETTER:
{letter_text}

EXTRACTED JSON:
{extracted_json}
"""
