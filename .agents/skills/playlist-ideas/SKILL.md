---
name: playlist-ideas
description: Generate new video topic ideas for a given playlist by checking the dashboard for existing videos and avoiding duplicates. Use when Tom asks for video ideas, topic suggestions, or what to do next for any playlist, including Geography Potpourri, History Potpourri, World War Two, Movements in Modern Art, Big Ideas, and similar playlists. Also use when Tom asks for a specific number of ideas.
---

# Playlist Ideas

Generate specific video topic ideas for a playlist. First check what has already been done, then choose underrepresented structural angles, then present specific YouTube-ready topics.

## Step 1 - Load existing videos

Read `C:\Users\tomew\Documents\agent-test\documents\video-dashboard-data.json`.

Filter by the requested playlist name. Collect existing `title` values and hold them in memory. Do not display them unless Tom asks.

## Step 2 - Pick the generation mode

Use one of two modes:

- Default mode: Tom asks for N ideas. Go all the way to specific video topics.
- Category mode: Tom explicitly asks for categories or wants to choose the angle first. Present the category options and wait.

## Step 3 - Choose underrepresented angles

Reason about which structural categories are least represented in the existing titles. Use 2-3 categories that are missing or thinly represented.

The standard structural categories are:

1. Coincidences
2. Small causes with big effects
3. Near-misses
4. Wrong turns
5. Accidental discoveries
6. The thing invented twice
7. The expert consensus that was completely wrong
8. The solution that created a bigger problem
9. The fake that became real
10. The prediction that came true
11. The decision that almost went the other way
12. The discovery hiding in plain sight
13. The wrong person in the right place

## Step 4 - Generate ideas

Distribute the requested number of ideas across the chosen categories. Each idea must:

- Fit the chosen structural angle
- Fit the playlist scope and tone
- Be narrow and specific: one incident, one place, one chain of events
- Have a surprising angle or irony
- Sound like a usable YouTube title

## Step 5 - Filter and present

Remove any idea that closely matches an existing video title or angle.

Present the surviving ideas as a numbered list. For each idea, give:

- A YouTube-ready title
- One sentence on the angle
- The category it came from

If fewer ideas survive filtering than requested, say so and offer another category.
