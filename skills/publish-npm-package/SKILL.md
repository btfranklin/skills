---
name: publish-npm-package
description: >-
  Use when configuring or troubleshooting npm package publication with GitHub Actions and npm Trusted Publishing, including JavaScript or TypeScript packages and the npm side of mixed-language repositories. Covers release events, OIDC permissions, package metadata, tarball verification, provenance, first-publication bootstrap, and npm/GitHub settings. Do not use for applications, repositories without an npm distribution, generic CI, containers, or token publishing unless requested. Return scoped workflow changes, required settings, validation results, and external steps.
---

# Publish npm Packages

Build an npm release path that is minimal, inspectable, and consistent with the package's existing conventions.

## Workflow

1. Confirm that the repository produces a publishable npm package and identify the exact workspace or package directory.
2. Inspect `package.json`, the repository's lockfile and package-manager choice, supported Node.js versions, exports, files, repository metadata, release conventions, workflows, and repository instructions before proposing changes.
3. Run the repository's normal validation and build commands. Create an exact tarball with `npm pack`, inspect its manifest and contents, and smoke-test an isolated install when package contents or declarations are material to the request.
4. Configure npm Trusted Publishing around the repository's approved release event:
   - use a supported hosted runner and a currently compatible Node.js/npm pair;
   - grant `id-token: write` only to the publishing job and keep ordinary repository permissions read-only;
   - align the npm package, GitHub owner/repository, workflow filename, environment, and allowed publish action exactly;
   - publish the exact validated tarball rather than rebuilding in the publishing job;
   - rely on Trusted Publishing's automatic provenance for eligible public packages unless the repository has a concrete reason to disable it.
5. Handle a package's first publication as an explicit bootstrap. Determine whether the package already exists and whether npm currently permits its trust relationship to be configured before first publication. If an authenticated bootstrap is required, validate the exact artifact first and obtain authorization for that exact `npm publish` command before proceeding.
6. If the same release also publishes to another registry, apply that registry's publishing skill and require every release artifact to pass preflight before any publisher runs. Derive all artifact versions from the same approved release identity.
7. Validate YAML, package metadata, archive contents, permissions, event semantics, and all manual GitHub/npm configuration. After an authorized release, verify registry metadata, provenance when expected, and a clean installation. Do not claim that external settings or a live publication were verified when they were not.

## Freshness

Before changing action references, Node.js matrices, npm requirements, Trusted Publishing configuration, provenance flags, or staged-publishing settings, check the current primary documentation and upstream releases. Follow repository pinning or SHA policies when present. Otherwise use current supported action references verified during the task; never describe a frozen reference as “latest.” Record the relevant versions or verification date when they affect the change.

## Guardrails

- Respect the repository's package manager for dependency installation and validation. Use the npm CLI for npm registry operations that require it.
- Do not introduce a long-lived npm publish token unless the user explicitly requires token-based publishing. Keep any token needed to install private dependencies read-only and separate from publication.
- Do not create or push tags, publish releases, configure registry trust, alter repository settings, bootstrap a package, or perform a live upload without explicit authorization.
- Treat package names and versions as immutable registry coordinates. Recheck name availability immediately before a first publication, and never try to overwrite an existing version.
- Inspect lifecycle scripts and the packed archive before publication; `npm pack` and `npm publish` can execute package scripts.
- Scope workspace commands to the intended package. Do not assume trust-management commands understand npm workspaces.
- If one registry succeeds and another fails, preserve the successful immutable release and recover only the failed publisher from the exact preflight artifact. Do not rebuild or republish the successful version.
- Preserve existing workflow names and release conventions unless changing them is necessary to make the publishing identity correct.

## Resources

- Read [references/workflow-templates.md](references/workflow-templates.md) when creating or substantially restructuring GitHub Actions workflows, configuring a trusted publisher, handling an initial package bootstrap, or coordinating npm with another registry. Adapt the patterns after verifying current primary documentation and action references.

## Output

Report:

1. Existing npm release coverage and gaps.
2. Workflow changes and why each permission or event is required.
3. Manual GitHub and npm settings, including whether an initial bootstrap remains.
4. Package and artifact validation results, plus anything still externally unverifiable.
5. Coordination with other registries, if present.
6. Authorized next steps, clearly separating configuration from live release actions.
