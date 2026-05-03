# Notes

Day 1 — set up new Mac, scaffolded repo, wrote hello + minimal CLI. Rusty bits: nothing yet, this was tooling. Next: real CLI commands over a CSV.

Day 2 — built inspect and summarise commands using pandas on the Titanic dataset. Slightly confusing: naming a file inspect.py shadows Python's stdlib inspect module and breaks pandas — renamed to csvinfo.py. Next: add filtering (e.g. --where col=value) or export summarised output to a file.

Day 3 — added missing and filter commands. missing shows null counts per column with percentages (Titanic: Age 19.9%, Cabin 77.1%). filter matches rows by column=value, handles both numeric and categorical columns, supports --limit. Next: export filtered results to a new CSV.
