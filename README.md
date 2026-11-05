# Visual Supports

A growing library of visual supports for ages 0–18, organized by age, category, and keyword.

## Age strands

- **0–5** — Early childhood
- **6–11** — Childhood
- **12–18** — Adolescence

Every age strand uses the same categories: daily routines, communication, feelings and regulation, schedules and transitions, social situations, learning and tasks, self-care and independence, and safety and community, and recreation.

Age is a starting filter. Allow children and caregivers to choose other age strands and styles according to preference and support needs. Use age-respectful artwork at every level of communication or reading ability.

## Current contents

The library contains 24 planned starter entries plus 30 morning-routine PNG visuals across three age strands. The morning-routine sets are available under `visuals/<age-strand>/daily-routines/morning-routine/`. The 23 newer images are drafts awaiting review. All routine images are square, transparent, and text-free. Planned entries are ideas, not downloadable supports.

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

## Next milestone

Choose an illustration style and create the same communication support (for example, “I need help”) for all three age strands. Review those together before expanding the library.

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

## Morning routine sets

Each age strand now has the same ten steps. New images are marked `draft` in the catalog; the original teen set remains `ready`. Labels below are separate from the PNG artwork.

| Step | Ages 0–5 | Ages 6–11 | Ages 12–18 |
|---|---|---|---|
| Wake up | [PNG](visuals/0-5/daily-routines/morning-routine/01-wake-up.png) | [PNG](visuals/6-11/daily-routines/morning-routine/01-wake-up.png) | [PNG](visuals/12-18/daily-routines/morning-routine/01-wake-up.png) |
| Use the toilet | [PNG](visuals/0-5/daily-routines/morning-routine/02-use-toilet.png) | [PNG](visuals/6-11/daily-routines/morning-routine/02-use-toilet.png) | [PNG](visuals/12-18/daily-routines/morning-routine/02-use-toilet.png) |
| Wash hands | [PNG](visuals/0-5/daily-routines/morning-routine/03-wash-hands.png) | [PNG](visuals/6-11/daily-routines/morning-routine/03-wash-hands.png) | [PNG](visuals/12-18/daily-routines/morning-routine/03-wash-hands.png) |
| Brush teeth | [PNG](visuals/0-5/daily-routines/morning-routine/04-brush-teeth.png) | [PNG](visuals/6-11/daily-routines/morning-routine/04-brush-teeth.png) | [PNG](visuals/12-18/daily-routines/morning-routine/04-brush-teeth.png) |
| Get dressed | [PNG](visuals/0-5/daily-routines/morning-routine/05-get-dressed.png) | [PNG](visuals/6-11/daily-routines/morning-routine/05-get-dressed.png) | [PNG](visuals/12-18/daily-routines/morning-routine/05-get-dressed.png) |
| Eat breakfast | [PNG](visuals/0-5/daily-routines/morning-routine/06-eat-breakfast.png) | [PNG](visuals/6-11/daily-routines/morning-routine/06-eat-breakfast.png) | [PNG](visuals/12-18/daily-routines/morning-routine/06-eat-breakfast.png) |
| Pack a bag | [PNG](visuals/0-5/daily-routines/morning-routine/07-pack-bag.png) | [PNG](visuals/6-11/daily-routines/morning-routine/07-pack-bag.png) | [PNG](visuals/12-18/daily-routines/morning-routine/07-pack-bag.png) |
| Wash face | [PNG](visuals/0-5/daily-routines/morning-routine/08-wash-face.png) | [PNG](visuals/6-11/daily-routines/morning-routine/08-wash-face.png) | [PNG](visuals/12-18/daily-routines/morning-routine/08-wash-face.png) |
| Put on shoes | [PNG](visuals/0-5/daily-routines/morning-routine/09-put-on-shoes.png) | [PNG](visuals/6-11/daily-routines/morning-routine/09-put-on-shoes.png) | [PNG](visuals/12-18/daily-routines/morning-routine/09-put-on-shoes.png) |
| Leave home | [PNG](visuals/0-5/daily-routines/morning-routine/10-leave-home.png) | [PNG](visuals/6-11/daily-routines/morning-routine/10-leave-home.png) | [PNG](visuals/12-18/daily-routines/morning-routine/10-leave-home.png) |

Drafts can be found with `python3 search.py --status draft`.

## Learning and planning

[Review 19 new draft visuals](LEARNING-AND-PLANNING-REVIEW.md): writing in a journal and planning with a calendar in all three age strands, plus shared calendar, notebook, folder, pencils, pens, markers, crayons, glue, tape, scissors, binder, book, and library images. Shared objects are indexed for ages 0–18 and stored once under `visuals/shared/learning-and-tasks/`.

## Activities and sports

[Review 30 new draft action visuals](ACTIVITIES-AND-SPORTS-REVIEW.md): walking the dog, checking the mail, swimming, basketball, soccer, tennis, ice hockey, baseball, dance lessons, and gymnastics. Every age strand contains all ten actions. Sports and lessons use the shared Recreation category; dog walking and checking mail use Daily routines.

## Character expressions

[Review seven facial expressions on all three characters](CHARACTER-EXPRESSIONS-REVIEW.md). Six transparent comparison sheets contain 21 expression variants, saved as drafts.
