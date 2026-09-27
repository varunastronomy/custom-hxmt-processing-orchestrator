<p align="center"><img src="assets/banner.svg" alt="Custom HXMT Processing Orchestrator cover" width="100%"></p>

# Custom HXMT Processing Orchestrator

[![Quality checks](https://github.com/varunastronomy/custom-hxmt-processing-orchestrator/actions/workflows/quality-checks.yml/badge.svg)](https://github.com/varunastronomy/custom-hxmt-processing-orchestrator/actions/workflows/quality-checks.yml)

Research-stage orchestration template for HE, ME, and LE Insight-HXMT product workflows.

> **Scientific boundary:** This is a partial template: several mission-tool stages are commented out and the active commands require HXMTDAS, calibration, correct detector selections, and source-specific validation.

## Copyright, permission, and mandatory citation

> **COPYRIGHT © 2026 M. VARUN, CHRIST (DEEMED TO BE UNIVERSITY), BENGALURU, INDIA. ALL RIGHTS RESERVED.**
>
> **NO PERMISSION IS GRANTED TO USE, COPY, MODIFY, REDISTRIBUTE, REPUBLISH, OR INCORPORATE THIS SOFTWARE INTO ANOTHER PROJECT WITHOUT PRIOR WRITTEN PERMISSION FROM THE AUTHOR. APPROVED USE REQUIRES CLEAR ATTRIBUTION AND CITATION.**

## Installation and use

```bash
python -m pip install -r requirements.txt
python hxmt_processing_orchestrator.py --help
```

Some interactive scripts do not implement `--help`; run them from a prepared analysis directory and follow their prompts. Read the source-level defaults before execution. Mission-specific programs additionally require the relevant mission software, calibration, network access, and data layout.

## Provenance and validation

The scientific source is copied from `Final_HXMT_pipeline.py` in the private research archive. The archived original remains unchanged. Repository checks validate Python syntax only. No real observation, mission pipeline, fit, download, plot suite, or scientific result was executed or validated for publication. Outputs must be inspected before scientific use.

No open-source license is granted. Citation metadata are in [`CITATION.cff`](CITATION.cff).

## Author

**M. Varun**<br>X-ray astronomy researcher and scientific Python developer<br>CHRIST (Deemed to be University), Bengaluru, India<br>[GitHub: varunastronomy](https://github.com/varunastronomy)
