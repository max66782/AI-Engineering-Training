# Day 1 — Prompt Engineering

## 1. Objective

The objective of Day 1 was to understand the fundamentals of Prompt Engineering and learn how to design effective prompts that produce accurate, relevant, and structured responses from AI models.

---

## 2. What I Studied

### 2.1 What is a Prompt?

A prompt is an instruction or input provided to an AI model to generate a desired output.

**Example:**

> Explain Python to a beginner.

---

### 2.2 What is Prompt Engineering?

Prompt Engineering is the process of designing, refining, and structuring prompts to obtain better and more reliable results from AI models.

---

### 2.3 Components of an Effective Prompt

I learned the five major components of a well-structured prompt:

1. **Role** — Defines who the AI should act as.
2. **Task** — Defines what the AI needs to do.
3. **Context** — Provides relevant background information.
4. **Constraints** — Defines rules and limitations.
5. **Output Format** — Specifies how the response should be presented.

**Example:**

```text
Role:
Act as a senior technical recruiter.

Task:
Review my resume for an AI Engineering role.

Context:
Consider my background, skills, projects, and experience.

Constraints:
Focus only on skills relevant to the current role.

Output Format:
Area → Gap → Suggestion
```

---

## 3. Prompting Techniques

### 3.1 Zero-Shot Prompting

The model is asked to perform a task without providing examples.

**Example:**

```text
Classify this review as Positive, Negative, or Neutral.
```

**Key idea:** 0 examples are provided.

---

### 3.2 One-Shot Prompting

One example is provided to demonstrate the expected behavior.

**Example:**

```text
Input: "I am not feeling well."
Output: "I would like to request work from home."

Input: "I have a fever."
Output:
```

**Key idea:** 1 example is provided.

---

### 3.3 Few-Shot Prompting

Multiple examples are provided before asking the model to perform a new task.

**Example:**

```text
Python → Programming Language
Java → Programming Language
Apple → Fruit
Mango → Fruit

RAG → ?
```

**Key idea:** Multiple examples are provided.

---

## 4. Prompt Refinement

Prompt refinement means improving an existing prompt to make the expected output more accurate and useful.

**Basic prompt:**

```text
Tell me about AI.
```

**Refined prompt:**

```text
Act as an AI mentor. Explain Artificial Intelligence to a complete
beginner using simple, step-by-step language and real-world examples.
```

The refined prompt provides more context, defines the audience, specifies a role, and controls the response style.

---

## 5. Instructions vs Context

I learned to distinguish between instructions and context.

**Instruction — what the AI should do:**

```text
Explain FastAPI.
```

**Context — information about the situation:**

```text
I am a beginner in backend development.
```

Combining both allows the AI to provide a more relevant response.

---

## 6. Structured Outputs

Prompts can specify the required output structure, including JSON.

**Example:**

```text
Extract the person's name, age, and city from the given text.
Return only valid JSON using exactly these keys:
name, age, city.
```

**Expected output:**

```json
{
  "name": "Ankit",
  "age": 23,
  "city": "Delhi"
}
```

---

## 7. Prompting for Different Tasks

I practiced designing prompts for different AI tasks:

| Task | Purpose |
|---|---|
| Generation | Creating new content |
| Summarization | Reducing content to key points |
| Classification | Assigning categories |
| Extraction | Extracting specific information |
| Transformation | Converting information into another format |
| Question Answering | Answering questions using provided information |
| Code Analysis | Reviewing, debugging, or analyzing code |

---

## 8. Prompt Evaluation

I learned to evaluate a prompt using the following questions:

- Is the task clearly defined?
- Is sufficient context provided?
- Are the requirements specific?
- Are there conflicting instructions?
- Is the expected output format clear?
- Does the prompt prevent unnecessary assumptions?

---

## 9. Common Prompt Engineering Mistakes

The main mistakes I learned to avoid are:

1. Using vague instructions.
2. Providing insufficient context.
3. Not specifying the expected output.
4. Giving conflicting instructions.
5. Adding unnecessary information.
6. Assuming the AI has access to information that was not provided.
7. Not specifying how the AI should handle missing information.

---

## 10. Practical Exercise — Customer Support AI Chatbot

I designed a complete prompt for a customer-support chatbot.

### Role

Act as a professional customer support executive for the company.

### Task

Answer customer questions related to orders, products, delivery, returns, refunds, and other company-related services.

### Context

You are an AI customer-support chatbot for a specific company. The company knowledge base contains the information required to answer customer queries.

### Constraints

Use only information available in the company knowledge base. Do not make assumptions or invent information. If the answer is not available in the knowledge base, clearly state that the information is not available.

### Output Format

```text
Question: [Customer's question]
Answer: [Clear and concise answer]
```

---

## 11. Key Learnings

Through Day 1, I learned that effective prompting is not simply about asking an AI a question. It involves clearly defining the task, providing relevant context, controlling the model's behavior through constraints, and specifying the desired output.

I also learned how zero-shot, one-shot, and few-shot prompting can be used depending on whether examples are required to guide the model.

---

## 12. Practical Outcome

By the end of Day 1, I was able to:

- Design structured prompts.
- Identify the different components of a prompt.
- Use zero-shot, one-shot, and few-shot prompting.
- Refine prompts based on the desired output.
- Provide context and constraints.
- Request structured/JSON responses.
- Design prompts for different AI tasks.
- Create a complete prompt for a customer-support AI chatbot.
- Identify common prompting mistakes and evaluate prompt quality.

---

## 13. Status

**Day 1 — Prompt Engineering: COMPLETED ✅**