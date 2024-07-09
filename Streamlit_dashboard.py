import streamlit as st
import plotly.express as px
import pandas as pd

# Load the data
file_path = r'C:\Users\Laptops\Documents\MasoodPharma\Shopify\SocialMedia\MetaAds.xlsx'  # Adjust the path if necessary
df = pd.read_excel(file_path, sheet_name='MetaAds')

# Title and introductory text
st.title("MetaAds Dataset Descriptive Analysis (June 2023 – June 2024)")

st.markdown("""
## Descriptive Statistics and Visualizations

### Frequency vs. Ad Spend
The scatter plot illustrates the variation in the frequency of ads relative to the ad spend. A discernible trend indicates that higher ad spend generally corresponds to a higher frequency. However, this relationship is not strictly linear, suggesting other contributing factors.
""")
fig1 = px.scatter(df, x='AdSpend', y='Frequency', title='Frequency vs. Ad Spend')
st.plotly_chart(fig1)

st.markdown("""
### Frequency vs. Reach
This scatter plot demonstrates that as reach increases, frequency tends to increase as well. Despite this general trend, numerous outliers suggest that additional variables may influence frequency beyond just reach.
""")
fig2 = px.scatter(df, x='Reach', y='Frequency', title='Frequency vs. Reach')
st.plotly_chart(fig2)

st.markdown("""
### Frequency vs. Impressions
Similar to reach, higher impressions typically correlate with higher frequency. Nevertheless, the data points are widely scattered, indicating a more complex relationship between these variables.
""")
fig3 = px.scatter(df, x='Impressions', y='Frequency', title='Frequency vs. Impressions')
st.plotly_chart(fig3)

st.markdown("""
### Frequency vs. Reach Category
The box plot displays the distribution of frequency across different reach categories. Certain categories exhibit a broader range of frequency, implying significant variability in ad display frequency within each category.
""")
fig4 = px.box(df, x='ReachCategory', y='Frequency', title='Frequency vs. Reach Category')
st.plotly_chart(fig4)

st.markdown("""
### Frequency vs. Impressions Category
This box plot shows that specific impression categories have a higher median frequency, although there is considerable overlap between the categories. This highlights the variability in frequency distribution across different impression levels.
""")
fig5 = px.box(df, x='ImpressionsCategory', y='Frequency', title='Frequency vs. Impressions Category')
st.plotly_chart(fig5)

st.markdown("""
These visualizations collectively provide insights into how frequency varies with different metrics, enhancing our understanding of ad performance dynamics.
""")

st.header("Stepwise Regression Analysis Results")

st.subheader("Factors Affecting Ad Spend")
st.markdown("""
The stepwise regression analysis identifies reach, impressions, and total clicks as the most significant factors influencing ad spend. The model explains 96.8% of the variance in ad spend (R-squared = 0.968).

- Reach: Negative effect (-0.3253, p < 0.001)
- Impressions: Positive effect (0.2349, p < 0.001)
- Total Clicks: Positive effect (1.5502, p < 0.001)
- Frequency, Page Engagement, Follows/Likes, Post Engagement: Not significant
""")
fig6 = px.scatter(df, x='AdSpend', y='Reach', title='Ad Spend vs. Reach')
st.plotly_chart(fig6)

st.subheader("Factors Affecting CTR")
st.markdown("""
The analysis for click-through rate (CTR) indicates that reach, impressions, frequency, and ad spend are significant predictors. This model explains 56.7% of the variance in CTR (R-squared = 0.567).

- Reach: Positive effect (5.31e-08, p < 0.001)
- Impressions: Negative effect (-2.94e-08, p < 0.01)
- Frequency: Positive effect (0.1297, p < 0.05)
- Ad Spend: Positive effect (2.84e-06, p < 0.01)
- Total Clicks, Page Engagement, Follows/Likes, Post Engagement: Not significant
""")
fig7 = px.scatter(df, x='Frequency', y='CTR', title='Frequency vs. CTR')
st.plotly_chart(fig7)

st.subheader("Factors Affecting CPC")
st.markdown("""
For cost per click (CPC), reach, impressions, frequency, and total clicks are significant predictors. This model accounts for 54.1% of the variance in CPC (R-squared = 0.541).

- Reach: Positive effect (7.84e-08, p < 0.01)
- Impressions: Negative effect (-3.50e-08, p < 0.05)
- Frequency: Positive effect (0.1815, p < 0.05)
- Total Clicks: Negative effect (-1.74e-05, p < 0.05)
- Ad Spend, Page Engagement, Follows/Likes, Post Engagement: Not significant
""")
fig8 = px.scatter(df, x='Frequency', y='CPC', title='Frequency vs. CPC')
st.plotly_chart(fig8)

st.subheader("Factors Affecting Cost Per Engagement")
st.markdown("""
The analysis for cost per engagement indicates that reach, impressions, frequency, and total clicks are significant predictors. This model explains 59.9% of the variance (R-squared = 0.599).

- Reach: Positive effect (1.70e-06, p < 0.01)
- Impressions: Negative effect (-1.04e-06, p < 0.05)
- Frequency: Positive effect (1.2877, p < 0.05)
- Total Clicks: Positive effect (0.0013, p < 0.01)
- Ad Spend, Page Engagement, Follows/Likes, Post Engagement: Not significant
""")
fig9 = px.scatter(df, x='Frequency', y='CostPerPageEngagement', title='Frequency vs. Cost Per Engagement')
st.plotly_chart(fig9)

st.subheader("Composition Analysis of Ad Spend")
st.markdown("""
The regression model examining the composition of ad spend in relation to cost per result and CPC shows:

- Cost Per Result: Positive effect (71.0677, p = 0.332)
- CPC: Positive effect (3901.9970, p = 0.457)

The model explains only 7.6% of the variance in ad spend (R-squared = 0.076), suggesting that while cost per result and CPC contribute to ad spend, they do not fully explain its variability.
""")
fig10 = px.scatter(df, x='AdSpend', y='CostPerResult', title='Ad Spend vs. Cost Per Result')
st.plotly_chart(fig10)
fig11 = px.scatter(df, x='AdSpend', y='CPC', title='Ad Spend vs. CPC')
st.plotly_chart(fig11)

st.subheader("Factors Affecting Follows/Likes")
st.markdown("""
The stepwise regression analysis identifies the following factors and their effects on follows/likes across different ad sets:

- Intercept: 29.8332 (p = 0.003)
- Reach: 3.789e-06 (p = 0.957)
- Impressions: 2.158e-05 (p = 0.526)
- Frequency: -5.1300 (p = 0.175)
- Total Clicks: -0.0001 (p = 0.748)
- Page Engagement: 0.9997 (p < 0.001)
- Post Engagement: -0.9997 (p < 0.001)
- Ad Spend: -9.826e-05 (p = 0.446)
""")
fig12 = px.scatter(df, x='PageEngagement', y='Follows_Likes', title='Page Engagement vs. Follows/Likes')
st.plotly_chart(fig12)

st.subheader("Total Clicks vs. Unique Link Clicks")
st.markdown("""
A regression analysis was performed to determine whether total clicks generate more unique link clicks. The findings are as follows:

- Intercept: 212.0821 (p = 0.634)
- Total Clicks: 0.2500 (p < 0.001)

The R-squared value is 0.786, indicating that 78.6% of the variance in unique link clicks is explained by total clicks. The relationship is significant, with a coefficient of 0.2500 for total clicks, suggesting that for every additional click, there is an average increase of 0.25 in unique link clicks.
""")
fig13 = px.scatter(df, x='TotalClicks', y='UniqueLinkClicks', title='Total Clicks vs. Unique Link Clicks')
st.plotly_chart(fig13)

st.subheader("CTR vs. Unique CTR")
st.markdown("""
A regression analysis was performed to determine whether CTR generates more unique CTR. The findings are as follows:

- Intercept: 1.4389 (p < 0.001)
- CTR: 0.1605 (p = 0.040)

The R-squared value is 0.087, indicating that only 8.7% of the variance in unique CTR is explained by CTR. The relationship is significant, with a coefficient of 0.1605 for CTR, suggesting that for every 1% increase in CTR, there is an average increase of 0.1605% in unique CTR.
""")
fig14 = px.scatter(df, x='CTR', y='UniqueCTR', title='CTR vs. Unique CTR')
st.plotly_chart(fig14)

st.markdown("""
CTR does generate more unique CTR, but the relationship is relatively weak. This trend suggests that while an increase in CTR can lead to an increase in unique CTR, the impact is not strong. Marketers should consider other factors that may influence unique CTR to optimize ad performance.

### Stepwise Regression Analysis Results for CTR and Unique CTR

#### Factors Affecting CTR
The stepwise regression analysis for CTR reveals the following factors:

- Intercept: 3.1900 (p < 0.001)
- Total Clicks: Positive effect (0.0002, p < 0.001)
- Page Engagement: Positive effect (0.0248, p = 0.030)
- Follows/Likes: Negative effect (-0.0248, p = 0.030)
- Post Engagement: Negative effect (-0.0248, p = 0.030)
- Ad Spend: Negative effect (-2.118e-05, p = 0.025)
- Reach, Impressions, Frequency: Not significant

The model explains 59.1% of the variance in CTR (R-squared = 0.591).

#### Factors Affecting Unique CTR
The stepwise regression analysis for unique CTR reveals the following factors:

- Intercept: 0.0312 (p = 0.925)
- Frequency: Positive effect (0.7205, p < 0.001)
- Total Clicks: Positive effect (4.084e-05, p = 0.001)
- Impressions: Negative effect (-1.834e-06, p = 0.090)
- Reach, Page Engagement, Follows/Likes, Post Engagement, Ad Spend: Not significant

The model explains 72.5% of the variance in unique CTR (R-squared = 0.725).

#### Key Findings
- **CTR**:
  - Total Clicks: The most significant positive factor, indicating more clicks lead to higher CTR.
  - Page Engagement: Positive effect, suggesting that higher engagement increases CTR.
  - Follows/Likes and Post Engagement: Both have negative effects, indicating that higher counts in these metrics may decrease CTR.
  - Ad Spend: Small negative effect, suggesting that higher spending might slightly decrease CTR.
- **Unique CTR**:
  - Frequency: The most significant positive factor, indicating that higher frequency leads to higher unique CTR.
  - Total Clicks: Significant positive effect, meaning more clicks also contribute to higher unique CTR.
  - Impressions: Negative effect, though not as significant, suggesting that higher impressions may slightly reduce unique CTR.

For CTR, total clicks and page engagement are the most significant positive factors, while follows/likes, post engagement, and ad spend have negative impacts. For unique CTR, frequency and total clicks are significant positive factors, while impressions have a slight negative effect. Marketers should focus on increasing total clicks and page engagement to improve CTR and increasing frequency and total clicks to enhance unique CTR.

### Key Relationships to Investigate

#### Ad Spend vs. Reach
If the regression shows a significant positive relationship, it indicates that increasing ad spend leads to an increase in reach.

**Regression Analysis Summary**
- R-squared: 0.626
- Coefficient: 5.452e-05 (p < 0.001)

The regression analysis shows a significant positive relationship between ad spend and reach, indicating that increasing ad spend leads to an increase in reach.

#### Ad Spend vs. Frequency
If the regression shows a significant positive relationship, it indicates that increasing ad spend leads to an increase in frequency.

**Regression Analysis Summary**
- R-squared: 0.002
- Coefficient: 0.005 (p = 0.795)

The regression analysis shows no significant relationship between ad spend and frequency, indicating that increasing ad spend does not necessarily lead to an increase in frequency.

#### Frequency vs. CTR
If the regression shows a significant negative relationship, it indicates that increasing frequency leads to a decrease in CTR.

**Regression Analysis Summary**
- R-squared: 0.000
- Coefficient: 0.0016 (p = 0.995)

The regression analysis shows no significant relationship between frequency and CTR, indicating that increasing frequency does not lead to a decrease in CTR.

### Conclusion
- **Ad Spend vs. Reach**: There is a significant positive relationship, so increasing ad spend results in increased reach.
- **Ad Spend vs. Frequency**: No significant relationship, so increasing ad spend does not necessarily result in increased frequency.
- **Frequency vs. CTR**: No significant relationship, so increasing frequency does not necessarily lead to a decrease in CTR.

### Advanced Metric Importance Ranking Analysis


#### Total Clicks
**Analysis**: There is a high correlation between total clicks, CTR, and reach, suggesting that total clicks significantly drive user engagement and campaign visibility.
**Proposed Optimization Strategy**: It could be beneficial to explore strategies aimed at maximizing clicks. Engaging ad formats, such as carousels or videos, which typically generate higher interaction rates, might be particularly effective.

#### Page Engagement
**Analysis**: Page engagement shows a strong influence on CTR, indicating that ads with higher engagement rates are more likely to be clicked.
**Proposed Optimization Strategy**: Consider utilizing interactive content, polls, or questions within ads to boost engagement. Regularly updating creatives to maintain audience interest could also be advantageous.

#### Frequency
**Analysis**: Frequency has a moderate impact on CTR and ad spend. Higher frequency can lead to ad fatigue, potentially reducing ad effectiveness.
**Proposed Optimization Strategy**: Employing frequency capping to limit the number of times an individual sees an ad may help. Additionally, retargeting users at different stages of the buying journey could be worth exploring.

#### Unique CTR
**Analysis**: Unique CTR is directly related to CTR, highlighting the effectiveness of ad content in attracting unique clicks.
**Proposed Optimization Strategy**: Tailoring ad copy and visuals to be highly relevant to the target audience might improve performance. Testing different messages and images to find the most effective combination could be a good approach.

#### Ad Spend
**Analysis**: Ad spend is essential for increasing reach and impressions, making efficient budget allocation crucial.
**Proposed Optimization Strategy**: Using performance data to dynamically allocate budget to the best-performing ads and audiences might enhance efficiency. Automated bidding strategies provided by ad platforms could also be considered.

#### Impressions
**Analysis**: Impressions are important for visibility but can have diminishing returns if not managed properly.
**Proposed Optimization Strategy**: Focusing on quality impressions by targeting the right audience may help. Using lookalike audiences to expand reach without sacrificing relevance could also be beneficial.

#### Reach
**Analysis**: Reach is critical for expanding the audience base and is directly related to ad spend and total clicks.
**Proposed Optimization Strategy**: Leveraging a mix of broad and targeted campaigns might be effective. High-reach formats like video ads could be used to capture a wider audience.

#### CPC
**Analysis**: CPC affects ad spend efficiency. Lower CPC can improve ROI.
**Proposed Optimization Strategy**: Optimizing for lower CPC by improving ad relevance and quality scores might be helpful. A/B testing to refine ads for cost efficiency could also be considered.

#### Unique Link Clicks
**Analysis**: Unique link clicks indicate genuine user interest and interaction.
**Proposed Optimization Strategy**: Creating compelling landing pages that align with ad content to encourage more unique clicks might be beneficial. Tracking and analyzing user behavior post-click to improve conversion rates could also be explored.

#### Outbound Clicks
**Analysis**: Outbound clicks measure the extent of user engagement beyond the ad platform.
**Proposed Optimization Strategy**: Ensuring a seamless user experience from ad click to website navigation could be important. Optimizing landing pages for speed and mobile friendliness might also be advantageous.

### Data-Driven ROI Optimization Strategies

#### Targeting and Segmentation
 Utilizing AI-driven audience insights to create highly specific audience segments could be benefic ial. Implementing predictive analytics to forecast the most responsive segments might also be worth exploring.
**Example**: Machine learning algorithms could analyze past campaign data to identify high-value audience segments.

#### Ad Creative and Messaging
 Employing dynamic creative optimization (DCO) to automatically generate and test multiple ad variations could enhance performance.

#### Budget Allocation and Bidding Strategies
 Implementing automated budget allocation tools that optimize spend based on real-time performance metrics might improve efficiency.
**Example**: Programmatic advertising could automatically adjust bids in response to changing market conditions and competitor actions.

#### Frequency Capping
 Using data to determine the optimal frequency cap for different audience segments could be beneficial.
**Example**: Analyzing engagement and conversion data to set frequency caps that maximize exposure without causing ad fatigue might be worth considering.

#### Optimization of Ad Placements
 Utilizing cross-channel attribution models to identify the most effective ad placements could improve ROI.
**Example**: Integrating data from multiple platforms to understand the full customer journey and allocate budget to the most impactful placements might be advantageous.

#### Retargeting and Lookalike Audiences
 Using advanced retargeting strategies like sequential messaging to guide users through the sales funnel could enhance effectiveness.
**Example**: Creating lookalike audiences based on high-value customers and using predictive analytics to target potential new customers might be beneficial.""")

