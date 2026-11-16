#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""owfadevelop attached audit: the target pin must parse once present.

Attached-audit contract (kernel: check(ctx) returning an issue list). One rule,
inherited from the project protocol's check 0.2 (it moved here with the spin-out —
a protocol-level check must not know an optional plugin): when
`PROJECT/owfadevelop/target.md` exists it must carry exactly one
`target: owfa/<kernel|protocol|package:<id>>` line plus a non-empty `why:` line;
the loop must never enforce a pin it cannot parse. Read-only, zero side effects.
Messages in Chinese (project-protocol convention).
"""
import os
import re

TARGET_RE = re.compile(r"^target: owfa/(kernel|protocol|package:[\w.-]+)\s*$")


def check(ctx):
    issues = []
    root = getattr(ctx, "root", os.getcwd())
    tpath = os.path.join(root, "PROJECT", "owfadevelop", "target.md")
    if not os.path.isfile(tpath):
        return issues
    lines = open(tpath, encoding="utf-8").read().splitlines()
    targets = [raw for raw in lines if raw.startswith("target:")]
    if len(targets) != 1 or not TARGET_RE.match(targets[0]):
        issues.append({"level": "error",
                       "message": "PROJECT/owfadevelop/target.md 钉子不可解析（须恰好一行 "
                                  "`target: owfa/<kernel|protocol|package:<id>>`）——dev loop 拒绝执行无法解析的钉子"})
    if not any(raw.startswith("why:") and raw[len("why:"):].strip() for raw in lines):
        issues.append({"level": "error", "message": "PROJECT/owfadevelop/target.md 缺 why: 一句话理由（改钉须留痕）"})
    return issues
