from xml.etree import ElementTree as ET


string = '''<?xml version="1.0" encoding="UTF-8"?>
<article xmlns:xlink="http://www.w3.org/1999/xlink">
  <front>
    <journal-meta>
      <journal-title-group>
        <journal-title>Muhammad Ilham PAKAWARU, Arung Gihna MAYAPADA, Nadhira AFDALIA, Andi Ainil Mufidah TANRA, Muhammad AFDHAL /
Journal of Asian Finance, Economics and Business Vol</journal-title>
      </journal-title-group>
      <issn pub-type="ppub">2288-4637</issn>
    </journal-meta>
    <article-meta>
      <article-id pub-id-type="doi">10.13106/jafeb.2021.vol8.no2.0903</article-id>
      <title-group>
        <article-title>The Relationship of Corporate Social Responsibility (CSR) Disclosure and Earnings Management: Evidence from Indonesia</article-title>
      </title-group>
      <contrib-group>
        <contrib contrib-type="author">
          <string-name>Muhammad Ilham PAKAWARU</string-name>
          <email>pakawaruilham4@gmail.com</email>
        </contrib>
        <contrib contrib-type="author">
          <string-name>Arung Gihna MAYAPADA</string-name>
          <email>arunggihna@gmail.com</email>
        </contrib>
        <contrib contrib-type="author">
          <string-name>Nadhira AFDALIA</string-name>
          <email>nadhira.afdalia88@gmail.com</email>
        </contrib>
        <contrib contrib-type="author">
          <string-name>Andi Ainil Mufidah TANRA</string-name>
          <email>ainilmufidah.am@gmail.com</email>
        </contrib>
        <contrib contrib-type="author">
          <string-name>Muhammad AFDHAL</string-name>
          <email>afdhalafdhal499@gmail.com</email>
        </contrib>
        <contrib contrib-type="author">
          <string-name>JEL Classification Code: M</string-name>
        </contrib>
      </contrib-group>
      <pub-date>
        <year>2021</year>
      </pub-date>
      <volume>2</volume>
      <issue>2021</issue>
      <fpage>903</fpage>
      <lpage>909</lpage>
      <history>
        <date date-type="accepted">
          <day>15</day>
          <month>1</month>
          <year>2021</year>
        </date>
        <date date-type="received">
          <day>05</day>
          <month>11</month>
          <year>2020</year>
        </date>
        <date date-type="revised">
          <day>05</day>
          <month>1</month>
          <year>2021</year>
        </date>
      </history>
      <abstract>
        <p>The relationship between corporate social responsibility (CSR) and earnings management is still a debate. Several previous studies showed that CSR is a determinant of earnings management. Meanwhile, others revealed the reverse. Therefore, this study aims to investigate the effect of CSR disclosure on earnings management and the effect of earnings management on CSR disclosure. This study was conducted with mining companies listed on the Indonesia Stock Exchange (IDX) in the 2016-2019 period. The research data was analyzed using multiple linear regression analysis. The data is obtained from financial statements, annual reports, and sustainability reports. The results reveal that there is a positive relationship between CSR disclosure and earnings management. This study also shows that the relationship model of CSR disclosure and earnings management is recursive. This finding implies that CSR disclosure is a tool used by management to cover up unethical actions from stakeholders. These results verify the agency theory and opportunist hypothesis regarding the relationship between CSR and earnings management. The novelty of this study lies in highlighting the recursive model of the relationship between CSR and earnings management.</p>
      </abstract>
      <kwd-group>
        <kwd>Corporate Social Responsibility Disclosure</kwd>
        <kwd>Earnings Management</kwd>
        <kwd>Recursive Model</kwd>
      </kwd-group>
    </article-meta>
  </front>
  <body>
    <sec id="sec-1">
      <title>1. Introduction</title>
      <p>
        Law No. 40 of 2007 concerning Limited Liability
Companies regulates that Indonesian firms that carry out
their business activities in and related to natural resources
must carry out social and environmental responsibility.
Even so, the implementation of these regulations is still
very minimal. Cases of exploitation of natural resources
and environmental pollution have increased in Indonesia
        <xref ref-type="bibr" rid="ref36">(Rokhmawati &amp; Gunardi, 2017)</xref>
        . Besides, the absence
of standards regulated by law regarding the format of
corporate social responsibility (CSR) reporting also makes
the quantity and quality of CSR reporting still vary in
Indonesia
        <xref ref-type="bibr" rid="ref28 ref34 ref35">(Muliati et al., 2020; Ridho, 2017; Ridwan &amp;
Mayapada, 2020)</xref>
        .
      </p>
      <p>CSR is represented as an ethical act by the company to
all stakeholders, namely investors, creditors, employees,
suppliers, customers, government, society, and the
surrounding environment. The concept of CSR based on
stakeholder theory stated that the firm should accommodate
all stakeholder interests to ensure operating activities?
sustainability. Based on this concept, reliable financial
reporting is part of the implementation of CSR.</p>
      <p>Reliable financial reporting is financial reporting
that is free from earnings management actions. Earnings
management is the use of accounting techniques to
produce financial statements that present an overly positive
view of a company?s business activities and financial position
to maximize personal gain and ignore other stakeholders?
interests. Based on agency theory, earnings management is
carried out because of the information asymmetry between
management and stakeholders. This information asymmetry
creates agency problems that are detrimental to stakeholders.
Therefore, earnings management is often manifested as
unethical actions.</p>
      <p>
        The relationship between CSR and earnings management
has been studied by accounting academics
        <xref ref-type="bibr" rid="ref18 ref9">(Gargouri et al.,
2010; Jordaan et al., 2018)</xref>
        . However, these studies? results
are still mixed and even contradictory
        <xref ref-type="bibr" rid="ref27 ref43">(Moratis &amp; Van
Egmond, 2018; Yip et al., 2011)</xref>
        . Examination by
        <xref ref-type="bibr" rid="ref3">Ben
and Chakroun (2018)</xref>
        , and
        <xref ref-type="bibr" rid="ref42">Scholtens and Kang (2013)</xref>
        revealed that CSR disclosure is a determinant of earnings
management. According to
        <xref ref-type="bibr" rid="ref23">Liu et al. (2017)</xref>
        , firms that carry
out CSR are ethical firms that will not carry out unethical
actions such as earnings management.
        <xref ref-type="bibr" rid="ref32">Prior et al. (2008)</xref>
        found that earnings management affects CSR disclosure.
According to
        <xref ref-type="bibr" rid="ref25">Martínez-Ferrero et al. (2016)</xref>
        , firms report
CSR to distract stakeholders from management?s earnings
management actions.
      </p>
      <p>
        Previous researches findings, which are still
inconsistent, mean that the relationship between CSR
disclosure and earnings management cannot be concluded
        <xref ref-type="bibr" rid="ref14">(Huynh, 2020)</xref>
        . Therefore, this study aims to analyze
the relationship between CSR disclosure and earnings
management in mining firms in Indonesia. This study is
different from previous research because the study aims
to investigate the bidirectional relationship between CSR
disclosure and earnings management, which to the best
of the researcher?s knowledge, has never been studied in
Indonesia. Meanwhile, mining firms were chosen as the
subject of this study because mining firms? operational
activities are closely related to social and environmental
issues. Therefore, this study aims to analyze the
twoway relationship between CSR disclosure and earnings
management in mining firms listed on the Indonesia
Stock Exchange.
      </p>
    </sec>
    <sec id="sec-2">
      <title>2. Literature Review</title>
      <sec id="sec-2-1">
        <title>2.1. Agency Theory</title>
        <p>
          Agency theory refers to the relationship between
management and firm owners as an agency relationship.
According to
          <xref ref-type="bibr" rid="ref15">Jensen and Meckling (1976)</xref>
          , an agency
relationship is a relationship in which the principal (firm
owner) delegates his authority to the agent (management).
In the corporate context, management is in charge of fully
managing the company. As a result, management has more
information about the firm than the owners themselves.
This information asymmetry triggers agency costs in which
management acts opportunistically by not presenting reliable
information, which maximizes personal gain and harms
owners and other stakeholders.
        </p>
        <p>
          The issue of earnings management and CSR cannot be
separated from agency theory, which separates company
ownership and control. Management can select and
even manipulate the financial information it reports as
accountability to stakeholders by performing earnings
management. Meanwhile, management can also adjust its
CSR disclosure items based on their importance, considering
that CSR disclosure is voluntary and full of management
discretion
          <xref ref-type="bibr" rid="ref18 ref33">(Jordaan et al., 2018; Rao &amp; Tilt, 2016)</xref>
          . Based
on the agency theory, the relationship between earnings
management and CSR can be stated in an opportunist
hypothesis which assumes that companies express CSR well
to distract stakeholders from earnings management actions
that have been done by the management
          <xref ref-type="bibr" rid="ref1 ref25">(Almahrog et al.,
2018; Martínez-Ferrero et al., 2016)</xref>
          .
        </p>
      </sec>
      <sec id="sec-2-2">
        <title>2.2. Stakeholder Theory</title>
        <p>Stakeholder theory is based on the concept that a
company is not an entity that only operates for its interests
but must provide benefits to stakeholders. Stakeholders are
the firm owners and all parties related to the firm such as
employees, customers, suppliers, government, society, and
even the environment. Based on the stakeholder theory, the
firm should accommodate all stakeholder interests for the
sake of business continuity, including providing information
about the firm?s activities to all stakeholders.</p>
        <p>
          Stakeholder theory states that firms can reduce agency
costs by carrying out social initiatives that affect their
relationship with stakeholders, including CSR
          <xref ref-type="bibr" rid="ref42">(Scholtens
&amp; Kang, 2013)</xref>
          . Firms that focus on CSR disclosure tend
to be cited as ethical companies. Based on the stakeholder
theory, the relationship between earnings management and
CSR is an ethical hypothesis. The ethical hypothesis states
that firms that disclose their CSR are less likely to carry out
earnings management, which is an unethical act
          <xref ref-type="bibr" rid="ref20">(Kumala
&amp; Siregar, 2020)</xref>
          .
        </p>
      </sec>
      <sec id="sec-2-3">
        <title>2.3. Hypotheses Development</title>
        <p>
          CSR is a concept in accounting that emphasizes
that firms have economic and legal responsibility and
social and moral responsibility to investors, suppliers,
customers, employees, government, society, and the
environment
          <xref ref-type="bibr" rid="ref30">(Omair Alotaibi &amp; Hussainey, 2016)</xref>
          . Based
on the triple bottom line concept, CSR is identified
into three aspects: economic welfare, environmental
quality improvement, and social justice. CSR is the
business world?s commitment to contribute to sustainable
economic development by considering economic, social,
and environmental issues. Therefore, CSR disclosure is
defined as a signal of a firm?s commitment to socially
responsible behavior
          <xref ref-type="bibr" rid="ref10">(Gavana et al., 2017)</xref>
          .
        </p>
        <p>
          Earnings management is the act of changing the
reported economic performance by management to mislead
stakeholders in making economic decisions. Earnings
management can be done by using existing accounting
standards to obtain predetermined profits or achieve
specific goals
          <xref ref-type="bibr" rid="ref16">(Jones, 2011)</xref>
          . Accounting is closely related
to estimates, judgments, and policies made by management.
Also, accrual accounting can be used by management to
promote and delay recording transactions. Flexibility in
accounting standards creates ambiguity for practitioners in
applying specific standards so that earnings management
practices can be carried out
          <xref ref-type="bibr" rid="ref13">(Hong &amp; Andersen, 2011)</xref>
          .
        </p>
        <p>
          Firms that report their CSR activities are identified
as transparent and accountable companies
          <xref ref-type="bibr" rid="ref24">(Management
Association, 2019)</xref>
          . Firms that commit to CSR will be
responsible for reporting their financial statements
          <xref ref-type="bibr" rid="ref5">(Choi
et al., 2013)</xref>
          . Firms that have such an ethical attitude will
not do earnings management
          <xref ref-type="bibr" rid="ref17 ref3">(Ben &amp; Chakroun, 2018; Jones,
1995)</xref>
          . This concept is supported by the research findings
of
          <xref ref-type="bibr" rid="ref3">Ben and Chakroun (2018)</xref>
          ,
          <xref ref-type="bibr" rid="ref5">Choi et al. (2013)</xref>
          ,
          <xref ref-type="bibr" rid="ref13">Hong and
Andersen (2011)</xref>
          ,
          <xref ref-type="bibr" rid="ref21 ref22">Li and Thibodeau (2019)</xref>
          , and
          <xref ref-type="bibr" rid="ref22">Liu and Lee
(2019)</xref>
          . They revealed that firms that disclose CSR tend not
to do earnings management.
        </p>
        <p>
          However, other studies have revealed that CSR disclosure
is a mask that firms use in covering up their unethical actions,
including earnings management
          <xref ref-type="bibr" rid="ref12">(Hemingway &amp; Maclagan,
2004)</xref>
          . The firm seeks to divert stakeholders? attention,
especially investors, to the reliability of its financial
statements by disclosing CSR.
          <xref ref-type="bibr" rid="ref18">Jordaan et al. (2018)</xref>
          ,
          <xref ref-type="bibr" rid="ref19">Kim
et al. (2012)</xref>
          ,
          <xref ref-type="bibr" rid="ref25">Martínez-Ferrero et al. (2016)</xref>
          , and
          <xref ref-type="bibr" rid="ref31">Patro and
Pattanayak (2017)</xref>
          stated that CSR disclosure has a positive
effect on earnings management. Therefore, the research
hypothesis is formulated as follows:
        </p>
        <p>H1: Corporate social responsibility (CSR) disclosure
has a significant effect on earnings management.</p>
        <p>
          Earnings management is often perceived as irresponsible
and contrary to CSR
          <xref ref-type="bibr" rid="ref32">(Prior et al., 2008)</xref>
          . CSR activities are
identified as ethical actions. Thus, companies that carry out
earnings management are seen as unethical companies and
tend not to carry out CSR. However, the research findings
of
          <xref ref-type="bibr" rid="ref6">Choi et al. (2018)</xref>
          revealed that companies that carry
out earnings management are better at reporting their CSR
activities. CSR ratings are negatively correlated with the
level of earnings management when all firms are considered.
However, the relationship is weaker for firms with highly
concentrated ownership, which suggests that CSR practices
can be abusively used by those firms to conceal their poor
earnings quality. The adverse use of CSR is discouraged if
the fraction of shares owned by institutional investors is high.
CSR is used to divert the attention of stakeholders from their
opportunistic actions towards investors
          <xref ref-type="bibr" rid="ref2">(Almahrog et al.,
2015)</xref>
          .
          <xref ref-type="bibr" rid="ref32">Prior et al. (2008)</xref>
          investigated the connection between
earnings management and CSR. They argued that earnings
management practices damage the collective interests of
stakeholders; hence, managers who manipulate earnings can
deal with stakeholder activism and vigilance by resorting to
CSR practices. They found a positive impact on earnings
management practices on CSR; this relationship holds for
different robustness checks. Also, they demonstrated that
the combination of earnings management and CSR has a
negative impact on financial performance. By disclosing
CSR, the firm seeks public recognition as an ethical and
socially responsible company. The firm is convincing other
stakeholders to validate its unethical actions, including
earnings management. Therefore, the research hypothesis is
as follows:
        </p>
        <p>H2: Earnings management has a significant effect on
corporate social responsibility (CSR) disclosure.</p>
      </sec>
    </sec>
    <sec id="sec-3">
      <title>3. Research Methods</title>
      <sec id="sec-3-1">
        <title>3.1. Population and Sample</title>
        <p>This research uses secondary data which was obtained
from sustainability reports, annual reports, and audited annual
financial statements. The data is downloaded through the
company?s official website. This study?s target population is
all firms engaged in the mining sector listed on the Indonesia
Stock Exchange (IDX). The sample selection is made
using the purposive sampling method, namely determining
the sample by considering specific criteria. Based on this
method, the total model of this study is 20 firms.
(1)
(2)
Sig.
0.125
0.001***
0.068*
0.056*</p>
        <p>where AbsDAi is absolute discretionary accruals
(earnings management), a are constants, b1 ? b3 are regression
coefficients, CSRDi is CSR disclosure, Sizei is firm size,
Levi is leverage, and e are disturbance errors.</p>
      </sec>
    </sec>
    <sec id="sec-4">
      <title>4. Results</title>
      <sec id="sec-4-1">
        <title>4.1. The Model of the Influence of Corporate</title>
      </sec>
      <sec id="sec-4-2">
        <title>Social Responsibility (CSR) Disclosure on Earnings Management</title>
        <p>The analysis of multiple linear regression models with
the dependent variable of earnings management shows
that the model has met all the classical assumptions, and
the model is declared feasible. The simultaneous test result
shows that the CSR disclosure, firm size, and leverage
simultaneously have a significant effect on earnings
management as indicated by a significance value less than
0.05. Table 2 also shows that the coefficient of determination
of this model is 0.366, in which 36.6% of the variability of
earnings management is explained by CSR disclosure, firm
size, and leverage.</p>
        <p>
          Table 2 shows that CSR disclosure has a significant
effect on earnings management. This result is indicated
by the significance of the CSR disclosure variable, which
is less than 0.05. Meanwhile, the relationship between
CSR disclosure and earnings management is positive,
as indicated by the standardized coefficient value of
0.434. This result is in line with the findings of
          <xref ref-type="bibr" rid="ref4">Buertey
et al. (2020)</xref>
          ,
          <xref ref-type="bibr" rid="ref9">Gargouri et al. (2010)</xref>
          , and
          <xref ref-type="bibr" rid="ref41">Salewski and
Zülch (2012)</xref>
          . Meanwhile, firm size and leverage have a
significant effect at a 10% level of significance on earnings
management, respectively.
        </p>
        <p>Model
(Constant)
AbsDA
Size
Lev
R = 0.523
R Square = 0.273</p>
        <p>Standardized
Coefficients
(Beta)
0.709
0.498
?0.094
?0.109</p>
        <p>T</p>
        <p>
          The measurement of CSR disclosure in this study uses
the content analysis method. Researchers analyzed any
content related to CSR topics based on the Global Reporting
Initiative G4 standards contained in the annual report and
separate CSR (if any)
          <xref ref-type="bibr" rid="ref11">(Hamid &amp; Atan, 2011)</xref>
          . Furthermore,
the CSR disclosure index is calculated by a weighted
nonaverage index by dividing the actual total score obtained by
the total score that should be disclosed by the company
          <xref ref-type="bibr" rid="ref37">(Rosli
et al., 2016)</xref>
          . In this study, earnings management is proxied by
discretionary accruals, which is the accrual rate determined
by management policy. The higher the discretionary accrual,
the higher the level of earnings management in the financial
statements. Discretionary accruals are calculated using a
modified Jones model
          <xref ref-type="bibr" rid="ref7">(Dechow et al., 1995)</xref>
          . This study
involved two control variables, namely firm size and leverage
          <xref ref-type="bibr" rid="ref40">(Saraswati et al., 2020)</xref>
          . The firm size is proxied by the
natural logarithm of the company?s total sales. Meanwhile,
leverage uses the debt to equity ratio.
        </p>
      </sec>
      <sec id="sec-4-3">
        <title>3.3. Data Analysis Method</title>
        <p>The data analysis method used in this study is the
multiple linear regression analysis. This study examines a
two-way relationship between CSR disclosure and earnings
management so that the multiple linear regression equations
for this study are as follows.</p>
        <p>AbsDAi = a + b1CSRDi,t + b2Sizei,t</p>
        <p>+ b3Levi,t + e
CSRDi = a + b1AbsDAi,t + b2Sizei,t</p>
        <p>+ b3Levi,t + e
Model
(Constant)
CSRD
Size
Lev
R = 0.605
R Square = 0.366</p>
        <p>Standardized
Coefficients
(Beta)
0.255
0.434
?0.233
0.236</p>
        <p>T
1.566
3.485
?1.871
1.964
Note: ***, ** and * indicates significant at 1%, 5% and 10% level of
significance based on t-statistics.</p>
        <p>Note: ***, ** and * indicates significant at 1%, 5% and 10% level of
significance based on t-statistics.</p>
      </sec>
      <sec id="sec-4-4">
        <title>4.2. The Model of the Influence of Earnings</title>
      </sec>
      <sec id="sec-4-5">
        <title>Management on Corporate Social</title>
      </sec>
      <sec id="sec-4-6">
        <title>Responsibility (CSR) Disclosure</title>
        <p>The second model?s classic assumption test results
show that the model meets the assumptions of normality,
heteroscedasticity, multicollinearity, and autocorrelation.
Thus, this model is worthy of further interpretation. Table 3
shows that the coefficient of determination of the model is
27.3%, which means that 27.3% of CSR disclosure variability
is explained by earnings management, firm size, and
leverage. The simultaneous test results show that earnings
management, firm size, and leverage simultaneously have a
significant effect on the CSR disclosure as indicated by a
significance value of less than 0.05. This result also means
that the multiple linear regression analysis model is feasible.</p>
        <p>
          Table 3 above also shows the partial test results. The table
shows that the significance value of the earnings management
variable is 0.003 below the 0.05 significance rate. This result
means that earnings management has a significant effect
on CSR disclosure. Meanwhile, the standard coefficient
of earnings management variables is 0.498, which means
that every one-point increase in the earnings management
variable will increase the CSR variable by 0.498. This result
also means that the direction of earnings management?s
influence on CSR disclosure is positive. This result is the
same as the research result of
          <xref ref-type="bibr" rid="ref14">Huynh (2020)</xref>
          ,
          <xref ref-type="bibr" rid="ref29">Muttakin et al.
(2015)</xref>
          , and
          <xref ref-type="bibr" rid="ref32">Prior et al. (2008)</xref>
          . Meanwhile, the multiple linear
regression analysis results above also show that company
size and leverage do not significantly affect CSR disclosure.
        </p>
      </sec>
    </sec>
    <sec id="sec-5">
      <title>5. Discussion and Conclusions</title>
      <p>
        The results of this study reveal that there is a causal
relationship between CSR and earnings management.
The relationship between the two has a positive direction.
These results support the opportunist hypothesis, which
reveals that CSR disclosure is a corporate strategy to cover
up earnings management actions. Companies that carry
out earnings management will try to divert investors? and
other stakeholders? attention by prioritizing the disclosure
of CSR activities
        <xref ref-type="bibr" rid="ref32">(Prior et al., 2008)</xref>
        . This action is done to
avoid adverse reactions from stakeholders on management?s
discretion in preparing financial statements that only
maximize management?s benefits
        <xref ref-type="bibr" rid="ref26">(Martínez-Ferrero et al.,
2015)</xref>
        . The management hopes that by disclosing CSR to
stakeholders, management will be seen as having ethical
and responsible behavior
        <xref ref-type="bibr" rid="ref8">(Faisal et al., 2020)</xref>
        . Management
gets support from other stakeholders, primarily social and
environmental activists, from the disciplinary action of
shareholders whose long-term interests are not fulfilled due
to earnings management
        <xref ref-type="bibr" rid="ref41">(Salewski &amp; Zülch, 2012)</xref>
        .
      </p>
      <p>
        Based on the results of multiple linear regression
analysis in the first model, CSR disclosure has a positive
effect on earnings management. Meanwhile, the results
of multiple linear regression analysis in the second model
indicate that earnings management impacts CSR disclosure.
These results suggest that CSR disclosure and earnings
management are two-way relationships or a recursive model
        <xref ref-type="bibr" rid="ref26">(Martínez-Ferrero et al., 2015)</xref>
        . This finding is in line with
        <xref ref-type="bibr" rid="ref6">Choi et al. (2018)</xref>
        , who revealed the endogeneity problem
in the relationship between CSR disclosure and earnings
management.
      </p>
      <p>This study reveals that CSR disclosure is part of the
management strategy in conducting earnings management.
These results verify agency theory that management
can exploit information asymmetry in maximizing
selfinterest. This study also reveals that CSR disclosure and
earnings management are two-way relationships. Therefore,
there is an opportunity for further research to study this
relationship more deeply. Meanwhile, this study results
have implications for regulators to increase supervision and
control over companies in preparing financial reports and
implementing CSR activities. Regulators should formulate
a guideline for disclosure of CSR, which is mandatory
for all companies so that the form of disclosure of social
responsibility among companies is uniform. This study?s
findings must be interpreted with caution, considering that
the study population includes mining companies listed on
the Indonesia Stock Exchange (IDX).</p>
    </sec>
  </body>
  <back>
    <ref-list>
      <ref id="ref1">
        <mixed-citation>
          <string-name>
            <surname>Almahrog</surname>
            ,
            <given-names>Y.</given-names>
          </string-name>
          ,
          <string-name>
            <surname>Ali Aribi</surname>
            ,
            <given-names>Z.</given-names>
          </string-name>
          , &amp;
          <string-name>
            <surname>Arun</surname>
            ,
            <given-names>T.</given-names>
          </string-name>
          (
          <year>2018</year>
          ).
          <article-title>Earnings management and corporate social responsibility: UK evidence</article-title>
          .
          <source>Journal of Financial Reporting and Accounting</source>
          ,
          <volume>16</volume>
          (
          <issue>2</issue>
          ),
          <fpage>311</fpage>
          -
          <lpage>332</lpage>
          . https://doi.org/10.1108/JFRA-11-2016-0092
        </mixed-citation>
      </ref>
      <ref id="ref2">
        <mixed-citation>
          <string-name>
            <surname>Almahrog</surname>
            ,
            <given-names>Y.</given-names>
          </string-name>
          ,
          <string-name>
            <surname>Marai</surname>
            ,
            <given-names>A.</given-names>
          </string-name>
          , &amp;
          <string-name>
            <surname>Kne?evi?</surname>
            ,
            <given-names>G.</given-names>
          </string-name>
          (
          <year>2015</year>
          ).
          <article-title>Earnings management and its relations with corporate social responsibility</article-title>
          .
          <source>Facta Universitatis</source>
          ,
          <volume>12</volume>
          (
          <issue>4</issue>
          ),
          <fpage>347</fpage>
          -
          <lpage>356</lpage>
          . http://casopisi.junis.ni.ac. rs/index.php/FUEconOrg/article/view/839
        </mixed-citation>
      </ref>
      <ref id="ref3">
        <mixed-citation>
          <string-name>
            <surname>Ben</surname>
            ,
            <given-names>A. A.</given-names>
          </string-name>
          , &amp;
          <string-name>
            <surname>Chakroun</surname>
            ,
            <given-names>S.</given-names>
          </string-name>
          (
          <year>2018</year>
          ).
          <article-title>Do the dimensions of corporate social responsibility affect earnings management?: Evidence from France</article-title>
          .
          <source>Journal of Financial Reporting and Accounting</source>
          ,
          <volume>16</volume>
          (
          <issue>2</issue>
          ),
          <fpage>348</fpage>
          -
          <lpage>370</lpage>
          . https://doi.org/10.1108/JFRA-05-2017-0033
        </mixed-citation>
      </ref>
      <ref id="ref4">
        <mixed-citation>
          <string-name>
            <surname>Buertey</surname>
            ,
            <given-names>S.</given-names>
          </string-name>
          ,
          <string-name>
            <surname>Sun</surname>
            ,
            <given-names>E.</given-names>
          </string-name>
          ,
          <string-name>
            <surname>Lee</surname>
            ,
            <given-names>J. S.</given-names>
          </string-name>
          , &amp;
          <string-name>
            <surname>Hwang</surname>
            ,
            <given-names>J.</given-names>
          </string-name>
          (
          <year>2020</year>
          ).
          <article-title>Corporate social responsibility and earnings management: The moderating effect of corporate governance mechanisms</article-title>
          .
          <source>Corporate Social Responsibility and Environmental Management</source>
          ,
          <volume>27</volume>
          (
          <issue>1</issue>
          ),
          <fpage>256</fpage>
          -
          <lpage>271</lpage>
          . https://doi.org/10.1002/csr.1803
        </mixed-citation>
      </ref>
      <ref id="ref5">
        <mixed-citation>
          <string-name>
            <surname>Choi</surname>
            ,
            <given-names>B. B.</given-names>
          </string-name>
          ,
          <string-name>
            <surname>Lee</surname>
            ,
            <given-names>D.</given-names>
          </string-name>
          , &amp;
          <string-name>
            <surname>Park</surname>
            ,
            <given-names>Y.</given-names>
          </string-name>
          (
          <year>2013</year>
          ).
          <article-title>Corporate social responsibility, corporate governance, and earnings quality: Evidence from Korea: CSR, corporate governance, and earnings quality</article-title>
          .
          <source>Corporate Governance: An International Review</source>
          ,
          <volume>21</volume>
          (
          <issue>5</issue>
          ),
          <fpage>447</fpage>
          -
          <lpage>467</lpage>
          . https://doi.org/10.1111/corg.12033
        </mixed-citation>
      </ref>
      <ref id="ref6">
        <mixed-citation>
          <string-name>
            <surname>Choi</surname>
            ,
            <given-names>H.</given-names>
          </string-name>
          ,
          <string-name>
            <surname>Choi</surname>
            ,
            <given-names>B.</given-names>
          </string-name>
          , &amp;
          <string-name>
            <surname>Byun</surname>
            ,
            <given-names>J.</given-names>
          </string-name>
          (
          <year>2018</year>
          ).
          <article-title>The relationship between corporate social responsibility and earnings management: Accounting for endogeneity</article-title>
          .
          <source>Investment Management and Financial Innovations</source>
          ,
          <volume>15</volume>
          (
          <issue>4</issue>
          ),
          <fpage>69</fpage>
          -
          <lpage>84</lpage>
          . https://doi.org/10.21511/ imfi.
          <volume>15</volume>
          (
          <issue>4</issue>
          ).
          <year>2018</year>
          .06
        </mixed-citation>
      </ref>
      <ref id="ref7">
        <mixed-citation>
          <string-name>
            <surname>Dechow</surname>
            ,
            <given-names>P. M.</given-names>
          </string-name>
          ,
          <string-name>
            <surname>Sloan</surname>
            ,
            <given-names>R. G.</given-names>
          </string-name>
          , &amp;
          <string-name>
            <surname>Amy</surname>
            ,
            <given-names>P.</given-names>
          </string-name>
          (
          <year>1995</year>
          ).
          <article-title>Detecting earnings management</article-title>
          .
          <source>The Accounting Review</source>
          ,
          <volume>70</volume>
          (
          <issue>2</issue>
          ),
          <fpage>193</fpage>
          -
          <lpage>225</lpage>
          . https:// www.jstor.org/stable/248303
        </mixed-citation>
      </ref>
      <ref id="ref8">
        <mixed-citation>
          <string-name>
            <surname>Faisal</surname>
            ,
            <given-names>F.</given-names>
          </string-name>
          ,
          <string-name>
            <surname>Situmorang</surname>
            ,
            <given-names>L. S.</given-names>
          </string-name>
          ,
          <string-name>
            <surname>Achmad</surname>
            ,
            <given-names>T.</given-names>
          </string-name>
          , &amp;
          <string-name>
            <surname>Prastiwi</surname>
            ,
            <given-names>A.</given-names>
          </string-name>
          (
          <year>2020</year>
          ).
          <article-title>The role of government regulations in enhancing corporate social responsibility disclosure and firm value</article-title>
          .
          <source>The Journal of Asian Finance, Economics, and Business</source>
          ,
          <volume>7</volume>
          (
          <issue>8</issue>
          ),
          <fpage>509</fpage>
          -
          <lpage>518</lpage>
          . https://doi.org/10.13106/jafeb.
          <year>2020</year>
          .
          <year>vol7</year>
          .
          <year>no8</year>
          .
          <fpage>509</fpage>
        </mixed-citation>
      </ref>
      <ref id="ref9">
        <mixed-citation>
          <string-name>
            <surname>Gargouri</surname>
            ,
            <given-names>R. M.</given-names>
          </string-name>
          ,
          <string-name>
            <surname>Shabou</surname>
            ,
            <given-names>R.</given-names>
          </string-name>
          , &amp;
          <string-name>
            <surname>Francoeur</surname>
            ,
            <given-names>C.</given-names>
          </string-name>
          (
          <year>2010</year>
          ).
          <article-title>The relationship between corporate social performance and earnings management</article-title>
          .
          <source>Canadian Journal of Administrative Sciences</source>
          ,
          <volume>27</volume>
          (
          <issue>4</issue>
          ),
          <fpage>320</fpage>
          -
          <lpage>334</lpage>
          . https://doi.org/10.1002/cjas.178
        </mixed-citation>
      </ref>
      <ref id="ref10">
        <mixed-citation>
          <string-name>
            <surname>Gavana</surname>
            ,
            <given-names>G.</given-names>
          </string-name>
          ,
          <string-name>
            <surname>Gottardo</surname>
            ,
            <given-names>P.</given-names>
          </string-name>
          , &amp;
          <string-name>
            <surname>Moisello</surname>
            ,
            <given-names>A.</given-names>
          </string-name>
          (
          <year>2017</year>
          ).
          <article-title>Earnings management and CSR disclosure</article-title>
          .
          <article-title>Family vs. non-family firms</article-title>
          .
          <source>Sustainability</source>
          ,
          <volume>9</volume>
          (
          <issue>12</issue>
          ),
          <volume>2327</volume>
          . https://doi.org/10.3390/su9122327
        </mixed-citation>
      </ref>
      <ref id="ref11">
        <mixed-citation>
          <string-name>
            <surname>Hamid</surname>
            ,
            <given-names>F. Z. A.</given-names>
          </string-name>
          , &amp;
          <string-name>
            <surname>Atan</surname>
            ,
            <given-names>R.</given-names>
          </string-name>
          (
          <year>2011</year>
          ).
          <article-title>Corporate social responsibility by the Malaysian telecommunication firms</article-title>
          .
          <source>The Special Issue on Contemporary Issues in Business and Economics</source>
          ,
          <volume>2</volume>
          (
          <issue>5</issue>
          ),
          <fpage>198</fpage>
          -
          <lpage>208</lpage>
          . http://ijbssnet.com/journals/Vol._
          <volume>2</volume>
          _No._
          <volume>5</volume>
          _ %5BSpecial_
          <string-name>
            <surname>Issue</surname>
          </string-name>
          _-_
          <string-name>
            <surname>March</surname>
          </string-name>
          _
          <year>2011</year>
          %5D/25.pdf
        </mixed-citation>
      </ref>
      <ref id="ref12">
        <mixed-citation>
          <string-name>
            <surname>Hemingway</surname>
            ,
            <given-names>C. A.</given-names>
          </string-name>
          , &amp;
          <string-name>
            <surname>Maclagan</surname>
            ,
            <given-names>P. W.</given-names>
          </string-name>
          (
          <year>2004</year>
          ).
          <article-title>Managers' personal values as drivers of corporate social responsibility</article-title>
          .
          <source>Journal of Business Ethics</source>
          ,
          <volume>50</volume>
          (
          <issue>1</issue>
          ),
          <fpage>33</fpage>
          -
          <lpage>44</lpage>
          . https://doi.org/10.1023/ B:BUSI.
          <volume>0000020964</volume>
          .80208.c9
        </mixed-citation>
      </ref>
      <ref id="ref13">
        <mixed-citation>
          <string-name>
            <surname>Hong</surname>
            ,
            <given-names>Y.</given-names>
          </string-name>
          , &amp;
          <string-name>
            <surname>Andersen</surname>
            ,
            <given-names>M. L.</given-names>
          </string-name>
          (
          <year>2011</year>
          ).
          <article-title>The relationship between corporate social responsibility and earnings management: An exploratory study</article-title>
          .
          <source>Journal of Business Ethics</source>
          ,
          <volume>104</volume>
          (
          <issue>4</issue>
          ),
          <fpage>461</fpage>
          -
          <lpage>471</lpage>
          . https://doi.org/10.1007/s10551-011-0921-y
        </mixed-citation>
      </ref>
      <ref id="ref14">
        <mixed-citation>
          <string-name>
            <surname>Huynh</surname>
            ,
            <given-names>Q. L.</given-names>
          </string-name>
          (
          <year>2020</year>
          ).
          <article-title>A triple of corporate governance, social responsibility, and earnings management</article-title>
          .
          <source>Journal of Asian Finance, Economics, and Business</source>
          ,
          <volume>7</volume>
          (
          <issue>3</issue>
          ),
          <fpage>29</fpage>
          -
          <lpage>40</lpage>
          . https://doi. org/10.13106/jafeb.
          <year>2020</year>
          .
          <year>vol7</year>
          .
          <year>no3</year>
          .
          <fpage>29</fpage>
        </mixed-citation>
      </ref>
      <ref id="ref15">
        <mixed-citation>
          <string-name>
            <surname>Jensen</surname>
            ,
            <given-names>M. C.</given-names>
          </string-name>
          , &amp;
          <string-name>
            <surname>Meckling</surname>
            ,
            <given-names>W. H.</given-names>
          </string-name>
          (
          <year>1976</year>
          ).
          <article-title>Theory of the firm: Managerial behavior, agency costs, and ownership structure</article-title>
          .
          <source>Journal of Financial Economics</source>
          ,
          <volume>3</volume>
          (
          <issue>4</issue>
          ),
          <fpage>305</fpage>
          -
          <lpage>360</lpage>
          . https://doi. org/10.1016/
          <fpage>0304</fpage>
          -
          <lpage>405X</lpage>
          (
          <issue>76</issue>
          )
          <fpage>90026</fpage>
          -X
        </mixed-citation>
      </ref>
      <ref id="ref16">
        <mixed-citation>
          <string-name>
            <surname>Jones</surname>
            ,
            <given-names>M.</given-names>
          </string-name>
          (
          <year>2011</year>
          ).
          <article-title>Creative accounting, fraud, and international accounting scandals</article-title>
          . Hoboken, NJ, USA: John Wiley &amp; Sons.
        </mixed-citation>
      </ref>
      <ref id="ref17">
        <mixed-citation>
          <string-name>
            <surname>Jones</surname>
            ,
            <given-names>T. M.</given-names>
          </string-name>
          (
          <year>1995</year>
          ).
          <article-title>Instrumental stakeholder theory: A synthesis of ethics and economics</article-title>
          .
          <source>Academy of Management Review</source>
          ,
          <volume>20</volume>
          (
          <issue>2</issue>
          ),
          <fpage>404</fpage>
          -
          <lpage>437</lpage>
          . https://doi.org/10.5465/amr.
          <year>1995</year>
          .9507312924
        </mixed-citation>
      </ref>
      <ref id="ref18">
        <mixed-citation>
          <string-name>
            <surname>Jordaan</surname>
            ,
            <given-names>L. A.</given-names>
          </string-name>
          ,
          <string-name>
            <surname>De Klerk</surname>
            ,
            <given-names>M.</given-names>
          </string-name>
          , &amp;
          <string-name>
            <surname>De Villiers</surname>
            ,
            <given-names>C. J.</given-names>
          </string-name>
          (
          <year>2018</year>
          ).
          <article-title>Corporate social responsibility and earnings management of South African companies</article-title>
          .
          <source>South African Journal of Economic and Management Sciences</source>
          ,
          <volume>21</volume>
          (
          <issue>1</issue>
          ),
          <year>a1849</year>
          . https://doi.org/10.4102/sajems.v21i1.
          <year>1849</year>
        </mixed-citation>
      </ref>
      <ref id="ref19">
        <mixed-citation>
          <string-name>
            <surname>Kim</surname>
            ,
            <given-names>Y.</given-names>
          </string-name>
          ,
          <string-name>
            <surname>Park</surname>
            ,
            <given-names>M. S.</given-names>
          </string-name>
          , &amp;
          <string-name>
            <surname>Wier</surname>
            ,
            <given-names>B.</given-names>
          </string-name>
          (
          <year>2012</year>
          ).
          <article-title>Is earnings quality associated with corporate social responsibility? The Accounting Review</article-title>
          ,
          <volume>87</volume>
          (
          <issue>3</issue>
          ),
          <fpage>761</fpage>
          -
          <lpage>796</lpage>
          . https://doi.org/10.2308/accr-10209
        </mixed-citation>
      </ref>
      <ref id="ref20">
        <mixed-citation>
          <string-name>
            <surname>Kumala</surname>
            ,
            <given-names>R.</given-names>
          </string-name>
          , &amp;
          <string-name>
            <surname>Siregar</surname>
            ,
            <given-names>S. V.</given-names>
          </string-name>
          (
          <year>2020</year>
          ).
          <article-title>Corporate social responsibility, family ownership, and earnings management: The case of Indonesia. Social Responsibility Journal, ahead-of-print (ahead-of-print)</article-title>
          . https://doi.org/10.1108/SRJ-09-2016-0156
        </mixed-citation>
      </ref>
      <ref id="ref21">
        <mixed-citation>
          <string-name>
            <surname>Li</surname>
            ,
            <given-names>Z. F.</given-names>
          </string-name>
          , &amp;
          <string-name>
            <surname>Thibodeau</surname>
            ,
            <given-names>C.</given-names>
          </string-name>
          (
          <year>2019</year>
          ).
          <article-title>CSR-contingent executive compensation incentive and earnings management</article-title>
          .
          <source>Sustainability</source>
          ,
          <volume>11</volume>
          (
          <issue>12</issue>
          ),
          <volume>3421</volume>
          . https://doi.org/10.3390/su11123421
        </mixed-citation>
      </ref>
      <ref id="ref22">
        <mixed-citation>
          <string-name>
            <surname>Liu</surname>
            ,
            <given-names>H.</given-names>
          </string-name>
          , &amp;
          <string-name>
            <surname>Lee</surname>
            ,
            <given-names>H. A.</given-names>
          </string-name>
          (
          <year>2019</year>
          ).
          <article-title>The effect of corporate social responsibility on earnings management and tax avoidance in Chinese listed companies</article-title>
          .
          <source>International Journal of Accounting &amp; Information Management</source>
          ,
          <volume>27</volume>
          (
          <issue>4</issue>
          ),
          <fpage>632</fpage>
          -
          <lpage>652</lpage>
          . https://doi. org/10.1108/IJAIM-08-2018-0095
        </mixed-citation>
      </ref>
      <ref id="ref23">
        <mixed-citation>
          <string-name>
            <surname>Liu</surname>
            ,
            <given-names>M.</given-names>
          </string-name>
          ,
          <string-name>
            <surname>Shi</surname>
            ,
            <given-names>Y.</given-names>
          </string-name>
          , Wilson,
          <string-name>
            <given-names>C.</given-names>
            , &amp;
            <surname>Wu</surname>
          </string-name>
          ,
          <string-name>
            <surname>Z.</surname>
          </string-name>
          (
          <year>2017</year>
          ).
          <article-title>Does family involvement explain why corporate social responsibility affects earnings management</article-title>
          ?
          <source>Journal of Business Research</source>
          ,
          <volume>75</volume>
          ,
          <fpage>8</fpage>
          -
          <lpage>16</lpage>
          . https://doi.org/10.1016/j.jbusres.
          <year>2017</year>
          .
          <volume>02</volume>
          .001
        </mixed-citation>
      </ref>
      <ref id="ref24">
        <mixed-citation>
          <string-name>
            <given-names>Management</given-names>
            <surname>Association</surname>
          </string-name>
          . (
          <year>2019</year>
          ).
          <article-title>Corporate social responsibility: Concepts, methodologies, tools, and applications</article-title>
          . Pennsylvania: IGI Global. https://doi.org/10.4018/978-1-
          <fpage>5225</fpage>
          -6192-7
        </mixed-citation>
      </ref>
      <ref id="ref25">
        <mixed-citation>
          <string-name>
            <surname>Martínez-Ferrero</surname>
            ,
            <given-names>J.</given-names>
          </string-name>
          ,
          <string-name>
            <surname>Banerjee</surname>
            ,
            <given-names>S.</given-names>
          </string-name>
          , &amp;
          <string-name>
            <surname>García-Sánchez</surname>
            ,
            <given-names>I. M.</given-names>
          </string-name>
          (
          <year>2016</year>
          ).
          <article-title>Corporate social responsibility as a strategic shield against costs of earnings management practices</article-title>
          .
          <source>Journal of Business Ethics</source>
          ,
          <volume>133</volume>
          (
          <issue>2</issue>
          ),
          <fpage>305</fpage>
          -
          <lpage>324</lpage>
          . https://doi.org/10.1007/s10551-014-2399-x
        </mixed-citation>
      </ref>
      <ref id="ref26">
        <mixed-citation>
          <string-name>
            <surname>Martínez-Ferrero</surname>
            ,
            <given-names>J.</given-names>
          </string-name>
          ,
          <string-name>
            <surname>Gallego-Álvarez</surname>
            ,
            <given-names>I.</given-names>
          </string-name>
          , &amp;
          <string-name>
            <surname>García-Sánchez</surname>
            ,
            <given-names>I. M.</given-names>
          </string-name>
          (
          <year>2015</year>
          ).
          <article-title>A bidirectional analysis of earnings management and corporate social responsibility: The moderating effect of stakeholder and investor protection: Earnings management and corporate social responsibility</article-title>
          .
          <source>Australian Accounting Review</source>
          ,
          <volume>25</volume>
          (
          <issue>4</issue>
          ),
          <fpage>359</fpage>
          -
          <lpage>371</lpage>
          . https://doi.org/10.1111/auar.12075
        </mixed-citation>
      </ref>
      <ref id="ref27">
        <mixed-citation>
          <string-name>
            <surname>Moratis</surname>
            ,
            <given-names>L.</given-names>
          </string-name>
          , &amp; Van Egmond,
          <string-name>
            <surname>M.</surname>
          </string-name>
          (
          <year>2018</year>
          ).
          <article-title>Concealing social responsibility? Investigating the relationship between CSR, earnings management, and the effect of the industry through quantitative analysis</article-title>
          .
          <source>International Journal of Corporate Social Responsibility</source>
          ,
          <volume>3</volume>
          (
          <issue>1</issue>
          ), 8. https://doi.org/10.1186/s40991- 018-0030-7
        </mixed-citation>
      </ref>
      <ref id="ref28">
        <mixed-citation>
          <string-name>
            <surname>Muliati</surname>
            ,
            <given-names>M.</given-names>
          </string-name>
          ,
          <string-name>
            <surname>Iqbal</surname>
            ,
            <given-names>M.</given-names>
          </string-name>
          , &amp;
          <string-name>
            <surname>Mayapada</surname>
            ,
            <given-names>A. G.</given-names>
          </string-name>
          (
          <year>2020</year>
          ).
          <article-title>The effect of organizational culture on firm performance with social responsibility as a mediating variable</article-title>
          . Research in World Economy,
          <volume>11</volume>
          (
          <issue>5</issue>
          ), 279. https://doi.org/10.5430/rwe.v11n5p279
        </mixed-citation>
      </ref>
      <ref id="ref29">
        <mixed-citation>
          <string-name>
            <surname>Muttakin</surname>
            ,
            <given-names>M. B.</given-names>
          </string-name>
          ,
          <string-name>
            <surname>Khan</surname>
            ,
            <given-names>A.</given-names>
          </string-name>
          , &amp;
          <string-name>
            <surname>Azim</surname>
            ,
            <given-names>M. I.</given-names>
          </string-name>
          (
          <year>2015</year>
          ).
          <article-title>Corporate social responsibility disclosures and earnings quality: Are they a reflection of managers' opportunistic behavior?</article-title>
          <source>Managerial Auditing Journal</source>
          ,
          <volume>30</volume>
          (
          <issue>3</issue>
          ),
          <fpage>277</fpage>
          -
          <lpage>298</lpage>
          . https://doi.org/10.1108/ MAJ-02-2014-0997
        </mixed-citation>
      </ref>
      <ref id="ref30">
        <mixed-citation>
          <string-name>
            <given-names>Omair</given-names>
            <surname>Alotaibi</surname>
          </string-name>
          ,
          <string-name>
            <given-names>K.</given-names>
            , &amp;
            <surname>Hussainey</surname>
          </string-name>
          ,
          <string-name>
            <surname>K.</surname>
          </string-name>
          (
          <year>2016</year>
          ).
          <article-title>Determinants of CSR disclosure quantity and quality: Evidence from nonfinancial listed firms in Saudi Arabia</article-title>
          .
          <source>International Journal of Disclosure and Governance</source>
          ,
          <volume>13</volume>
          (
          <issue>4</issue>
          ),
          <fpage>364</fpage>
          -
          <lpage>393</lpage>
          . https://doi. org/10.1057/jdg.
          <year>2016</year>
          .2
        </mixed-citation>
      </ref>
      <ref id="ref31">
        <mixed-citation>
          <string-name>
            <surname>Patro</surname>
            ,
            <given-names>B.</given-names>
          </string-name>
          , &amp;
          <string-name>
            <surname>Pattanayak</surname>
            ,
            <given-names>J. K.</given-names>
          </string-name>
          (
          <year>2017</year>
          ).
          <article-title>Corporate governance as a moderating variable for identifying the relationship between CSR and earnings management: A study of listed Indian mining firms</article-title>
          .
          <source>Prabandhan: Indian Journal of Management</source>
          ,
          <volume>10</volume>
          (
          <issue>10</issue>
          ),
          <volume>24</volume>
          . https://doi.org/10.17010/pijom/2017/v10i10/118812
        </mixed-citation>
      </ref>
      <ref id="ref32">
        <mixed-citation>
          <string-name>
            <surname>Prior</surname>
            ,
            <given-names>D.</given-names>
          </string-name>
          ,
          <string-name>
            <surname>Surroca</surname>
            ,
            <given-names>J.</given-names>
          </string-name>
          , &amp;
          <string-name>
            <surname>Tribó</surname>
            ,
            <given-names>J. A.</given-names>
          </string-name>
          (
          <year>2008</year>
          ).
          <article-title>Are socially responsible managers really ethical? Exploring the relationship between earnings management and corporate social responsibility</article-title>
          .
          <source>Corporate Governance: An International Review</source>
          ,
          <volume>16</volume>
          (
          <issue>3</issue>
          ),
          <fpage>160</fpage>
          -
          <lpage>177</lpage>
          . https://doi.org/10.1111/j.1467-
          <fpage>8683</fpage>
          .
          <year>2008</year>
          .
          <volume>00678</volume>
          .x
        </mixed-citation>
      </ref>
      <ref id="ref33">
        <mixed-citation>
          <string-name>
            <surname>Rao</surname>
            ,
            <given-names>K.</given-names>
          </string-name>
          , &amp;
          <string-name>
            <surname>Tilt</surname>
            ,
            <given-names>C.</given-names>
          </string-name>
          (
          <year>2016</year>
          ).
          <article-title>Board diversity and CSR reporting: An Australian study</article-title>
          .
          <source>Meditari Accountancy Research</source>
          ,
          <volume>24</volume>
          (
          <issue>2</issue>
          ),
          <fpage>182</fpage>
          -
          <lpage>210</lpage>
          . https://doi.org/10.1108/MEDAR-08-2015-0052
        </mixed-citation>
      </ref>
      <ref id="ref34">
        <mixed-citation>
          <string-name>
            <surname>Ridho</surname>
            ,
            <given-names>T. K.</given-names>
          </string-name>
          (
          <year>2017</year>
          ).
          <article-title>CSR in Indonesia: ?ompany`s perception and implementation</article-title>
          .
          <source>The EUrASEANs: Journal on Global SocioEconomic Dynamics</source>
          ,
          <volume>3</volume>
          (
          <issue>4</issue>
          ),
          <fpage>68</fpage>
          -
          <lpage>74</lpage>
          . https://euraseans.com/index. php/journal/article/view/41
        </mixed-citation>
      </ref>
      <ref id="ref35">
        <mixed-citation>
          <string-name>
            <surname>Ridwan</surname>
            ,
            <given-names>R.</given-names>
          </string-name>
          , &amp;
          <string-name>
            <surname>Mayapada</surname>
            ,
            <given-names>A. G.</given-names>
          </string-name>
          (
          <year>2020</year>
          ).
          <article-title>Does sharia governance influence corporate social responsibility disclosure in Indonesia Islamic banks</article-title>
          ?
          <source>Journal of Sustainable Finance &amp; Investment</source>
          ,
          <volume>3</volume>
          (
          <issue>5</issue>
          ),
          <fpage>1</fpage>
          -
          <lpage>20</lpage>
          . https://doi.org/10.1080/20430795.
          <year>2020</year>
          .1749819
        </mixed-citation>
      </ref>
      <ref id="ref36">
        <mixed-citation>
          <string-name>
            <surname>Rokhmawati</surname>
            ,
            <given-names>A.</given-names>
          </string-name>
          , &amp;
          <string-name>
            <surname>Gunardi</surname>
            ,
            <given-names>A.</given-names>
          </string-name>
          (
          <year>2017</year>
          ).
          <article-title>Is going green good for profit? Empirical evidence from listed manufacturing firms in Indonesia</article-title>
          .
          <source>International Journal of Energy Economics and Policy</source>
          ,
          <volume>7</volume>
          (
          <issue>4</issue>
          ),
          <fpage>181</fpage>
          -
          <lpage>192</lpage>
          . http://www.econjournals.com/index. php/ijeep/article/viewFile/5381/3217
        </mixed-citation>
      </ref>
      <ref id="ref37">
        <mixed-citation>
          <string-name>
            <surname>Rosli</surname>
            ,
            <given-names>M. H. B.</given-names>
          </string-name>
          ,
          <string-name>
            <surname>Said</surname>
            ,
            <given-names>J.</given-names>
          </string-name>
          , &amp;
          <string-name>
            <surname>Fauzi</surname>
            ,
            <given-names>N. A. B.</given-names>
          </string-name>
          (
          <year>2016</year>
          ).
          <article-title>Company characteristics and corporate social responsibility disclosure</article-title>
        </mixed-citation>
      </ref>
      <ref id="ref38">
        <mixed-citation>
          <source>on Accounting Studies (ICAS)</source>
          <year>2016</year>
          ,
          <fpage>15</fpage>
          -18
          <source>August</source>
          <year>2016</year>
          ,
        </mixed-citation>
      </ref>
      <ref id="ref39">
        <mixed-citation>
          proceedings/168-company
          <article-title>-characteristics-and-corporate-social-</article-title>
        </mixed-citation>
      </ref>
      <ref id="ref40">
        <mixed-citation>
          <string-name>
            <surname>Saraswati</surname>
            ,
            <given-names>E.</given-names>
          </string-name>
          ,
          <string-name>
            <surname>Sagitaputri</surname>
            ,
            <given-names>A.</given-names>
          </string-name>
          , &amp;
          <string-name>
            <surname>Rahadian</surname>
            <given-names>Y.</given-names>
          </string-name>
          (
          <year>2020</year>
          ).
          <article-title>Political connections and CSR disclosures in Indonesia</article-title>
          .
          <source>Journal of Asian Finance, Economics, and Business</source>
          ,
          <volume>7</volume>
          (
          <issue>11</issue>
          ),
          <fpage>1097</fpage>
          -
          <lpage>1104</lpage>
          . https://doi.org/10.13106/jafeb.
          <year>2020</year>
          .
          <year>vol7</year>
          .
          <year>no11</year>
          .
          <fpage>1097</fpage>
        </mixed-citation>
      </ref>
      <ref id="ref41">
        <mixed-citation>
          <string-name>
            <surname>Salewski</surname>
            ,
            <given-names>M.</given-names>
          </string-name>
          , &amp;
          <string-name>
            <surname>Zülch</surname>
            ,
            <given-names>H.</given-names>
          </string-name>
          (
          <year>2012</year>
          ).
          <article-title>The impact of corporate social responsibility (CSR) on financial reporting quality: Evidence from European blue chips</article-title>
          .
          <source>SSRN Electronic Journal</source>
          . https:// doi.org/10.2139/ssrn.2141768
        </mixed-citation>
      </ref>
      <ref id="ref42">
        <mixed-citation>
          <string-name>
            <surname>Scholtens</surname>
            ,
            <given-names>B.</given-names>
          </string-name>
          , &amp;
          <string-name>
            <surname>Kang</surname>
            ,
            <given-names>F. C.</given-names>
          </string-name>
          (
          <year>2013</year>
          ),
          <article-title>Corporate social responsibility and earnings management: Evidence from Asian economies: SR and earnings management in Asia</article-title>
          .
          <source>Corporate Social Responsibility and Environmental Management</source>
          ,
          <volume>20</volume>
          (
          <issue>2</issue>
          ),
          <fpage>95</fpage>
          -
          <lpage>112</lpage>
          . https://doi.org/10.1002/csr.1286
        </mixed-citation>
      </ref>
      <ref id="ref43">
        <mixed-citation>
          <string-name>
            <surname>Yip</surname>
            ,
            <given-names>E.</given-names>
          </string-name>
          ,
          <string-name>
            <surname>Van Staden</surname>
            ,
            <given-names>C.</given-names>
          </string-name>
          , &amp;
          <string-name>
            <surname>Cahan</surname>
            ,
            <given-names>S.</given-names>
          </string-name>
          (
          <year>2011</year>
          ),
          <article-title>Corporate social responsibility reporting and earnings management: The Role of Political Costs</article-title>
          .
          <source>Australasian Accounting, Business and Finance Journal</source>
          ,
          <volume>5</volume>
          (
          <issue>3</issue>
          ),
          <fpage>17</fpage>
          -
          <lpage>34</lpage>
          . https://ro.uow.edu.au/aabfj/ vol5/iss3/3/
        </mixed-citation>
      </ref>
    </ref-list>
  </back>
</article>'''


root = ET.fromstring(string)
for tag in root.iter(tag = 'article-title'):
  result = tag.text
print(result)