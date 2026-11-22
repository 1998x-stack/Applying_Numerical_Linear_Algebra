# Content and verification standard

## Standalone explanation

Every page is a complete teaching unit, not a summary of what another chapter or section contains. Avoid phrases such as “the textbook discusses” or “this section introduces” as a substitute for explanation. Start with the reader's concrete question and supply the context needed to answer it.

A strong article follows this sequence:

1. **Problem:** what is being computed, from which data, and why is it difficult?
2. **Model:** define dimensions, variables, boundary conditions and assumptions.
3. **Mechanism:** derive the operation and show its data flow.
4. **Mathematics:** state the equation with correct signs, indices and shapes.
5. **Algorithm:** explain update order, work per iteration and stopping logic.
6. **Experiment:** provide a deterministic example with expected invariants.
7. **Limitations:** say when the method is not applicable or when a claim is model-specific.
8. **Evidence:** cite the primary source or official implementation documentation near the claim.

## Mathematical correctness

- Define whether the discrete operator represents (-Delta) or (Delta); this controls the signs in the stencil.
- State whether a grid count means interior unknowns or all grid points.
- State the vectorization convention before writing Kronecker products. Column-major and row-major order produce different-looking, but permutation-equivalent, matrices.
- Distinguish discretization error from algebraic/iteration error.
- A small residual does not automatically imply a small forward error for an ill-conditioned matrix.
- A convergence statement must name its assumptions. Never generalize a model-problem spectral-radius identity to arbitrary matrices.

## Visual explanations

- Each figure has a question, a descriptive SVG `title`, `desc`, `role="img"`, and a meaningful caption.
- Arrows represent real data flow; grid edges represent actual stencil adjacency.
- Color is not the only way to convey a distinction; labels and line styles must remain meaningful in grayscale.
- Provide a useful static default. JavaScript may reveal additional states but must not be required to understand the main claim.
- Controls use native HTML elements, visible focus and a live output region.

## Mathematics and responsive layout

- Use native MathML for substantial equations in new HTML pages; do not rely on CDN MathJax or Unicode-only fake fractions.
- Keep long equations in a named, keyboard-focusable `.math-scroll` region. Never solve a formula overflow by hiding overflow on the entire document.
- Test 1440, 768, 390 and 360 CSS-pixel widths. Also inspect print emulation and browser console errors.
- No externally hosted CSS, JavaScript, fonts or image dependencies on new article pages.

## Code and reproducibility

- Keep examples deterministic and dependency-light.
- Label toy examples as illustrations, not benchmark reproductions.
- Validate dimensions, boundary handling, residuals, symmetry or equivalence to an independently written operator.
- Explain the expected result and how to run the code.
- Python and MATLAB companions should use the same sign convention and mathematical model.

## Evidence ledger

Each `evidence.json` has an `article` field and a `claims` array. Each claim contains:
- `id`: stable local identifier;
- `claim`: one factual or quantitative statement;
- `kind`: `definition`, `derivation`, `implementation` or `complexity`;
- `source_url`: primary book, paper or official documentation;
- `locator`: page, section, equation or API field;
- `status`: `verified`, `derived`, `illustrative` or `unverified`;
- `notes`: scope and caveats.

Never label an estimate or toy value as an externally measured benchmark. Do not infer browser test success from static parsing.
