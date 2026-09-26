# OBCX package registry — development cutover

This independent repository is the registry source. The `actor-registry/`
directory in core is a conformance snapshot, not a second validator.

## Local checks

Entries are strict v2 `entries/<package-id>/package.toml` files for actors or
ordinary libraries. Validation lives in core/SDK `package_tool.py`; this
repository contains only a command wrapper, not a copied parser or schema.
Pass the tool, entries directory and output explicitly:

```sh
python3 generate_package_index.py --tool /absolute/path/to/package_tool.py \
  validate --entries entries
python3 generate_package_index.py --tool /absolute/path/to/package_tool.py \
  generate --entries entries --output index/packages.json
python3 generate_package_index.py --tool /absolute/path/to/package_tool.py \
  generate --entries entries --output index/packages.json --check
OBCX_PACKAGE_TOOL=/absolute/path/to/package_tool.py \
  python3 -m unittest discover -s tests -v
```

The wrapper requires tool protocol 2.0.0. To inspect the authoritative schema,
use that tool's `schema --kind package --output <file>` command. Required fields
are not filled in by the registry. Metadata alone does not fetch package sources
or choose workspace dependency versions.

## Publication boundary

`index/packages.json` is explicitly `development-metadata-only`: each record
contains canonical `metadata` and its source path/hash. It does **not** advertise
binary availability, invent download URLs from version numbers, or claim that
a source metadata migration rebuilt old release assets. The previous generated
actor-only download index and its `resolve` command are removed, not retained
as a compatibility format.

Actual release inventories, verified assets, published tooling bundle pins and
remote issuance are deferred. PR automation requires an explicitly configured
full core commit in repository variable `OBCX_TOOLING_COMMIT`; no default branch
is substituted. The manual generation workflow likewise requires a full tooling
commit. Until a suitable commit is approved and available, run the local checks
above. Automatic index publication is disabled during this development cutover.
