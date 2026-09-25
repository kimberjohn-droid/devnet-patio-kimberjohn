# Module 1 — Git & GitHub

**Student:** Kimber John F. Patio
**Date:** September 25, 2026

---

## What is Git? What is GitHub? (explain like you're teaching a friend who's never used either)

Git is a tool that keeps track of changes in my code. It helps me save different versions of my work so I can see what I changed and go back to an older version if needed.

GitHub is a website where I can store my Git repositories online. It also lets me work with branches, pull requests, and other people on the same project.

---

## Key vocabulary (in your own words)

- Repository: a place where the project files and Git history are stored
- Commit: a saved change in the project
- Branch: a separate version of the project where I can work on changes
- Push / pull: push sends my changes to GitHub, while pull gets changes from GitHub
- Pull request: a request to add changes from one branch into another
- Merge conflict: a problem that happens when Git cannot automatically combine changes

---

## Walking through what I did

I created a branch called `lesson1-variables` instead of working directly on `main`. I edited the Lesson 1 file, committed my changes, and then created a Pull Request to merge my branch into `main`.

```bash
git checkout -b lesson1-variables
git add module-2-python-basics/lesson-1-variables-datatypes.py
git commit -m "Complete Lesson 1: Variables and Data Types"
git push origin lesson1-variables
