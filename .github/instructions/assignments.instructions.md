---
description: "Instructions to use whenever creating or editing assignment markdown files to ensure consistency and clarity for students."
applyTo: "assignments/**/*.md"
---

# Assignment Markdown Structure Guidelines

All assignment markdown files should follow these guidelines:

## 1. Template Usage

- Assignment markdown files must follow the structure in [`templates/assignment-template.md`](../../templates/assignment-template.md).
- The assignment must be created as a `README.md` file
- Do not remove or skip required sections from the template.

### Required frontmatter

- Every `README.md` assignment file must include YAML frontmatter with at least `title`, `difficulty`, and `estimated_time` fields. Example:

```yaml
---
title: "Loops and Conditionals"
difficulty: "Beginner"
estimated_time: "30-45 minutes"
---
```

## 2. Section Guidance

The section headers should reflect the structure in the template, including the exact icon usage.

- **Title**: Replace `[Assignment Title]` with a short, descriptive name (e.g., `Python Basics`, `Loops and Conditionals`, `Functions and Modules`).
- **Objective**: Write 1-2 sentences summarizing what the student will learn or accomplish. Focus on the main skills or concepts.
- **Tasks**: For each task:
   - Use a specific, action-oriented task name
   - In the Description, clearly state what the student must do.
   - In Requirements, use bullet points to list the expected outcomes or features. Be specific and measurable
   - Provide example input/output in code blocks if helpful.

- **Title**: Replace `[Assignment Title]` with a short, descriptive name (e.g., `Python Basics`, `Loops and Conditionals`, `Functions and Modules`).
- **Objective**: Write 1-2 sentences summarizing what the student will learn or accomplish. Focus on the main skills or concepts.
- **Tasks**: For each task:
   - Use a specific, action-oriented task name.
   - In the Description, clearly state what the student must do.
   - In Requirements, use bullet points to list the expected outcomes or features. Be specific and measurable.
   - Provide example input/output in code blocks if helpful.

### Prohibited content

- Do not include solutions in the assignment `README.md`. Solutions belong in `starter-code.py` or separate instructor notes.

### Quick checklist (before publishing)

- YAML frontmatter present and valid.
- All template sections filled and not removed.
- Clear objective and measurable requirements.
- Example I/O included where applicable.

Only add extra sections when they are explicitly required by the assignment (e.g., `Resources`, `Hints`).