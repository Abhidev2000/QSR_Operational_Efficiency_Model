# QSR Operational Efficiency Model: Identifying 15-Minute Profit Leakage

[QSR Dashboard](QSR_Dashboard_BI.png)

## The Business Problem
Quick-Service Restaurants (QSRs) and retail operations frequently experience "Profit Leakage." This occurs when labor schedules do not align with actual customer footfall—resulting in overstaffing during lulls (wasting cash) and understaffing during rushes (losing potential revenue and increasing wait times). 

Having managed POS systems and handled 500+ daily customer interactions in a high-volume operational environment, I experienced this bottleneck firsthand. I built this full-stack data pipeline to solve it.

## The Solution
I engineered an automated data model that merges disjointed HR shift schedules with raw POS transaction logs, breaking the data down into 15-minute rolling windows to visualize the exact moments labor costs exceed revenue.

## The Tech Stack & Architecture
* **Python:** Scripted synthetic, high-volume POS transaction logs and HR scheduling data to mimic the chaotic reality of a multi-store retail environment.
* **SQL (PostgreSQL):** Utilized Common Table Expressions (CTEs), Window Functions, and Date/Time formatting to standardize and merge the disparate HR and Sales databases into a single analytical table.
* **Power BI:** Designed an executive-level dashboard focusing on high-contrast visual storytelling (Cost vs. Revenue) to allow Area Managers to instantly identify operational inefficiencies on a shift-by-shift basis.

## Key Insights
* **Granular Visibility:** Transformed massive daily aggregations into actionable 15-minute operational heartbeats.
* **Cost Contrast:** Visually isolated the exact timestamps where the labor cost percentage spiked dangerously above the generated revenue.
