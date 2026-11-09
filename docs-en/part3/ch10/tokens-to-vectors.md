# Tokens become lists of numbers

<p class="ep-meta"><span>Ch. 10 · 10.1</span><span>About 6 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - A chatbot turns each token into an ID number, then turns each ID into its own ==long list of numbers (a vector)== to do its math.
    - People don't choose these numbers. They get set during training.
    - Each list of numbers works like a "location for meaning."

## From an address to coordinates

An address like "1600 Pennsylvania Avenue, Washington, DC" means something to people. But a map app turns it into **two numbers, latitude and longitude**, to work out distances. It needs numbers to do math.

A chatbot is the same. In Chapter 1, text got split into **tokens**. A computer can't do math on letters directly (a neural network works with numbers). So each token gets an **ID number**, and each ID is turned into a **list of many numbers (a vector)**. This step is called **embedding**.

!!! tip "In 10-year-old words"
    A token is like an address, and its embedding is like map coordinates. Once you have coordinates, you can measure distances.

## What a list of numbers looks like

For example, the token "potato" might become a list like this. (We made these numbers up and cut each list to 3 numbers to keep it simple.)

| Token | List of numbers (made-up example) |
|---|---|
| potato | 0.8, −0.2, 0.5 |
| sweet potato | 0.7, −0.1, 0.6 |
| car | −0.6, 0.9, 0.1 |

Real lists are much longer than 3. According to 3Blue1Brown's lesson, in GPT-3 each token becomes a list of **12,288** numbers. Its vocabulary has **50,257** tokens.

## The lookup table is the model's first part

The **lookup table** that turns token IDs into lists of numbers is the model's first part. 3Blue1Brown's lesson calls it the **embedding matrix**. Its values start out random and **are learned during training**. With 12,288 numbers for each of 50,257 tokens, this first step alone uses about 618 million numbers (617,558,016). These numbers are also part of the parameters from Chapter 9.

In other words, people don't decide which list each token gets. **The model figures it out while practicing next-word guessing.**

## Why lists of numbers?

- **To do math.** Everything inside the model is number crunching.
- **To show what's similar.** A single ID can't show that "potato" and "sweet potato" are alike. With lists of numbers, nearby lists can stand for similar meanings (next page).
- **To handle new words.** A word it has never seen can be split into known pieces, and each piece has its own list (tokens, Chapter 1).

!!! note "★ Going deeper"
    - Representing words as lists of numbers was common well before transformers. In 2013, Tomas Mikolov and others proposed two quick ways to learn word vectors from very large text collections. They reported learning good word vectors from 1.6 billion words in less than a day. This is the paper behind the well-known tool **word2vec**.
    - The list length (12,288) is a design choice made by the model's builders. 3Blue1Brown explains that very long lists give room for many different directions, which turns out to be useful.
    - Images and sound can also be turned into lists of numbers and handled in the same space as text (multimodal, Chapter 4).

## Try it yourself

**Do the math.** See how big these numbers are.

1. What is 50,257 × 12,288? Use a calculator. (It's 617,558,016.)
2. About what percent is that of GPT-3's 175 billion parameters? (About 0.35%. This first step is huge, but it's a tiny slice of the whole.)

**A quick puzzle.** Which two of these tokens probably have the closest lists of numbers: "cat," "dog," "refrigerator"? (We can't be sure, but "cat" and "dog" are the likely pair. The next page explains why.)

## Use it today

1. **Spell key words exactly.** A different spelling means a different token, which means a different list of numbers. This matters most for names.
2. **It's fine to try other words for the same idea.** Similar meanings have similar lists, so you usually get similar answers.
3. **Spell out unusual abbreviations and slang.** Rare words may split into many pieces or have fuzzy meanings.
4. **This is part of why the same idea works across languages.** But the number of pieces can differ by language (Chapter 1).
5. **Don't try to read the numbers yourself.** The meaning isn't in any single number. It's in where the whole list points.

## Common mix-ups

- "AI stores dictionary definitions of words." It stores lists of numbers learned in training, not a dictionary.
- "Each number in the list means one thing." The meaning comes from the whole list's position, not from single numbers.
- "Tokens with close ID numbers have close meanings." IDs are just labels given in order. It's the lists of numbers that need to be close.

---

## Sources and date checked

!!! quote "Sources (we read these and explain the ideas in our own words)"
    - 3Blue1Brown (Grant Sanderson), [Transformers, the tech behind LLMs](https://www.3blue1brown.com/lessons/gpt), 2024-04-01. The embedding matrix, a vocabulary of 50,257, a dimension of 12,288, 617,558,016 weights, and values learned in training. Read on 2026-11-09.
    - Tomas Mikolov and others, [Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/abs/1301.3781), arXiv, 2013-01-16. We summarized the abstract.

- **Date checked:** 2026-11-09
- **Status:** First draft
- **Note:** The numbers in the lesson are for GPT-3. Today's models differ. The 3-number lists in the table are made up. We worked out 0.35% ourselves (617,558,016 ÷ 175,000,000,000).
