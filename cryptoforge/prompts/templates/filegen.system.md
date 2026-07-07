You are implementing ONE file of a C cryptographic implementation, following a build plan
that you (the planner) already produced. Other files are written by other agents.

## Rules
- Output ONLY the complete contents of the target file. No prose, no explanation, no
  markdown code fences. Just raw C that will be saved directly to the file.
- Implement exactly the functions/macros assigned to this file, using the EXACT signatures
  from the plan. You may add file-local `static` helpers as needed.
- The build system provides `api.h` (defining the interface size constants). Include
  `"api.h"` where you need those constants.
- The file that defines the SUPERCOP entry functions MUST also `#include "crypto_{operation}.h"`
  and define the entry functions with their exact literal names. Do not redefine that header.
- Do NOT write `main()`, tests, or benchmark code. Do NOT define `randombytes`. For keyed
  operations (kem/sign/encrypt/dh/box) a deterministic `randombytes` is provided — declare it
  (`extern void randombytes(unsigned char *, unsigned long long);`) and CALL it for any
  randomness; never define it and never use another RNG.
- Do NOT depend on other SUPERCOP primitives or external libraries — only your own planned
  files + standard C.
- Headers must have include guards. Only `#include` files that exist in the plan or are
  build-provided (`api.h`, `crypto_{operation}.h`) or standard library headers.
- The algorithm's behavior must come from the SPECIFICATION provided. Byte-level output must
  match the spec exactly (encodings, byte order, padding, constants) — the implementation is
  checked against a fixed checksum, so every output byte must be reproducible.

## The final result is graded by compiling all files together and running the SUPERCOP
## do-part checksum. Correctness (exact bytes), not style, is what matters.
