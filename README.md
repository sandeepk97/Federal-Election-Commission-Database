DMQL Milestone 2 Report

**I have read and understood the course academic integrity policy in the syllabus of the class.**

Team members:

1. Ashwin Ashok (<aashok3@buffalo.edu>)
2. Sandeep Kunusoth (<skunusot@buffalo.edu>)
3. Shreyas Sujjaluru Lakshminarasimhan (<ssujjalu@buffalo.edu>) 

<a name="_int_uvzps35s"></a>**Problem Statement:**

The Federal Election Commission (FEC) is responsible for enforcing the campaign finance laws in the United States. As part of this responsibility, the FEC collects and publishes data on campaign contributions and expenditure. This data is used by journalists, researchers, and the public to monitor the influence of money in politics. The goal of this project is to create a comprehensive database of campaign finance data for the 2022-2023 election cycle. This database should be easily searchable and accessible to the public, journalists, and researchers. This data is crucial for building a platform to display the campaign contributions and expenditures from past years. It will be much simpler to maintain this data in databases, which also makes it possible to obtain findings instantly. Overall, it seems that the data elements in dataset are all related to the complex web of money and politics in the United States. By analyzing data together, it may be possible to gain insights into how money influences elections and which individuals and organizations are most involved in the political process.

Link: [Federal Election Commission Database](https://www.fec.gov/data/browse-data/?tab=bulk-data)

**Why Databases and not EXCEL?**

**EXCEL:**

- Large data is challenging to preserve due of size. Additionally, Excel has difficulty maintaining the large number of entities needed to establish links between the data.
- Data relationships are difficult to maintain and are not possible.
- It will not support the real time data.

**DATABASE:**

- When it comes to manipulating and analyzing data, databases are significantly more powerful and adaptable than Excel. Data can be stored in a variety of formats, including text, photos, audio, and video.
- It is flexible for the larger data.
- The relations between the tables are easy.
- The database facilitates real-time applications.
- Using a database, we may conduct more complicated actions like connecting two tables, doing computations, and bulk updating. They also enable increased security and scalability.

**Target User:**

Journalists, Researchers, Advocacy Groups, Voters, and General Public comprise the end users. Journalists often rely on campaign finance data to uncover potential conflicts of interest and to report on the influence of money in politics. They may use the database to search for contributions from specific individuals or organizations, or to compare the fundraising and spending patterns of different candidates. Researchers in political science, economics, and other fields may use the database to analyze the impact of money on political campaigns, to identify trends in campaign finance, or to explore the relationship between political donations and policy outcomes. Advocacy groups may use the database to monitor the fundraising and spending activities of candidates or political parties, to track the activities of specific donors or interest groups, or to identify potential avenues for advocacy and engagement. Voters may use the database to research the candidates running in their districts or states, to learn more about the sources of funding for their campaigns, and to assess the potential influence of money on their elected representatives. The database can be accessed by anyone who is interested in learning more about the role of money in politics during the 2022-2023 election cycle in the United States. The data can be used to increase transparency and accountability in the political process and to inform public discourse on the issue.

Administrator: Federal Election commission maintains a public database, called the Electronic Filing System (EFS), which contains financial information provided by political committees and candidates.

**Entity Relation Diagram (ERD)**

Before we start designing the E/R diagram, we need to understand the tables in the dataset and their relationships. Based on the table names provided, we can identify the following entities:

Entities:

1. Candidates
2. Committees
3. Contributors
4. Campaigns
5. Contributions
6. Expenditures
7. Transactions

Now, let's consider the relationships between these entities. Here are some possible relationships that we can identify based on the dataset:

Relationships:

Candidates – Committees:- Many to One

CurrentCampaignsForHouseandSenate - Candidates:- One to One

ContributionsByIndividuals - Committees:-  Many to Many

IndependentExpenditures - Candidates:- Many to One

Committees – IndependentExpenditures:- One to Many

Committees – OperatingExpenditures:- One to Many

Committees – PAC&PartySummary:- One to One

Committees – AnyTransactionFromOneCommmitteeToAnother:- Many to Many

Based on these relationships, we can draw an E/R diagram that looks something like this:

![](images/Aspose.Words.6ec778c9-0139-44bc-878e-428ad5bf2b92.001.png)

In this diagram, we have entities represented as rectangles. The relationships between these entities are represented as lines connecting them.

***NOTE:***

***In all the further sections green indicates the addition of new column/table post normalization and red indicates removal of column/table post the normalization.***




**Database Implementation:** 

` `**Database Schema, Attributes, Primary key and Foreign Key:**

- **candidate****										       

**Description:** The **candidate** contains information about individual candidates running for office. This will include data on the candidate’s name, party affiliation, campaign platform, and other relevant information. The committee relation contains the below attributes.

`     `**Attributes and Datatypes:**

|**Column Name**|**Column Type**|<p>**Can be**</p><p>**Null**</p>|**Default**|**Description**|
| :- | :- | :- | :- | :- |
|CAND\_ID|VARCHAR(9)|**No**||ID of the candidate. First character indicates office sought - H=House, S=Senate, P=Presidential. Characters 3 & 4 are the state abbreviation for Congressional candidates. Example value (H0AK00105)|
|CAND\_NAME|VARCHAR(200)|**Yes**|''|Name of candidate. Example Value (Martha Washington)|
|CAND\_PTY\_AFFILIATION|VARCHAR(3)|**Yes**|''|The political party affiliation reported by the candidate. Dem=Democrat<br>Rep=Republican<br>[full list of party affiliations](https://www.fec.gov/campaign-finance-data/party-code-descriptions/) Example value (Dem)|
|CAND\_ELECTION\_YR|Numeric(4)|**No**||Year of election. Example value: 2022|
|CAND\_OFFICE\_ST|VARCHAR(2)|**Yes**|''|<p>Candidate state. </p><p>House = state of race<br>President = US<br>Senate = state of race</p><p>Example value: (VA)</p>|
|CAND\_OFFICE|VARCHAR(1)|**Yes**|<p>''</p><p></p>|<p>Candidate Office.</p><p>H = House<br>P = President<br>S = Senate.  Example value: (H)</p>|
|CAND\_OFFICE\_DISTRICT|VARCHAR(2)|**Yes**|<p>''</p><p></p>|Candidate district. Congressional district number<br>Congressional at-large 00<br>Senate 00<br>Presidential 00. Example value: 01|
|CAND\_ICI|VARCHAR(1)|**Yes**|<p>''</p><p></p>|<p>Incumbent challenger status.</p><p>C = Challenger<br>I = Incumbent<br>O = Open Seat is used to indicate an open seat; Open seats are defined as seats where the incumbent never sought re-election.</p><p>Example value: I</p>|
|CAND\_STATUS|VARCHAR(1)|**Yes**|<p>''</p><p></p>|<p>Candidate status. </p><p>C = Statutory candidate<br>F = Statutory candidate for future election<br>N = Not yet a statutory candidate<br>P = Statutory candidate in prior cycle.</p><p>Example value: C</p>|
|CAND\_PCC|VARCHAR(9)|**Yes**|<p>''</p><p></p>|Principal campaign committee. The ID assigned by the Federal Election Commission to the candidate's principal campaign committee for a given election cycle. Example value: C00100005|
|CAND\_ST1|VARCHAR(34)|**Yes**|<p>''</p><p></p>|<p>Mailing address – street.</p><p>Example value: 1001 George Washington Hwy</p>|
|CAND\_ST2|VARCHAR(34)|**Yes**|<p>''</p><p></p>|<p>Mailing address – street2</p><p>Example value: Suite 100</p>|
|CAND\_CITY|VARCHAR(30)|**Yes**|<p>''</p><p></p>|<p>Mailing address – city</p><p>Example value: Alexandria</p>|
|CAND\_ST|VARCHAR(2)|**Yes**|<p>''</p><p></p>|<p>Mailing address – state</p><p>Example value: VA</p>|
|CAND\_ZIP|VARCHAR(9)|**Yes**|<p>''</p><p></p>|<p>Mailing address - ZIP code</p><p>Example value: 22201</p>|

**Primary Key: (CAND\_ID)** In the case of the candidate table, the CAND\_ID column is the most appropriate choice for the primary key because it uniquely identifies each candidate. This is evident from the fact that the CAND\_ID column has a unique value for each row in the table. Moreover, it is a unique identifier assigned by the Federal Election Commission (FEC) to each candidate and is used to track the candidate's fundraising and spending activities. Additionally, foreign keys in other tables that reference the candidate table can use the CAND\_ID column to establish the relationship between the tables.

**Schema:** 

CREATE TABLE candidate (

CAND\_ID VARCHAR(9) NOT NULL PRIMARY KEY,

CAND\_NAME VARCHAR(200),

CAND\_PTY\_AFFILIATION VARCHAR(3),

CAND\_ELECTION\_YR NUMERIC(4),

CAND\_OFFICE\_ST VARCHAR(2),

CAND\_OFFICE VARCHAR(1),

CAND\_OFFICE\_DISTRICT VARCHAR(2),

CAND\_ICI VARCHAR(1),

CAND\_STATUS VARCHAR(1),

CAND\_PCC VARCHAR(9),

CAND\_ST1 VARCHAR(34),

CAND\_ST2 VARCHAR(34),

CAND\_CITY VARCHAR(30),

CAND\_ST VARCHAR(2),

CAND\_ZIP VARCHAR(9)

);

- **committee****										       

**Description:** The **committee** contains information about the various political committees involved in the election process. This includes data on the committee’s name, purpose, funding sources, and other relevant information. The **committee** relation contains the below attributes.

`     `**Attributes and Datatypes:**

|**Column Name**|**Column Type**|<p>**Can be**</p><p>**Null**</p>|**Default**|**Description**|
| :- | :- | :- | :- | :- |
|CMTE\_ID|VARCHAR(9)|**No**||Committee identification. A 9-character alpha-numeric code assigned to a committee by the Federal Election Commission. Committee IDs are unique and an ID for a specific committee always remains the same. Example value: C00100005|
|CMTE\_NM|VARCHAR(200)|**Yes**|<p>''</p><p></p>|Committee name	. Example value: Martha Washington for Congress|
|TRES\_NM|VARCHAR(90)|**Yes**|<p>''</p><p></p>|Treasurer's name. The officially registered treasurer for the committee. Example value: Alexander Hamilton|
|CMTE\_ST1|VARCHAR(34)|**Yes**|''|Mailing address – street.Example value: 1001 George Washington Hwy|
|CMTE\_ST2|VARCHAR(34)|**Yes**|<p>''</p><p></p>|<p>Mailing address – street2</p><p>Example value: Suite 100</p>|
|CMTE\_CITY|VARCHAR(30)|**Yes**|<p>''</p><p></p>|<p>Mailing address – city</p><p>Example value: Alexandria</p>|
|CMTE\_ST|VARCHAR(2)|**Yes**|<p>''</p><p></p>|<p>Mailing address – state</p><p>Example value: VA</p>|
|CAND\_ZIP|VARCHAR(9)|**Yes**|<p>''</p><p></p>|<p>Mailing address - ZIP code</p><p>Example value: 22201</p>|
|CMTE\_DSGN|VARCHAR(1)|**Yes**|<p>''</p><p></p>|<p>Committee designation.  A = Authorized by a candidate<br>B = Lobbyist/Registrant PAC<br>D = Leadership PAC<br>J = Joint fundraiser<br>P = Principal campaign committee of a candidate<br>U = Unauthorized. </p><p>Example value: A</p>|
|CMTE\_TP|VARCHAR(1)|**Yes**|<p>''</p><p></p>|<p>Committee type. [List of committee type codes](https://www.fec.gov/campaign-finance-data/committee-type-code-descriptions)</p><p>Example value: H</p>|
|CMTE\_PTY\_AFFILIATION|VARCHAR(3)|**Yes**|<p>''</p><p></p>|<p>Committee party. [List of party codes](https://www.fec.gov/campaign-finance-data/party-code-descriptions)</p><p>Example value: NON</p>|
|CMTE\_FILING\_FREQ|VARCHAR(1)|**Yes**|<p>''</p><p></p>|<p>Filing frequency. A = Administratively terminated<br>D = Debt, M = Monthly filer, Q = Quarterly filer<br>T = Terminated, W = Waived.</p><p>Example value: Q</p>|
|ORG\_TP|VARCHAR(1)|**Yes**|<p>''</p><p></p>|<p>Interest group category. C = Corporation<br>L = Labor organization<br>M = Membership organization<br>T = Trade association<br>V = Cooperative<br>W = Corporation without capital stock.</p><p>Example value: C</p>|
|CONNECTED\_ORG\_NM|VARCHAR(200)|**Yes**|<p>''</p><p></p>|<p>Connected organization's name.</p><p>Example value: ‘Widgets, Incorporated’</p>|
|CAND\_ID|VARCHAR(9)|**Yes**|<p>''</p><p></p>|<p>Candidate identification.  When a committee has a committee type designation of H, S, or P, the candidate's identification number will be entered in this field.</p><p>Example value: H1VA01225</p>|

**Primary Key: (CMTE\_ID)** Using CMTE\_ID as the primary key ensures that each row in the table is uniquely identifiable by its committee ID. It also allows for efficient searching and retrieval of data related to a specific committee using the primary key index. Furthermore, since CMTE\_ID is a unique identifier assigned by the Federal Election Commission (FEC), it is a reliable and stable identifier that is unlikely to change over time, which makes it a good candidate for the primary key.

**Foreign Key:** **(CAND\_ID)** This relationship exists because a committee can be associated with a candidate. A committee may support a candidate. Therefore, it is appropriate to include a foreign key constraint in the committee table that references the candidate table's primary key. Additionally, this foreign key relationship allows for easy querying of data related to a candidate's committees and contributions to those committees.

**Schema:** 

CREATE TABLE committee (

CMTE\_ID VARCHAR(9) NOT NULL PRIMARY KEY,

CMTE\_NM VARCHAR(200),

TRES\_NM VARCHAR(90),

CMTE\_ST1 VARCHAR(34),

CMTE\_ST2 VARCHAR(34),

CMTE\_CITY VARCHAR(30),

CMTE\_ST VARCHAR(2),

CMTE\_ZIP VARCHAR(9),

CMTE\_DSGN VARCHAR(1),

CMTE\_TP VARCHAR(1),

CMTE\_PTY\_AFFILIATION VARCHAR(3),

CMTE\_FILING\_FREQ VARCHAR(1),

ORG\_TP VARCHAR(1),

CONNECTED\_ORG\_NM VARCHAR(200),

CAND\_ID VARCHAR(9)

);


- **Candidate- committee linkage****										   

**Description:** The **candidate-committee linkage** contains information linking the candidate's information to information about his or her committee**.** The candidate-committee linkage relation contains the bellow attributes.

`     `**Attributes and Datatypes:**

|**Column Name**|**Column Type**|<p>**Can be**</p><p>**Null**</p>|**Default**|**Description**|
| :- | :- | :- | :- | :- |
|CAND\_ID|VARCHAR(9)|**No**||Candidate identification. A 9-character alpha-numeric code assigned to a candidate by the Federal Election Commission. The candidate ID for a specific candidate remains the same across election cycles as long as the candidate is running for the same office. Example value: C00100005|
|CAND\_ELECTION\_YR|Numeric(4)|**No**|<p></p><p></p>|Candidate election year. Example value: 2022|
|FEC\_ELECTION\_YR|Numeric(4)|**No**|<p></p><p></p>|FEC election year. Active 2-year period.  Example value: 2022|
|CMTE\_ID|VARCHAR(9)|**No**||Committee identification. A 9-character alpha-numeric code assigned to a committee by the Federal Election Commission. The committee ID for a specific committee always remains the same. Example value: C00100005|
|CMTE\_DSGN|VARCHAR(1)|**Yes**|<p>''</p><p></p>|<p>Committee designation.  A = Authorized by a candidate<br>B = Lobbyist/Registrant PAC<br>D = Leadership PAC<br>J = Joint fundraiser<br>P = Principal campaign committee of a candidate<br>U = Unauthorized. </p><p>Example value: A</p>|
|CMTE\_TP|VARCHAR(1)|**Yes**|<p>''</p><p></p>|<p>Committee type. [List of committee type codes](https://www.fec.gov/campaign-finance-data/committee-type-code-descriptions)</p><p>Example value: H</p>|
|LINKAGE\_ID|Numeric(12)|**No**|<p></p><p></p>|<p>Linkage ID. Unique link ID</p><p>Example value: 123456789012</p>|

**Primary Key**: **(LINKAGE\_ID)** The candidate\_committee table serves as an association table that links the candidate and committee tables, which already have their own primary keys (CAND\_ID and CMTE\_ID, respectively). Therefore, the primary key for the candidate\_committee table should be a unique combination of **CAND\_ID, CAND\_ELECTION\_YR, FEC\_ELECTION\_YR, CMTE\_ID**. For every unique combination of **CAND\_ID, CAND\_ELECTION\_YR, FEC\_ELECTION\_YR, CMTE\_ID there is a unique** LINKAGE\_ID which should be the primary key. The CAND\_ELECTION\_YR and FEC\_ELECTION\_YR columns represent the year of the candidate's election and the year of the corresponding FEC election respectively.

**Foreign Key:** **(CAND\_ID, CMTE\_ID).** The candidate\_committee table contains a link between a candidate and a committee, indicating which candidate has received contributions from which committee. Therefore, the foreign key in this table should reference the primary keys of the candidate and committee tables, which are CAND\_ID and CMTE\_ID, respectively. These foreign keys ensure that the link between a candidate and a committee is valid and references existing records in the candidate and committee tables.

**Schema:** 

CREATE TABLE candidate\_committee (

CAND\_ID VARCHAR(9),

CAND\_ELECTION\_YR Numeric(4),

FEC\_ELECTION\_YR Numeric(4),

CMTE\_ID VARCHAR(9),

CMTE\_TP VARCHAR(1),

CMTE\_DSGN VARCHAR(1),

LINKAGE\_ID Numeric(12),

PRIMARY KEY (LINKAGE\_ID),

UNIQUE (CAND\_ID, CAND\_ELECTION\_YR, FEC\_ELECTION\_YR,CMTE\_ID),

FOREIGN KEY (CAND\_ID) REFERENCES candidate (CAND\_ID),

FOREIGN KEY (CMTE\_ID) REFERENCES committee (CMTE\_ID)

);

- **contributor****										   

**Description:** The contributor contains the information of the contributor**.** The contributor relation contains the bellow attributes.

`     `**Attributes and Datatypes:**

|**Column Name**|**Column Type**|<p>**Can be**</p><p>**Null**</p>|**Default**|**Description**|
| :- | :- | :- | :- | :- |
|**CONTRIBUTOR\_ID**|**Varchar(9)**|**No**||Contributor id|
|**NAME**|**Varchar(200)**|**Yes**||Contributor/Lender/Trader Name|
|**CITY**|**Varchar(30)**|**Yes**||City|
|**STATE**|**Varchar(2)**|**Yes**||State|
|**ZIP\_CODE**|**Varchar(9)**|**Yes**||Zip Code|
|**EMPLOYER**|**VARCHAR(38)**|**Yes**||Employer|
|**OCCUPATION**|**Varchar(38)**|**Yes**||Occupation|

**Primary Key**: **(CONTRIBUTOR\_ID)** Using CONTRIBUTOR\_ID as the primary key ensures that each row in the table is uniquely identifiable by its contributor ID. It also allows for efficient searching and retrieval of data related to a specific contributor using the primary key index.

**Schema:** 

**CREATE TABLE contributor (**

`    `**CONTRIBUTOR\_ID character varying(9),**

`    `**NAME character varying(200),**

`    `**CITY character varying(2),**

`    `**STATE character varying(2),**

`    `**ZIP\_CODE character varying(9),**

`    `**EMPLOYER character varying(38),**

`    `**OCCUPATION character varying(38)**

**)**

- **Contributionsbyindividuals**


**Description:**  The **contributions by individuals** relation contains information for contributions given by individuals.

**Attributes & Datatyes:** 

|**Column Name**|**Column Type**|<p>**Can be**</p><p>**Null**</p>|**Default**|**Description**|
| :- | :- | :- | :- | :- |
|**CMTE\_ID**|**Varchar(9)**|**No**||A 9-character alpha-numeric code assigned to a committee by the Federal Election Commission|
|**AMNDT\_IND**|**Varchar(1)**|**Yes**||Indicates if the report being filed is new (N), an amendment (A) to a previous report or a termination (T) report.|
|**RPT\_TP**|**Varchar(3)**|**Yes**||Indicates the type of report filed |
|**TRANSACTION\_PGI**|**Varchar(5)**|**Yes**||This code indicates the election for which the contribution was made. |
|**IMAGE\_NUM**|**Varchar(18)**|**Yes**||18-digit Image Number Format|
|**TRANSACTION\_TP**|**Varchar(3)**|**Yes**||Transaction Type|
|**ENTITY\_TP**|**Varchar(3)**|**Yes**||Entity Type|
|**CONTRIBUTOR\_ID**|**Varchar(9)**|**Yes**||Contributor Id|
|**NAME**|**Varchar(200)**|**Yes**||Contributor/Lender/Trader Name|
|**CITY**|**Varchar(30)**|**Yes**||City|
|**STATE**|**Varchar(2)**|**Yes**||State|
|**ZIP\_CODE**|**Varchar(9)**|**Yes**||Zip Code|
|**EMPLOYER**|**VARCHAR(38)**|**Yes**||Employer|
|**OCCUPATION**|**Varchar(38)**|**Yes**||Occupation|
|**TRANSACTION\_DT**|**Date**|**Yes**||Transaction. Date|
|**TRANSACTION\_AMT**|**Numeric (14,2)**|**Yes**||Transaction Amount|
|**OTHER\_ID**|**Varchar(9)**|**Yes**||For contributions from candidates or other committees this column will contain that contributor's FEC ID.|
|**TRAN\_ID**|**Varchar(32)**|**Yes**||Transaction ID|
|**FILE\_NUM**|**Numeric(22)**|**Yes**||Unique report id|
|**MEMO\_CD**|**Varchar(1)**|**Yes**||Memo code|
|**MEMO\_TEXT**|**Varchar(100)**|**Yes**||A description of the activity. Memo Text is available on itemized amounts on Schedules A and B.|
|**SUB\_ID**|**Numeric(19)**|**No**||FEC record number|

**Primary Key: (SUB\_ID)** In the case of the contributionbyindividuals table, the SUB\_ID is the primary key as it uniquely identifies each contribution made by the individuals. Moreover, it is a unique identifier assigned by the Federal Election Commission (FEC) to record the individual’s contributions to committees.

**Foreign Key: (CMTE\_ID)** The committee’s identification number is used to link the contributions made to the committees

**Schema:** 

`	`**CREATE TABLE contributionsbyindividuals (**

`    `**CMTE\_ID character varying(9) NOT NULL,**

`    `**AMNDT\_IND character varying(1),**

`    `**RPT\_TP character varying(3),**

`    `**TRANSACTION\_PGI character varying(5),**

`    `**IMAGE\_NUM character varying(18),**

`    `**TRANSACTION\_TP character varying(3),**

`    `**ENTITY\_TP character varying(3),**

`    `**CONTRIBUTOR\_ID character varying(9),**

`    `**NAME character varying(200),**

`    `**CITY character varying(2),**

`    `**STATE character varying(2),**

`    `**ZIP\_CODE character varying(9),**

`    `**EMPLOYER character varying(38),**

`    `**OCCUPATION character varying(38),**

`    `**TRANSACTION\_DT date,**

`    `**TRANSACTION\_AMT numeric(14,2),**

`    `**OTHER\_ID character varying(9),**

`    `**TRAN\_ID character varying(32),**

`    `**FILE\_NUM numeric(22,0),**

`    `**MEMO\_CD character varying(1),**

`    `**MEMO\_TEXT character varying(100),**
**
`    		    `**SUB\_ID numeric(19,0) NOT NULL PRIMARY KEY,**

`   		    `**FOREIGN KEY (CMTE\_ID) REFERENCES Committee (CMTE\_ID)**

**)**

- **anytransactionfromcommitteetoanother**

**Description:** This relation contains each contribution or independent expenditure that one committee gives to another during the two-year election cycle, including PACs, Party committees, Candidate committees or other federal committees

**Attributes & Datatyes:** 

|**Column Name**|**Column Type**|<p>**Can be**</p><p>**Null**</p>|**Default**|**Description**|
| :- | :- | :- | :- | :- |
|**CMTE\_ID**|**Varchar(9)**|**No**||A 9-character alpha-numeric code assigned to a committee by the Federal Election Commission|
|**AMNDT\_IND**|**Varchar(1)**|**Yes**||Indicates if the report being filed is new (N), an amendment (A) to a previous report or a termination (T) report.|
|**RPT\_TP**|**Varchar(3)**|**Yes**||Indicates the type of report filed |
|**TRANSACTION\_PGI**|**Varchar(5)**|**Yes**||This code indicates the election for which the contribution was made. |
|**IMAGE\_NUM**|**Varchar(18)**|**Yes**||18-digit Image Number Format|
|**TRANSACTION\_TP**|**Varchar(3)**|**Yes**||Transaction Type|
|**ENTITY\_TP**|**Varchar(3)**|**Yes**||Entity Type|
|**CONTRIBUTOR\_ID**|**Varchar(3)**|**Yes**||Contributor Id|
|**NAME**|**Varchar(200)**|**Yes**||Contributor/Lender/Trader Name|
|**CITY**|**Varchar(30)**|**Yes**||City|
|**STATE**|**Varchar(2)**|**Yes**||State|
|**ZIP\_CODE**|**Varchar(9)**|**Yes**||Zip Code|
|**EMPLOYER**|**VARCHAR(38)**|**Yes**||Employer|
|**OCCUPATION**|**Varchar(38)**|**Yes**||Occupation|
|**TRANSACTION\_DT**|**Date**|**Yes**||Transaction. Date|
|**TRANSACTION\_AMT**|**Numeric (14,2)**|**Yes**||Transaction Amount|
|**OTHER\_ID**|**Varchar(9)**|**Yes**||For contributions from candidates or other committees this column will contain that contributor's FEC ID.|
|**TRAN\_ID**|**Varchar(32)**|**Yes**||Transaction ID|
|**FILE\_NUM**|**Numeric(22)**|**Yes**||Unique report id|
|**MEMO\_CD**|**Varchar(1)**|**Yes**||Memo code|
|**MEMO\_TEXT**|**Varchar(100)**|**Yes**||A description of the activity. Memo Text is available on itemized amounts on Schedules A and B.|
|**SUB\_ID**|**Numeric(19)**|**No**||FEC record number|


**Primary Key: : (SUB\_ID)** In the case of the anytransactionfromonecommitteetoanother table, the SUB\_ID is the primary key as it uniquely identifies each contribution made by the individuals. Moreover, it is a unique identifier assigned by the Federal Election Commission (FEC) to record the contributions to committees.

**Foreign Key: (CMTE\_ID)** The committee’s identification number is used to link the contributions made from one committee to another committee

**Schema:** 

`	`**CREATE TABLE anytransactionfromonecommitteetoanother (**

`    `**CMTE\_ID character varying(9) NOT NULL,**

`    `**AMNDT\_IND character varying(1),**

`    `**RPT\_TP character varying(3),**

`    `**TRANSACTION\_PGI character varying(5),**

`    `**IMAGE\_NUM character varying(18),**

`    `**TRANSACTION\_TP character varying(3),**

`    `**ENTITY\_TP character varying(3),**

`    `**CONTRIBUTOR\_ID character varying(9),**

`    `**NAME character varying(200),**

`    `**CITY character varying(2),**

`    `**STATE character varying(2),**

`    `**ZIP\_CODE character varying(9),**

`    `**EMPLOYER character varying(38),**

`    `**OCCUPATION character varying(38),**

`    `**TRANSACTION\_DT date,**

`    `**TRANSACTION\_AMT numeric(14,2),**

`    `**OTHER\_ID character varying(9),**

`    `**TRAN\_ID character varying(32),**

`    `**FILE\_NUM numeric(22,0),**

`    `**MEMO\_CD character varying(1),**

`    `**MEMO\_TEXT character varying(100),**
**
`    		    `**SUB\_ID numeric(19,0) NOT NULL PRIMARY KEY,**

`		    `**FOREIGN KEY (CMTE\_ID) REFERENCES Committee (CMTE\_ID)** 

**)**

- **currentcampaignforhouseandsenate**


**Description:** The **current campaigns for House and Senate** relation contains summary financial information for each campaign committee. The relation has one record per House and Senate campaign committee and shows information about the candidate, total receipts, transfers received from authorized committees, total disbursements, transfers given to authorized committees, cash-on-hand totals, loans and debts, and other financial summary information.

**Attributes & Datatyes:**

|**Column Name**|**Column Type**|<p>**Can be**</p><p>**Null**</p>|**Default**|**Description**|
| :- | :- | :- | :- | :- |
|**CAND\_ID**|**Varchar(9)**|**No**||Chandidate identication|
|**CAND\_NAME**|**Varchar(200)**|**Yes**||Candidate name|
|**CAND\_ICI**|**Varchar(1)**|**Yes**||Incumbent challenger status|
|**PTY\_CD**|**Varchar(1)**|**Yes**||Party code|
|**CAND\_PTY\_AFFILIATION**|**Varchar(3)**|**Yes**||Party affiliation|
|**TTL\_RECEIPTS**|**Numeric(14,2)**|**Yes**||Total receipts|
|**TRANS\_FROM\_AUTH**|**Numeric(14,2)**|**Yes**||Transfers from authorized committees|
|**TTL\_DISB**|**Numeric(14,2)**|**Yes**||Total disbursements|
|**TRANS\_TO\_AUTH**|**Numeric(14,2)**|**Yes**||Transfers to authorized committees|
|**COH\_BOP**|**Numeric(14,2)**|**Yes**||Beginning cash|
|**COH\_COP**|**Numeric(14,2)**|**Yes**||Ending cash|
|**CAND\_CONTRIB**|**Numeric(14,2)**|**Yes**||Contributions from candidate|
|**CAND\_LOANS**|**Numeric(14,2)**|**Yes**||Loans from candidates|
|**OTHER\_LOANS**|**Numeric(14,2)**|**Yes**||Other loans|
|**CAND\_LOAN\_REPAY**|**Numeric(14,2)**|**Yes**||Candidate loan repayments|
|**OTHER\_LOAN\_REPAY**|**Numeric(14,2)**|**Yes**||Other loan repayments|
|**DEBTS\_OWED\_BY**|**Numeric(14,2)**|**Yes**||Debts owed by|
|**TTL\_INDIV\_CONTRIB**|**Numeric(14,2)**|**Yes**||Total individuals contributions|
|**CAND\_OFFICE\_ST**|**Varchar(2)**|**Yes**||Candidate state|
|**CAND\_OFFICE\_DISTRICT**|**Varchar(2)**|**Yes**||Candidate district|
|**SPEC\_ELECTION**|**Varchar(1)**|**Yes**||Special election status|
|**PRIM\_ELECTION**|**Varchar(1)**|**Yes**||Primary election status|
|**RUN\_ELECTION**|**Varchar(1)**|**Yes**||Runoff election status|
|**GEN\_ELECTION**|**Varchar(1)**|**Yes**||General election status|
|**GEN\_ELECTION\_PRECENT**|**Numeric(7,4)**|**Yes**||General election percentage|
|**OTHER\_POL\_CMTE\_CONTRIB**|**Numeric(14,2)**|**Yes**||Contributions from other political committees|
|**POL\_PTY\_CONTRIB**|**Numeric(14,2)**|**Yes**||Contributions from party committees|
|**CVG\_END\_DT**|**Date**|**Yes**||Coverage and date|
|**INDIV\_REFUNDS**|**Numeric(14,2)**|**Yes**||Refunds to individuals|
|**CMTE\_REFUNDS**|**Numeric(14,2)**|**Yes**||Refunds to committee|


**Primary Key: (CAND\_ID)** This table contains one record which contains information about the candidate, total receipts, total disbursements and other details per house and senate campaign committee. So, here candidate id uniquely identifies each record in the relation.

**Foreign Key: (CAND\_ID)** The candidate’s identification number is used to link the current-campaign-for-house-and-senate with the candidate and it’s committee.

**Schema:**

`	`**CREATE TABLE currentcampaignforhouseandsenate (**

`    `**CAND\_ID character varying(9) NOT NULL PRIMARY KEY,**

`    `**CAND\_NAME character varying(200),**

`    `**CAND\_ICI character varying(1),**

`    `**PTY\_CD character varying(1),**

`    `**CAND\_PTY\_AFFILIATION character varying(3),**

`    `**TTL\_RECEIPTS numeric(14,2),**

`    `**TRANS\_FROM\_AUTH numeric(14,2),**

`    `**TTL\_DISB numeric(14,2),**

`    `**TRANS\_TO\_AUTH numeric(14,2),**

`    `**COH\_BOP numeric(14,2),**

`    `**COH\_COP numeric(14,2),**

`    `**CAND\_CONTRIB numeric(14,2),**

`    `**CAND\_LOANS numeric(14,2),**

`    `**OTHER\_LOANS numeric(14,2),**

`    `**CAND\_LOAN\_REPAY numeric(14,2),**

`    `**OTHER\_LOAN\_REPAY numeric(14,2),**

`    `**DEBTS\_OWED\_BY numeric(14,2),**

`    `**TTL\_INDIV\_CONTRIB numeric(14,2),**

`     `**CAND\_OFFICE\_ST character varying(2),**

`     `**CAND\_OFFICE\_DISTRICT character varying(2),**

`     `**SPEC\_ELECTION character varying(1),**

`    `**PRIM\_ELECTION character varying(1),**

`    `**RUN\_ELECTION character varying(1),**

`    `**GEN\_ELECTION character varying(1),**

`    `**GEN\_ELECTION\_PRECENT numeric(7,4),**

`    `**OTHER\_POL\_CMTE\_CONTRIB numeric(14,2),**

`    `**POL\_PTY\_CONTRIB numeric(14,2),**

`    `**CVG\_END\_DT date,**

`    `**INDIV\_REFUNDS numeric(14,2),**

`    `**CMTE\_REFUNDS numeric(14,2),**

`    `**FOREIGN KEY (CAND\_ID) REFERENCES Candidate (CAND\_ID)**

**)**

- ` `**independentexpenditures**

**Description:** This table contains each contribution or independent expenditure made by a:

- PAC
- Party committee
- Candidate committee
- Other federal committee

**Attributes and Datatypes:**

|**Column name**|**Can be Null**|**Data type**|**Default**|**Description**|
| :- | :- | :- | :- | :- |
|CMTE\_ID|N|VARCHAR2 (9)||A 9-character alpha-numeric code assigned to a committee by the Federal Election Commission|
|AMNDT\_IND|Y|VARCHAR2 (1)||Indicates if the report being filed is new (N), an amendment (A) to a previous report or a termination (T) report.|
|RPT\_TP|Y|VARCHAR2 (3)||Indicates the type of report filed. [List of report type codes](https://www.fec.gov/campaign-finance-data/report-type-code-descriptions)|
|TRANSACTION\_PGI|Y|VARCHAR2 (5)||This code indicates the election for which the contribution was made. EYYYY (election Primary, General, Other plus election year)|
|IMAGE\_NUM|Y|VARCHAR2 (11)<br>or VARCHAR2(18)||11-digit image number format<br>YYOORRRFFFF<br>YY - scanning year<br>OO - office (01 - House, 02 - Senate, 03 - FEC Paper, 90-99 - FEC Electronic)<br>RRR - reel number<br>FFFF- frame number<br><br>18-digit image number normat (June 29, 2015)<br>YYYYMMDDSSPPPPPPPP<br>YYYY - scanning year<br>MM - scanning month<br>DD - scanning day<br>SS - source (02 - Senate, 03 - FEC Paper, 90-99 - FEC Electronic)<br>PPPPPPPP - page (reset to zero every year on January 1)|
|TRANSACTION\_TP|Y|VARCHAR2 (3)||Transaction types 10J, 11J, 13, 15J, 15Z, 16C, 16F, 16G, 16R, 17R, 17Z, 18G, 18J, 18K, 18U, 19J, 20, 20C, 20F, 20G, 20R, 22H, 22Z, 23Y, 24A, 24C, 24E, 24F, 24G, 24H, 24K, 24N, 24P, 24R, 24U, 24Z and 29 are included in the OTH file. Beginning with 2016 transaction types 30F, 30G, 30J, 30K, 31F, 31G, 31J, 31K, 32F, 32G, 32J, 32K, 40, 40Z, 41, 41Z, 42 and 42Z are also included in the OTH file.<br>For more information about transaction type codes see this [list of transaction type codes](https://www.fec.gov/campaign-finance-data/transaction-type-code-descriptions)|
|ENTITY\_TP|Y|VARCHAR2 (3)||ONLY VALID FOR ELECTRONIC FILINGS received after April 2002. CAN = Candidate<br>CCM = Candidate Committee<br>COM = Committee<br>IND = Individual (a person)<br>ORG = Organization (not a committee and not a person)<br>PAC = Political Action Committee<br>PTY = Party Organization|
|CONTRIBTOR\_ID|Y|VARCHAR2 (9)||Contributor Id|
|NAME|Y|VARCHAR2 (200)||Name|
|CITY|Y|VARCHAR2 (30)||City|
|STATE|Y|VARCHAR2 (2)||State as a part of address|
|ZIP\_CODE|Y|VARCHAR2 (9)||ZIP\_code as a part of address|
|EMPLOYER|Y|VARCHAR2 (38)||Employer details|
|OCCUPATION|Y|VARCHAR2 (38)||Occupation details|
|TRANSACTION\_DT|Y|DATE||Date on which transaction happened|
|TRANSACTION\_AMT|Y|<p>NUMERIC(14,2)</p><p></p>||Amount of transaction|
|OTHER\_ID|Y|VARCHAR2 (9)||For contributions from individuals this column is null. For contributions from candidates or other committees this column will contain that contributor's FEC ID.|
|CAND\_ID|Y|VARCHAR2 (9)||A 9-character alpha-numeric code assigned to a candidate by the Federal Election Commission. The candidate ID for a specific candidate remains the same across election cycles as long as the candidate is running for the same office.|
|TRAN\_ID|Y|VARCHAR2 (32)||ONLY VALID FOR ELECTRONIC FILINGS. A unique identifier associated with each itemization or transaction appearing in an FEC electronic file. A transaction ID is unique for a specific committee for a specific report. In other words, if committee, C1, files a Q3 New with transaction SA123 and then files 3 amendments to the Q3 transaction SA123 will be identified by transaction ID SA123 in all 4 filings.|
|FILE\_NUM|Y|<p>NUMERIC(14,2)</p><p></p>||Unique report id|
|MEMO\_CD|Y|VARCHAR2 (1)||'X' indicates that the amount is NOT to be included in the itemization total.|
|MEMO\_TEXT|Y|VARCHAR2 (100)||A description of the activity. Memo text is available on itemized amounts on Schedules A and B. These transactions are included in the itemization total.|
|SUB\_ID|N|<p>NUMERIC(14,2)</p><p></p>||Unique row ID|

**Primary Key: : (SUB\_ID)** In the case of the independentexpenditures table, the SUB\_ID is the primary key as it uniquely identifies each expenditure made by the individuals. Moreover, it is a unique identifier assigned by the Federal Election Commission (FEC) to record these expenditures.

**Foreign Key: (CMTE\_ID)** The committee’s identification number is used to link the other tables.

**Schema:**

**create table independentexpenditures(**

**CMTE\_ID varchar(50),**

**AMNDT\_IND varchar(10),**

**RPT\_TP varchar(255),**

**TRANSACTION\_PGI varchar(255),**

**TRANSACTION\_TP varchar(255),**

**ENTITY\_TP varchar(255),**

**CONTRIBUTOR\_ID varchar(9)**

**NAME varchar(255),**

**CITY varchar(255),**

**STATE varchar(255),**

**ZIP\_CODE varchar(100),**

**EMPLOYER varchar(100),**

**OCCUPATION varchar(100),**

**TRANSACTION\_DT varchar(100),**

**TRANSACTION\_AMT NUMERIC(255),**

**OTHER\_ID NUMERIC(10),**

**TRAN\_ID NUMERIC(10),**

**MEMO\_CD varchar(50),**

**SUB\_ID NUMERIC(50)) NOT NULL primary key,**

`                          `FOREIGN KEY(CMTE\_ID) REFERENCES COMMITTEE (CMTE\_ID)

**);**

- **operatingexpenditures**

**Description:**

The file contains information about the committee making the disbursement, the report 	where the operating expenditure is disclosed, the entity receiving the disbursement, the 	disbursement’s date, amount, purpose, and additional information about the operating 	expenditure (if provided).The end-of-line (EOL) marker is line feed '\n' (LF, 0x0A, 10 in 	decimal).

`      `**Attributes and Datatypes:**

|**Column name**|**Can be Null**|**Data type**|**Default**|**Description**|
| :- | :- | :- | :- | :- |
|CMTE\_ID|N|VARCHAR2 (9)||Identification number of committee filing report. A 9-character alpha-numeric code assigned to a committee by the Federal Election Commission|
|AMNDT\_IND|Y|VARCHAR2 (1)||Indicates if the report being filed is new (N), an amendment (A) to a previous report, or a termination (T) report.|
|RPT\_YR|Y|<p>NUMERIC(14,2)</p><p></p>|||
|RPT\_TP|Y|VARCHAR2 (3)||Indicates the type of report filed. [List of report type codes](https://www.fec.gov/campaign-finance-data/fec-committee-type-codes)|
|IMAGE\_NUM|Y|VARCHAR2 (11) or VARCHAR2(18)||11-digit Image Number Format<br>YYOORRRFFFF<br>YY - scanning year<br>OO - office (01 - House, 02 - Senate, 03 - FEC Paper, 90-99 - FEC Electronic)<br>RRR - reel number<br>FFFF- frame number<br><br>18-digit Image Number Format (June 29, 2015)<br>YYYYMMDDSSPPPPPPPP<br>YYYY - scanning year<br>MM - scanning month<br>DD - scanning day<br>SS - source (02 - Senate, 03 - FEC Paper, 90-99 - FEC Electronic)<br>PPPPPPPP - page (reset to zero every year on January 1)|
|LINE\_NUM|Y|<p>NUMERIC(14,2)</p><p></p>||Indicates FEC form line number|
|FORM\_TP\_CD|Y|VARCHAR2 (8)||Indicates FEC Form|
|SCHED\_TP\_CD|Y|VARCHAR2 (8)||Schedule B - Itemized disbursements|
|CONTRIBUTOR\_ID|Y|<p>VARCHAR2</p><p>(9)</p>||Contributor Id|
|NAME|Y|VARCHAR2 (200)||` `Name|
|CITY|Y|VARCHAR2 (30)||` `City as a part of address|
|STATE|Y|VARCHAR2 (2)||` `State as a part of address|
|ZIP\_CODE|Y|VARCHAR2 (9)||Zip code as a part of address|
|TRANSACTION\_DT|Y|DATE||<p>` `Date on which transaction was performed.</p><p></p>|
|TRANSACTION\_AMT|Y|<p>` `NUMERIC(14,2)</p><p></p>||` `Amount of transaction|
|TRANSACTION\_PGI|Y|VARCHAR2 (5)|| |
|PURPOSE|Y|VARCHAR2 (100)||` `Purpose of transaction|
|CATEGORY|Y|VARCHAR2 (3)||001-012 and 101-107|
|CATEGORY\_DESC|Y|VARCHAR2 (40)||List of [Disbursement Category Codes](https://www.fec.gov/campaign-finance-data/disbursement-category-code-descriptions) and their meaning|
|MEMO\_CD|Y|VARCHAR2 (1)||'X' indicates that the amount is NOT to be included in the itemization total.|
|MEMO\_TEXT|Y|VARCHAR2 (100)||A description of the activity. Memo Text is available on itemized amounts on Schedule B. These transactions are included in the itemization total.|
|ENTITY\_TP|Y|VARCHAR2 (3)||ONLY VALID FOR ELECTRONIC FILINGS received after April 2002. CAN = Candidate<br>CCM = Candidate committee<br>COM = Committee<br>IND = Individual (a person)<br>ORG = Organization (not a committee and not a person)<br>PAC = Political action committee<br>PTY = Party organization|
|SUB\_ID|N|<p>NUMERIC(14,2)</p><p></p>||Unique row ID|
|FILE\_NUM|Y|<p>NUMERIC(14,2)</p><p></p>||Unique report id|
|TRAN\_ID||VARCHAR2 (32)||ONLY VALID FOR ELECTRONIC FILINGS. A unique identifier associated with each itemization or transaction appearing in an FEC electronic file. A transaction ID is unique for a specific committee for a specific report. In other words, if committee, C1, files a Q3 New with transaction SA123 and then files 3 amendments to the Q3 transaction SA123 will be identified by transaction ID SA123 in all 4 filings.|
|BACK\_REF\_TRAN\_ID|Y|VARCHAR2 (32)||ONLY VALID FOR ELECTRONIC FILINGS. Used to associate one transaction with another transaction in the same report (using file number, transaction ID and back reference transaction ID). For example, a credit card payment and the subitemization of specific purchases. The back reference transaction ID of the specific purchases will equal the transaction ID of the payment to the credit card company.|

**Primary Key:  (SUB\_ID)** In the case of the operating expenditures table, the SUB\_ID is the primary key as it uniquely identifies each expenditure made by the committee. Moreover, it is a unique identifier assigned by the Federal Election Commission (FEC) to record the expenditures of the committees.

**Foreign Key: (CMTE\_ID)** The committee’s identification number is used to link the expenditures made from one committee to another committee.

**Table Schema:**

**create table operatingexpenditures(** 

**CMTE\_ID varchar(50) ,**

**AMNDT\_IND varchar(10),**

**RTP\_YR NUMERIC(10),**

**RPT\_TP varchar(255),**

**LINE\_NUM NUMERIC(100),**

**SCHED\_TP\_CD NUMERIC(10),**

**CONTRIBUTOR\_ID varchar(9),**

**NAME  varchar(255),**

**CITY varchar(255),**

**STATE varchar(255),**

**ZIP\_CODE varchar(100),**

**TRANSACTION\_DT varchar(100),** 

**TRANSACTION\_AMT varchar(100),** 

**TRANSACTION\_PGI varchar(100),** 

**PURPOSE varchar(100),**

**CATEGORY varchar(100),**

**CATEGORY\_DESC varchar(100),**

**MEMO\_CD varchar(100),**

**MEMO\_TEXT varchar(100),**

**ENTITY\_TP varchar(100),**

**SUB\_ID varchar(100) NOT NULL primary key,** 

**FILE\_NUM varchar(100),** 

**TRAN\_ID varchar(100),**  

**BACK\_REF\_TRAN\_ID varchar(100),** 

**FOREIGN KEY(CMTE\_ID) REFERENCES COMMITTEE (CMTE\_ID),**

**FOREIGN KEY (CONTRIBUTOR\_ID) REFERENCES contributor (CONTRIBUTOR\_ID)**

**);**

- **pacandpartysummary**

**Description:**

The file has one record per PAC and Party committee and shows information about the 	committee, total receipts and disbursements, receipts and disbursements broken down 	by type, contributions to other committees, independent expenditures made by the 	committee, and other financial summary information. The end-of-line (EOL) marker is 	line feed '\n' (LF, 0x0A, 10 in decimal).

**Attributes and Datatypes:**

|**Column name**|**Null**|**Data type**|**Default**|**Description**|
| :- | :- | :- | :- | :- |
|CMTE\_ID|N|VARCHAR2 (9)||ID of the committee|
|CMTE\_NM|Y|VARCHAR2 (200)||Committee Name|
|CMTE\_TP|Y|VARCHAR2 (1)|||
|CMTE\_DSGN|Y|VARCHAR2 (1)|||
|CMTE\_FILING\_FREQ|Y|VARCHAR2 (1)|||
|TTL\_RECEIPTS|Y|NUMERIC(14,2)|||
|TRANS\_FROM\_AFF|Y|<p>NUMERIC(14,2)</p><p></p>|||
|INDV\_CONTRIB|Y|<p>NUMERIC(14,2)</p><p></p>|||
|OTHER\_POL\_CMTE\_CONTRIB|Y|<p>NUMERIC(14,2)</p><p></p>|||
|CAND\_CONTRIB|Y|<p>NUMERIC(14,2)</p><p></p>||Not applicable|
|CAND\_LOANS|Y|<p>NUMERIC(14,2)</p><p></p>||Not applicable|
|TTL\_LOANS\_RECEIVED|Y|<p>NUMERIC(14,2)</p><p></p>|||
|TTL\_DISB|Y|<p>NUMERIC(14,2)</p><p></p>|||
|TRANF\_TO\_AFF|Y|<p>NUMERIC(14,2)</p><p></p>|||
|INDV\_REFUNDS|Y|<p>NUMERIC(14,2)</p><p></p>|||
|OTHER\_POL\_CMTE\_REFUNDS|Y|<p>NUMERIC(14,2)</p><p></p>|||
|CAND\_LOAN\_REPAY|Y|<p>NUMERIC(14,2)</p><p></p>||Not applicable|
|LOAN\_REPAY|Y|<p>NUMERIC(14,2)</p><p></p>|||
|COH\_BOP|Y|<p>NUMERIC(14,2)</p><p></p>|||
|COH\_COP|Y|<p>NUMERIC(14,2)</p><p></p>|||
|DEBTS\_OWED\_BY|Y|<p>NUMERIC(14,2)</p><p></p>|||
|NONFED\_TRANS\_RECEIVED|Y|<p>NUMERIC(14,2)</p><p></p>|||
|CONTRIB\_TO\_OTHER\_CMTE|Y|<p>NUMERIC(14,2)</p><p></p>|||
|IND\_EXP|Y|<p>NUMERIC(14,2)</p><p></p>|||
|PTY\_COORD\_EXP|Y|<p>NUMERIC(14,2)</p><p></p>|||
|NONFED\_SHARE\_EXP|Y|<p>NUMERIC(14,2)</p><p></p>|||
|CVG\_END\_DT|Y|DATE(MM/DD/YYYY)||Through date|

**Primary Key: (CMTE\_ID)** In the case of the pacandpartysummary table, the CMTE\_ID is the primary key as it uniquely identifies each summary related to a committee. Moreover, it is a unique identifier assigned by the Federal Election Commission (FEC) to record the summary of these transactions.

Table Schema:

**create table pacandpartysummary(**

**CMTE\_ID varchar(9)  NOT NULL primary key,**

**CMTE\_NM varchar(200),**

**CMTE\_TP varchar(1),**

**CMTE\_DSGN varchar(1),**

**CMTE\_FILING\_FREQ varchar(1),**

**TTL\_RECEIPTS NUMERIC(14,2),**

**TRANS\_FROM\_AFF NUMERIC(14,2),**

**INDV\_CONTRIB NUMERIC(14,2),**

**OTHER\_POL\_CMTE\_CONTRIB NUMERIC(14,2),**

**CAND\_CONTRIB NUMERIC(14,2),**

**CAND\_LOANS NUMERIC(14,2),**

**TTL\_LOANS\_RECEIVED NUMERIC(14,2),**

**TTL\_DISB NUMERIC(14,2),**

**TRANF\_TO\_AFF NUMERIC(14,2),**

**INDV\_REFUNDS NUMERIC(14,2),**

**OTHER\_POL\_CMTE\_REFUNDS NUMERIC(14,2),**

**CAND\_LOAN\_REPAY NUMERIC(14,2),**

**LOAN\_REPAY NUMERIC(14,2),**

**COH\_BOP NUMERIC(14,2),**

**COH\_COP NUMERIC(14,2),**

**DEBTS\_OWED\_BY NUMERIC(14,2),**

**NONFED\_TRANS\_RECEIVED NUMERIC(14,2),**

**CONTRIB\_TO\_OTHER\_CMTE NUMERIC(14,2),**

**IND\_EXP NUMERIC(14,2),**

**PTY\_COORD\_EXP NUMERIC(14,2),**

**NONFED\_SHARE\_EXP NUMERIC(14,2),**

**CVG\_END\_DT DATE,** 

**FOREIGN KEY(CMTE\_ID) REFERENCES COMMITTEE (CMTE\_ID)** 

**);**

**Note on Foreign keys:** When the primary key (that the foreign key refer to) is deleted, the record with that foreign key is deleted (Cascade delete) 

**Database SQL Statements:**

**CREATE DATABASE federalelectioncommission;**

**DROP DATABASE federalelectioncommission;**

**Loading into Database:**

Data for this dataset is present on federal election commission website in form of text files where each line is row separated by comma delimiter.  We have written python script to load the data from these text files. Below snippet shows the code which connects to a PostgreSQL database and inserts data from text files into different tables in the database.

![](images/Aspose.Words.6ec778c9-0139-44bc-878e-428ad5bf2b92.002.png)

**Insert statement for candidate:** 

INSERT INTO candidate (CAND\_ID, CAND\_NAME, CAND\_PTY\_AFFILIATION, CAND\_ELECTION\_YR, CAND\_OFFICE\_ST, CAND\_OFFICE, CAND\_OFFICE\_DISTRICT, CAND\_ICI, CAND\_STATUS, CAND\_PCC, CAND\_ST1, CAND\_ST2, CAND\_CITY, CAND\_ST, CAND\_ZIP) VALUES ('C12345678', 'John Smith', 'REP', '2020', 'CA', 'H', '03', 'O', 'C', 'PCC123456', '123 Main Street', '', 'Los Angeles', 'CA', '90001');

**Insert statement for committee:** 

INSERT INTO committee (CMTE\_ID, CMTE\_NM, TRES\_NM, CMTE\_ST1, CMTE\_CITY, CMTE\_ST, CMTE\_ZIP, CMTE\_DSGN, CMTE\_TP, CMTE\_PTY\_AFFILIATION, CMTE\_FILING\_FREQ, ORG\_TP, CONNECTED\_ORG\_NM, CAND\_ID) VALUES 

('C00000001', 'Friends of Jane Doe', 'John Smith', '123 Main St', 'Los Angeles', 'CA', '90001', 'A', 'P', 'DEM', 'Q', 'C', 'ABC Consulting', 'C12345678'),

('C00000002', 'Republicans for John Smith', 'Jane Doe', '456 Lincoln Blvd', 'San Francisco', 'CA', '94102', 'B', 'N', 'REP', 'M', 'P', NULL, 'C98765432'),

('C00000003', 'Independent Committee to Elect Jim Brown', 'Sarah Lee', '555 Independence Ave', 'Washington', 'DC', '20001', 'A', 'O', NULL, 'Q', 'M', 'XYZ Agency', 'C00098765');

**Insert statement for candidate-committee:**

INSERT INTO candidate\_committee (CAND\_ID, CAND\_ELECTION\_YR, FEC\_ELECTION\_YR, CMTE\_ID, CMTE\_TP, CMTE\_DSGN, LINKAGE\_ID) VALUES ('C12345678', 2022, 2022, 'C00000001', 'P', 'D', 34567);

**Insert statement for contributor:**

INSERT INTO contributor (CONTRIBUTOR\_ID, NAME, CITY, STATE, ZIP\_CODE, EMPLOYER, OCCUPATION) VALUES ('123456789', 'John Smith', 'NY', 'NY', '10001', 'ABC Inc.', 'Engineer');

**Insert statement for contribution-by-individual:**

INSERT INTO contributionsbyindividuals (CMTE\_ID, AMNDT\_IND, RPT\_TP, TRANSACTION\_PGI, IMAGE\_NUM, TRANSACTION\_TP, ENTITY\_TP, CONTRIBUTOR\_ID, TRANSACTION\_DT, TRANSACTION\_AMT, OTHER\_ID, TRAN\_ID, FILE\_NUM, MEMO\_CD, MEMO\_TEXT, SUB\_ID) VALUES ('C00000001', 'N', 'Q1', 'P', '12345678910111213', '15', 'IND', '123456789', '2022-01-01', '1000.00', NULL, 'ABCDE1234-2022-01-01-1', 1234567890, 'X', 'Donation for campaign expenses', 9876543210987654321); 

**Insert statement for any-transaction-from-one-committee-to-another:** INSERT INTO anytransactionfromonecommitteetoanother (CMTE\_ID, AMNDT\_IND, RPT\_TP, TRANSACTION\_PGI,IMAGE\_NUM, TRANSACTION\_TP, ENTITY\_TP, CONTRIBUTOR\_ID,TRANSACTION\_DT, TRANSACTION\_AMT, OTHER\_ID, TRAN\_ID, FILE\_NUM, MEMO\_CD, MEMO\_TEXT, SUB\_ID) VALUES ('C00000001', 'N', 'Q1', 'P', '12345678910111213','15', 'COM', '123456789', '2022-01-01', 1000.00, NULL,'ABCDE1234-2022-01-01-1', 1234567890, 'X', 'Donation for campaign expenses', 9876543210987654321); 

**Insert statement for current-campaign-for-house-and-senate:** 

INSERT INTO currentcampaignforhouseandsenate (CAND\_ID, PTY\_CD, TTL\_RECEIPTS, TRANS\_FROM\_AUTH, TTL\_DISB, TRANS\_TO\_AUTH, COH\_BOP, COH\_COP, CAND\_CONTRIB, CAND\_LOANS, OTHER\_LOANS, CAND\_LOAN\_REPAY, OTHER\_LOAN\_REPAY, DEBTS\_OWED\_BY, TTL\_INDIV\_CONTRIB, SPEC\_ELECTION, PRIM\_ELECTION, RUN\_ELECTION, GEN\_ELECTION, GEN\_ELECTION\_PRECENT, OTHER\_POL\_CMTE\_CONTRIB, POL\_PTY\_CONTRIB, CVG\_END\_DT, INDIV\_REFUNDS, CMTE\_REFUNDS) VALUES ('C12345678', 'D', 100000.00, 5000.00, 80000.00, 6000.00, 20000.00, 18000.00, 10000.00, 5000.00, 0.00, 0.00, 0.00, 1000.00, 50000.00, 'N', 'Y', 'N','N', 0.00, 4000.00, 8000.00, '2022-11-03', 0.00, 0.00);

**Insert statement for independentexpenditures:** 

INSERT INTO independentexpenditures (CMTE\_ID, AMNDT\_IND, RPT\_TP, TRANSACTION\_PGI, TRANSACTION\_TP, ENTITY\_TP, CONTRIBUTOR\_ID, TRANSACTION\_DT, TRANSACTION\_AMT, OTHER\_ID, TRAN\_ID, MEMO\_CD, SUB\_ID) VALUES ('C00000001', 'N', 'M2', 'P', 'IE', 'ORG', '123456789', '2022-10-15', 5000.00, NULL, 987654321, NULL, 1234567890);

**Insert statement for operatingexpenditures:** 

INSERT INTO operatingexpenditures (CMTE\_ID, AMNDT\_IND, RTP\_YR, RPT\_TP, LINE\_NUM, SCHED\_TP\_CD, CONTRIBUTOR\_ID, TRANSACTION\_DT, TRANSACTION\_AMT, TRANSACTION\_PGI, PURPOSE, CATEGORY, CATEGORY\_DESC,MEMO\_CD, MEMO\_TEXT, ENTITY\_TP, SUB\_ID, FILE\_NUM, TRAN\_ID, BACK\_REF\_TRAN\_ID) VALUES ('C00000001', 'N', 2022, 'M2', 1, 1, '123456789','2022-10-15', 500.00, 'G', 'Test Purpose', 'Test Category', 'Test Category Desc', NULL, NULL, 'ORG', '1234567890', '100', '987654321', NULL);

**Insert statement for pacandpartysummary:**

INSERT INTO pacandpartysummary (CMTE\_ID, TTL\_RECEIPTS, TRANS\_FROM\_AFF, INDV\_CONTRIB, OTHER\_POL\_CMTE\_CONTRIB, CAND\_CONTRIB, CAND\_LOANS, TTL\_LOANS\_RECEIVED, TTL\_DISB, TRANF\_TO\_AFF, INDV\_REFUNDS, OTHER\_POL\_CMTE\_REFUNDS, CAND\_LOAN\_REPAY, LOAN\_REPAY, COH\_BOP, COH\_COP, DEBTS\_OWED\_BY, NONFED\_TRANS\_RECEIVED, CONTRIB\_TO\_OTHER\_CMTE, IND\_EXP, PTY\_COORD\_EXP, NONFED\_SHARE\_EXP, CVG\_END\_DT) VALUES ('C12345', 100000, 20000, 50000, 30000, 10000, 2000, 5000, 80000, 3000, 2000, 500, 1000, 200, 300000, 200000, 10000, 4000, 50000, 2000, 1000, 500, '2022-01-01');

**Normalization of the tables**

**Functional Dependencies:**

**candidates**

CAND\_ID -> CAND\_NAME, CAND\_PTY\_AFFILIATION, CAND\_ELECTION\_YR, CAND\_OFFICE\_ST, CAND\_OFFICE, CAND\_OFFICE\_DISTRICT, CAND\_ICI, CAND\_STATUS, CAND\_PCC, CAND\_ST1, CAND\_ST2, CAND\_CITY, CAND\_ST, CAND\_ZIP

**committees**

CTME\_ID -> CMTE\_NM, TRES\_NM, CMTE\_ST1, CMTE\_ST2, CMTE\_CITY, CMTE\_ST, CMTE\_ZIP, CMTE\_DSGN, CMTE\_TP, CMTE\_PTY\_AFFILIATION, CMTE\_FILING\_FREQ, ORG\_TP, CONNECTED\_ORG\_NM, CAND\_ID

**candidate\_committee**

LINKAGE\_ID -> CAND\_ID, CAND\_ELECTION\_YR, FEC\_ELECTION\_YR, CMTE\_ID, CMTE\_TP, CMTE\_DSGN

**contributor**

CONTRIBUTOR\_ID -> NAME, CITY, STATE, ZIP\_CODE, EMPLOYER, OCCUPATION

**contributionsbyindividuals**

SUB\_ID -> CMTE\_ID, AMNDT\_IND, RPT\_TP, TRANSACTION\_PGI, IMAGE\_NUM, TRANSACTION\_TP, ENTITY\_TP, CONTRIBUTOR\_ID, TRANSACTION\_DT, TRANSACTION\_AMT, OTHER\_ID, TRAN\_ID, FILE\_NUM, MEMO\_CD, MEMO\_TEXT

CONTRIBUTOR\_ID -> NAME, CITY, STATE, ZIP\_CODE, EMPLOYER, OCCUPATION

**anytransactionfromonecommitteetoanother**

SUB\_ID -> CMTE\_ID, AMNDT\_IND, RPT\_TP, TRANSACTION\_PGI, IMAGE\_NUM, TRANSACTION\_TP, ENTITY\_TP, CONTRIBUTOR\_ID, TRANSACTION\_DT, TRANSACTION\_AMT, OTHER\_ID, TRAN\_ID, FILE\_NUM, MEMO\_CD, MEMO\_TEXT

CONTRIBUTOR\_ID -> NAME, CITY, STATE, ZIP\_CODE, EMPLOYER, OCCUPATION

**Currentcampaignforhouseandsenate**

CAND\_ID -> CAND\_NAME, CAND\_ICI, PTY\_CD, CAND\_PTY\_AFFILIATION, TTL\_RECEIPTS, TRANS\_FROM\_AUTH, TTL\_DISB, TRANS\_TO\_AUTH, COH\_BOP, COH\_COP, CAND\_CONTRIB, CAND\_LOANS, OTHER\_LOANS, CAND\_LOAN\_REPAY, OTHER\_LOAN\_REPAY, DEBTS\_OWED\_BY, TTL\_INDIV\_CONTRIB, CAND\_OFFICE\_ST, CAND\_OFFICE\_DISTRICT, SPEC\_ELECTION, PREM\_ELECTION, RUN\_ELECTION, GEN\_ELECTION, GEN\_ELECTION\_PERCENT, OTHER\_POL\_CMTE\_CONTRIB, POL\_PTY\_CONTRIB, CVG\_END\_DT, INDIV\_REFUNDS, CMTE\_REFUNDS 

**Independentexpenditures**

SUB\_ID -> CMTE\_ID, AMNDT\_IND, RPT\_TP, TRANSACTION\_PGI, TRANSACTION\_TP, ENTITY\_TP, CONTRIBUTOR\_ID, TRANSACTION\_DT, TRANSACTION\_AMT, OTHER\_ID, TRAN\_ID, MEMO\_CD

CONTRIBUTOR\_ID -> NAME, CITY, STATE, ZIP\_CODE, EMPLOYER, OCCUPATION

**Operatingexpenditures**

SUB\_ID -> CMTE\_ID, AMNDT\_IND, RTP\_YR, RTP\_TP, LINE\_NUM, SCHED\_TP\_CD, CONTRIBUTOR\_ID, TRANSACTION\_DT, TRANSACTION\_AMT, TRANSACTION\_PGI, PURPOSE, CATEGORY, CATEGORY\_DESC, MEMO\_CD, MEMO\_TEXT, ENTITY\_TP, FILE\_NUM, TRAN\_ID, BACK\_REF\_TRAN\_ID 

CONTRIBUTOR\_ID -> NAME, CITY, STATE, ZIP\_CODE

**pacandpartysummary**

CMTE\_ID -> CMTE\_NM, CMTE\_TP, CMTE\_DESN, CMTE\_FILING\_FREQ, TTL\_RECEIPTS, TRANS\_FROM\_AFF, INDIV\_CONTRIB, OTHER\_POL\_CMTE\_CONTRIB, CAND\_CONTRIB, CAND\_LOANS, TTL\_LOANS\_RECEIVED, TTL\_DISB, TRANF\_TO\_AFF, INDV\_REFUNDS, OTHER\_POL\_CMTE\_REFUNDS, CAND\_LOAN\_REPAY, LOAN\_REPAY, COH\_BOP, COH\_COP, DEBTS\_OWED\_BY, NONFAD\_TRANS\_RECEIVED, CONTRIB\_TO\_OTHER\_CMTE, IND\_EXP, PTY\_COORD\_EXP, NONFED\_SHARE\_EXP, CVG\_END\_DT 

The functional dependencies of each of the tables are listed above. We observe the LHS of the functional dependencies is a super key of its relation. All the functional dependencies are also non-trivial dependencies. These conditions imply that the relations are in BCNF. But, found that the relations contain redundancy anomalies. The details of the contributor repeated in all the tables, so we ended up creating a new relation **contributors** to store these details and add the id the contributor in the respective tables.

**Indexing of the tables**

Since the dataset was large, while loading the data, we had to do modifications to the data(to fit into our tables) and also  since we decomposed the tables, we carried out data file manipulation and then we loaded it into the database. After doing these things and loading the data to the database, while performing the queries, our join operations specifically was taking lot of time for execution, therefore we added indexing for candidate and committee tables since all other tables mostly have cand\_id and cmte\_id as the foreign key. After incorporating this we could see significant improvement in the performance of the database.

**CREATE INDEX idx\_candid ON candidate (CAND\_ID);**


**CREATE INDEX idx\_comteid ON committee (cmte\_id)**



**Testing the database with SQL queries.** 

**Queries for each inserting, deleting, and updating operation in your dataset and select queries of different types of statements**

1. Candidate

![](images/Aspose.Words.6ec778c9-0139-44bc-878e-428ad5bf2b92.003.png)

![](images/Aspose.Words.6ec778c9-0139-44bc-878e-428ad5bf2b92.004.png)

![](images/Aspose.Words.6ec778c9-0139-44bc-878e-428ad5bf2b92.005.png)

![](images/Aspose.Words.6ec778c9-0139-44bc-878e-428ad5bf2b92.006.png)







2. Committe

![](images/Aspose.Words.6ec778c9-0139-44bc-878e-428ad5bf2b92.007.png)

![](images/Aspose.Words.6ec778c9-0139-44bc-878e-428ad5bf2b92.008.png)







![](images/Aspose.Words.6ec778c9-0139-44bc-878e-428ad5bf2b92.009.png)

3. Candidate\_committee

![](images/Aspose.Words.6ec778c9-0139-44bc-878e-428ad5bf2b92.010.png)





![](images/Aspose.Words.6ec778c9-0139-44bc-878e-428ad5bf2b92.011.png)

![](images/Aspose.Words.6ec778c9-0139-44bc-878e-428ad5bf2b92.012.png)

![](images/Aspose.Words.6ec778c9-0139-44bc-878e-428ad5bf2b92.013.png)

4. Contributor

![](images/Aspose.Words.6ec778c9-0139-44bc-878e-428ad5bf2b92.014.png)






![](images/Aspose.Words.6ec778c9-0139-44bc-878e-428ad5bf2b92.015.png)

5. Contributionbyindividuals

![](images/Aspose.Words.6ec778c9-0139-44bc-878e-428ad5bf2b92.016.png)





![](images/Aspose.Words.6ec778c9-0139-44bc-878e-428ad5bf2b92.017.png)

6. Anytransactionfromonecommitteetoanother

![](images/Aspose.Words.6ec778c9-0139-44bc-878e-428ad5bf2b92.018.png)






![](images/Aspose.Words.6ec778c9-0139-44bc-878e-428ad5bf2b92.019.png)

7. Currentcampaignforhouseandsenate

![](images/Aspose.Words.6ec778c9-0139-44bc-878e-428ad5bf2b92.020.png)






![](images/Aspose.Words.6ec778c9-0139-44bc-878e-428ad5bf2b92.021.png)

8. Independent Expenditures

![](images/Aspose.Words.6ec778c9-0139-44bc-878e-428ad5bf2b92.022.png)

![](images/Aspose.Words.6ec778c9-0139-44bc-878e-428ad5bf2b92.023.png)

9. Operating Expenditures

![](images/Aspose.Words.6ec778c9-0139-44bc-878e-428ad5bf2b92.024.png)





![](images/Aspose.Words.6ec778c9-0139-44bc-878e-428ad5bf2b92.025.png)

10. Pacpartyandsummary

![](images/Aspose.Words.6ec778c9-0139-44bc-878e-428ad5bf2b92.026.png)

![](images/Aspose.Words.6ec778c9-0139-44bc-878e-428ad5bf2b92.027.png)

11. Joining candidate\_committee and committe

![](images/Aspose.Words.6ec778c9-0139-44bc-878e-428ad5bf2b92.028.png)






![](images/Aspose.Words.6ec778c9-0139-44bc-878e-428ad5bf2b92.029.png)

![](images/Aspose.Words.6ec778c9-0139-44bc-878e-428ad5bf2b92.030.png)





12. Join on candidate\_committee and anytransactionsfromonetoanother

![](images/Aspose.Words.2c68961b-8eb5-42d1-9c96-a925b9664449.005.png)

13. Join on contributor and independent expenditures

![](images/Aspose.Words.2c68961b-8eb5-42d1-9c96-a925b9664449.006.png)





14. Join on operating expenditures and contributor

![](images/Aspose.Words.2c68961b-8eb5-42d1-9c96-a925b9664449.007.png)

**Query execution analysis**

**Problematic queries were:**

` `**1.**

**SELECT c.CAND\_NAME, com.CMTE\_NM**

**FROM candidate c**

**JOIN candidate\_committee cc ON cc.CAND\_ID = c.CAND\_ID**

**JOIN committee com ON com.CMTE\_ID = cc.CMTE\_ID**

**WHERE cc.CAND\_ELECTION\_YR = 2020**

**GROUP BY c.CAND\_NAME, com.CMTE\_NM**

**ORDER BY c.CAND\_NAME ASC, com.CMTE\_NM ASC;**

![](images/Aspose.Words.2c68961b-8eb5-42d1-9c96-a925b9664449.008.png)

Based on the execution plan,  it seems that the most expensive operation in the query is the sequential scan of the "committee" table, which has a cost of 24.29.

To improve the performance of the query, we can consider creating an index on the "CMTE\_ID" column of the "committee" table, which is used in the join condition with the "candidate\_committee" table. This will allow for faster retrieval of the relevant rows from the "committee" table.

CREATE INDEX committee\_cmte\_id\_idx ON committee (CMTE\_ID);

**2.**

**SELECT \***

**FROM operatingexpenditures**

**LEFT JOIN contributor**

**ON operatingexpenditures.CONTRIBUTOR\_ID = contributor.CONTRIBUTOR\_ID;**

![Graphical user interface, text, application, email

Description automatically generated](images/Aspose.Words.2c68961b-8eb5-42d1-9c96-a925b9664449.009.png)

Based on the execution pla, it appears that the problematic query involves a left join between the **operatingexpenditures** and **contributor** tables on their respective **contributor\_id** columns. The left join operation can be expensive and can consume a lot of resources, especially if the tables are large.

To optimize this query, consider the following options:

1. Add an index to the **contributor\_id** column on both tables to speed up the join operation. This can significantly reduce the amount of time required to perform the join by allowing the database to quickly locate matching rows.
2. Rewrite the query to use a more efficient join algorithm. For example, a nested loop join may be more efficient than a hash join or a merge join for small tables.
3. Use a subquery or a common table expression (CTE) to filter the rows before joining. This can reduce the size of the result set and improve the efficiency of the join operation.

**3.**

**SELECT \***

**FROM committee** 

**FULL OUTER JOIN candidate\_committee** 

**ON committee.CMTE\_ID = candidate\_committee.CMTE\_ID;**

![Graphical user interface, text, application

Description automatically generated](images/Aspose.Words.2c68961b-8eb5-42d1-9c96-a925b9664449.010.png)

Based on the execution plan, it appears that the problematic query involves a full join between the **candidate\_committee** and **committee** tables on their respective **cmte\_id** columns. The full join operation can be expensive and can consume a lot of resources, especially if the tables are large.

To optimize this query, consider the following options:

1. Add an index to the **cmte\_id** column on both tables to speed up the join operation. This can significantly reduce the amount of time required to perform the join by allowing the database to quickly locate matching rows.
2. Rewrite the query to use a more efficient join algorithm. For example, a nested loop join may be more efficient than a hash join or a merge join for small tables.
3. Use a subquery or a common table expression (CTE) to filter the rows before joining. This can reduce the size of the result set and improve the efficiency of the join operation.









