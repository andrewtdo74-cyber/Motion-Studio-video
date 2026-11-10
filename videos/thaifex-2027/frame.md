---
version: alpha
name: Thaifex Journey — Frame (video / frame layer)
description: >
  Nền giấy kem sáng, thẻ trắng bóng đổ rất nhẹ, chữ xám than, 4 màu nhấn dịu theo 4 chặng
  (đỏ đất nung, vàng đất, xanh dương phấn, xanh lá xô thơm), font Be Vietnam Pro, minh họa vẽ phẳng.
unit: the frame — 1920×1080 primary; 9:16 documented
principle: atoms are sacred · composition is free · numbers come from the script

colors:
  bg: "#F5F2EC"
  bg-deep: "#E9E4DA"
  card: "#FFFFFF"
  text: "#2F343B"
  text-muted: "#6E727A"
  line: "rgba(47,52,59,0.12)"
  stage-1: "#B4544D"
  stage-2: "#C49A4E"
  stage-3: "#4F74A8"
  stage-4: "#5F8F6C"
  alert: "#B4544D"
  ok: "#5F8F6C"

radii:
  pill: "100px"
  card-lg: "20px"
  card-md: "14px"
  card-sm: "10px"
  circle: "50%"

typography:
  body:      { fontFamily: "Be Vietnam Pro", cqw: 1.5, weight: 400, lineHeight: 1.45, color: "text-muted" }
  eyebrow:   { fontFamily: "Be Vietnam Pro", cqw: 1.1, weight: 700, tracking: "0.08em", upper: true, color: "stage" }
  chip:      { fontFamily: "Be Vietnam Pro", cqw: 1.25, weight: 600, color: "text" }
  h3:        { fontFamily: "Be Vietnam Pro", cqw: 2.0, weight: 700, lineHeight: 1.25, color: "text" }
  h2:        { fontFamily: "Be Vietnam Pro", cqw: 3.0, weight: 800, lineHeight: 1.15, tracking: "-0.01em", color: "text" }
  h1:        { fontFamily: "Be Vietnam Pro", cqw: 4.4, weight: 800, lineHeight: 1.1, tracking: "-0.015em", color: "text" }
  stamp:     { fontFamily: "Be Vietnam Pro", cqw: 2.2, weight: 900, tracking: "0.06em", upper: true }

spacing:
  pad-x: "5cqw"
  pad-y-top: "5cqw"
  gap-cards: "1.6cqw"
  progress-reserve: "8cqh at the bottom"

components:
  card:
    backgroundColor: "{colors.card}"
    rounded: "{radii.card-lg}"
    shadow: "0 6px 24px rgba(47,52,59,0.06)"
    description: "White card, very soft shadow. Never a heavy outline."
  chip:
    backgroundColor: "{colors.card}"
    border: "1.5px solid {colors.line}"
    rounded: "{radii.pill}"
    typography: "{typography.chip}"
    description: "Pill with a small flat icon on the left; pops in with a bounce."
  stage-badge:
    backgroundColor: "the current stage colour"
    textColor: "{colors.card}"
    rounded: "{radii.pill}"
    typography: "{typography.eyebrow} in white"
    description: "“CHẶNG 1 · …” label at the top-left of each stage scene."
  stamp:
    border: "4px solid the stamp colour"
    rounded: "{radii.card-sm}"
    rotate: "-8deg"
    typography: "{typography.stamp}"
    description: "Rubber stamp (KHAI BÁO, THÔNG QUAN, DỄ SAI NHẤT) that slams down with a small shake."
  progress-4:
    description: >
      Persistent 4-stage journey bar along the bottom edge: four numbered circles joined by a line,
      labels 1 Chuẩn bị · 2 Gửi hàng · 3 Tại Bangkok · 4 Kết thúc. The current stage lights in its colour,
      done stages keep a soft tint, upcoming ones are muted gray. Hidden on the opening, built in scene 2.
  illustration:
    description: >
      Flat / light-isometric vector drawings in the palette (no emoji, no photos): exhibition booths
      with walls, counter and name board, kraft cartons, container ship, customs gate with scan beam,
      calendar, plane, simple regional map, van, stylised IMPACT hall, ฿ coins, bank card, document folder, QR.
---

# Thaifex Journey — Frame

## Overview

A bright, calm, neutral guide video. Warm paper ground (`#F5F2EC` easing to `#E9E4DA`), white cards with
the faintest shadow, charcoal text, and four soft accents — one per stage of the exhibitor's journey. The
voice is a helpful briefing, not an ad: clear, friendly, trustworthy. Be Vietnamese-first: every glyph
with diacritics must set cleanly, so Be Vietnam Pro carries every role.

## Colors

- `bg` / `bg-deep`: the paper ground, a gentle vertical gradient. Never a dark background, including the end.
- `card`: white surfaces; `text` charcoal for headlines, `text-muted` for secondary copy.
- `stage-1..4`: the only accents. A scene uses its own stage colour; the opening and the closing may show all four as a band.
- `alert` (= stage-1) for warnings and red circles; `ok` (= stage-4) for the green “THÔNG QUAN” stamp and ticks.

## Typography

Be Vietnam Pro only. Headlines 700–800, body 400, chips 600, stamps 900 uppercase. Text reveals word by word.
Keep lines short; never break a Vietnamese word group awkwardly; nothing over the illustrations.

## Motion notes

- Words appear one by one; objects bounce or build up; stamps slam down; lines draw themselves; slow camera push.
- Transitions: soft slide or blur-fade.
- Every picture and word enters exactly when the voiceover names it.
- Sound cues: whoosh on scene change, stamp thud, tick, “ding” on completion.

## Do

- Keep the 4-stage bar visible on every stage scene; light the current stage.
- One clear message per frame; generous paper space.
- Flat, consistent illustrations in the palette.

## Don't

- No emoji, no dark grounds, no neon or saturated colours.
- No invented figures, dates or prices: show a placeholder or nothing.
- No heavy outlines or hard shadows.

Made from: mục 2 "Phong cách hình ảnh" trong YEU-CAU-VIDEO-THAIFEX-2026.md. What the user likes: tông sáng, trung tính, không chói, 4 màu nhấn theo 4 chặng.
