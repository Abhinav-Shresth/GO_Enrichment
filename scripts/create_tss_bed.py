import gzip

with gzip.open("data/human_gene_annotation.tsv.gz", "rt") as f:

    next(f)

    for line in f:

        cols = line.strip().split("\t")

        chrom = cols[4]
        tss = cols[7]
        gene = cols[6]
        strand_num = cols[5]

        if strand_num == "1":
            strand = "+"
        else:
            strand = "-"

        start = int(tss)
        end = start + 1

        if chrom == "MT":
            chrom = "chrM"
        else:
            chrom = "chr" + chrom

        name = f"{chrom}@{start}-{end}|{gene}"

        print(
            chrom,
            start,
            end,
            name,
            ".",
            strand,
            sep="\t"
        )