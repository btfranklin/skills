# Django and DaisyUI Integration Patterns

Use this reference after inspecting the repository. Installation syntax and supported versions change; verify them from primary documentation before implementation.

## Primary sources

- [Tailwind CSS documentation](https://tailwindcss.com/docs/installation)
- [DaisyUI documentation](https://daisyui.com/docs/install/)
- [DaisyUI theme documentation](https://daisyui.com/docs/themes/)
- [Django static-files documentation](https://docs.djangoproject.com/en/6.0/howto/static-files/)
- Official documentation for the repository's existing bundler, component library, and deployment platform

Do not copy an installation snippet from this reference. Use the current official syntax that matches the versions actually resolved by the project.

## Pipeline selection

Prefer the smallest option compatible with the existing repository:

1. Extend an existing Node/Tailwind pipeline when one already builds production assets.
2. Use the repository's established Django-integrated Tailwind package when it is maintained and compatible.
3. Add a minimal Node build only when no suitable pipeline exists and Django's deployment process can run it deterministically.

Define:

- Source CSS entrypoint and configuration ownership
- Template/content paths used to discover classes
- Development watch command
- Reproducible production build command
- Generated output path under Django static assets
- Whether generated output is committed or built in CI/deployment
- `collectstatic` order and deployment cache behavior

Avoid CDN delivery for a production application unless the user explicitly accepts its customization, CSP, availability, and reproducibility tradeoffs.

## File ownership

- **Django templates:** semantic structure, server-rendered data, validation, permissions, and component composition
- **CSS entrypoint:** current Tailwind/DaisyUI setup, custom theme declarations, base rules, and narrowly scoped overrides
- **Template components/includes:** repeated interface patterns with documented context and variants
- **Scripts:** behavior that cannot be expressed with native HTML or the project's existing enhancement layer
- **Generated CSS:** build output only; never hand-edit it

Keep source and generated directories visually distinct. Remove replaced pipelines rather than leaving two competing build paths.

## Components

Start with repeated, stable interface patterns such as buttons, form fields, alerts, cards, navigation, dialogs, and tables. Preserve semantic elements regardless of DaisyUI classes.

For each reusable template component, define:

- Required and optional context
- Allowed visual variants
- Accessible name and description behavior
- Error, disabled, loading, and empty states where relevant
- Whether callers provide content through context, includes, or the repository's existing component mechanism

Do not abstract a one-off fragment or expose arbitrary class strings as an undocumented component API.

## Themes

Map product semantics—primary action, surface, text, success, warning, and error—to DaisyUI's current theme mechanism. Verify current theme declaration syntax before editing.

If theme switching is required, define:

- Server or client ownership of the selected theme
- Default and system-preference behavior
- Persistence in account data, session, cookie, or local storage
- First-render behavior that avoids an unintended flash
- Keyboard-accessible control and a usable no-script default

Check contrast and state visibility in every supported theme; theme names alone do not establish accessibility.

## Migration and validation

1. Make the new production build reproducible before migrating templates.
2. Establish theme tokens and base styles.
3. Migrate representative components and pages, then broaden in reviewable batches.
4. Remove superseded CSS, scripts, configuration, and dependencies when their last consumer is gone.
5. Run template tests, asset builds, static collection, linting, accessibility checks, and representative visual checks.
6. Verify production paths, cache invalidation, CSP, missing assets, narrow viewports, keyboard operation, form errors, and every supported theme.
