# owfa-owfadevelop

**Optional owfa-development package** — needs the
[project protocol](https://github.com/owfadev/owfa-project) (`project.org.v1`): the
kernel refuses to install it into a workspace without `project`. Installing it is the
choice to develop owfa *in a workspace shaped for developing*:

- **project + owfadevelop** is the recommended dev shape —
- **project without owfadevelop** is a plain project workspace, untouched by any of this.

What it carries:

- **The target pin** — `PROJECT/owfadevelop/target.md` declares the one owfa component
  this workspace develops (`target: owfa/<kernel|protocol|package:<id>>` + a why line).
  With the pin in force the dev loop refuses out-of-target work; changing the pin goes
  through `PROJECT/decisions.md`. A malformed pin is an audit error (attached audit
  `owfadevelop/scripts/check.py`).
- **The `owfa-develop` command** — the dev loop: pin gate + five steps (environment /
  sandbox / iterate / test / release gate), with the three owfa dev tracks
  (kernel / protocol / package) as pinned specializations of the generic release gate.
- **The dev territory** — `PROJECT/owfadevelop/`: `target.md`, `env.md` (host
  declarations, read every session), `releases.md` (append-only release ledger).

Spun out of the project protocol package at project 0.4 (there it shipped 0.1–0.2 as a
protocol member, reaching every project workspace — the opposite of optional).
