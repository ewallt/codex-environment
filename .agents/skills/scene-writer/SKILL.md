---
name: scene-writer
description: Write scene-format source documents for NotebookLM cinematic videos. Use when creating an NLM video source document, especially history, biography, theology, narrative explainers, or any topic with a story arc or progression. Produces concrete visual scenes, a whole-video focus prompt, and saves source docs to the NLM project sources folder when requested.
---

# Scene Writer

Use this skill whenever writing a source document for an NLM cinematic video.

## Core Principle

Every scene must give the rendering engine something physical to animate. Abstract concepts without a physical anchor cause pseudo-animation: a static image with a camera pan applied.

A well-formed scene answers three questions:

1. What is the physical subject or environment?
2. What is moving or changing within the scene?
3. What is the camera doing?

## Scene Rules

1. Use one camera action per scene. Do not combine movements.
   - Good actions: push-in, pull-back reveal, tilt up, tilt down, tracking shot, aerial shot, handheld, rack focus.
   - Use slow pans only. Fast pans smear.
   - Do not write editing operations such as cut, fade to black, or whip pan.
2. Give every scene a physical anchor: a person acting, an environment with dynamics, an object being used, or an atmospheric condition.
3. Describe in-scene motion explicitly. Do not assume the engine will infer it.
4. Use sensory and atmospheric language: lighting, weather, texture, and sound woven into prose.
5. Write as a screenwriter, not a narrator. Each scene is physical action; narration carries the explanation.
6. Match camera action to conceptual role:
   - Push-in or zoom in: emphasis, revelation.
   - Pull-back: scale, context.
   - Tracking shot: progress, journey.
   - Aerial: overview, big picture.
   - Handheld: tension, urgency.
   - Rack focus: shift in attention.

## Known Failure Modes

- Pseudo-animation: abstract content, missing motion verbs, or no camera action.
- Object hallucination: ambiguous physical descriptions. Be specific about every physical object named.

## Example Reference

For a calibrated full example, read eferences/point-nemo-example.md when scene density, tone, or structure is uncertain.

## Source Document Structure

Use this format:

```markdown
# [Short, Specific Title]

[2-4 sentence overview: what the video is about, the angle, why it matters]

Scene 1 - [Short Descriptive Title]
[1-3 paragraphs. One idea. Concrete and visual. Camera intent embedded in prose, not labeled.]

SETTING: [Physical location and time of day]
SUBJECT: [Who or what is the physical anchor]
IN-SCENE MOTION: [What is moving within the frame]
LIGHTING: [Specific lighting condition]
NARRATION BEAT: [What concept or information is being conveyed in the audio]

Scene 2 - [...]
[...]

Key Takeaway
[2 sentences. What the viewer should walk away with.]
```

Aim for 5-8 scenes. Prefer more shorter scenes over fewer longer ones.

Split a scene when:

- It covers more than one distinct idea or moment.
- Setting, time, or subject shifts mid-paragraph.
- The emotional or narrative climax deserves focus.

## Translating Abstract Concepts

| Abstract concept | Physical scene anchor |
|---|---|
| Passage of time | Timelapse of light moving across a stone floor; camera tilts up slowly. |
| Divine patience | An elderly figure sitting at a window, watching rain; slow push-in on face. |
| Tension between ideas | Two figures at opposite ends of a long table, neither speaking; handheld, slightly unstable. |
| Rapid change | A city street; tracking shot as pedestrians blur past. |
| Revelation or insight | A dark room; a door opens and light floods in; pull-back reveal. |

## Focus Prompt

Write a whole-video focus prompt for `nlm video create --focus`. Include:

- A directorial persona.
- Overall visual tone and emotional register.
- The rule: one primary camera action per scene; never combine movements.
- Text suppression: no text overlays, no captions, no on-screen typography.
- The narrative arc in one sentence.

Example pattern:

```text
You are a visionary documentary filmmaker with a strong cinematic voice. Treat this as a story unfolding through physical scenes, not an academic explanation. Every frame must earn its place. One primary camera action per scene; never combine movements. No text overlays, no captions, no on-screen typography. The tone is [tone]. Honor the arc: from [starting image] to [ending image].
```

## Focus Prompt Rules for Geography Potpourri

For Geography Potpourri source docs, the focus prompt should follow these rules:

1. Lead with the angle, not the atmosphere. The first sentence should name the irony, paradox, or surprising fact.
2. State the hook explicitly. Do not hint at it; make the reason the story matters obvious immediately.
3. Restate the topic minimally. Use the topic name once, then move on to the angle.
4. Keep it short: 3-5 sentences total.
   - Sentence 1: the hook.
   - Sentence 2: tone and visual register.
   - Sentence 3: the arc from X to Y.
   - Optional sentence 4: only if there is a real drift risk.
5. Tone language still matters, but it belongs after the hook. Phrases like "red earth, white concrete, civic ambition" should support the angle, not replace it.
## Save Location

When saving for Tom's NLM project, use:

```text
C:\Users\tomew\Documents\codex-test\Projects\nlm\sources\<topic-name>.md
```

Use lowercase, hyphenated filenames such as `cognitive-dissonance.md` or `fall-of-constantinople.md`.

## Pre-Generation Checklist

Each scene must have:

- Physical anchor.
- Explicit in-scene motion.
- Camera intent embedded in prose, not labeled.
- Specific lighting condition.
- Screenwriter framing rather than narrator framing.

The focus prompt must have:

- Directorial persona.
- Visual tone.
- Single-motion rule.
- Text suppression.
- Narrative arc.
## Test Mode

When Tom says this is a scene-writer test, maintain a short test trace at:

```text
C:\Users\tomew\Documents\codex-test\Projects\nlm\tmp\scene-writer-test-trace.md
```

Record:

- Files read.
- References read.
- Output source file written.
- Checklist pass completed.
- Worklog updated.

After the test, use this trace plus the generated source document to run the scene-writer rubric in `Projects\nlm\README.md`.

Remove this Test Mode section after the scene-writer test passes.

