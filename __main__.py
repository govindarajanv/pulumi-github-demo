"""A GitHub Python Pulumi program"""

import pulumi
import pulumi_github as github

# Create a GitHub repository
repository = github.Repository("demo-repo",name="demo-repo", 
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
    commit_email="admin@repo.com",
    overwrite_on_create=True)

repo_user = github.get_user(username="govindarajanv")

repo_branch_protection = github.BranchProtection("repoBranchProtection",
    repository_id=repository.node_id,
    pattern="main",
    required_status_checks=[github.BranchProtectionRequiredStatusCheckArgs(
        strict=True
    )],
    required_pull_request_reviews=[github.BranchProtectionRequiredPullRequestReviewArgs(
        require_code_owner_reviews=True,
        required_approving_review_count=2,
        dismiss_stale_reviews=True,
        restrict_dismissals=True
    )],
    enforce_admins=True,
    allows_deletions=True)
# Export the Name of the repository
pulumi.export('name', repository.name)
