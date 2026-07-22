import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib import rcParams
import arabic_reshaper
from bidi.algorithm import get_display
from matplotlib.backends.backend_pdf import PdfPages

# Set Arabic font support with RTL
rcParams['font.family'] = 'Arial'
rcParams['figure.figsize'] = (12, 8)
rcParams['figure.dpi'] = 100

def fix_arabic_text(text):
    """Fix Arabic text direction for matplotlib"""
    if isinstance(text, str):
        reshaped_text = arabic_reshaper.reshape(text)
        return get_display(reshaped_text)
    return text

# Read the Excel file
df = pd.read_excel('فيديوهات_القناة_احصائيات.xlsx')

# Convert date column to datetime
df['تاريخ النشر'] = pd.to_datetime(df['تاريخ النشر'])

# Sort by date for time series
df_sorted = df.sort_values('تاريخ النشر')

# Create output directory for charts
import os
os.makedirs('charts', exist_ok=True)

# Create PDF file
pdf_filename = 'charts/video_analysis_report.pdf'
pdf = PdfPages(pdf_filename)

print("Generating visualizations...")

# 1. SCATTER CHART: x-axis = video names, y-axis = views, color = likes
plt.figure(figsize=(16, 10))
scatter = plt.scatter(range(len(df)), df['عدد المشاهدات'], 
                      c=df['عدد اللايكات'], cmap='viridis', 
                      s=100, alpha=0.7, edgecolors='black', linewidth=1)
plt.colorbar(scatter, label=fix_arabic_text('عدد اللايكات'))
plt.xlabel(fix_arabic_text('أسماء الفيديوهات'), fontsize=12)
plt.ylabel(fix_arabic_text('عدد المشاهدات'), fontsize=12)
plt.title(fix_arabic_text('علاقة المشاهدات واللايكات لكل فيديو'), fontsize=14, fontweight='bold')
plt.xticks(range(len(df)), [fix_arabic_text(name) for name in df['اسم الفيديو']], rotation=90, ha='right', fontsize=8)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('charts/scatter_views_likes.png', dpi=300, bbox_inches='tight')
pdf.savefig()
plt.close()

# 2. BAR CHART: Views per video
plt.figure(figsize=(16, 8))
plt.bar(range(len(df)), df['عدد المشاهدات'], color='steelblue', edgecolor='black')
plt.xlabel(fix_arabic_text('أسماء الفيديوهات'), fontsize=12)
plt.ylabel(fix_arabic_text('عدد المشاهدات'), fontsize=12)
plt.title(fix_arabic_text('عدد المشاهدات لكل فيديو'), fontsize=14, fontweight='bold')
plt.xticks(range(len(df)), [fix_arabic_text(name) for name in df['اسم الفيديو']], rotation=90, ha='right', fontsize=8)
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig('charts/bar_views.png', dpi=300, bbox_inches='tight')
pdf.savefig()
plt.close()

# 3. BAR CHART: Likes per video
plt.figure(figsize=(16, 8))
plt.bar(range(len(df)), df['عدد اللايكات'], color='coral', edgecolor='black')
plt.xlabel(fix_arabic_text('أسماء الفيديوهات'), fontsize=12)
plt.ylabel(fix_arabic_text('عدد اللايكات'), fontsize=12)
plt.title(fix_arabic_text('عدد اللايكات لكل فيديو'), fontsize=14, fontweight='bold')
plt.xticks(range(len(df)), [fix_arabic_text(name) for name in df['اسم الفيديو']], rotation=90, ha='right', fontsize=8)
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig('charts/bar_likes.png', dpi=300, bbox_inches='tight')
pdf.savefig()
plt.close()

# 4. LINE CHART: Views over time
plt.figure(figsize=(14, 6))
plt.plot(df_sorted['تاريخ النشر'], df_sorted['عدد المشاهدات'], marker='o', linewidth=2, markersize=8, color='steelblue')
plt.xlabel(fix_arabic_text('تاريخ النشر'), fontsize=12)
plt.ylabel(fix_arabic_text('عدد المشاهدات'), fontsize=12)
plt.title(fix_arabic_text('تطور المشاهدات مع الوقت'), fontsize=14, fontweight='bold')
plt.xticks(rotation=45, ha='right')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('charts/line_views_time.png', dpi=300, bbox_inches='tight')
pdf.savefig()
plt.close()

# 5. LINE CHART: Likes over time
plt.figure(figsize=(14, 6))
plt.plot(df_sorted['تاريخ النشر'], df_sorted['عدد اللايكات'], marker='o', linewidth=2, markersize=8, color='coral')
plt.xlabel(fix_arabic_text('تاريخ النشر'), fontsize=12)
plt.ylabel(fix_arabic_text('عدد اللايكات'), fontsize=12)
plt.title(fix_arabic_text('تطور اللايكات مع الوقت'), fontsize=14, fontweight='bold')
plt.xticks(rotation=45, ha='right')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('charts/line_likes_time.png', dpi=300, bbox_inches='tight')
pdf.savefig()
plt.close()

# 6. HISTOGRAM: Views
plt.figure(figsize=(10, 6))
plt.hist(df['عدد المشاهدات'], bins=15, color='steelblue', edgecolor='black', alpha=0.7)
plt.xlabel(fix_arabic_text('عدد المشاهدات'), fontsize=12)
plt.ylabel(fix_arabic_text('عدد الفيديوهات'), fontsize=12)
plt.title(fix_arabic_text('توزيع المشاهدات'), fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig('charts/histogram_views.png', dpi=300, bbox_inches='tight')
pdf.savefig()
plt.close()

# 7. HISTOGRAM: Likes
plt.figure(figsize=(10, 6))
plt.hist(df['عدد اللايكات'], bins=15, color='coral', edgecolor='black', alpha=0.7)
plt.xlabel(fix_arabic_text('عدد اللايكات'), fontsize=12)
plt.ylabel(fix_arabic_text('عدد الفيديوهات'), fontsize=12)
plt.title(fix_arabic_text('توزيع اللايكات'), fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig('charts/histogram_likes.png', dpi=300, bbox_inches='tight')
pdf.savefig()
plt.close()

# 8. CORRELATION HEATMAP
plt.figure(figsize=(10, 8))
correlation_data = df[['عدد المشاهدات', 'عدد اللايكات', 'عدد التعليقات']].corr()
correlation_data.columns = [fix_arabic_text(col) for col in correlation_data.columns]
correlation_data.index = [fix_arabic_text(idx) for idx in correlation_data.index]
sns.heatmap(correlation_data, annot=True, cmap='coolwarm', center=0, square=True, linewidths=1, cbar_kws={"shrink": 0.8})
plt.title(fix_arabic_text('مصفوفة الارتباط'), fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('charts/correlation_heatmap.png', dpi=300, bbox_inches='tight')
pdf.savefig()
plt.close()

# 9. PIE CHART: Top 10 videos by views
top_10_views = df.nlargest(10, 'عدد المشاهدات')
plt.figure(figsize=(10, 10))
colors = plt.cm.Set3(range(len(top_10_views)))
plt.pie(top_10_views['عدد المشاهدات'], labels=[fix_arabic_text(name) for name in top_10_views['اسم الفيديو']], autopct='%1.1f%%', startangle=90, colors=colors)
plt.title(fix_arabic_text('أعلى 10 فيديوهات من حيث المشاهدات'), fontsize=14, fontweight='bold')
plt.axis('equal')
plt.tight_layout()
plt.savefig('charts/pie_top10_views.png', dpi=300, bbox_inches='tight')
pdf.savefig()
plt.close()

# 10. BUBBLE CHART: Views vs Likes (size = comments)
plt.figure(figsize=(12, 8))
plt.scatter(df['عدد المشاهدات'], df['عدد اللايكات'], s=df['عدد التعليقات']*10 + 50, alpha=0.6, c='purple', edgecolors='black')
plt.xlabel(fix_arabic_text('عدد المشاهدات'), fontsize=12)
plt.ylabel(fix_arabic_text('عدد اللايكات'), fontsize=12)
plt.title(fix_arabic_text('المشاهدات مقابل اللايكات (حجم الدائرة = التعليقات)'), fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('charts/bubble_views_likes_comments.png', dpi=300, bbox_inches='tight')
pdf.savefig()
plt.close()

# Save summary to file
with open('charts/summary_report.txt', 'w', encoding='utf-8') as f:
    f.write('='*50 + '\n')
    f.write('VIDEO DATA ANALYSIS SUMMARY REPORT\n')
    f.write('='*50 + '\n\n')
    f.write(f"Total videos: {len(df)}\n")
    f.write(f"Total views: {df['عدد المشاهدات'].sum():,}\n")
    f.write(f"Total likes: {df['عدد اللايكات'].sum():,}\n")
    f.write(f"Total comments: {df['عدد التعليقات'].sum():,}\n\n")
    f.write(f"Average views per video: {df['عدد المشاهدات'].mean():.2f}\n")
    f.write(f"Average likes per video: {df['عدد اللايكات'].mean():.2f}\n")
    f.write(f"Average comments per video: {df['عدد التعليقات'].mean():.2f}\n\n")
    f.write(f"Max views: {df['عدد المشاهدات'].max():,}\n")
    f.write(f"Max likes: {df['عدد اللايكات'].max():,}\n\n")
    f.write(f"Top video by views: {df.loc[df['عدد المشاهدات'].idxmax(), 'اسم الفيديو']}\n")
    f.write(f"Top video by likes: {df.loc[df['عدد اللايكات'].idxmax(), 'اسم الفيديو']}\n\n")
    f.write('Correlation Matrix:\n')
    f.write(correlation_data.to_string())

# Close PDF file
pdf.close()
print(f"\nAll charts and reports saved in 'charts' directory! PDF: {pdf_filename}")
