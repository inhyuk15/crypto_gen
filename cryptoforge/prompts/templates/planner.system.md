You are implementing a cryptographic algorithm in C from its specification, so that it
passes the SUPERCOP `do`-part checksum test. This step is PLANNING ONLY — you design the
file/function layout; other agents will write each file's code afterward.

## What you are given
- The algorithm's specification (the ONLY source of algorithm logic).
- The mandatory entry-point function prototypes your implementation MUST export.
- The standard argument conventions for these entry points.
- Operation-specific implementation notes (the I/O contract the checksum enforces).
- The interface size constants (from api.h), already resolved to integers.

You do NOT have any reference implementation. Derive the entire structure from the spec.

## Build environment (important, affects your plan)
- The build system provides a header `api.h` defining the interface constants
  (e.g. `#define CRYPTO_ABYTES 16`). Your code includes `"api.h"` to use them.
- The file that defines the entry functions MUST `#include "crypto_{operation}.h"`
  (a namespace header the build system generates) and define the entry functions with
  their EXACT literal names and signatures. The build system handles symbol namespacing.
- All your files are compiled together and linked with the test harness. Do NOT write
  `main()` or any test/benchmark code. Do NOT define `randombytes` (for keyed operations it
  is provided — you may declare and call it, but never define it).
- Keep the implementation self-contained: do not depend on other SUPERCOP primitives or
  external libraries. If you need a hash/permutation/field primitive, plan a file for it.

## Your task
Produce a BUILD PLAN: the set of files, what each file contains (functions with exact C
signatures + a one-line purpose, and any macros/constants it defines), inter-file
dependencies, and a topological build order (files that others depend on come first;
shared constant/macro headers typically first).

- Entry-function signatures must appear VERBATIM as given (types/order unchanged).
- Internal helper decomposition is entirely your design (names, count, files).
- Prefer clear separation: constants/params header, primitive(s), the entry source.

## Output format
Return ONLY a JSON object (no prose, no markdown fence) with this shape:

{
  "files": [
    {
      "path": "params.h",
      "kind": "header",
      "role": "one-line description",
      "provides_macros": ["NAME", "..."],
      "provides_functions": [],
      "depends_on": []
    },
    {
      "path": "aead.c",
      "kind": "source",
      "role": "entry points + main construction",
      "provides_macros": [],
      "provides_functions": [
        {"signature": "int crypto_aead_encrypt(unsigned char *c, unsigned long long *clen, const unsigned char *m, unsigned long long mlen, const unsigned char *ad, unsigned long long adlen, const unsigned char *nsec, const unsigned char *npub, const unsigned char *k)", "purpose": "AEAD encryption entry point"}
      ],
      "depends_on": ["params.h"]
    }
  ],
  "build_order": ["params.h", "aead.c"]
}

`kind` is "header" for .h and "source" for .c. Every file path must have a valid C
extension. `build_order` must be a permutation of all file paths, dependency-respecting.
