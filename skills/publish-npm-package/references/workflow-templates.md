# npm Workflow Patterns

Use these examples as structural patterns. Do not copy their version references without verification. Before implementation, verify current npm and action requirements in the official documentation. Apply the target repository's action-pinning policy.

Primary sources:

- [npm Trusted Publishing](https://docs.npmjs.com/trusted-publishers/)
- [`npm trust`](https://docs.npmjs.com/cli/v11/commands/npm-trust/)
- [npm provenance](https://docs.npmjs.com/generating-provenance-statements/)
- [GitHub OIDC](https://docs.github.com/en/actions/reference/security/oidc)
- [`actions/setup-node` Trusted Publishing guidance](https://github.com/actions/setup-node/blob/main/docs/advanced-usage.md#trusted-publishing)

## Publish an exact tarball on an approved release event

Replace every `<verified-...-ref>` after you check the current upstream release and repository policy. Use a supported Node.js and npm pair. Replace the example version when it no longer satisfies npm Trusted Publishing requirements.

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

Keep `id-token: write` at publishing-job scope. GitHub does not require a job-level environment. An environment helps produce an exact identity match and can protect deployment. Trusted Publishing generates provenance automatically for eligible public packages. Do not add an explicit `--provenance` flag unless current npm behavior or repository policy requires it.

If the repository uses pnpm or Yarn, keep its established install, build, and validation commands. Set up a compatible npm CLI separately for the registry publication step.

## Configure and verify package trust

Match these values exactly and case-sensitively:

- npm package name.
- GitHub owner and repository.
- Workflow filename only, including `.yml` or `.yaml`.
- GitHub environment, when used.
- allowed action: direct `npm publish`, staged publication, or both.

The npm website supports this configuration. An authenticated npm CLI that meets the current version requirement can also manage it:

```bash
npm trust github <package-name> \
  --file <workflow-file.yml> \
  --repo <owner/repository> \
  --env <environment> \
  --allow-publish \
  --yes

npm trust list <package-name> --json
```

These commands change external state. Check the current CLI requirements. Obtain explicit authorization before you create, replace, or revoke trust. npm currently permits one trusted-publisher configuration per package.

Verify publication requirements and trust-management requirements separately. The `npm trust` command can require a newer npm CLI than OIDC publication requires. Current npm documentation also requires write access to the package that you configure. Do not assume that the command reserves or creates a package name that you do not own.

## First-publication bootstrap

Check package existence and current npm bootstrap support before the release:

1. Recheck package-name availability immediately before first publication. Availability checks do not reserve a name.
2. Build, inspect, and preserve the exact tarball through the normal release preflight.
3. Do not upload until the user authorizes the exact package, version, tarball, registry, and access level.
4. If npm requires authentication before it permits package-level trust, publish only the validated tarball. Then configure and verify Trusted Publishing.
5. Record that a manual bootstrap can lack the provenance expected from later OIDC publications. Do not invent a replacement version that incorrectly represents the bootstrap as an OIDC publication.

Do not use a PyPI pending publisher as evidence that npm supports the same unpublished-package process. Verify each registry independently.

## Coordinated releases with another registry

For a release that publishes multiple language packages:

In this section, a package file is the file that a registry accepts. The npm package file is a tarball. The PyPI package files are a wheel and source distribution.

- Build and validate every exact package file before either publisher becomes eligible.
- When the repository requires lockstep versions, confirm that the release tag and every package manifest specify the intended version.
- Upload each exact package file one time. Make the publisher jobs use that file.
- Do not claim transactional publication across registries.
- If one publisher succeeds and another fails, preserve the successful immutable version.
- Recover only the failed publisher from the preserved package file.
- verify each registry and isolated consumer independently after publication.

## npm package checks

- Confirm each applicable field that exists in the package: `name`, `version`, `repository`, `license`, `type`, `exports`, `types`, `files`, `bin`, and `publishConfig`.
- Confirm the intended workspace and ensure the root package is not accidentally published.
- Inspect `npm pack --dry-run` and the actual tarball file list.
- Reject unexpected credentials, source-only files, caches, tests, or build output omissions.
- Inspect `prepack`, `prepare`, `prepublishOnly`, and related lifecycle scripts.
- Install the tarball into an empty temporary consumer. Test the runtime, declarations, binaries, or browser bundling that the package provides.
- Confirm the registry version, dist-tag, integrity metadata, provenance when expected, and a fresh registry install after publication.

## Adaptation checklist

- Confirm the package manager, workspace, package metadata, and repository commands.
- Verify current Node.js, npm, and action requirements from primary upstream sources.
- Confirm the approved release event and default branch behavior.
- Match the npm publisher owner, repository, workflow filename, environment, and allowed action.
- Determine whether the package exists and whether the first publication needs authentication.
- Validate YAML and inspect effective job permissions.
- Distinguish local tarball validation from live GitHub and npm state.
- Coordinate preflight and failure recovery with every other registry in the same release.
