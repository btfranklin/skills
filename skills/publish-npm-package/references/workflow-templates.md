# npm Workflow Patterns

Use these as structural patterns, not copy-paste version locks. Before implementation, verify current npm and action requirements in the official documentation and apply the target repository's action-pinning policy.

Primary sources:

- [npm Trusted Publishing](https://docs.npmjs.com/trusted-publishers/)
- [`npm trust`](https://docs.npmjs.com/cli/v11/commands/npm-trust/)
- [npm provenance](https://docs.npmjs.com/generating-provenance-statements/)
- [GitHub OIDC](https://docs.github.com/en/actions/reference/security/oidc)
- [`actions/setup-node` Trusted Publishing guidance](https://github.com/actions/setup-node/blob/main/docs/advanced-usage.md#trusted-publishing)

## Publish an exact artifact on an approved release event

Replace every `<verified-...-ref>` after checking the current upstream release and repository policy. Use a currently supported Node.js/npm pair; do not preserve the example version after it stops satisfying npm's Trusted Publishing requirements.

```yaml
name: Publish npm Package

on:
  release:
    types: [published]

permissions:
  contents: read

jobs:
  preflight:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@<verified-checkout-ref>
      - uses: actions/setup-node@<verified-setup-node-ref>
        with:
          node-version: "<supported-compatible-version>"
          cache: npm
      - run: npm ci
      - run: npm run <repository-check-command>
      - run: npm pack --pack-destination release-dist
      - uses: actions/upload-artifact@<verified-upload-artifact-ref>
        with:
          name: npm-package
          path: release-dist/*.tgz
          if-no-files-found: error

  publish:
    needs: preflight
    runs-on: ubuntu-latest
    environment: release
    permissions:
      actions: read
      contents: read
      id-token: write
    steps:
      - uses: actions/setup-node@<verified-setup-node-ref>
        with:
          node-version: "<supported-compatible-version>"
          registry-url: https://registry.npmjs.org
          package-manager-cache: false
      - uses: actions/download-artifact@<verified-download-artifact-ref>
        with:
          name: npm-package
          path: npm-package
      - run: npm publish ./npm-package/<verified-package-name-and-version>.tgz --access public
```

Keep `id-token: write` at publishing-job scope. A job-level GitHub environment is optional at the platform level but useful for an exact identity match and deployment protection. Trusted Publishing generates provenance automatically for eligible public packages; an explicit `--provenance` flag is unnecessary unless current npm behavior or repository policy requires it.

If the repository uses pnpm or Yarn, keep its established install, build, and validation commands. Set up a compatible npm CLI separately for the registry publication step.

## Configure and verify package trust

Match these values exactly and case-sensitively:

- npm package name;
- GitHub owner and repository;
- workflow filename only, including `.yml` or `.yaml`;
- GitHub environment, when used;
- allowed action: direct `npm publish`, staged publication, or both.

The npm website supports this configuration. A sufficiently current authenticated npm CLI can also manage it:

```bash
npm trust github <package-name> \
  --file <workflow-file.yml> \
  --repo <owner/repository> \
  --env <environment> \
  --allow-publish \
  --yes

npm trust list <package-name> --json
```

Treat these as external mutations. Check the current CLI requirements and obtain explicit authorization before creating, replacing, or revoking trust. npm currently permits one trusted-publisher configuration per package.

Verify the publishing and trust-management requirements separately: the `npm trust` command can require a newer npm CLI than OIDC publication itself. Current npm documentation also requires write access to the package being configured, so do not assume the command reserves or creates an unowned package name.

## First-publication bootstrap

Check package existence and current npm bootstrap support before the release:

1. Recheck package-name availability immediately before first publication. Availability checks do not reserve a name.
2. Build, inspect, and preserve the exact tarball through the normal release preflight.
3. Attempt no live upload until the user authorizes the exact package, version, artifact, registry, and access level.
4. If npm requires an authenticated first publication before package-level trust can be configured, publish only the validated tarball, then configure and verify Trusted Publishing.
5. Record that a manual bootstrap may lack the provenance expected from later OIDC publications. Do not invent a replacement version solely to make the historical bootstrap look automated.

Do not treat a PyPI pending publisher as evidence that npm supports the same unpublished-package flow; verify each registry independently.

## Coordinated releases with another registry

For a release that publishes multiple language packages:

- build and validate every exact artifact before either publisher becomes eligible;
- assert that the release tag and every package manifest resolve to the same intended version when lockstep versioning is part of the repository contract;
- upload exact artifacts once and make publisher jobs consume them;
- do not claim transactional publication across registries;
- if one publisher succeeds and another fails, leave the successful immutable version alone and recover only the failed publisher from the preserved artifact;
- verify each registry and isolated consumer independently after publication.

## npm package checks

- Confirm `name`, `version`, `repository`, `license`, `type`, `exports`, `types`, `files`, `bin`, and `publishConfig` as applicable.
- Confirm the intended workspace and ensure the root package is not accidentally published.
- Inspect `npm pack --dry-run` and the actual tarball file list.
- Reject unexpected credentials, source-only files, caches, tests, or build output omissions.
- Inspect `prepack`, `prepare`, `prepublishOnly`, and related lifecycle scripts.
- Install the tarball into an empty temporary consumer and exercise runtime, declarations, binaries, or browser bundling as appropriate.
- Confirm the registry version, dist-tag, integrity metadata, provenance when expected, and a fresh registry install after publication.

## Adaptation checklist

- Confirm the package manager, workspace, package metadata, and repository commands.
- Verify current Node.js, npm, and action requirements from primary upstream sources.
- Confirm the approved release event and default branch behavior.
- Match the npm publisher owner, repository, workflow filename, environment, and allowed action.
- Determine whether the package exists and whether a bootstrap is required.
- Validate YAML and inspect effective job permissions.
- Distinguish local artifact validation from live GitHub/npm state.
- Coordinate preflight and failure recovery with every other registry in the same release.
