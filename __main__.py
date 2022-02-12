"""A GitHub Python Pulumi program"""

import pulumi
import pulumi_github as github

# Create a GitHub repository
repository = github.Repository('demo-repo', 
                    description="Demo Repository for GitHub",
                    is_template="true",
                    topics=["12345","abcapp","production"],
                    gitignore_template="Java",
                    visibility="public")


development = github.Branch("develop",
    repository=repository.name,
    branch="develop")
default = github.BranchDefault("default",
    repository=repository.name,
    branch="main")

codeowners = github.RepositoryFile("codeowners",
    repository=repository.name,
    branch=default.branch,
    file="CODEOWNERS.md",
    content="dummy",
    commit_message="Added by automation",
    commit_author="Admin Bot",
    commit_email="admin@example.com",
    overwrite_on_create=True)
# Export the Name of the repository
pulumi.export('name', repository.name)
