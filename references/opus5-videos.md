# Opus 5.5 videos — optional prompt agent

Source: [yihui-dev/awesome-opus5-5-videos](https://github.com/yihui-dev/awesome-opus5-5-videos) (MIT). It is a catalog of prompts for videos people made by asking a model to write animation code (HTML, Canvas, SVG, Three.js). It is not a skill and not a renderer.

Index: `data/videos.json`, an array of `{ slug, title, author, author_url, post_url, category, tech_tags, prompt, prompt_partial, poster_url, skillry_url, has_remake, added }`.

Categories: `motion`, `explainer`, `3d`, `interactive`.

Prompt files also live in `prompts/<slug>.md`. The JSON prompt is enough when it is complete. If `prompt_partial` is true, say so in the brief and do not pretend the missing half exists.

## When to select it

Select `opus5-videos-agent` when the user explicitly wants a starting prompt from this catalog, or names Opus 5.5 videos, Skillry remakes, or this repo.

Otherwise skip it. `prompt-reference-agent` still covers Blotato and Remotion patterns.

This agent does not own the film. HyperFrames, Remotion, and motionmaxxing stay the only video renderers, and only one of those runs.

## How to read it

On approval, clone once outside the project:

```bash
git clone --depth 1 https://github.com/yihui-dev/awesome-opus5-5-videos.git "${OPUS5_VIDEOS_DIR:-$HOME/.designme/awesome-opus5-5-videos}"
```

Do not vendor the catalog into designme. Pick 3 matching entries. Prefer prompts with a duration, a structure, and a ban list over "go all out" one-liners.

## Free-only and credit rules

- Ignore any paid generator, paid voice, or paid asset step inside a source prompt. Replace it with local code or user-provided media.
- Credit author and original post in `opus-prompt-brief.md`.
- Do not copy their brand, logo, or shot list. Rewrite the craft for the approved brief.
- Do not depend on skillry.dev. Links in the catalog are for the human, not a runtime.
