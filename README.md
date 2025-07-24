<div align="left" style="position: relative;">
<img src="https://img.icons8.com/external-tal-revivo-duo-tal-revivo/100/external-markdown-a-lightweight-markup-language-with-plain-text-formatting-syntax-logo-duo-tal-revivo.png" align="right" width="30%" style="margin: -20px 0 0 20px;">
<h1>AI_TRIPPLANNER.GIT</h1>

## 🔗 Table of Contents

- [📍 Overview](#-overview)
- [👾 Features](#-features)
- [📁 Project Structure](#-project-structure)
  - [📂 Project Index](#-project-index)
- [🚀 Getting Started](#-getting-started)
  - [☑️ Prerequisites](#-prerequisites)
  - [⚙️ Installation](#-installation)
  - [🤖 Usage](#🤖-usage)
  - [🧪 Testing](#🧪-testing)
- [📌 Project Roadmap](#-project-roadmap)
- [🔰 Contributing](#-contributing)
- [🎗 License](#-license)
- [🙌 Acknowledgments](#-acknowledgments)

---

## 📍 Overview

<code>❯ 

Atriyos is an AI-powered travel planning agent designed to automate the process of generating personalized itineraries based on user input such as location, interest, duration, and more.

The system is modularly designed with a production-ready mindset — featuring a Streamlit-based user interface and an ASGI-compatible backend (Uvicorn). The flow and logic are mapped using state diagrams and flowcharts to ensure clarity and maintainability from day one.

Whether you're building agentic apps or learning AI+UX integration, Atriyos serves as a great starter blueprint.

</code>

---

## 👾 Features

<code>❯ 

- 🔍 **Input-Aware Planning**: Accepts user input like location, days, interest (e.g., food, adventure, relaxation).
- 🧠 **Modular Agent Workflow**: Core logic split into agent, config, and exception handling — scalable and clean.
- ⛅ **Environment-Responsive**: Can incorporate weather or external APIs to generate context-aware plans.
- 🎨 **Interactive Frontend**: Built using Streamlit for a lightweight and modern UI.
- ⚙️ **ASGI-Ready Backend**: Powered by Uvicorn for fast, asynchronous performance.
- 🧱 **Config-Driven Execution**: Centralized YAML config support for agent tuning and deployment control.
- 🗺️ **Visual Planning**: Includes Mermaid/flowchart diagrams that map the logic and decision tree clearly.


</code>

---

## 📁 Project Structure

```sh
└── AI_TRIPPLANNER.git/
    ├── Flowchart diargam for AI_TRAVELAGENT.png
    ├── README.md
    ├── Statediagram for AITRAVELAGENT.png
    ├── agent
    │   ├── __init__.py
    │   └── agentic_workflow.py
    ├── config
    │   ├── __init__.py
    │   └── config.yaml
    ├── exception
    │   ├── __init__.py
    │   └── exception_handling.py
    ├── logger
    │   ├── __init__.py
    │   └── logging.py
    ├── main.py
    ├── my_graph.png
    ├── notebook
    │   └── experiments.ipynb
    ├── prompt_library
    │   ├── __init__.py
    │   └── prompt.py
    ├── pyproject.toml
    ├── requirements.txt
    ├── setup.py
    ├── streamlit_app.py
    ├── tools
    │   ├── __init__.py
    │   ├── arthamatic_op_tool.py
    │   ├── currency_conversion_tool.py
    │   ├── expense_calculator_tool.py
    │   ├── place_search_tool.py
    │   └── weather_info_tool.py
    └── utils
        ├── __init__.py
        ├── config_loader.py
        ├── currency_converter.py
        ├── expense_calculator.py
        ├── model_loaders.py
        ├── place_info_serach.py
        ├── save_to_document.py
        └── weather_info.py
```


### 📂 Project Index
<details open>
	<summary><b><code>AI_TRIPPLANNER.GIT/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/Vinay0905/AI_TRIPPLANNER.git/blob/master/streamlit_app.py'>streamlit_app.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/Vinay0905/AI_TRIPPLANNER.git/blob/master/main.py'>main.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/Vinay0905/AI_TRIPPLANNER.git/blob/master/requirements.txt'>requirements.txt</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/Vinay0905/AI_TRIPPLANNER.git/blob/master/pyproject.toml'>pyproject.toml</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/Vinay0905/AI_TRIPPLANNER.git/blob/master/setup.py'>setup.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- agent Submodule -->
		<summary><b>agent</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/Vinay0905/AI_TRIPPLANNER.git/blob/master/agent/agentic_workflow.py'>agentic_workflow.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- config Submodule -->
		<summary><b>config</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/Vinay0905/AI_TRIPPLANNER.git/blob/master/config/config.yaml'>config.yaml</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- notebook Submodule -->
		<summary><b>notebook</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/Vinay0905/AI_TRIPPLANNER.git/blob/master/notebook/experiments.ipynb'>experiments.ipynb</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- logger Submodule -->
		<summary><b>logger</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/Vinay0905/AI_TRIPPLANNER.git/blob/master/logger/logging.py'>logging.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- prompt_library Submodule -->
		<summary><b>prompt_library</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/Vinay0905/AI_TRIPPLANNER.git/blob/master/prompt_library/prompt.py'>prompt.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- utils Submodule -->
		<summary><b>utils</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/Vinay0905/AI_TRIPPLANNER.git/blob/master/utils/save_to_document.py'>save_to_document.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/Vinay0905/AI_TRIPPLANNER.git/blob/master/utils/weather_info.py'>weather_info.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/Vinay0905/AI_TRIPPLANNER.git/blob/master/utils/expense_calculator.py'>expense_calculator.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/Vinay0905/AI_TRIPPLANNER.git/blob/master/utils/config_loader.py'>config_loader.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/Vinay0905/AI_TRIPPLANNER.git/blob/master/utils/currency_converter.py'>currency_converter.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/Vinay0905/AI_TRIPPLANNER.git/blob/master/utils/place_info_serach.py'>place_info_serach.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/Vinay0905/AI_TRIPPLANNER.git/blob/master/utils/model_loaders.py'>model_loaders.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- exception Submodule -->
		<summary><b>exception</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/Vinay0905/AI_TRIPPLANNER.git/blob/master/exception/exception_handling.py'>exception_handling.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			</table>
		</blockquote>
	</details>
</details>

---
## 🚀 Getting Started

### ☑️ Prerequisites

Before getting started with AI_TRIPPLANNER.git, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python
- **Package Manager:** Pip


### ⚙️ Installation

Install AI_TRIPPLANNER.git using one of the following methods:

**Build from source:**

1. Clone the AI_TRIPPLANNER.git repository:
```sh
❯ git clone https://github.com/Vinay0905/AI_TRIPPLANNER.git
```

2. Navigate to the project directory:
```sh
❯ cd AI_TRIPPLANNER.git
```

3. Install the project dependencies:


**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pip install -r requirements.txt
```




### 🤖 Usage
Run AI_TRIPPLANNER.git using the following command:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ python {entrypoint}
```


### 🧪 Testing
Run the test suite using the following command:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pytest
```


---
## 📌 Project Roadmap

- [X] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three.

---

## 🔰 Contributing

- **💬 [Join the Discussions](https://github.com/Vinay0905/AI_TRIPPLANNER.git/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/Vinay0905/AI_TRIPPLANNER.git/issues)**: Submit bugs found or log feature requests for the `AI_TRIPPLANNER.git` project.
- **💡 [Submit Pull Requests](https://github.com/Vinay0905/AI_TRIPPLANNER.git/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/Vinay0905/AI_TRIPPLANNER.git
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/Vinay0905/AI_TRIPPLANNER.git/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=Vinay0905/AI_TRIPPLANNER.git">
   </a>
</p>
</details>

---

## 🎗 License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## 🙌 Acknowledgments

- List any resources, contributors, inspiration, etc. here.

---
