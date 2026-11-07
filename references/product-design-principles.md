# Twenty practical product-design principles

Reference version: **1.0.0**. Source: the user-supplied 20-point product-design list.

These 20 user-supplied principles are mandatory planning/review criteria for /designme. They refine the existing design system, anti-slop constitution, accessibility/performance gates and Speckit scope; they do not authorize invented product claims, assets, tokens, copy or backend features.

Use stable IDs DP01–DP20 throughout brief.json and all five `/speckit-theme-design/` files. Apply each to the actual page, not as a generic slogan pasted into a checklist. A genuinely irrelevant case needs an explicit source/scope rationale; an unresolved choice is OPEN QUESTION and stops locking under the Speckit contract. Already supplied principles need no repeated approval; missing product-specific decisions still need real answers/evidence.

## Principle catalog

| ID | User principle | Required planning and acceptance behavior | Existing task mapping |
| --- | --- | --- | --- |
| DP01 | Delete filler badges | Remove decorative new/beta/AI pills that carry no useful decision or status information. Keep real status/availability/proof only when accurate and meaningful; do not invent badges or hide useful state. | T002, T009, T016 |
| DP02 | Drop redundant labels | Remove copy that merely repeats an obvious heading/control. Keep accessible form labels, units, status and instructions users need; visible labels and accessible names must remain unambiguous. | T002, T006, T009, T014 |
| DP03 | Un-italicize the random word in your header | Use a coherent heading style without arbitrary single-word italics. A meaningful explicitly approved typographic treatment needs a rationale and real responsive evidence. | T005, T007, T008, T016 |
| DP04 | Only use mono where necessary | Use proportional typography for general UI/copy; reserve monospace for actual code or another justified technical role. Tabular numerals do not require a monospace font. Stay inside the approved max-two-font system. | T003, T005, T010 |
| DP05 | Use a design system | Use the locked primitive → semantic → component tokens for palette/type/spacing/radii/shadows/states and responsive behavior. Reuse components and document bindings; no one-off hardcoded design values. | T003, T004, T009, T010 |
| DP06 | Show the actual product | Specify real product UI, a functioning approved preview or supplied/verified product assets as primary evidence. For a service/non-product page, show its actual workflow/result/proof with a scoped rationale. Never fabricate a screenshot, metric, feature or testimonial. Missing required real assets/copy are OPEN QUESTION inputs. | T001, T005, T007, T008 |
| DP07 | Enlarge the main feature | Give the primary product/feature demonstration meaningful visual area and hierarchy over secondary decoration. Lock the focal object, crop/scale constraints and mobile treatment from approved references/spec; do not simply enlarge every card or obstruct the CTA. | T007, T008, T013 |
| DP08 | Group with spacing | Use the spacing scale and proximity to show related groups and separation between groups. Test consistent vertical rhythm and mobile reflow instead of adding arbitrary boxes, rules or repeated labels. | T003, T004, T006, T008, T013 |
| DP09 | Add specificity to your headline | The approved headline states what the product/service does, for whom and its concrete supported benefit. Use real approved copy and facts; vague hype or invented promises fail. Resolve unknown claims in the grill. | T001, T007, T008 |
| DP10 | Emphasize the CTA | Define one primary action per decision area with a clear label, visual priority, contrast and visible focus. Keep secondary actions subordinate and preserve keyboard/touch access; decorative motion cannot compete with or intercept it. | T007, T009, T013, T014 |
| DP11 | Add an accent color | Use a named approved accent token to guide attention to the primary action or meaningful emphasis. Its value, contrast and light/dark behavior come from locked sources; do not invent a hex, sprinkle unrelated accents or default to generic purple gradients. | T003, T004, T009, T014 |
| DP12 | Keep icons consistent | Use one approved icon family with consistent optical size, stroke, weight, bounding/visible area and alignment. Label functional icons accessibly, hide decorative ones appropriately and do not substitute emoji. | T005, T006, T009, T016 |
| DP13 | Remove unnecessary embellishments | Delete visual effects, borders, glow, shapes, fake glass and background detail without a product/hierarchy/feedback purpose. Retain only justified brand/functional detail within the locked style and performance budget. | T002, T010, T016 |
| DP14 | Inner corner radius equals outer corner radius minus padding | For nested rounded surfaces, derive inner radius from the outer radius minus the effective inset/padding in the same units: inner = max(0, outer − padding). Record the token relationship and border/inset convention; avoid disconnected radii or negative values. Use existing approved values, not new arbitrary numbers. | T003, T009, T010 |
| DP15 | Improve text contrast | Verify WCAG AA contrast for real text over actual resting/moving surfaces in all relevant states/themes: 4.5:1 ordinary text, 3:1 large text, with applicable 3:1 UI/focus contrast. Muted/placeholder text and moving backdrops are not exempt. | T003, T012, T014 |
| DP16 | Wrap headline text properly | Specify a readable headline measure, meaningful word groups and responsive line-breaking behavior. Check approved copy at 320/768/1024/1440 and after fonts load; avoid orphaned words, clipping and brittle forced breaks across every viewport. | T007, T008, T013 |
| DP17 | Align by eye, not just by pixel size | Inspect perceived alignment and visible visual mass of icons, text, controls and images, not only equal CSS boxes. Record justified optical corrections as named approved component tokens/variants and verify them in actual screenshots; keep keyboard hit targets/layout stable. | T006, T009, T013 |
| DP18 | Use tabular nums | Apply font-variant-numeric: tabular-nums to comparable/changing numerical UI such as prices, timers, counts and table columns to prevent jitter and aid comparison. Confirm the approved font supports it; do not switch the whole interface to mono or apply it blindly to prose. | T003, T009, T010 |
| DP19 | Add loading states | Specify real loading/pending states for relevant asynchronous UI/media, with stable reserved layout, posters/skeletons/spinners as appropriate, accessible status and no duplicate submission. Test transition to success/empty/error; never invent backend behavior or fake timers to simulate functionality. | T009, T014, T015 |
| DP20 | Animate useful feedback | Use restrained purposeful feedback for actual hover/focus/press, pending/success/error and state transitions. Declare duration/easing/transform/opacity and reduced/static equivalents; avoid perpetual decoration and never delay access, lose focus or convey meaning by motion alone. | T011, T012, T014 |

## Planner capture

planner-griller reads this reference before finalizing the brief. Inspect available actual page/repo/reference evidence, group relevant questions with the existing grill, and collect product-specific answers: the real product/proof asset, main feature, approved headline/claims, primary/secondary CTA, accent/type/icon choices, responsive grouping and state/feedback requirements. Avoid twenty repetitive questions when the source already answers them.

Write `brief.json.designPrinciples` with the reference path/version and one record for every ID: apply / not-applicable / open-question, rationale, relevant page/section/component, approved input/evidence, locked decision or the concrete unanswered question, and test/acceptance expectation. Factual audit observations and user-approved design choices remain distinct. A screenshot-based estimated value is not a locked token. Do not silently drop a principle because the existing implementation violates it.

## Incorporate into the five Markdown files

| File | Required content |
| --- | --- |
| project_context.md | A 20-row principle audit: actual current-state observation/evidence, applicability/rationale, locked decision/provenance, affected section/component and concrete OPEN QUESTION if unresolved. Include missing actual-product/copy assets instead of faking them. |
| constitution.md | Promote applicable principles to non-negotiable theme rules: meaningful content only, token discipline, purposeful typography/icons/color/hierarchy, spacing/nested-radius consistency, contrast, numeric readability and real loading/useful reduced-safe feedback. Preserve all prior constitution requirements and scope limits. |
| spec.md | Translate every applicable ID into actual approved token/section/component/copy/asset/state/motion/responsive decisions with measurable acceptance. Include headline/CTA/product focal hierarchy, spacing/icon/optical rules, derived nested radii, font/tabular roles, full loading/empty/error/focus states and reduced mappings. Resolve token values from approved sources only. |
| plan.md | Map IDs to the existing A–E phases, token/component boundaries, real files/tool choices and verification method. Describe real product asset preparation, numeric/CSS/radius relationships, responsive wrapping, accessibility/loading checks and purposeful feedback without adding design or business logic. |
| tasks.md | Attach DP IDs and concrete acceptance/evidence to the existing T001–T018 tasks using the catalog mapping and exact spec order. Do not add/reorder tasks or user stories merely to fit the 20 principles. T016 audits coverage; T017/T018 preserve last-after-QA export and package lock. |

The builder's lock checklist records all 20 IDs, their five-file locations and source/spec/task links. Not-applicable must be justified and consistent everywhere. A generic statement such as "use a design system" without actual named tokens/bindings/acceptance does not implement DP05.

## Reviewer and final evidence

The read-only Speckit reviewer checks all IDs for coverage, evidence, concrete decisions, cross-file consistency and spec→plan→task traceability. Report FAIL with file/line/exact fix for omissions, unjustified N/A, invented assets/values or vague unverifiable wording. Missing choices return to the builder as concrete questions under the existing two-attempt limit; do not change that loop or invent fixes.

At implementation QA, inspect the actual integrated product representation, CTA, type/line breaks, icon/optical alignment, spacing/radii, numeric changes, loading/error paths and useful feedback at the declared viewports/motion modes. Link contrast/motion/state evidence to motion-a11y.md, performance evidence to perf-report.md and all applicable DP IDs to audit.md. Code/plan presence alone is not proof of a correctly rendered result.
