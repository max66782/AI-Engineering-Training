# Day 7 — GitHub CI/CD & Collaboration

## Objective

Learn and practice a professional GitHub workflow involving:

- Git branches
- Feature development
- Commits
- Pushing branches
- Pull Requests
- Code review
- Merging
- GitHub collaboration
- Basic CI/CD concepts

---

## Git Workflow

The workflow practiced in this project is:

    main
      ↓
    Create feature branch
      ↓
    Make changes
      ↓
    Test changes
      ↓
    Commit changes
      ↓
    Push feature branch
      ↓
    Create Pull Request
      ↓
    Review
      ↓
    Merge into main

---

## Branches

A Git branch provides an independent line of development.

The main branch contains the stable version of the project.

For Day 7, a separate feature branch was created:

    day-07-github-cicd

The branch was created using:

    git switch -c day-07-github-cicd

This allows changes to be developed without directly modifying `main`.

---

## Why Use Feature Branches?

Feature branches are useful because they:

- Keep `main` stable
- Isolate new changes
- Allow developers to work independently
- Make code review easier
- Reduce the risk of breaking the main project
- Support team collaboration

---

## Git Commands Practiced

Check the current repository status:

    git status

List branches:

    git branch

Create and switch to a new branch:

    git switch -c branch-name

Switch between branches:

    git switch branch-name

Stage changes:

    git add .

Commit changes:

    git commit -m "Commit message"

Push a branch:

    git push origin branch-name

Pull the latest changes:

    git pull origin main

View commit history:

    git log --oneline

---

## Pull Requests

A Pull Request (PR) is a request to merge changes from one branch into another branch.

Typical workflow:

    feature branch
          ↓
       git push
          ↓
    GitHub Pull Request
          ↓
       Code Review
          ↓
       Approval
          ↓
       Merge
          ↓
         main

Pull Requests allow teams to review code before it becomes part of the main project.

---

## Code Review

During code review, developers can check:

- Correctness
- Code quality
- Security
- Maintainability
- Tests
- Documentation
- Possible bugs

Reviewers can leave comments and request changes before the Pull Request is merged.

---

# CI/CD

## What is CI?

CI stands for Continuous Integration.

Continuous Integration means automatically building and testing code whenever developers push changes or create Pull Requests.

A basic CI workflow is:

    Developer pushes code
            ↓
       CI pipeline
            ↓
       Install dependencies
            ↓
          Run tests
            ↓
      Check code quality
            ↓
       Pass / Fail

---

## What is CD?

CD can refer to Continuous Delivery or Continuous Deployment.

Continuous Delivery means the software is kept in a state where it can be released safely.

Continuous Deployment goes one step further by automatically deploying successful changes to a production environment.

---

## Why CI/CD?

CI/CD helps teams:

- Detect bugs early
- Automatically run tests
- Reduce manual work
- Improve development speed
- Maintain consistent quality
- Safely integrate changes
- Automate deployment processes

---

# Day 7 Branch

The Day 7 feature branch is:

    day-07-github-cicd

It was created from:

    main

The purpose of this branch is to practice a real collaborative GitHub workflow without directly modifying the main branch.

---

# Key Concepts Learned

- Git repository
- Git branch
- Main branch
- Feature branch
- Commit
- Push
- Pull
- Pull Request
- Code review
- Merge
- Continuous Integration
- Continuous Delivery
- Continuous Deployment
- CI/CD pipeline

---

# Conclusion

Day 7 focuses on moving from individual Git usage toward a professional collaborative GitHub workflow.

The goal is to understand how developers work on isolated branches, commit and push their changes, create Pull Requests, review code, merge approved changes, and use CI/CD automation to improve software quality and reliability.