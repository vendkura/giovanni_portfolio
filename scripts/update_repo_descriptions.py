#!/usr/bin/env python3
"""
GitHub Repository Description Updater

This script updates the descriptions (About section) of multiple GitHub repositories
using the GitHub REST API. It is designed to make repository descriptions more
professional and portfolio-ready.

Usage:
    export GITHUB_TOKEN=your_github_personal_access_token
    python update_repo_descriptions.py

Requirements:
    - Python 3.6+
    - requests library (pip install requests)
    - A GitHub personal access token with 'repo' scope
"""

import os
import sys
import logging
import requests
from typing import Dict, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

# GitHub API base URL
GITHUB_API_BASE = "https://api.github.com"

# Repository owner
OWNER = "vendkura"

# Repository descriptions to update
REPO_DESCRIPTIONS: Dict[str, str] = {
    "wine_quality": (
        "Machine learning project for predicting wine quality based on "
        "physicochemical properties using data science techniques and "
        "classification algorithms."
    ),
    "disease-search-engine": (
        "Specialized medical information retrieval system built with Python, "
        "enabling efficient search and discovery of disease-related data for "
        "healthcare research and education."
    ),
    "talk-with-gama-app": (
        "Interactive conversational AI application for querying GAMA platform "
        "documentation, built with TypeScript to provide intelligent assistance "
        "and knowledge retrieval."
    ),
    "cheating_exam": (
        "Computer vision-based exam proctoring system for detecting suspicious "
        "behavior and maintaining academic integrity during online examinations "
        "using Python and OpenCV."
    ),
    "HospitalResourceOptimizer": (
        "Data-driven optimization system for efficient hospital resource "
        "allocation, leveraging machine learning to improve healthcare delivery "
        "and operational efficiency."
    ),
    "gama-doc-scraping": (
        "Automated web scraping tool built with TypeScript for extracting and "
        "processing GAMA platform documentation, enabling systematic "
        "documentation management and analysis."
    ),
    "tailwindProducer": (
        "Modern Tailwind CSS utility generator and design tool built with "
        "TypeScript, streamlining frontend development workflows and UI "
        "component creation."
    ),
    "product_management_testing_tool": (
        "JavaScript-based testing and validation tool designed for product "
        "management workflows, streamlining QA processes and product "
        "requirement verification."
    ),
    "search_my_doc": (
        "Document search and retrieval utility for efficiently finding "
        "information across document collections, enhancing productivity "
        "and information access."
    ),
    "sports_motion_recognition": (
        "Computer vision model for recognizing and classifying sports movements "
        "and activities using Python and deep learning, applicable to sports "
        "analytics and training applications."
    ),
    "Power_Note_AI": (
        "AI-powered intelligent note-taking application leveraging machine "
        "learning for smart content organization, automatic categorization, "
        "and enhanced productivity."
    ),
    "talk-with-nextjs-app": (
        "Interactive Next.js documentation assistant powered by conversational "
        "AI, enabling developers to query and learn about Next.js features "
        "through natural language interactions."
    ),
}


def get_github_token() -> str:
    """
    Retrieve the GitHub token from environment variable.

    Returns:
        str: The GitHub personal access token.

    Raises:
        SystemExit: If the token is not found in environment variables.
    """
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        logger.error(
            "GITHUB_TOKEN environment variable is not set. "
            "Please set it with your GitHub personal access token."
        )
        sys.exit(1)
    return token


def update_repository_description(
    token: str,
    owner: str,
    repo: str,
    description: str
) -> Optional[Dict]:
    """
    Update the description of a GitHub repository.

    Args:
        token: GitHub personal access token.
        owner: Repository owner (username or organization).
        repo: Repository name.
        description: New description for the repository.

    Returns:
        dict: The API response data if successful, None otherwise.
    """
    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}"
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    payload = {"description": description}

    response = None
    try:
        response = requests.patch(url, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        logger.info(f"Successfully updated description for {owner}/{repo}")
        return response.json()
    except requests.exceptions.HTTPError as e:
        if response is not None:
            if response.status_code == 404:
                logger.error(f"Repository {owner}/{repo} not found or inaccessible.")
            elif response.status_code == 401:
                logger.error("Authentication failed. Check your GitHub token.")
            elif response.status_code == 403:
                logger.error(
                    f"Permission denied for {owner}/{repo}. "
                    "Ensure your token has 'repo' scope."
                )
            else:
                logger.error(f"HTTP error for {owner}/{repo}: {e}")
        else:
            logger.error(f"HTTP error for {owner}/{repo}: {e}")
        return None
    except requests.exceptions.Timeout:
        logger.error(f"Request timeout for {owner}/{repo}")
        return None
    except requests.exceptions.RequestException as e:
        logger.error(f"Request failed for {owner}/{repo}: {e}")
        return None


def main() -> int:
    """
    Main function to update all repository descriptions.

    Returns:
        int: Exit code (0 for success, 1 for any failures).
    """
    logger.info("Starting GitHub repository description updater...")
    logger.info(f"Target owner: {OWNER}")
    logger.info(f"Number of repositories to update: {len(REPO_DESCRIPTIONS)}")

    token = get_github_token()

    success_count = 0
    failure_count = 0

    for repo, description in REPO_DESCRIPTIONS.items():
        logger.info(f"Updating {repo}...")
        result = update_repository_description(token, OWNER, repo, description)
        if result:
            success_count += 1
        else:
            failure_count += 1

    logger.info("=" * 50)
    logger.info("Summary:")
    logger.info(f"  Successful updates: {success_count}")
    logger.info(f"  Failed updates: {failure_count}")
    logger.info("=" * 50)

    if failure_count > 0:
        logger.warning(
            "Some updates failed. Check the logs above for details."
        )
        return 1

    logger.info("All repository descriptions updated successfully!")
    return 0


if __name__ == "__main__":
    sys.exit(main())
