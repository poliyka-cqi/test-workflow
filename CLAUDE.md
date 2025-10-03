# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a test repository for GitHub Actions workflows, primarily focused on automated branch synchronization.

## Branch Strategy

This repository uses a specific branch synchronization pattern:
- **eks-test**: Source branch containing the latest changes
- **eks-dev**: Target branch that is automatically synchronized from eks-test
- **main**: Main branch (standard)

The synchronization workflow automatically:
1. Deletes the remote `eks-dev` branch
2. Recreates `eks-dev` from `eks-test`
3. Force pushes to ensure complete synchronization

## GitHub Actions Workflows

### Daily Branch Sync (`.github/workflows/sync-dev-branch.yml`)

**Triggers:**
- Scheduled: Daily at 00:00 Taiwan time (16:00 UTC)
- Manual: Via GitHub Actions UI workflow_dispatch

**Purpose:** Ensures `eks-dev` branch is an exact copy of `eks-test` branch daily

**Testing the workflow manually:**
```bash
# Navigate to GitHub Actions → "每日同步 dev 分支 (Daily Sync dev Branch)"
# Click "Run workflow" button
```

## Git Operations

**Check workflow status:**
```bash
gh run list --workflow=sync-dev-branch.yml
```

**View workflow logs:**
```bash
gh run view [run-id] --log
```

## Important Notes

- The sync workflow uses force push operations
- The `eks-dev` branch is completely replaced during sync, losing any unique commits
- Workflow requires `contents: write` permission in repository settings
