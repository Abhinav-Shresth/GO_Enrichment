# GO Enrichment Analysis of Promoter Regions
GO_Enrichment
This project focuses on identifying genes containing a specific transcription factor binding motif in their promoter regions and performing Gene Ontology (GO) enrichment analysis on the resulting gene set.

The workflow includes:

* Generating TSS BED coordinates
* Extracting upstream promoter regions
* Mapping promoter sequences from the human genome
* Searching for transcription factor motifs
* Performing GO enrichment analysis

Based on the assignment description provided in 

## Project Structure

```text
go_project/
│
├── data/
│   └── Reference genome and annotation files
│
├── input_bed/
│   └── Original TSS BED files
│
├── mapped/
│   └── Extracted FASTA sequences from promoter regions
│
├── results/
│   └── Motif search and enrichment analysis outputs
│
├── scripts/
│   └── create_tss_bed.py
│
└── sorted_beds/
    └── Sorted BED files for downstream processing
```

## Objective

The aim of this project is to analyze transcription factor binding motifs within promoter regions of human genes and infer biological functions associated with the identified genes through GO enrichment analysis.

The motif explored in this assignment is:

```text
GCGC..GCGC
```

This sequence is associated with the NRF1 transcription factor, which is involved in mitochondrial biogenesis and several cellular regulatory processes.

## Workflow

### 1. Generate TSS BED File

Gene annotation data is converted into BED format containing:

* Chromosome
* Transcription Start Site (TSS)
* Strand information
* Gene identifiers

Example:

```text
chr1    11869   11870   chr1@11869-11870|DDX11L2        .       +
```

Script used:

```bash
python scripts/create_tss_bed.py
```

## 2. Create Upstream Promoter Regions

Promoter regions extending 500 bases upstream of each TSS are generated in a strand-aware manner using `bedtools slop`.

Example output:

```text
tss_upstream_500.bed
```

## 3. Extract Genome Sequences

Promoter sequences are extracted from the human genome FASTA file.

Generated file:

```text
tss_upstream_500.fa
```

## 4. Motif Search

The promoter FASTA sequences are scanned for the NRF1 motif:

```text
GCGC..GCGC
```

Genes containing motif matches are collected for downstream analysis.

## 5. GO Enrichment Analysis

The identified gene list is analyzed using GO enrichment tools such as:

* clusterProfiler
* Bioconductor packages

The enrichment analysis helps determine overrepresented biological functions and pathways.

## Files Included

| File                   | Description                                     |
| ---------------------- | ----------------------------------------------- |
| `tss.bed`              | BED file containing TSS coordinates             |
| `tss_upstream_500.bed` | 500 bp upstream promoter regions                |
| `tss_upstream_500.fa`  | FASTA sequences extracted from promoter regions |
| `create_tss_bed.py`    | Script for generating TSS BED file              |

## Tools and Technologies

* Python 3.12
* BEDTools
* EMBOSS
* clusterProfiler
* Bioconductor
* Human Genome hg38
* Linux / WSL / macOS environment

## Environment Setup

Create environment:

```bash
mamba create -n go_enrichment python=3.12
```

Activate environment:

```bash
mamba activate go_enrichment
```

Install dependencies:

```bash
mamba install bioconda::emboss
mamba install bioconda::bedtools
```

## Required Datasets

### Human Genome

Download:

```text
hg38.fa.gz
```

From:

```text
https://hgdownload.soe.ucsc.edu/goldenPath/hg38/bigZips/
```

### Additional Tools

* EMBOSS
* BEDTools
* clusterProfiler

## Example Pipeline

### Generate BED file

```bash
python scripts/create_tss_bed.py
```

### Sort BED file

```bash
sort -k1,1 -k2,2n tss.bed > sorted_tss.bed
```

### Generate upstream regions

```bash
bedtools slop \
-i sorted_tss.bed \
-g genome.txt \
-l 500 \
-r 0 \
-s > tss_upstream_500.bed
```

### Extract FASTA sequences

```bash
bedtools getfasta \
-fi hg38.fa \
-bed tss_upstream_500.bed \
-s \
-fo tss_upstream_500.fa
```

## Learning Outcomes

This project demonstrates:

* Genomic coordinate manipulation
* BED file processing
* Strand-aware promoter extraction
* FASTA sequence generation
* Motif discovery
* Functional genomics analysis
* GO enrichment workflows

