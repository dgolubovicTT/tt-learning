# tt-learning

Learning material for Tenstorrent hardware and software, organised by topic.

Each page is a single standalone HTML file with no build step and no external
dependencies. Browse online at
**[dgolubovictt.github.io/tt-learning](https://dgolubovictt.github.io/tt-learning/)**,
or clone the repo and open any file directly in a browser.

## Topics

### [Kernel programming](kernel-programming/)

Writing and reasoning about Tensix kernels, on a Wormhole N150.

| Page | What it is |
|---|---|
| [Roofline](kernel-programming/roofline.html) | Interactive performance model. What bandwidth and compute throughput actually mean, how `GB/s`, `TFLOP/s` and `FLOP/byte` connect, where both hardware ceilings come from on Wormhole and Blackhole, and a live chart with knobs for algorithm, data format, cores, fidelity and clock. |
| [Crossing the Ridge](kernel-programming/test.html) | A 19-statement true/false self-test on which performance levers actually move a kernel between the memory-bound and compute-bound regimes. |

## Layout

```
index.html            topic list
shell.css             shared styling for the index pages
<topic>/
  index.html          the topic's contents
  <page>.html         standalone, self-contained
```

Adding a topic means creating a folder with its own `index.html` and linking it
from the root index.

## Where the numbers come from

Every hardware figure is derived from the public
[tt-metal](https://github.com/tenstorrent/tt-metal) repository, and the source
file is cited in each page's footer:

- `tech_reports/matrix_engine/matrix_engine.md` — matrix engine throughput and
  the math-fidelity table
- `tech_reports/GEMM_FLOPS/GEMM_FLOPS.md` — cycles per tile, maximum compute grids
- `tech_reports/Blackhole/BlackholeBringUpProgrammingGuide.md` — grid, bank and
  L1 geometry for both architectures
- `tech_reports/FlashAttention/FlashAttention.md` — DRAM channels and theoretical
  bandwidth
- `tech_reports/LLMs/llms.md` — achieved interleaved and sharded bandwidth

Peak figures assume a 1 GHz clock, which the matrix-engine report uses
throughout. Substitute your board's real frequency from
`device->get_clock_rate_mhz()`.

## Licence

Apache-2.0.
