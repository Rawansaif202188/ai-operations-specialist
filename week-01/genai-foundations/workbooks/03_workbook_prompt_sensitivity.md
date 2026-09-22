# In-Class Workbook: Prompt Sensitivity (10 minutes)

Paste this into a Google Colab cell and run it. It's the same greedy
pipeline from `genai-demo/colab_full_cycle.py`, wrapped in a function so
you can try many prompts quickly.

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

MODEL_NAME = "gpt2-medium"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
model.eval()

def top5(text):
    input_ids = tokenizer.encode(text, return_tensors="pt")
    with torch.no_grad():
        outputs = model(input_ids)
    next_token_logits = outputs.logits[0, -1]
    probs = torch.softmax(next_token_logits, dim=-1)
    top_probs, top_ids = torch.topk(probs, 5)
    print(repr(text))
    for p, i in zip(top_probs, top_ids):
        print(f"  {tokenizer.decode(i)!r}: {p.item():.3f}")

top5("I think the answer is")
```

## Task 1: One character can change everything

Run both and compare the top-5 predictions.

```python
top5("I think the answer is")
top5("I think the answer is,")
```

Write down what changed: 

### My Result

Adding a comma changed the top-5 predictions and their probabilities. Without the comma, the most likely token was `yes` with a probability of `0.178`. After adding the comma, the most likely token became a space followed by a quote (`'`) with a probability of `0.087`.

This shows that even a small change in the prompt can change the model's next-token predictions.


<details>
<summary>💡 What's happening</summary>

Adding a comma changes what kind of token is grammatically likely to
come next — the model isn't reasoning about meaning, it's predicting
what character/word pattern statistically follows the exact sequence of
tokens it was given. A trailing comma, space, or punctuation mark can
shift the whole distribution because it changes the model's expectation
of sentence structure.

</details>

## Task 2: Confident vs. ambiguous prompts

Run all four. For each, look at the probability of the #1 token — is it
close to 1.0 (very confident) or spread more evenly across the top 5
(uncertain)?

```python
top5("The capital of France is")
top5("The capital of that country is")
top5("My favorite color is")
top5("The most important thing in life is")
```

| Prompt                              | #1 Token Probability | Confident or uncertain? |
| ----------------------------------- | -------------------: | ----------------------- |
| The capital of France is            |      0.174 (`Paris`) | Confident               |
| The capital of that country is      |        0.048 (`the`) | Uncertain               |
| My favorite color is                |       0.062 (`blue`) | Uncertain               |
| The most important thing in life is |         0.432 (`to`) | Confident               |

### My Observation

I noticed that more specific prompts can have a higher probability for the next token, while broader prompts can have the probability spread across several possible tokens.


<details>
<summary>💡 Answer</summary>

Factual, narrowly-constrained prompts ("The capital of France is") tend
to produce one dominant, high-probability token (" Paris"). Prompts with
many reasonable continuations ("My favorite color is", "The most
important thing in life is") spread probability more evenly across the
top 5 — there's no single "correct" next word, so the model is less
confident. This is a preview of why some questions get consistent
answers from an LLM and others get different phrasing every time.

</details>

## Task 3: Try your own pair

Write two prompts that differ by only a word or two, where you predict
the completions will diverge a lot. Run `top5()` on both and see if you
were right.

```python
top5("your_prompt_1")
top5("your_prompt_2")
```

```python
top5("The student passed the")
top5("The student failed the")
```

### My Result

I used two prompts that differed by only one word:

* `The student passed the`
* `The student failed the`

The predictions were different. For `passed`, the most likely token was `test` with a probability of `0.148`. For `failed`, the most likely token was `course` with a probability of `0.073`.

This shows that changing even one word can change the model's next-token predictions and their probabilities.

## Discussion (2 minutes)

If small wording changes can shift what a model predicts, what does that
imply about how careful you need to be when writing prompts for a
production system — and why might the same prompt behave differently
across model versions?

### My Answer

Small changes in a prompt can change the model's predictions, so prompts for production systems need to be clear and carefully written.

I also learned that the same prompt may behave differently across model versions because the models can have different training data, architectures, or settings. This means prompts should be tested when the model is changed or updated.
