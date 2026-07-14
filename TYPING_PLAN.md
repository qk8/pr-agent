# Implementation Plan: Improve Type Safety with Pyright (Strict Mode)

## Current State
- **7,313 errors, 12,915 warnings** in strict mode
- **86 Python files, ~22K lines**, Python 3.12+
- **1,323 tests**
- Top error categories: `reportMissingParameterType` (1,704), `reportOptionalMemberAccess` (300), `reportCallIssue` (74)
- Top error files: test_mosaico_router.py (363), gitea_provider.py (335), pr_similar_issue.py (223), pr_code_suggestions.py (217), github_provider.py (204), algo/utils.py (203)

## Phase Plan

### Phase 0: Foundation & Configuration
- Verify pyrightconfig.json is correct
- Add `__init__.py` type exports where helpful
- Baseline: confirm current error count

### Phase 1: Core Utilities (`pr_agent/algo/`)
- `algo/types.py` - Already good, may add `__slots__` or TypedDict variants
- `algo/utils.py` (203 errors) - Add proper types for DynaBox settings access, Range, etc.
- `algo/pr_processing.py` (122 errors) - Add types to processing functions
- `algo/ai_handlers/` - Add types to AI handler classes

### Phase 2: Configuration Loader (`pr_agent/config_loader.py`, `custom_merge_loader.py`)
- Fix DynaBox-related `type: ignore` comments with proper type aliases
- Add types to custom merge loader

### Phase 3: Git Provider Base & Small Providers
- `git_provider.py` (ABC base) - Add proper abstract method signatures with generics
- `gitea_provider.py` (335 errors) - Full type annotations
- `gitlab_provider.py` (179 errors) - Full type annotations
- `bitbucket_server_provider.py` (112 errors)
- `bitbucket_provider.py`
- `azuredevops_provider.py` (134 errors)
- `gitea_provider.py`
- `local_provider.py`
- `utils.py` (git_providers)

### Phase 4: GitHub Provider (Largest)
- `github_provider.py` (204 errors) - Full type annotations

### Phase 5: Agent & Tools
- `agent/pr_agent.py` - Fix partial[type] errors, add types
- `tools/pr_reviewer.py` (128 errors)
- `tools/pr_description.py` (174 errors)
- `tools/pr_code_suggestions.py` (217 errors)
- `tools/pr_similar_issue.py` (223 errors)
- `tools/pr_config.py`
- `tools/` remaining files

### Phase 6: Servers Layer
- `servers/github_app.py`
- `servers/github_action_runner.py` (105 errors)
- `servers/utils.py`
- Other server files

### Phase 7: Mosaico Subsystem
- All `mosaico/` files (executor.py has 39 errors in tests)
- `test_mosaico_*.py` test files

### Phase 8: Test Suite & Cleanup
- Fix remaining test file type annotations
- Run full test suite
- Final Pyright pass
- Ruff lint pass

## Key Strategies
1. Use `TypedDict` for structured dicts (webhook payloads, PR data)
2. Use `Protocol` where duck typing is needed
3. Use `TypeAlias` for repeated complex types
4. Use `cast()` only with explanation when DynaBox dynamic attributes are needed
5. Use narrowest possible `# type: ignore` scopes
6. Run tests + Pyright after each phase

## Commit Strategy
Each phase = one commit with message like:
`refactor(type-safety): Add type annotations to pr_agent/algo/`
