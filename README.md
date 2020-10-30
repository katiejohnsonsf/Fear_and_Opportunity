# Does the likelihood of fearing failure decrease with the perception of opportunity?

# Background
Creativity and seeing potential in the world around you is a phenomena shared by people in every part of the world. While some may be motivated by the economics, others may also be moitvated to create to improve each other's lives. Wanting to make a positive contribution is a beautiful part of what makes us human. At the same time, fear and, in many cultures fearing failure inparticular, is another core aspect of the human experience. 

As someone who is passionate about creating things and experiences that help people, I was curious about the relationship between fear of failure and perception of opportunity to start a business. Would the prevalence of fear of failure be greater among those who did not see an opportunity around them? How does perception of opportunity relate to the prevalence of fear of failure? What other factors globally or within specific countries contribute to the prevalance of citing fear of failure as the reason for not starting a business? Let's explore the data, shall we.

# Data

The Global Entreprenuership Monitor (GEM) is a London-based non-profit that collects data directly from individual entrepreneurs. GEM's theory of change rests on the assumption that entreprenuership is a core mechanism for economic development and for meeting social needs, like the United Nations Sustainable Development goals (SDGs). The organization conducts an annual survey to collect data on the attitudes and behaviors of people in 115+ countries on topics related to entreprenuership. In each country, reseachers interview 2000 people using a questionnaire and prescribed methodology. I'll be focusing on the 2016 global individual-level dataset, because it is the most recent dataset available. 

For this project, I'm exploring how people's perception of business opportunity in their communities relates to their citing fear of failure. Does seeing opportunity make it more of less likely someone will site fear as the reason they are not starting a business? Or is fear of failure present more often for people who don't see opportunity? 

<br>

# Data Cleaning

Initially, I had been intersted in focusing on exploring my topics for India. However, there was not data for my data fields of interest, so I switched to a global focus instead.

To clearn the global data, after indexing out my columns of interest, I removed rows containing NaN using the <code>Pandas</code> method <code>df.dropna()</code>. 

This reduced the number of rows from 194,824 to 126,608, each representing the response of a study participant. Though a large proportion of the dataset, the remaining data was still large enough for my global analysis. 

<br>

# Data Collection Methods

## Perception of Opportunity Research
<br>

* If an individual sees opportunities to start a firm in the area where they live

<br>

>"In the next six months, will there be good opportunities for starting a business in the area where you live? "

<br>

## Fear of Failure Research 

<br>


* If fear of failure would prevent an individual from setting up a business

<br>

>"Would fear of failure prevent you from starting a business?"

<br>

To understand if there is a statistically significant relationship between fear of failure and perception of opportunity, I began analysis with the Fisher's Exact test. 

<br>

# Analysis: Fear of Failure & Perception of Opportunity

My curiousity led me to the alternative hypothesis that the proportion of individuals who cite fear of failure is higher among inviduals who do not perceive opportunity. My Null is, therefore, that there is no statistical significance or relationship between fear of failure and those who perceieve opportunity.

To test my Null hypothesis against the data, I began by running a Fisher's exact test.

<br>

## Fisher's Exact Test

I chose Fisher's Exact test because it measures the significance of the association between two kinds of classification (in this case respondents citing fear of failure and perception of oppportunity to start a business).

I used a contingency table for the Fisher's Exact test, which shows the proportion of 126,608 respondents' answers over four response combinations. 

<br>

<table>
  <thead>
    <tr>
    </tr>
    <tr>
      <th>Response</th>
      <th>No (ff)</th>
      <th>Yes (ff)</th>
      <th>Row totals</th>
    </tr>
  </thead>
  <tbody>
    <tr>
    <td>No (po)</td>
      <td>40,614</td>
      <td>32,725</td>
      <td>73,339</td>
    </tr>
    <tr>
      <td>Yes (po)</td>
      <td>34,400</td>
      <td>18,869</td>
      <td>53,269</td>
    </tr>
    <tr>
      <td>Column totals</td>
      <td>75,014</td>
      <td>51,594</td>
      <td>N = 126,608</td>
    </tr>
  </tbody>
</table>
<br>
po = perception of opportunity
ff = fear of failure

<br>



The results of Fisher's Exact test on the data revealed an extremly low P-value (1.99e-238) indicating that the Null hypothesis of no statistical significance between fear of failure and perception of opportuniity should be rejected.

<br>

![histogram for fear of failure vs opportunity](img/fisher_hist.png)


Based on the Fisher's Exact test, I can now answer my question:
<br>

Does the likelihood of fearing failure decrease with the perception of opportunity? Yes.

<br>

## Bayes A/B Test

To understand if the probability of seeing fear of failure would be greater in the group of people who <strong> do not</strong> perceive opportunity, I conducted a Bayes A/B test. 

You can see in the two probability distributions below that the group that does not perceive opportunity is more likely to fear failure with a probability of ~0.44 compared to the group that does see opportunity, which has a probability of fearing failure of ~0.36.

![Comparison of groups and how they cite fear of failure](img/Bayes_AB_prob.png)

Using these distributions to 10,000 simulations, I found no instances where the probability of fear of failure was greater in the variant of no opportunity than the variant that did perceive opportunity.

## Education level and Fear of Failure

<br>

![histogram of fear of failure across different levels of education](img/Fear_education.png)

### Education Levels (shown in x-axis above)
0. Pre-primary Education
1. Primary Education Or First Stage Of Basic Education
2. Lower  Secondary Or Second Stage Of Basic Education
3. (Upper) Secondary Education
4. Post-secondary Non-tertiary Education
5. First Stage Of Tertiary Education
6. Second Stage Of Tertiary Education

## Future Directions

* What influences someone's ability to see business opportunities in their communities? 


