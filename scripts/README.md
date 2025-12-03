# Repository Description Updater

This script updates the descriptions (About section) of multiple GitHub repositories to make them more professional and portfolio-ready.

## Prerequisites

- Python 3.6 or higher
- `requests` library
- A GitHub personal access token with `repo` scope

## Installation

1. Install the required Python library:

```bash
pip install requests
```

2. Create a GitHub personal access token:
   - Go to [GitHub Settings > Developer settings > Personal access tokens](https://github.com/settings/tokens)
   - Click "Generate new token (classic)"
   - Give it a descriptive name (e.g., "Repository Description Updater")
   - Select the `repo` scope (Full control of private repositories)
   - Click "Generate token"
   - Copy the token and save it securely

## Usage

1. Set your GitHub token as an environment variable:

```bash
# Linux/macOS
export GITHUB_TOKEN=your_github_personal_access_token

# Windows (Command Prompt)
set GITHUB_TOKEN=your_github_personal_access_token

# Windows (PowerShell)
$env:GITHUB_TOKEN = "your_github_personal_access_token"
```

2. Run the script:

```bash
python update_repo_descriptions.py
```

## Repositories Updated

The script updates descriptions for the following repositories:

| Repository | Description |
|------------|-------------|
| vendkura/wine_quality | Machine learning project for predicting wine quality |
| vendkura/disease-search-engine | Medical information retrieval system |
| vendkura/talk-with-gama-app | Conversational AI for GAMA platform documentation |
| vendkura/cheating_exam | Computer vision exam proctoring system |
| vendkura/HospitalResourceOptimizer | Hospital resource allocation optimization |
| vendkura/gama-doc-scraping | Web scraping tool for GAMA documentation |
| vendkura/tailwindProducer | Tailwind CSS utility generator |
| vendkura/product_management_testing_tool | Product management testing tool |
| vendkura/search_my_doc | Document search and retrieval utility |
| vendkura/sports_motion_recognition | Sports movement recognition model |
| vendkura/Power_Note_AI | AI-powered note-taking application |
| vendkura/talk-with-nextjs-app | Next.js documentation assistant |

## Customization

To update different repositories or descriptions, edit the `REPO_DESCRIPTIONS` dictionary in `update_repo_descriptions.py`:

```python
REPO_DESCRIPTIONS = {
    "repository-name": "New description for this repository",
    # Add more repositories as needed
}
```

## Error Handling

The script includes comprehensive error handling for:

- Missing GitHub token
- Repository not found (404)
- Authentication failures (401)
- Permission denied (403)
- Network timeouts
- Other API errors

Check the console output for detailed error messages and status updates.

## Output

The script provides detailed logging output including:

- Progress updates for each repository
- Success/failure status for each update
- A summary of total successful and failed updates

Example output:

```
2024-01-15 10:30:00 - INFO - Starting GitHub repository description updater...
2024-01-15 10:30:00 - INFO - Target owner: vendkura
2024-01-15 10:30:00 - INFO - Number of repositories to update: 12
2024-01-15 10:30:00 - INFO - Updating wine_quality...
2024-01-15 10:30:01 - INFO - Successfully updated description for vendkura/wine_quality
...
2024-01-15 10:30:15 - INFO - ==================================================
2024-01-15 10:30:15 - INFO - Summary:
2024-01-15 10:30:15 - INFO -   Successful updates: 12
2024-01-15 10:30:15 - INFO -   Failed updates: 0
2024-01-15 10:30:15 - INFO - ==================================================
2024-01-15 10:30:15 - INFO - All repository descriptions updated successfully!
```

## License

This script is part of the giovanni_portfolio project and is available under the MIT License.
