# Get Started

This guide walks you through installing PyPortion and using it to create your first project.

## Installation

Install PyPortion using pip:

<div class="termynal" data-termynal>
    <span data-ty>pip install pyportion</span>
</div>

## Verify Installation

After installation, verify that PyPortion is working correctly:

<div class="termynal" data-termynal>
    <span data-ty>portion --version</span>
</div>

## Getting Help

To view all available commands and options, use the `--help` flag:

<div class="termynal" data-termynal>
    <span data-ty>portion --help</span>
</div>

## Working with Templates

Templates define the structure and configuration of your projects. PyPortion provides built-in templates and supports custom templates.

### List Available Templates

View all templates currently available on your system:

<div class="termynal" data-termynal>
    <span data-ty>portion template list</span>
</div>

### Download a Template

Download a template from a remote repository:

<div class="termynal" data-termynal>
    <span data-ty>portion template download &lt;template-url&gt;</span>
</div>

Replace `<template-url>` with the URL of the template repository.

## Creating a Project

Once you have templates available, create a new project using the `new` command:

<div class="termynal" data-termynal>
    <span data-ty>portion new &lt;template-name&gt; &lt;project-name&gt;</span>
</div>

**Parameters:**

- `<template-name>` - The name of the template to use
- `<project-name>` - The name for your new project

**Example:**

<div class="termynal" data-termynal>
    <span data-ty>portion new python-cli my-awesome-app</span>
</div>

This command creates a new directory called `my-awesome-app` with the structure defined in the `python-cli` template.

## Next Steps

- Explore the available templates to find one that fits your project requirements
- Learn how to create custom templates to standardize your team's workflow
