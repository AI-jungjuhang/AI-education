---
name: episode
description: Makes one video script by going through research, script, and review in order. Use only when the user calls it directly.
disable-model-invocation: true
argument-hint: [page path]
---

Target page: $ARGUMENTS

Follow these steps in order to make the script for one video. Pass each step's result to the next. If you see a problem along the way, stop and tell the user.

1. Use the researcher agent to read the target page and list 3 key points with sources.
2. Pass only that summary to the scriptwriter agent to write a scene list. Follow the make-short skill's standards for the scene list.
3. Use the reviewer agent to compare the scene list with the target page and find anything the original doesn't say.
4. Show the user the review results as a list. Fix things only after the user decides.
