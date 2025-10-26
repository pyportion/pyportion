# Contributing to pyportion
Thank you for your interest in contributing to pyportion 🎉

## Types of Contributions
* 🐛 **Reporting bugs** – Found something broken? [Open an issue](https://github.com/pyportion/pyportion/issues)
* 💡 **Suggesting features** – Have an idea? [Start a discussion](https://github.com/pyportion/pyportion/discussions)
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

You can start the development process

6. **Install Pre-Commit**
One you are done from the development process, run the following:
```bash
poetry run pre-commit install
```

7. **Commit and Push your changes**
Use git to commit and push your changes to open a pull request

# Pre-Commit

Pre-Commit hooks will work locally upon comitting and do the following if needed:
* Format code
* Lint code
* Type check
* Sort imports
* Run test cases

Note that it might automatically fix the files you committed to match our coding style, so you’ll need to add and commit those changes again before pushing.

## 🔄 Pull Request Review
All pull requests go through an automatic review via GitHub Actions, followed by a manual review.

Reviewers focus on:
* Code clarity and readability
* Consistency with the project structure
* Test coverage
* Quality and clarity of commit messages

## 💬 Need Help?
If you’re unsure about something, feel free to open a [discussion](https://github.com/pyportion/pyportion/discussions).
