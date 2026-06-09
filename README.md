# VCH Medical Imaging — Capacity Planning Dashboard
 
A comprehensive analytics platform for Vancouver Coastal Health and Providence Health Care medical imaging operations, designed to support capacity planning decisions across all sites, modalities, and stakeholder roles.
 
---
 
## Overview
 
This dashboard consolidates patient volume, exam throughput, equipment status, labour FTEs, population demand, and waitlist data into a single role-aware interface. It was built to help medical imaging leadership move from reactive reporting to proactive capacity planning.
 
---
 
## Sites & Health Authorities
 
| Health Authority | Sites |
|---|---|
| VCH | VGH, UBC, RHS, LGH, SGH, SSH, QGH, WHC |
| PHC | SPH, MSJ |
 
Filters allow drill-down by health authority, individual site, modality, and reporting period. All views update dynamically based on the active filter context.
 
---
 
## Modalities
 
X-Ray · MRI · CT · Ultrasound (US) · Echocardiography (Echo) · Nuclear Medicine (Nuc Med) · Interventional Radiology (IR)
 
---
 
## Role-Based Views
 
The dashboard enforces role-level access by surfacing only the tabs and data relevant to each stakeholder. Switch roles using the selector in the top-right header.
 
| Role | Available tabs |
|---|---|
| Executive / Leadership | Overview, Demand vs Capacity, Alerts, AI Insights |
| Site Manager | Overview, Site Detail, Equipment, Labour FTEs, Waitlist, AI Insights |
| Modality Lead | Overview, Modality View, Equipment, Waitlist, AI Insights |
| Finance / Planning | Overview, Demand vs Capacity, Labour FTEs, Forecast, AI Insights |
| Clinical / Radiologist | Overview, Waitlist, Demand vs Capacity, AI Insights |
 
---
 
## Features
 
### Patient & Exam Volume
Toggle between patient count and exam count across any combination of sites and modalities. Year-over-year comparison with percentage change indicators.
 
### Demand vs Capacity
Modality-level utilisation rates with RAG thresholds:
- **< 80%** — optimal operating range
- **80–90%** — watch, monitor closely
- **> 90%** — critical, immediate action required
12-month seasonal trend line included for context.
 
### Equipment Inventory
Per-site, per-modality breakdown showing unit count, average equipment age (years), utilisation percentage, and condition status (Good / Fair / Aging / Critical). Visual utilisation bars with colour-coded status pills.
 
### Labour FTEs
FTE breakdown by role (Radiologists, Technologists, Admin & Clerical) per site. Stacked bar chart for cross-site comparison. Finance view includes a 2025 FTE demand projection with gap analysis and recommended actions (Maintain / Plan hire / Urgent recruit).
 
### Population & Visitor Demand
Catchment population and annual visitor volume per site, used alongside volume data to contextualise demand pressure relative to community size.
 
### Waitlist Analysis
Waitlist wait times (days) by site and modality in a full matrix view. Colour-coded against benchmarks:
- **< 30 days** — on target
- **30–60 days** — watch
- **> 60 days** — critical
### Alert Triage
Automated flags generated from equipment status, utilisation rates, and waitlist thresholds. Categorised as Critical, Warning, or Informational with plain-language descriptions and suggested actions.
 
### Demand Forecast (Finance / Planning view)
2025 monthly demand forecast using seasonal decomposition on 24 months of historical data, with population growth (2.1% per year) and visitor uplift applied. 95% confidence interval band displayed. Accompanied by FTE gap projection table.
 
### AI Insights Assistant
A conversational assistant powered by the Anthropic API (claude-sonnet-4-20250514) scoped to the active filter context and stakeholder role. Answers questions about site-specific pressure, modality trends, equipment risk, and staffing gaps using the live dashboard data as context.
 
---
 
## Tech Stack
 
| Layer | Technology |
|---|---|
| Frontend framework | React |
| Charting | Chart.js 4.4.1 |
| AI assistant | Anthropic Messages API (claude-sonnet-4-20250514) |
| Data processing | Python (pandas) |
| Styling | VCH brand guidelines — custom CSS |
 
---
 
## Branding
 
Styled to VCH brand standards:
 
| Token | Value |
|---|---|
| Ocean Blue (primary) | `#0078AE` |
| Harbour Teal (dark accent) | `#006271` |
| Seaside Teal (secondary) | `#009793` |
| Cyan Blue (light fill) | `#D4EFFC` |
| Sunlit Green (positive) | `#C1D82F` |
| Cool Grey (muted text) | `#53585F` |
 
---
 
## Data Notes
 
All data in the current build is **synthetic and generated for demonstration purposes**. No real patient, staffing, or operational data is included. To connect live data, replace the `SITE_DATA` object with your API or database integration layer.
 
---
 
## Acknowledgements
 
Developed based on what I observed in a recent Data Analytics Hackathon in Vancouver, Canada and my knowledge of internal processes of Vancouver Coastal Health Medical Imaging. 
