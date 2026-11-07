# Creating visual supports

1. Choose a concept, its category, and an age strand.
2. Check the catalog for an existing entry. Keep the meaning consistent across age strands while adapting the visual presentation and context.
3. Choose a style with the child’s preferences in mind: illustration, simple symbol, or photo. Use clear contrast, uncluttered backgrounds, readable labels, and meaning that does not depend on color alone.
4. Write the image prompt in `generation_prompt`. Describe the action, setting, style, and age-respectful presentation. Avoid identifiable children or personal information. Include a short list of search keywords in the prompt as metadata and instruct the generator to keep all text out of the artwork.
5. Save the approved artwork in its age and category folder. Use a stable name such as `i-need-help.png`. Add printable versions when available.
6. Add asset paths, a useful image description in `alt_text`, keywords, and the style to the catalog. Copy the search keywords into the catalog’s `keywords` array. Include the everyday action phrase, common synonyms, and distinctive objects. Check that a natural phrase finds the draft with `python3 search.py --query "your search phrase" --status draft`. Include creation/source and usage-rights information before distributing artwork.
7. Review the image for clear meaning, legible labels, respectful representation, and print quality. Mark it `ready` only after review and after the listed files exist.

The three age strands share categories, but do not need identical scenarios. Teens can use simple symbols with mature styling; younger children may prefer other approaches. Age does not determine a child’s abilities or preferences.
