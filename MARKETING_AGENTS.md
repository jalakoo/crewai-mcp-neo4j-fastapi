# TradieMate Marketing Analytics Agents

This document describes the specialized CrewAI agents configured for Google Ads campaign optimization and website performance analysis for trade businesses.

## 🎯 Agent Overview

The system uses **two specialized marketing agents** that automatically route queries based on content:

### 1. Google Ads Campaign Analyst
**Role**: Google Ads Campaign Analyst  
**Specialization**: PPC campaign optimization for trade businesses

**Expertise**:
- Campaign performance analysis (CTR, CPC, conversion rates, ROAS)
- Keyword effectiveness and bidding strategies
- Audience targeting optimization
- Budget allocation recommendations
- Competitor analysis and market positioning

**Triggers**: Queries containing keywords like:
- `ads`, `campaign`, `google ads`, `ppc`, `cpc`, `roas`, `ad spend`, `keywords`, `bidding`

### 2. Website Optimization Specialist  
**Role**: Website Optimization Specialist  
**Specialization**: Conversion rate optimization for trade websites

**Expertise**:
- Website performance analysis
- User behavior and conversion funnel optimization
- Landing page effectiveness
- Lead generation improvements
- SEO and organic traffic analysis

**Triggers**: Queries containing keywords like:
- `website`, `conversion`, `landing page`, `traffic`, `bounce rate`, `user experience`, `seo`

## 🔄 Intelligent Query Routing

The system automatically selects the most appropriate agent based on query content:

```python
# Google Ads queries → Ads Analyst
"How can we improve our plumbing ads ROAS?"
"Which keywords are driving the most conversions?"
"What's our best performing campaign?"

# Website queries → Web Optimizer  
"Why is our landing page bounce rate so high?"
"How can we improve quote request conversions?"
"What traffic sources convert best?"

# General queries → Default to Ads Analyst
"How can we get more leads?"
"What's our marketing performance?"
```

## 📊 Analysis Framework

Each agent follows a structured 5-step analysis process:

### 1. Data Discovery
- Examine Neo4j database schema
- Identify available marketing data sources
- Map relationships between campaigns, keywords, and conversions

### 2. Query Construction  
- Build targeted Cypher queries
- Extract relevant performance metrics
- Gather historical trend data

### 3. Performance Analysis
**Google Ads Focus**:
- Campaign ROI and ROAS analysis
- Keyword performance and search volume trends
- Ad group effectiveness and quality scores
- Audience segment performance
- Geographic and demographic insights

**Website Focus**:
- Traffic source analysis and attribution
- User journey and conversion funnel mapping
- Page performance and engagement metrics
- Form completion and lead quality analysis
- Mobile vs desktop performance

### 4. Insight Generation
- Identify optimization opportunities
- Discover performance patterns and trends
- Benchmark against industry standards
- Highlight underperforming areas

### 5. Actionable Recommendations
- Prioritized improvement strategies
- Budget reallocation suggestions
- Implementation timelines
- Success metrics and KPIs

## 📋 Output Format

Each analysis provides a comprehensive report:

### Executive Summary
- Key findings and primary recommendations
- High-impact opportunities identified
- Expected ROI from recommended changes

### Performance Metrics
- Current performance data with Neo4j evidence
- Trend analysis and benchmark comparisons
- Conversion funnel breakdown

### Optimization Opportunities
- Specific improvement areas with quantified impact
- Budget reallocation recommendations
- Targeting and messaging improvements
- Technical optimizations

### Action Plan
- Prioritized list of actionable recommendations
- Implementation timeline and resource requirements
- Success metrics to track progress
- Risk assessment and mitigation strategies

### Supporting Data
- Cypher queries used for analysis
- Data visualizations and insights
- Methodology explanation and assumptions

## 🎯 Trade Business Focus

Both agents are specifically trained for trade businesses with understanding of:

**Customer Behavior**:
- Emergency vs planned service requests
- Seasonal demand patterns
- Local market dynamics
- Price sensitivity and decision factors

**Marketing Challenges**:
- Local competition and market saturation
- Trust and credibility building
- Mobile-first customer interactions
- Quote request optimization

**Success Metrics**:
- Lead quality over quantity
- Cost per qualified lead
- Customer lifetime value
- Geographic market penetration

## 💡 Example Queries

### Google Ads Optimization
```
"What are our top performing Google Ads campaigns and how can we optimize budget allocation?"
"Which keywords are driving the most qualified leads for our electrical services?"
"How can we improve our plumbing ads ROAS in the Sydney market?"
"What audience segments convert best for our HVAC campaigns?"
```

### Website Optimization
```
"Why is our landing page conversion rate declining?"
"How can we improve quote request completions on mobile?"
"What traffic sources are bringing the highest quality leads?"
"Which pages have the highest bounce rates and how can we fix them?"
```

### General Marketing Analytics
```
"What's our overall marketing performance this quarter?"
"How can we get more leads for our roofing services?"
"What's the best channel for customer acquisition?"
"How do our conversion rates compare to industry benchmarks?"
```

## 🔧 Configuration

### Environment Requirements
- `OPENAI_API_KEY` - For LLM inference
- `NEO4J_URI` - Marketing data database
- `NEO4J_USERNAME` - Database authentication  
- `NEO4J_PASSWORD` - Database authentication

### Agent Features
- **Reasoning enabled** - For complex marketing analysis
- **Verbose mode** - For transparency in decision-making
- **Planning enabled** - For coordinated multi-agent analysis
- **Step callbacks** - For progress tracking

### Data Requirements

The agents expect Neo4j to contain marketing data such as:
- Google Ads campaign performance
- Website analytics and user behavior
- Conversion tracking and attribution
- Keyword performance and search data
- Customer demographics and segments

## 🚀 Getting Started

1. **Setup Environment**: Ensure all required environment variables are configured
2. **Load Marketing Data**: Import your Google Ads and website analytics data into Neo4j
3. **Test Queries**: Start with simple queries to verify agent functionality
4. **Analyze Results**: Review the comprehensive reports and implement recommendations
5. **Monitor Performance**: Track the success of implemented optimizations

The agents are designed to provide actionable, data-driven insights that help trade businesses optimize their digital marketing efforts and improve lead generation ROI.