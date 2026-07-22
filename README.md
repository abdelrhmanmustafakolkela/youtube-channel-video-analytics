# YouTube Channel Video Analytics

A Python data-analysis script that reads a channel's video statistics from an Excel file and produces a full set of visual reports — with **Arabic label support** (RTL-aware text rendering for charts).

## What it does

Given an Excel sheet with columns for video name, publish date, views, likes, and comments (in Arabic), the script generates:

- **Scatter chart** — views per video, colored by likes
- **Bar charts** — views per video, likes per video
- **Line charts** — views over time, likes over time
- **Histograms** — distribution of views, distribution of likes
- **Correlation heatmap** — views vs likes vs comments
- **Pie chart** — top 10 videos by views
- **Bubble chart** — views vs likes, bubble size = comments
- **Summary report** (`.txt`) — totals, averages, top videos, correlation matrix
- **Combined PDF report** with every chart

All charts are saved as high-resolution PNGs (300 DPI) plus one combined PDF, in a `charts/` folder.

## Requirements

```bash
pip install pandas matplotlib seaborn numpy arabic-reshaper python-bidi openpyxl
```

## Usage

1. Place your Excel file (with Arabic column headers: `تاريخ النشر`, `عدد المشاهدات`, `عدد اللايكات`, `عدد التعليقات`, `اسم الفيديو`) in the project folder.
2. Update the file path in `video_analysis.py` if needed.
3. Run:
   ```bash
   python video_analysis.py
   ```
4. Check the `charts/` folder for the generated PNGs, the PDF report, and `summary_report.txt`.

## Repository contents

```
youtube-channel-video-analytics/
├── video_analysis.py                          # Main analysis script
├── فيديوهات_القناة_احصائيات.xlsx      # Source data (28 videos)
└── charts/
    └── summary_report.txt                      # Text summary of the analysis
```

> **Note:** The generated chart images (`.png`) and the combined `video_analysis_report.pdf` from the original upload were left out of this repo since they are large binary files that can be regenerated at any time by simply running the script. Let me know if you'd like them pushed too.

## License

MIT
