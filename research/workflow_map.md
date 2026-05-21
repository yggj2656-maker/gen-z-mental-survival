# Production Workflow — 12-Step Mapping

From `deep-research-report.md`, adapted for local Claude Code + DeepSeek execution.

```
Audience/Keywords → Scrape Sources → Outline → Chapter Drafts → Quality Check → Format → Cover → Publish
```

| # | Step | Tool | Input | Output |
|---|------|------|-------|--------|
| 1 | Audience & Keywords | Claude + BrightData search | Pain point → search query list | Keyword list (EN/ZH) |
| 2 | External Data Scrape | BrightData scrape | Reddit, Amazon, forum URLs | Markdown / JSON content |
| 3 | Chapter Outline | DeepSeek + Claude | Book theme + audience context | Outline JSON (titles + key points) |
| 4 | Chapter Headings | DeepSeek | Chapter theme → subtitle generation | Section heading list |
| 5 | Chapter Draft | DeepSeek | Heading + word count + tone guide | Chapter body (Markdown) |
| 6 | Examples & Exercises | DeepSeek | Concept → real-life scenario prompt | Cases + exercise steps |
| 7 | Gamified Tasks | DeepSeek | Growth goal → quest design prompt | Task list + XP system |
| 8 | Style Polish | Claude Code | Raw draft → tone/style refinement | Final chapter draft |
| 9 | Quality Check | Claude + Manual | Full manuscript review | Issue report |
| 10 | Format Output | Pandoc | manuscript.md → EPUB/MOBI | .epub / .mobi files |
| 11 | Cover & Metadata | Claude + Image Gen | Title + theme → cover brief + prompt | Cover design + AI image prompt |
| 12 | KDP Upload Prep | Claude + Manual | Book metadata → CSV generation | KDP-ready CSV |

## Execution Order

Steps 1-2 (research) → Step 3-4 (structure) → Steps 5-7 per chapter (drafting) → Steps 8-9 (review) → Steps 10-12 (publish)

## Trigger Strategy (Local)

Instead of GitHub Actions, use:
- **Manual trigger**: Claude Code for each step
- **Batch mode**: Chain multiple steps per session
- **Per-chapter cycle**: Repeat 5→6→7→8 for each chapter
