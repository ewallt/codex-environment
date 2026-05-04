# Handoff

## Current State

- AutoHotkey v2 is installed at `C:\Users\tomew\AppData\Local\Programs\AutoHotkey\v2\AutoHotkey64.exe`.
- `codex-prompt-hotkeys.ahk` exists in the repo root.
- `Ctrl+Shift+J` is working when AutoHotkey is relaunched elevated with `-Verb RunAs`.
- `Ctrl+Shift+J` currently injects Tom's standing prompt instructions.
- `AGENTS.md` exists as a stub only.

## Next Steps

1. Move the standing instructions into `AGENTS.md`.
   - The hotkey works, but `AGENTS.md` should hold the durable version.
   - The hotkey can stay as prompt reinforcement.

2. Create `WORKLOG.md`.
   - Add the initial logging format.
   - Consider adding the first entry noting that AutoHotkey prompt injection was set up.

3. Expand `HANDOFF.md`.
   - Keep fields for current objective, files touched, commands/tests run, assumptions, blockers, and next step.

4. Create pre/post compact skills.
   - A skill exists for this kind of task: `skill-creator`.
   - Use that skill to create `pre-compact` and `post-compact` skills.

5. Update the hotkeys.
   - `Ctrl+Shift+J` is working.
   - Decide whether `Ctrl+Alt+H` and `Ctrl+Alt+R` should also be elevated/tested, or move them to `Ctrl+Shift+H/R`.

## Files Touched

- `AGENTS.md`
- `HANDOFF.md`
- `codex-prompt-hotkeys.ahk`

## Commands/Checks

- Installed AutoHotkey v2.0.24 from the official GitHub release installer.
- Launched AutoHotkey elevated with:
  `Start-Process -FilePath "C:\Users\tomew\AppData\Local\Programs\AutoHotkey\v2\AutoHotkey64.exe" -ArgumentList "C:\Users\tomew\Documents\codex-test\codex-prompt-hotkeys.ahk" -WindowStyle Hidden -Verb RunAs`
