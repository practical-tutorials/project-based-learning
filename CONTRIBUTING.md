# Contribution guidelines

Before making a pull request, please make sure of the following:

- The tutorial(s) you want to add do not already exist (search README.md for the URL and the title).
- Your tutorial is correctly placed under the appropriate language/technology section.
- The tutorial is free and open -- no paywall, login wall, or required newsletter signup.
- The tutorial is project-based -- following it, the reader builds a complete, working artifact (not just a concept explainer).
- If you're the author of the tutorial, or affiliated with the author or site, say so in the pull request.
- The pull request needs to have a descriptive title.
- If the language/technology of your tutorial does not exist, feel free to create a new entry in the table of contents.
- Make a separate pull request for each of the tutorials.
- Use the following format: `- [Title](link_to_tutorial)`.
- If your tutorial is a multi-part series, use the following format:
  ```
  - Title
    - [Part 1](link_to_part_1)
    - [Part 2](link_to_part_2)
  ```
- Check the spelling and grammar.
- Remove any trailing whitespace.
- Links must point straight to the tutorial -- no URL shorteners.

Before opening the pull request, run the validator locally from the repo root:

```
python3 scripts/check_readme.py lint
```

It must exit with status 0. It checks the grammar above, the Table of Contents, and for duplicate/shortened URLs.

CI also checks that any link you add is reachable. Some sites (Medium, Reddit, LinkedIn, Udemy, and similar) block automated checks and will show up as "could not verify" rather than failing the build -- that's expected, not something to fix.

Thank you for your suggestions! If you think there is anything to improve with the guidelines, please contact me at <tuvtran97@gmail.com>
