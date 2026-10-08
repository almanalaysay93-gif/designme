# Asset Pipeline — What You Were Missing

Before hyperframes-agent renders, it must:

1. Fonts: extract from design-dna, check license, download woff2, self-host, never use Inter as default unless brief says. Use frontend-design rule.
2. Images: optimize to webp, max 200kb each, add loading="lazy"
3. GLB: Draco compress, max 2MB, texture 1k max, use KTX2
4. Lottie: JSON minify, remove unused layers
5. Captions: if narration, add data-hf-caption, test readability (contrast 4.5:1)
6. Audio: 48kHz, no drift, seekable via HyperFrames timeline
7. Determinism check: render twice, compare hash, must match
8. A11y: prefers-reduced-motion fallback (static frame), captions, no auto-play audio without mute

Output: assets/manifest.json
