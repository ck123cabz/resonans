# map.json format

One file per project at `design-artifacts/technique-maps/<slug>/map.json`, next to a `refs/`
folder of images. The map page reads it together with `techniques.json`, so `map.json` holds
only what this project decided; definitions stay in `techniques.json`.

```json
{
  "title": "Resonans key visual",
  "artifact": "https://claude.ai/artifact/…",
  "brief": "One sentence: what the image is for and where it runs.",
  "idea": "The verb: what the image does with its truth. Empty until the brief settles it.",
  "job": "group",
  "refs": [
    {
      "id": "mako-vogue",
      "file": "refs/mako-vogue.jpg",
      "title": "Vogue Philippines cover, Szilveszter Makó",
      "source": "Christian's Eden board, 2026-10-20",
      "draft": false,
      "idea": "Optional: the idea read with /lens jason-murray classify, as a verb",
      "reads": [
        {"t": "visual-quotation", "why": "Restages a religious painting: wings, garden, saint's pose"},
        {"t": "visible-facture", "why": "Painted backdrop left visible behind the sitter"}
      ]
    }
  ],
  "shortlist": [
    {"t": "visual-quotation", "why": "What it would have him do here, one line"}
  ],
  "dissent": {"tool": "Via Negativa", "why": "The case against the shortlist, one line"},
  "gaps": ["A move seen in a reference that none of the 30 names"]
}
```

Rules the checker enforces (`scripts/check_map.py`):

- every `t` is an `id` in `techniques.json`
- every `file` exists and is a jpg, png or webp under 2 MB
- each ref has one to three `reads`; the shortlist has one to four entries
- `job`, when set, is one of the four jobs
- ref `id`s are unique

`shortlist`, `dissent`, `idea` and `job` may be empty while only `read` has run. The page
shows what is filled and leaves the rest out.
