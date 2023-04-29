DROP SCHEMA IF EXISTS public CASCADE;

CREATE SCHEMA public;
	
DROP TABLE IF EXISTS candidate_committee;
DROP TABLE IF EXISTS committee;
DROP TABLE IF EXISTS candidate;
DROP TABLE IF EXISTS contributor;
DROP TABLE IF EXISTS contributionsbyindividuals;
DROP TABLE IF EXISTS anytransactionfromonecommitteetoanother;
DROP TABLE IF EXISTS currentcampaignforhouseandsenate;
DROP TABLE IF EXISTS independentexpenditures;
DROP TABLE IF EXISTS operatingexpenditures;
DROP TABLE IF EXISTS pacandpartysummary;


CREATE TABLE candidate ( 

	CAND_ID VARCHAR(9) NOT NULL PRIMARY KEY, 

	CAND_NAME VARCHAR(200), 

	CAND_PTY_AFFILIATION VARCHAR(3), 

	CAND_ELECTION_YR NUMERIC(4), 

	CAND_OFFICE_ST VARCHAR(2), 

	CAND_OFFICE VARCHAR(1), 

	CAND_OFFICE_DISTRICT VARCHAR(2), 

	CAND_ICI VARCHAR(1), 

	CAND_STATUS VARCHAR(1), 

	CAND_PCC VARCHAR(9), 

	CAND_ST1 VARCHAR(34), 

	CAND_ST2 VARCHAR(34), 

	CAND_CITY VARCHAR(30), 

	CAND_ST VARCHAR(2), 

	CAND_ZIP VARCHAR(9) 
);

CREATE TABLE committee ( 

	CMTE_ID VARCHAR(9) NOT NULL PRIMARY KEY, 

	CMTE_NM VARCHAR(200), 

	TRES_NM VARCHAR(90), 

	CMTE_ST1 VARCHAR(34), 

	CMTE_ST2 VARCHAR(34), 

	CMTE_CITY VARCHAR(30), 

	CMTE_ST VARCHAR(2), 

	CMTE_ZIP VARCHAR(9), 

	CMTE_DSGN VARCHAR(1), 

	CMTE_TP VARCHAR(1), 

	CMTE_PTY_AFFILIATION VARCHAR(3), 

	CMTE_FILING_FREQ VARCHAR(1), 

	ORG_TP VARCHAR(1), 

	CONNECTED_ORG_NM VARCHAR(200), 

	CAND_ID VARCHAR(9) 

); 

CREATE TABLE candidate_committee ( 

	CAND_ID VARCHAR(9), 

	CAND_ELECTION_YR Numeric(4), 

	FEC_ELECTION_YR Numeric(4), 

	CMTE_ID VARCHAR(9), 

	CMTE_TP VARCHAR(1), 

	CMTE_DSGN VARCHAR(1), 

	LINKAGE_ID Numeric(12), 

	PRIMARY KEY (LINKAGE_ID), 

	UNIQUE (CAND_ID, CAND_ELECTION_YR, FEC_ELECTION_YR,CMTE_ID), 

	FOREIGN KEY (CAND_ID) REFERENCES candidate (CAND_ID), 

	FOREIGN KEY (CMTE_ID) REFERENCES committee (CMTE_ID) 
); 

CREATE TABLE contributor ( 

    CONTRIBUTOR_ID VARCHAR(9), 

    NAME VARCHAR(200), 

    CITY VARCHAR(2), 

    STATE VARCHAR(2), 

    ZIP_CODE VARCHAR(9), 

    EMPLOYER VARCHAR(38), 

    OCCUPATION VARCHAR(38),
	PRIMARY KEY (CONTRIBUTOR_ID)
);

CREATE TABLE contributionsbyindividuals ( 

    CMTE_ID VARCHAR(9) NOT NULL, 

    AMNDT_IND VARCHAR(1), 

    RPT_TP VARCHAR(3), 

    TRANSACTION_PGI VARCHAR(5), 

    IMAGE_NUM VARCHAR(18), 

    TRANSACTION_TP VARCHAR(3), 

    ENTITY_TP VARCHAR(3), 

    CONTRIBUTOR_ID VARCHAR(9), 

    TRANSACTION_DT date, 

    TRANSACTION_AMT numeric(14,2), 

    OTHER_ID VARCHAR(9), 

    TRAN_ID VARCHAR(32), 

    FILE_NUM numeric(22,0), 

    MEMO_CD VARCHAR(1), 

    MEMO_TEXT VARCHAR(100), 

    		    SUB_ID numeric(19,0) NOT NULL PRIMARY KEY, 

   		    FOREIGN KEY (CMTE_ID) REFERENCES Committee (CMTE_ID),
			 FOREIGN KEY (CONTRIBUTOR_ID) REFERENCES contributor (CONTRIBUTOR_ID)

);

CREATE TABLE anytransactionfromonecommitteetoanother ( 

    CMTE_ID VARCHAR(9) NOT NULL, 

    AMNDT_IND VARCHAR(1), 

    RPT_TP VARCHAR(3), 

    TRANSACTION_PGI VARCHAR(5), 

    IMAGE_NUM VARCHAR(18), 

    TRANSACTION_TP VARCHAR(3), 

    ENTITY_TP VARCHAR(3), 

    CONTRIBUTOR_ID VARCHAR(9), 
    TRANSACTION_DT date, 

    TRANSACTION_AMT numeric(14,2), 

    OTHER_ID VARCHAR(9), 

    TRAN_ID VARCHAR(32), 

    FILE_NUM numeric(22,0), 

    MEMO_CD VARCHAR(1), 

    MEMO_TEXT VARCHAR(100), 

    		    SUB_ID numeric(19,0) NOT NULL PRIMARY KEY, 

    FOREIGN KEY (CMTE_ID) REFERENCES Committee (CMTE_ID),
	FOREIGN KEY (CONTRIBUTOR_ID) REFERENCES contributor (CONTRIBUTOR_ID)

);

CREATE TABLE currentcampaignforhouseandsenate ( 

    CAND_ID VARCHAR(9) NOT NULL PRIMARY KEY,  
    PTY_CD VARCHAR(1), 

    TTL_RECEIPTS numeric(14,2), 

    TRANS_FROM_AUTH numeric(14,2), 

    TTL_DISB numeric(14,2), 

    TRANS_TO_AUTH numeric(14,2), 

    COH_BOP numeric(14,2), 

    COH_COP numeric(14,2), 

    CAND_CONTRIB numeric(14,2), 

    CAND_LOANS numeric(14,2), 

    OTHER_LOANS numeric(14,2), 

    CAND_LOAN_REPAY numeric(14,2), 

    OTHER_LOAN_REPAY numeric(14,2), 

    DEBTS_OWED_BY numeric(14,2), 

    TTL_INDIV_CONTRIB numeric(14,2), 
 

    SPEC_ELECTION VARCHAR(1), 

    PRIM_ELECTION VARCHAR(1), 

    RUN_ELECTION VARCHAR(1), 

    GEN_ELECTION VARCHAR(1), 

    GEN_ELECTION_PRECENT numeric(7,4), 

    OTHER_POL_CMTE_CONTRIB numeric(14,2), 

    POL_PTY_CONTRIB numeric(14,2), 

    CVG_END_DT date, 

    INDIV_REFUNDS numeric(14,2), 

    CMTE_REFUNDS numeric(14,2), 

    FOREIGN KEY (CAND_ID) REFERENCES Candidate (CAND_ID) 

);


create table independentexpenditures( 

	CMTE_ID varchar(50), 

	AMNDT_IND varchar(10), 

	RPT_TP varchar(255), 

	TRANSACTION_PGI varchar(255), 

	TRANSACTION_TP varchar(255), 

	ENTITY_TP varchar(255), 

	CONTRIBUTOR_ID varchar(9),


	TRANSACTION_DT varchar(100), 

	TRANSACTION_AMT NUMERIC(255), 

	OTHER_ID NUMERIC(10), 

	TRAN_ID NUMERIC(10), 

	MEMO_CD varchar(50), 

	SUB_ID NUMERIC(50) NOT NULL primary key, 

                          FOREIGN KEY(CMTE_ID) REFERENCES COMMITTEE (CMTE_ID),
						  FOREIGN KEY (CONTRIBUTOR_ID) REFERENCES contributor (CONTRIBUTOR_ID)


); 


create table operatingexpenditures( 

	CMTE_ID varchar(50) , 

	AMNDT_IND varchar(10), 

	RTP_YR NUMERIC(10), 

	RPT_TP varchar(255), 

	LINE_NUM NUMERIC(100), 

	SCHED_TP_CD NUMERIC(10), 

	CONTRIBUTOR_ID varchar(9),  

	TRANSACTION_DT varchar(100), 

	TRANSACTION_AMT varchar(100), 

	TRANSACTION_PGI varchar(100), 

	PURPOSE varchar(100), 

	CATEGORY varchar(100), 

	CATEGORY_DESC varchar(100), 

	MEMO_CD varchar(100), 

	MEMO_TEXT varchar(100), 

	ENTITY_TP varchar(100), 

	SUB_ID varchar(100) NOT NULL primary key, 

	FILE_NUM varchar(100), 

	TRAN_ID varchar(100), 

	BACK_REF_TRAN_ID varchar(100), 

	FOREIGN KEY(CMTE_ID) REFERENCES COMMITTEE (CMTE_ID),
	FOREIGN KEY (CONTRIBUTOR_ID) REFERENCES contributor (CONTRIBUTOR_ID)


); 


create table pacandpartysummary( 

	CMTE_ID varchar(9)  NOT NULL primary key, 
	TTL_RECEIPTS NUMERIC(14,2), 

	TRANS_FROM_AFF NUMERIC(14,2), 

	INDV_CONTRIB NUMERIC(14,2), 

	OTHER_POL_CMTE_CONTRIB NUMERIC(14,2), 

	CAND_CONTRIB NUMERIC(14,2), 

	CAND_LOANS NUMERIC(14,2), 

	TTL_LOANS_RECEIVED NUMERIC(14,2), 

	TTL_DISB NUMERIC(14,2), 

	TRANF_TO_AFF NUMERIC(14,2), 

	INDV_REFUNDS NUMERIC(14,2), 

	OTHER_POL_CMTE_REFUNDS NUMERIC(14,2), 

	CAND_LOAN_REPAY NUMERIC(14,2), 

	LOAN_REPAY NUMERIC(14,2), 

	COH_BOP NUMERIC(14,2), 

	COH_COP NUMERIC(14,2), 

	DEBTS_OWED_BY NUMERIC(14,2), 

	NONFED_TRANS_RECEIVED NUMERIC(14,2), 

	CONTRIB_TO_OTHER_CMTE NUMERIC(14,2), 

	IND_EXP NUMERIC(14,2), 

	PTY_COORD_EXP NUMERIC(14,2), 

	NONFED_SHARE_EXP NUMERIC(14,2), 

	CVG_END_DT    DATE,  

	FOREIGN KEY(CMTE_ID) REFERENCES COMMITTEE (CMTE_ID)  

);
