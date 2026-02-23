 # src/tools/data_viz.py
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import base64
import numpy as np
from typing import Optional
from langchain.tools import tool

# ========== Core chart creation function ==========
def create_chart_core(data: str, chart_type: str = "bar", title: Optional[str] = None) -> str:
    """
    Core function to create charts from data.
    Input: comma-separated numbers (e.g., "10,20,30,40,50")
    Returns: Base64 encoded PNG image or error message.
    """
    try:
        values = [float(x.strip()) for x in data.split(',') if x.strip()]
        if len(values) < 2:
            return "Error: Need at least 2 data points"

        fig, ax = plt.subplots(figsize=(10, 6))

        if chart_type == "bar":
            ax.bar(range(len(values)), values, color='skyblue', edgecolor='navy', alpha=0.7)
            ax.set_xlabel("Data Points")
        elif chart_type == "line":
            ax.plot(range(len(values)), values, marker='o', linewidth=2, markersize=8, color='green')
            ax.set_xlabel("Index")
            ax.grid(True, alpha=0.3)
        elif chart_type == "pie":
            ax.pie(values, labels=[f"Item {i+1}" for i in range(len(values))],
                   autopct='%1.1f%%', startangle=90)
        elif chart_type == "scatter":
            ax.scatter(range(len(values)), values, s=100, alpha=0.6, color='red')
            ax.set_xlabel("Index")
            ax.grid(True, alpha=0.3)
        else:
            ax.bar(range(len(values)), values, color='skyblue')
            ax.set_xlabel("Data Points")

        ax.set_title(title or f"{chart_type.title()} Chart of Data")
        ax.set_ylabel("Values")

        buf = io.BytesIO()
        fig.savefig(buf, format='png', dpi=100, bbox_inches='tight')
        buf.seek(0)
        img_base64 = base64.b64encode(buf.getvalue()).decode()
        plt.close(fig)

        return f"![{chart_type} Chart](data:image/png;base64,{img_base64})"

    except Exception as e:
        return f"Chart error: {str(e)}"

# ========== Core trend analysis function ==========
def analyze_trends_core(data: str) -> str:
    """
    Core function for statistical analysis.
    Input: comma-separated numbers
    Returns: Detailed statistical analysis.
    """
    try:
        values = [float(x.strip()) for x in data.split(',') if x.strip()]
        if len(values) < 2:
            return "Error: Need at least 2 data points"

        df = pd.DataFrame({'values': values})

        stats = {
            'count': len(values),
            'mean': df['values'].mean(),
            'median': df['values'].median(),
            'mode': df['values'].mode().iloc[0] if not df['values'].mode().empty else 'N/A',
            'min': df['values'].min(),
            'max': df['values'].max(),
            'std': df['values'].std(),
            'variance': df['values'].var(),
            'skew': df['values'].skew(),
            'kurtosis': df['values'].kurtosis(),
        }

        if len(values) > 2:
            x = np.arange(len(values))
            z = np.polyfit(x, values, 1)
            stats['slope'] = z[0]
            stats['intercept'] = z[1]
            stats['trend'] = 'increasing' if stats['slope'] > 0 else 'decreasing' if stats['slope'] < 0 else 'stable'
            stats['trend_strength'] = 'strong' if abs(stats['slope']) > 1 else 'moderate' if abs(stats['slope']) > 0.5 else 'weak'

        report = f"""
## 📊 REAL Statistical Analysis

### Summary Statistics
- **Number of Data Points:** {stats['count']}
- **Mean:** {stats['mean']:.3f}
- **Median:** {stats['median']:.3f}
- **Mode:** {stats['mode']}
- **Minimum:** {stats['min']:.3f}
- **Maximum:** {stats['max']:.3f}
- **Range:** {stats['max'] - stats['min']:.3f}
- **Standard Deviation:** {stats['std']:.3f}
- **Variance:** {stats['variance']:.3f}
- **Skewness:** {stats['skew']:.3f}
- **Kurtosis:** {stats['kurtosis']:.3f}
"""

        if 'slope' in stats:
            report += f"""
### Trend Analysis
- **Trend Direction:** {stats['trend'].title()}
- **Trend Slope:** {stats['slope']:.4f}
- **Trend Strength:** {stats['trend_strength'].title()}
- **Linear Model:** y = {stats['slope']:.4f}x + {stats['intercept']:.4f}
"""

        report += f"""
### Raw Data
{', '.join([f'{x:.3f}' for x in values])}

### Interpretation
- The data shows **{stats.get('trend', 'variable')}** pattern
- Values range from {stats['min']:.2f} to {stats['max']:.2f}
- Typical value (median): {stats['median']:.2f}
- Spread (std dev): {stats['std']:.2f}
"""
        return report

    except Exception as e:
        return f"Analysis error: {str(e)}"

# ========== LangChain tools (for agents) ==========
create_chart_tool = tool(create_chart_core)
analyze_trends_tool = tool(analyze_trends_core)

# ========== Class for convenient use (no @tool on methods) ==========
class DataVisualizationTool:
    def create_chart(self, data: str, chart_type: str = "bar", title: Optional[str] = None) -> str:
        return create_chart_core(data, chart_type, title)

    def analyze_trends(self, data: str) -> str:
        return analyze_trends_core(data)