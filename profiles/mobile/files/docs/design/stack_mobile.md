# Stack Notes — Mobile App

> Type-level facts common to a mobile app. Fill in the blanks. Project-specific
> structure lives in `architecture.md`; this file captures the stack, the
> everyday commands, and the device/emulator loop.

---

## Stack

- **Framework:** `<Flutter / React Native / Capacitor / native>`
- **Language:** `<Dart / TypeScript / Kotlin+Swift>`
- **Targets:** `<Android / iOS / both>`
- **State / data:** `<…>` (e.g. Riverpod + SQLite, Redux, …)
- **Offline behavior:** `<offline-first / online-only>`

## Everyday commands

- Install deps: `<flutter pub get / npm install>`
- Run on device/emulator: `<flutter run / npx cap run>`
- Test: `<flutter test / npm test>`
- Analyze / lint: `<flutter analyze / npm run lint>`
- Build release: `<flutter build apk / …>`

## Layout (typical)

    lib/ or src/     application code
    test/            tests
    android/ ios/    native project shells
    assets/          bundled data / images / translations

## Common gotchas

- Builds run on a device or emulator — most changes need a **human on a device**
  to verify. Use the editor/GUI task card in `human_handoff.md`.
- Keep signing keys and secrets out of the repo.
- Generated native build folders must stay git-ignored.
- Test both platforms if you target both; behavior diverges (permissions, files).

## Verify a change

- App builds and launches on the target platform.
- The affected screen/flow behaves as expected on a real device or emulator.
- Analyze/lint and unit/widget tests pass.
