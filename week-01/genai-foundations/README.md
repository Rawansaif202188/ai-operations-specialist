# Week 1 — GenAI Foundations

## Overview

This week focused on understanding the basic workflow behind Generative AI and Large Language Models (LLMs).

I worked through a practical GenAI demonstration that breaks the text generation process into several stages, from tokenization to autoregressive text generation.

## Topics Covered

* Tokenization
* Token IDs and decoding
* Embeddings
* Next-token prediction
* Logits and probabilities
* Autoregressive text generation
* Token sampling
* Hugging Face high-level APIs

## Practical Work

### 1. Tokenization

Explored how text is converted into tokens and token IDs, and how token IDs can be decoded back into text.

### 2. Embeddings

Examined how token IDs are mapped to numerical vectors using an embedding layer.

### 3. Next-Token Prediction

Explored how a pretrained language model assigns probabilities to possible next tokens and selects a likely continuation.

### 4. Text Generation

Studied autoregressive generation, where the model predicts and appends one token at a time until the generation limit is reached.

### 5. High-Level Generation API

Used the Hugging Face `pipeline()` API to perform text generation and compared it with the lower-level generation process.

## Key Learning

The main workflow explored during this week was:

```text
Text
 ↓
Tokenization
 ↓
Token IDs
 ↓
Embeddings
 ↓
Neural Network / Transformer
 ↓
Logits
 ↓
Probabilities
 ↓
Next-Token Selection
 ↓
Generated Text
```

## Tools & Technologies

* Python
* PyTorch
* Hugging Face Transformers
* GPT-2
* uv
* VS Code

## Training Materials

The practical exercises were completed as part of the AI Operations Specialist training. The repository contains my work and notes from the exercises I practiced during the training.

## Outcome

By the end of this week, I gained a practical understanding of how a language model processes text and generates new text token by token, as well as how high-level APIs simplify this workflow.
