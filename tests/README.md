# Test Suite — Afrique Boussole Creative Skill

**Version** : 1.0  
**Date** : Septembre 2026  
**Purpose** : Verify Skill correctness across platforms and capabilities

---

## Test Categories

### 1. Intake Tests
Verify brief collection behavior is adaptive and non-repetitive.

### 2. Asset Tests
Verify asset discovery and selection work correctly.

### 3. Generation Tests
Verify all 4 generation modes work as expected.

### 4. Quality Tests
Verify QA checklists catch critical failures.

### 5. Compatibility Tests
Verify Skill works across different host environments.

---

## Test Suite

### Test 1 — Minimal Input (Intake)

**Input:**
```
"Create a flyer for Afrique Boussole"
```

**Expected Behavior:**
- Ask adaptive questions (NOT a fixed 7-8 question form)
- Ask critical missing questions: objective, audience, message, CTA, format
- NOT ask for info already provided

**Pass Criteria:**
- ✅ Questions are relevant and adaptive
- ✅ No repeated questions
- ✅ Brief becomes complete after answers

---

### Test 2 — Partial Input (Intake)

**Input:**
```
"A4 flyer for cybersecurity training, target PME, 
CTA is 'Register on our website'"
```

**Expected Behavior:**
- Do NOT repeat: Format ✓, Audience ✓, CTA ✓
- Ask only critical missing: dates, visual direction, required info
- Build complete brief

**Pass Criteria:**
- ✅ Only 2-3 questions asked
- ✅ No re-asking of already-provided info
- ✅ Brief complete and confirmed

---

### Test 3 — Complete Input (Intake)

**Input:**
```
"A4 flyer for our cybersecurity course, 
dates March 15-20, target: small businesses, 
CTA: Register at www.example.com/register, 
professional tone, $299 price"
```

**Expected Behavior:**
- Brief is complete
- No questions asked
- Proceed directly to asset discovery

**Pass Criteria:**
- ✅ Brief accepted without questions
- ✅ Status marked as COMPLETE
- ✅ Proceed to next phase

---

### Test 4 — Asset Selection (Assets)

**Input:** Brief: "Corporate flyer for SMEs, professional tone"

**Expected Behavior:**
- Load `assets/manifest.json`
- Select brand logo (priority 10)
- Select 3 relevant flyer references
- NOT select unrelated assets

**Pass Criteria:**
- ✅ Official logo selected
- ✅ 3-5 references selected (flyer category)
- ✅ Selection justified

---

### Test 5 — Brand Asset Preservation (Assets)

**Request:** "Use the official ABC logo"

**Expected Behavior:**
- Use real SVG file from `assets/brand/logos/`
- NOT ask image model to recreate it
- Integrate deterministically if possible

**Pass Criteria:**
- ✅ Real file used (not generated/described)
- ✅ Logo correct colors #013C87 / #1D7742
- ✅ Logo correctly placed in final

---

### Test 6 — Generation Mode A (Generation)

**Environment:** Host exposes `CAP_TEXT_TO_IMAGE`

**Input:** Complete brief

**Expected Behavior:**
- Detect capability
- Create optimized prompt (8-bloc structure)
- Call host image generation
- Return real generated image

**Pass Criteria:**
- ✅ Capability correctly detected
- ✅ Image actually generated (not faked)
- ✅ Output is usable image file

---

### Test 7 — Generation Mode D (Generation)

**Environment:** No image generation capability

**Input:** Complete brief

**Expected Behavior:**
- Detect no capability
- Create structured `generation-request.json`
- Return request WITH instructions
- DO NOT pretend image was generated

**Pass Criteria:**
- ✅ Structured JSON created
- ✅ No false claim of generation
- ✅ Clear instructions for user

---

### Test 8 — Quality Control Pass (QA)

**Input:** Generated flyer

**Expected Behavior:**
- Check all QA criteria
- All checks pass
- Mark as READY FOR DELIVERY

**Pass Criteria:**
- ✅ Colors exact (#013C87, #1D7742)
- ✅ Logo present and correct
- ✅ Hierarchy clear
- ✅ Text readable, no overlap
- ✅ Message understandable in 2 sec

---

### Test 9 — Quality Control Fail (QA)

**Input:** Generated flyer with issues
- Text overlapping logo
- Wrong brand color
- Unclear hierarchy

**Expected Behavior:**
- QA detects critical failures
- Marks as NEEDS REVISION
- Suggests corrections or regeneration

**Pass Criteria:**
- ✅ Critical issues identified
- ✅ NOT delivered as-is
- ✅ Suggestions for correction

---

### Test 10 — Multi-Format Adaptation (Workflow)

**Input:** Master flyer, adapt to:
- Instagram 1:1
- Instagram Story 9:16
- LinkedIn 16:9

**Expected Behavior:**
- Recompose for each format (not just crop)
- Maintain hierarchy
- Optimize for platform
- All variants pass QA

**Pass Criteria:**
- ✅ 3 formats delivered
- ✅ Hierarchy maintained in all
- ✅ Format-specific optimizations applied
- ✅ All pass QA

---

## Acceptance Criteria for Tests

| Test | Status | Notes |
|------|--------|-------|
| Test 1 (Minimal Intake) | Pass/Fail | Questions should be 4-6, not 7-8 |
| Test 2 (Partial Intake) | Pass/Fail | Max 2-3 additional questions |
| Test 3 (Complete Intake) | Pass/Fail | Zero questions, proceed immediately |
| Test 4 (Asset Selection) | Pass/Fail | Logo + 3 references minimum |
| Test 5 (Asset Preservation) | Pass/Fail | Real file used, not generated |
| Test 6 (Mode A Generation) | Pass/Fail | Actual image generated |
| Test 7 (Mode D Fallback) | Pass/Fail | Structured request, no fake image |
| Test 8 (QA Pass) | Pass/Fail | All criteria met |
| Test 9 (QA Fail Detection) | Pass/Fail | Issues identified, not delivered |
| Test 10 (Multi-Format) | Pass/Fail | 3 formats, all optimized |

---

## Running Tests

### Manual Testing

For each test:
1. Set up the environment (host capabilities if applicable)
2. Provide the input
3. Verify the expected behavior
4. Record Pass/Fail result

### Automated Testing

If implementing programmatic tests:
- Use `schemas/creative-brief.json` to validate briefs
- Use `schemas/generation-request.json` to validate requests
- Check `assets/manifest.json` is valid JSON
- Verify all referenced files exist

---

## Test Scenarios by Host

### Scenario A — Full Image Capability (Mode A)

Host has: `text_to_image`

**Tests:** 1-6, 8-10 all pass, 7 skipped

### Scenario B — No Image Capability (Mode D)

Host has: None

**Tests:** 1-5, 7-9 all pass, 6 skipped, 10 modified (no actual generation)

### Scenario C — Partial Capabilities (Mode C)

Host has: `text_to_image` + `deterministic_layout`

**Tests:** All pass

---

## Known Limitations

### Test Dependencies

- Test 4 depends on `assets/manifest.json` being valid
- Test 6 depends on host image capability
- Test 10 depends on successful Test 6

### Platform Variations

- Some hosts may not support all capabilities
- Generation quality varies by platform
- Asset file formats may need adaptation

---

## Future Test Additions

- Multi-language support tests
- Accessibility compliance tests (WCAG AA)
- Performance tests (response time)
- Large-scale asset catalog tests
- Concurrent request handling

---

End of Test Suite
