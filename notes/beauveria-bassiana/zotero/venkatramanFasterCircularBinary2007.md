#### A faster circular binary segmentation algorithm for the analysis of array CGH data
E. S. Venkatraman, Adam B. Olshen
2007
[Volledige Tekst](zotero://select/library/items/SVYIHLHZ)

### Formatted Bibliography

Venkatraman, E. S., en Adam B. Olshen. ‘A Faster Circular Binary Segmentation Algorithm for the Analysis of Array CGH Data’. _Bioinformatics_ 23, nr. 6 (15 maart 2007): 657-63. [https://doi.org/10.1093/bioinformatics/btl646](https://doi.org/10.1093/bioinformatics/btl646).


### Abstract

Abstract
            Motivation: Array CGH technologies enable the simultaneous measurement of DNA copy number for thousands of sites on a genome. We developed the circular binary segmentation (CBS) algorithm to divide the genome into regions of equal copy number. The algorithm tests for change-points using a maximal t-statistic with a permutation reference distribution to obtain the corresponding P-value. The number of computations required for the maximal test statistic is O(N2), where N is the number of markers. This makes the full permutation approach computationally prohibitive for the newer arrays that contain tens of thousands markers and highlights the need for a faster algorithm.
            Results: We present a hybrid approach to obtain the P-value of the test statistic in linear time. We also introduce a rule for stopping early when there is strong evidence for the presence of a change. We show through simulations that the hybrid approach provides a substantial gain in speed with only a negligible loss in accuracy and that the stopping rule further increases speed. We also present the analyses of array CGH data from breast cancer cell lines to show the impact of the new approaches on the analysis of real data.
            Availability: An R version of the CBS algorithm has been implemented in the “DNAcopy” package of the Bioconductor project. The proposed hybrid method for the P-value is available in version 1.2.1 or higher and the stopping rule for declaring a change early is available in version 1.5.1 or higher.
            Contact:  venkatre@mskcc.org
            Supplementary information: Supplementary data are available at Bioinformatics online.


