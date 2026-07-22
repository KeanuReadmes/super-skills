# Repository Governance Docs

## Branch protection setup

1. Open repository **Settings** → **Branches**.
2. In **Branch protection rules**, click **Add rule**.
3. Set **Branch name pattern** to your default branch (usually `main`).
4. Enable:
   - **Require a pull request before merging**
   - **Require approvals** (minimum 1, recommended 2 for critical changes)
   - **Dismiss stale pull request approvals when new commits are pushed**
   - **Require status checks to pass before merging**
   - **Require conversation resolution before merging**
   - **Require signed commits** (if your team policy supports it)
   - **Require linear history** (optional, if merge commits are not desired)
   - **Do not allow bypassing the above settings**
5. In required status checks, add the repository workflows
   (for example `ci` and `codeql`).
6. Save the rule.

## Recommended policy baseline

- Keep `CODEOWNERS` updated so required reviewers are assigned automatically.
- Protect the default branch and any release branches (`release/*`).
- Require CodeQL and CI checks on protected branches.
- Restrict force pushes and branch deletion on protected branches.
- Use Dependabot security updates with auto-triage and SLA for remediation.
- Review and rotate repository admin access regularly.
