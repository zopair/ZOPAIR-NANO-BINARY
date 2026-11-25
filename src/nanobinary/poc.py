"""Command-line encode/decode workflow for the physical-scale PoC."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from nanobinary.binary import bits_to_bytes, bytes_to_bits
from nanobinary.pgm import read_binary_grid, write_binary_grid


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Render and recover an unchanged binary sequence as a 2-D grid."
    )
    commands = parser.add_subparsers(dest="command", required=True)

    encode = commands.add_parser("encode", help="render an input file as a binary PGM grid")
    encode.add_argument("--input", required=True, type=Path)
    encode.add_argument("--output", required=True, type=Path)
    encode.add_argument("--manifest", type=Path)
    encode.add_argument("--rows", type=int, default=1000)
    encode.add_argument("--columns", type=int, default=1000)
    encode.add_argument("--cell-px", type=int, default=3)
    encode.add_argument("--gap-px", type=int, default=2)

    decode = commands.add_parser("decode", help="recover a file from an aligned PGM grid")
    decode.add_argument("--input", required=True, type=Path)
    decode.add_argument("--output", required=True, type=Path)
    decode.add_argument("--rows", type=int, default=1000)
    decode.add_argument("--columns", type=int, default=1000)
    decode.add_argument("--cell-px", type=int, default=3)
    decode.add_argument("--gap-px", type=int, default=2)
    decode.add_argument("--threshold", type=int, default=127)
    decode.add_argument("--invert", action="store_true")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)

    if args.command == "encode":
        source = args.input.read_bytes()
        bits = bytes_to_bits(source)
        if len(bits) != args.rows * args.columns:
            raise SystemExit(
                f"Input contains {len(bits)} bits; requested grid contains "
                f"{args.rows * args.columns} cells. No padding or truncation is allowed."
            )
        width, height = write_binary_grid(
            bits,
            args.output,
            rows=args.rows,
            columns=args.columns,
            cell_px=args.cell_px,
            gap_px=args.gap_px,
        )
        manifest = {
            "format": "PGM P5, 8-bit grayscale",
            "source_sha256": hashlib.sha256(source).hexdigest(),
            "bit_count": len(bits),
            "rows": args.rows,
            "columns": args.columns,
            "cell_px": args.cell_px,
            "gap_px": args.gap_px,
            "raster_width_px": width,
            "raster_height_px": height,
            "mapping": {"0": "black", "1": "white"},
            "physical_measurement": "not measured; set by print/scan process",
        }
        manifest_path = args.manifest or args.output.with_suffix(".json")
        manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
        print(f"Rendered {len(bits):,} bits to {width}x{height} PGM: {args.output}")
        print(f"Manifest: {manifest_path}")
        return 0

    bits = read_binary_grid(
        args.input,
        rows=args.rows,
        columns=args.columns,
        cell_px=args.cell_px,
        gap_px=args.gap_px,
        threshold=args.threshold,
        invert=args.invert,
    )
    recovered = bits_to_bytes(bits)
    args.output.write_bytes(recovered)
    print(f"Recovered {len(bits):,} bits ({len(recovered):,} bytes): {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
