# Available Parsers

The following parser packages are currently available for use with `bam-masterdata`.
The dependency specifications below include the minimum versions or Git references to use.

| Parser package | Description | Dependency specification |
| --- | --- | --- |
| `bruker-powderxrd-parser` | A parser for Bruker Powder X-ray diffraction (XRD) data into openBIS. | [GitHub](https://github.com/BAMresearch/bruker-powderxrd-parser) |
| `sigmabam2openbis` | Converts SigmaBAM chemical inventory exports into an openBIS-compatible format. | [GitHub](https://github.com/BAMresearch/sigmabam2openbis) |
| `tof-sims-parser` | Parses ION-TOF ToF-SIMS SurfaceLab files and extracts measurement metadata for openBIS. | [GitHub](https://github.com/BAMresearch/Tof-Sims-Parser) |
| `creep-test-parser` | A parser for creep testing data at BAM, designed for integration with openBIS. | [GitHub](https://github.com/BAMresearch/creep-test-parser) |
| `bam-upload-parsers` | A collection of parsers for automatically extracting metadata from measurement files and uploading it to openBIS. | [GitHub](https://github.com/BAMresearch/openbis-metadata-parsers) |

## Parsers included in `bam-upload-parsers`

The `bam-upload-parsers` package provides six individual parsers:

| Parser | Description |
| --- | --- |
| **SEM** | Parses scanning electron microscopy (SEM) data and associated measurement metadata. |
| **Plate Reader** | Parses plate reader measurement data from multi-well plate experiments. |
| **IR** | Parses infrared (IR) spectroscopy data and associated measurement metadata. |
| **NMR** | Parses nuclear magnetic resonance (NMR) spectroscopy data and associated measurement metadata. |
| **TEM** | Parses transmission electron microscopy (TEM) data and associated measurement metadata. |
| **DLS** | Parses dynamic light scattering (DLS) measurement data used for particle size analysis. |