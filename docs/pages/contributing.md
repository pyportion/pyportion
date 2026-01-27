# Contributing to PyPortion

Thank you for your interest in contributing to PyPortion.

## Types of Contributions
* 🐛 **Reporting bugs** – Found something broken? [Open an issue](https://github.com/atharabia/pyportion/issues)
* 💡 **Suggesting features** – Have an idea? [Start a discussion](https://github.com/atharabia/pyportion/discussions)
* 🧪 **Testing new releases** – Try the latest versions and share feedback
* 🧱 **Improving documentation** – Help others understand pyportion
* 🧰 **Contributing code** – Fix bugs or add new features

## Local Development Setup

In order to contribute to PyPortion code, you can follow these steps:

1. **Fork the repository**
Go to the GitHub repo and click "Fork" to create your own copy.

2. **Clone your fork**
```bash
git clone https://github.com/<your-username>/pyportion
```

3. **Download poetry (if you don't have it)**
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

4. **Install project dependencies**
```bash
poetry install
```

5. **Start Development**

Make your changes to the codebase. Ensure your code follows the project's coding standards and includes appropriate tests.

6. **Install Pre-Commit Hooks**

Once you have completed your changes, install the pre-commit hooks:
```bash
poetry run pre-commit install
```

7. **Commit and Push your changes**
Use git to commit and push your changes to open a pull request

## Pre-Commit Hooks

Pre-commit hooks run automatically when you commit changes and perform the following checks:
* Format code
* Lint code
* Type check
* Sort imports
* Run test cases

**Note:** Pre-commit hooks may automatically modify files to match the project's coding style. If this occurs, stage and commit the changes again before pushing.

## Pull Request Review
All pull requests go through an automatic review via GitHub Actions, followed by a manual review.

Reviewers focus on:
* Code clarity and readability
* Consistency with the project structure
* Test coverage
* Quality and clarity of commit messages

## Need Help?

If you have questions or need clarification, open a [discussion](https://github.com/atharabia/pyportion/discussions) on GitHub.
