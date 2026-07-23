<style>
.gk-report h1 { font-size: 2.1rem; margin-top: 2rem; margin-bottom: 0.3rem; border-bottom: 3px solid #1f77b4; padding-bottom: 0.4rem; }
.gk-report h2 { font-size: 1.5rem; margin-top: 1.6rem; color: #1f4e79; }
.gk-report h3 { font-size: 1.15rem; margin-top: 1.1rem; color: #333; }
.gk-report p, .gk-report li { font-size: 1.05rem; line-height: 1.6; }
.gk-phase-tag { display:inline-block; background:#1f77b4; color:white; font-size:0.85rem; padding:3px 12px; border-radius:12px; margin-bottom:6px; }

.brand-header { display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; border-bottom:1px solid #e0e0e0; padding-bottom:14px; margin-bottom:10px; }
.brand-name { font-weight:800; font-size:1.05rem; color:#1f4e79; letter-spacing:0.02em; }
.brand-tag { font-size:0.85rem; color:#888; }

.match-info-box { background:#f5f7fa; border-radius:8px; padding:16px 20px; margin:16px 0 20px 0; border:1px solid #e2e6ea; }
.match-info-box table { width:100%; border-collapse:collapse; }
.match-info-box td { padding:4px 8px; font-size:1rem; }
.match-info-box td.label { color:#666; width:38%; font-weight:600; }

.data-source-box { background:#eef4fb; border-left:5px solid #1f77b4; border-radius:8px; padding:14px 20px; margin:16px 0; }
.data-source-box h3 { margin-top:0; }

.orientation-note { background:#fff8e6; border-left:5px solid #f0ad4e; border-radius:8px; padding:12px 18px; margin:14px 0; font-size:0.98rem; }

.visual-box { background:#f0f6ff; border-radius:8px; padding:14px 20px; margin:12px 0 18px 0; border:1px dashed #9db8d8; }
.visual-box h3 { margin-top:0; color:#1f4e79; }
.visual-box ul { margin-bottom:0; }
.lane-orange { color:#d35400; font-weight:700; }
.lane-blue { color:#1f77b4; font-weight:700; }

.metric-list { margin:14px 0 20px 0; }
.metric-item { background:#f9fafb; border-left:4px solid #1f77b4; border-radius:6px; padding:10px 16px; margin-bottom:10px; }
.metric-top { display:flex; justify-content:space-between; align-items:baseline; flex-wrap:wrap; gap:8px; }
.metric-name { font-weight:700; color:#1f4e79; font-size:1rem; }
.metric-badge { background:#1f77b4; color:white; font-weight:700; font-size:0.95rem; padding:2px 10px; border-radius:10px; }
.metric-desc { font-size:0.95rem; color:#444; margin-top:4px; }

.strengths-box, .weaknesses-box { border-radius:8px; padding:14px 18px; margin:10px 0; }
.strengths-box { background:#eafaf1; border-left:5px solid #2ecc71; }
.weaknesses-box { background:#fdecea; border-left:5px solid #e74c3c; }
.strengths-box h3, .weaknesses-box h3 { margin-top:0; }
.improve-list li { margin-bottom:8px; }
.footer-note { font-size:0.85rem; color:#999; text-align:center; margin-top:30px; border-top:1px solid #eee; padding-top:14px; }
</style>

<div class="gk-report">

<div class="brand-header">
<div class="brand-name">🟦 KooraVision</div>
<div class="brand-tag">AI-Powered Goalkeeper Performance Analysis</div>
</div>

# ⚽ Goalkeeper Performance Report

<div class="match-info-box">
<table>
<tr><td class="label">Goalkeeper</td><td>Matej Kovar (Czech Republic)</td></tr>
<tr><td class="label">Match</td><td>Czech Republic vs. South Korea</td></tr>
<tr><td class="label">Competition</td><td>2026 FIFA World Cup</td></tr>
</table>
</div>

<div class="data-source-box">

### 📡 Data Provided by KooraVision

This report is built entirely from data captured and processed by **KooraVision**, combining three sources:

- **Tracking data** — X/Y coordinate positions of every player and the ball throughout the sequence.
- **Event data** — discrete match actions such as passes and shots.
- **Body pose data** — frame-by-frame scanning behaviour and body orientation of the goalkeeper.

</div>

<div class="orientation-note">
⚠️ <strong>Heads-up:</strong> The 2D pitch visuals in this report are <strong>flipped on the Y-axis</strong> relative to a standard broadcast view. Please keep this in mind when reading player positioning and movement direction — it does not affect any of the underlying metrics.
</div>

## 🎬 Match Situation

Kovar faced a through-ball attack that developed into a 1v1 situation before the attacker used a fake shot and finished into an open goal. The sequence is analysed across three decision-making phases.

---

# Phase 1 — Defensive Organization & Preparation
<span class="gk-phase-tag">Frames 0–66</span>

**Objective:** Maintain optimal starting position while monitoring the attacking shape before the decisive pass.

<div class="visual-box">

### 🖼️ What the Visuals Show
- **Goalkeeper scanning** — head movement tracking how often Kovar checked his surroundings versus fixating on the ball.
- **Czech defensive line** — the shape and spacing of the outfield defenders ahead of Kovar.
- **South Korean passing options** — every available pass lane from the ball carrier, colour-coded by risk: <span class="lane-orange">orange lanes are dangerous and open</span>, while <span class="lane-blue">blue lanes are covered by a defender</span>.

</div>

### Key Metrics

<div class="metric-list">
<div class="metric-item"><div class="metric-top"><span class="metric-name">Mean Goal Line Depth</span><span class="metric-badge">4.96 m</span></div><div class="metric-desc">How far off his goal line Kovar stood on average — a measure of how proactively he positioned himself before the pass.</div></div>
<div class="metric-item"><div class="metric-top"><span class="metric-name">Goal Line Depth Change</span><span class="metric-badge">−0.23 m</span></div><div class="metric-desc">The shift in that depth across the phase, showing he eased slightly deeper as the danger developed.</div></div>
<div class="metric-item"><div class="metric-top"><span class="metric-name">Mean Lateral Error</span><span class="metric-badge">0.58 m</span></div><div class="metric-desc">Average sideways deviation from the ideal position on the goal-bisector relative to the ball.</div></div>
<div class="metric-item"><div class="metric-top"><span class="metric-name">Mean GK–Ball Distance</span><span class="metric-badge">33.82 → 30.93 m</span></div><div class="metric-desc">Distance between Kovar and the ball at the start versus end of the phase, reflecting play advancing toward goal.</div></div>
<div class="metric-item"><div class="metric-top"><span class="metric-name">Passing Lane Score</span><span class="metric-badge">72.9%</span></div><div class="metric-desc">Share of dangerous passing lanes into the box that were effectively covered by the defensive shape.</div></div>
<div class="metric-item"><div class="metric-top"><span class="metric-name">Mean Speed</span><span class="metric-badge">0.35 m/s</span></div><div class="metric-desc">Average movement speed during the phase, reflecting calm, controlled positioning rather than reactive movement.</div></div>
<div class="metric-item"><div class="metric-top"><span class="metric-name">Mean Scan Angle</span><span class="metric-badge">7.2°</span></div><div class="metric-desc">Average degree of head rotation away from the ball, indicating how much peripheral awareness Kovar showed.</div></div>
<div class="metric-item"><div class="metric-top"><span class="metric-name">Watching Ball</span><span class="metric-badge">100%</span></div><div class="metric-desc">Percentage of frames where visual focus stayed locked on the ball.</div></div>
<div class="metric-item"><div class="metric-top"><span class="metric-name">Ready Stance</span><span class="metric-badge">10.5%</span></div><div class="metric-desc">Percentage of the phase spent in an athletic, reaction-ready body position.</div></div>
</div>

<div class="strengths-box">

### ✅ Strengths
- Stable depth and defensive alignment
- Consistent lateral positioning
- Calm movement

</div>

<div class="weaknesses-box">

### ⚠️ Weaknesses
- Ball-dominant vision
- Minimal environmental scanning

</div>

---

# Phase 2 — Transition to Active Defending

<div class="visual-box">

### 🖼️ What the Visuals Show
- **Goalkeeper body orientation** — the direction Kovar's chest and hips were facing relative to the ball and the attacker as the situation developed.
- **Goalkeeper movement** — his path and speed profile as he transitioned from a set position into active defending.

</div>

### Key Metrics

<div class="metric-list">
<div class="metric-item"><div class="metric-top"><span class="metric-name">Reaction Time</span><span class="metric-badge">0.10 s</span></div><div class="metric-desc">Time taken to begin reacting once the ball was played through.</div></div>
<div class="metric-item"><div class="metric-top"><span class="metric-name">Ball Lock</span><span class="metric-badge">0.00 s</span></div><div class="metric-desc">Time to visually lock onto the ball after release — here, instantaneous.</div></div>
<div class="metric-item"><div class="metric-top"><span class="metric-name">Head Turn</span><span class="metric-badge">0.30 s</span></div><div class="metric-desc">Time taken to turn his head toward the developing attack.</div></div>
<div class="metric-item"><div class="metric-top"><span class="metric-name">Receiver Lock</span><span class="metric-badge">1.20 s</span></div><div class="metric-desc">Time taken to identify and fix attention on the receiving attacker.</div></div>
<div class="metric-item"><div class="metric-top"><span class="metric-name">Distance Covered</span><span class="metric-badge">7.51 m</span></div><div class="metric-desc">Total ground covered while transitioning into an active defensive position.</div></div>
<div class="metric-item"><div class="metric-top"><span class="metric-name">Mean Speed</span><span class="metric-badge">3.16 m/s</span></div><div class="metric-desc">Average speed maintained throughout the transition movement.</div></div>
<div class="metric-item"><div class="metric-top"><span class="metric-name">Peak Speed</span><span class="metric-badge">5.03 m/s</span></div><div class="metric-desc">The fastest speed reached while closing down the developing situation.</div></div>
</div>

<div class="strengths-box">

### ✅ Strengths
- Excellent reaction
- Strong acceleration
- Correct HOLD decision (the goalkeeper stays on his feet, holds his ground/depth rather than rushing out or diving)

</div>

<div class="weaknesses-box">

### ⚠️ Weaknesses
- Late receiver acquisition

</div>

---

# Phase 3 — 1v1 Execution

<div class="visual-box">

### 🖼️ What the Visuals Show
- **2v1 situation** — the numerical advantage Kovar had as a second defender was very close at the time of the shot.
- **Goal coverage** — the percentage of the goal frame Kovar's body was shielding at each moment.
- **Bisector angle** — how closely Kovar stayed on the line bisecting the angle between the ball and the two goalposts, the ideal defensive line.

</div>

<div class="strengths-box">

### ✅ Strengths
- Aggressive close-down
- High approach speed
- Immediate commitment

</div>

<div class="weaknesses-box">

### ⚠️ Weaknesses
- Lost bisector alignment
- Goal coverage reduced to 0% ( fake caused Kovar to leave most of the net empty)
- Committed fully to the fake
- Insufficient recovery for a second save

</div>

---

# 🏁 Overall Match Assessment

<div class="strengths-box">

### ✅ Positive
- Excellent initial positioning
- Fast reaction
- Strong athletic movement

</div>

### 🎯 Areas for Improvement

<ol class="improve-list">
<li>Increase pre-pass scanning</li>
<li>Lock onto the receiver earlier</li>
<li>Maintain bisector alignment</li>
<li>Delay full commitment against feints</li>
<li>Preserve balance for a second action</li>
</ol>

<div class="footer-note">Report generated by KooraVision · Tracking, Event & Pose Data Analysis</div>

</div>
