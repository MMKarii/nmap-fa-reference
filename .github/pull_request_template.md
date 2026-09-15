## Summary

Describe what changes and why.

## Documentation scope

- [ ] Persian and English files remain structurally aligned when content changes affect both editions.
- [ ] Terminology is consistent with the glossary and official Nmap terminology.
- [ ] Examples remain limited to education, administration, labs, or authorized security assessments.
- [ ] No credentials, secrets, customer identifiers, private target inventories, or sensitive scan data are included.

## Quality checks

- [ ] Local links and anchors resolve.
- [ ] External references were checked or intentionally documented.
- [ ] `python -m unittest scripts.test_check_docs scripts.test_check_external_links scripts.test_check_built_site` passes when those tests are present.
- [ ] `python scripts/check_docs.py` passes.
- [ ] Persian and English MkDocs builds pass with `--strict`.
- [ ] Mobile/RTL/LTR rendering was considered for visual changes.

## Release impact

- [ ] No release note needed.
- [ ] A changelog/release note update is included when user-visible behavior or publishing changes warrant it.
