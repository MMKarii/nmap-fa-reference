# Recommended `main` Branch Protection

The connected GitHub integration currently exposes branch-protection reads but no branch-protection write action. The repository should therefore use the following settings in GitHub repository rules/branch protection for `main` when administrative write support is available:

- Require a pull request before merging.
- Require status checks to pass before merging.
- Required check: the `build-and-deploy` job from `.github/workflows/docs.yml`.
- Require branches to be up to date before merging when practical.
- Require at least one approving review for non-owner/community contributions.
- Dismiss stale approvals when new commits materially change a reviewed PR.
- Require conversation resolution before merging.
- Block force pushes.
- Block branch deletion.
- Do not allow bypass for ordinary contributors.

## Verification

Current protection state can be read from:

`GET /repos/MMKarii/nmap-fa-reference/branches/main/protection`

Do not claim these settings are active until GitHub reports `main` as protected and the required status check is visible in the branch/ruleset configuration.
