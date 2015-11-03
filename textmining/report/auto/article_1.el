(TeX-add-style-hook
 "article_1"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("scrartcl" "DIV=calc" "paper=a4" "fontsize=11pt" "twocolumn")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("babel" "english") ("microtype" "protrusion=true" "expansion=true") ("xcolor" "svgnames") ("caption" "hang" "small" "labelfont=bf" "up" "textfont=it") ("appendix" "toc" "page")))
   (TeX-run-style-hooks
    "latex2e"
    "scrartcl"
    "scrartcl10"
    "lipsum"
    "babel"
    "microtype"
    "amsmath"
    "amsfonts"
    "amsthm"
    "xcolor"
    "caption"
    "booktabs"
    "fix-cm"
    "graphicx"
    "subfig"
    "cite"
    "appendix"
    "sectsty"
    "fancyhdr"
    "lastpage"
    "lettrine"
    "titling")
   (TeX-add-symbols
    '("initial" 1)
    "HorRule")
   (LaTeX-add-labels
    "classification")
   (LaTeX-add-bibliographies
    "sample")))

