# Visual Supports

A growing library of visual supports for ages 0–18, organized by age, category, and keyword.

## Age strands

- **0–5** — Early childhood
- **6–11** — Childhood
- **12–18** — Adolescence

Every age strand uses the same eight categories: daily routines, communication, feelings and regulation, schedules and transitions, social situations, learning and tasks, self-care and independence, and safety and community.

Age is a starting filter. Allow children and caregivers to choose other age strands and styles according to preference and support needs. Use age-respectful artwork at every level of communication or reading ability.

## Current contents

The library contains 18 planned starter entries and 13 PNG visuals. The morning-routine set is available under `visuals/12-18/daily-routines/morning-routine/`. All routine images are square, transparent, and text-free. Planned entries describe supports that are still in development.

- `catalog/age-strands.json`: age definitions
- `catalog/categories.json`: shared categories
- `catalog/visuals.json`: searchable catalog and asset metadata
- `visuals/<age-strand>/<category>/`: artwork and printable files
- `search.py`: local age, category, and keyword search
- `CREATING-VISUALS.md`: creation workflow

## Search

Requires Python 3; no packages needed.

```sh
python3 search.py --age 8
python3 search.py --age 15 --query break
python3 search.py --age 4 --category communication
python3 search.py --status ready
```

Search includes planned entries and clearly labels their status. A future browsing website can use the same catalog. No child profiles or personal information are needed to filter by age.

## Communication: I need help

Each image shows a request for help in a different everyday situation. Choose the scene that is most recognizable to the person using it.

### Ages 0–5

![A preschooler holds up a closed snack container and asks a caregiver for help.](visuals/0-5/communication/i-need-help.png)

### Ages 6–11

![A school-age child points to their backpack zipper and asks an adult for help.](visuals/6-11/communication/i-need-help.png)

### Ages 12–18

![A teen points to an open notebook and asks a peer for help.](visuals/12-18/communication/i-need-help.png)

## Feelings and regulation: I need a break

Use these visuals to ask for a pause during play, a group activity, or studying.

### Ages 0–5

![A preschooler pauses block play and gestures to a caregiver near a floor cushion.](visuals/0-5/feelings-and-regulation/i-need-a-break.png)

### Ages 6–11

![A child asks an adult for a pause during a tabletop activity.](visuals/6-11/feelings-and-regulation/i-need-a-break.png)

### Ages 12–18

![A teen asks a peer to pause while studying together.](visuals/12-18/feelings-and-regulation/i-need-a-break.png)

## Morning routine: teen series

### 1. Wake up

![Wake up](visuals/12-18/daily-routines/morning-routine/01-wake-up.png)

### 2. Use the toilet

![Use the toilet](visuals/12-18/daily-routines/morning-routine/02-use-toilet.png)

### 3. Wash hands

![Wash hands](visuals/12-18/daily-routines/morning-routine/03-wash-hands.png)

### 4. Brush teeth

![Brush teeth](visuals/12-18/daily-routines/morning-routine/04-brush-teeth.png)

### 5. Get dressed

![Get dressed](visuals/12-18/daily-routines/morning-routine/05-get-dressed.png)

### 6. Eat breakfast

![Eat breakfast](visuals/12-18/daily-routines/morning-routine/06-eat-breakfast.png)

### 7. Pack a bag

![Pack a bag](visuals/12-18/daily-routines/morning-routine/07-pack-bag.png)
