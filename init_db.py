import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="fec",
    user="postgres",
    password="sand"
)

cur = conn.cursor()
    
# open the initdb.sql file and read its contents
with open('schema.sql') as f:
    sql = f.read()

# execute the SQL commands in the file
cur.execute(sql)

def modifydata(data):
     cnt=0
     for vals in data:
          if data[cnt]=='':
               data[cnt]='1'
          cnt=cnt+1
     return data
    
def load_text_file_into_db(fileName, sqlInsert, cur):
     # Open the first text file and insert data into the table
    cnt=0
    with open(fileName, 'r') as f:
        for line in f:
                data = line.strip().split('|')
                print(data)
                print(len(data))
                # delete specific indices
                #indices_to_remove = [1, 2, 4, 18, 19] house and senate
                #indices_to_remove = [7, 8, 9, 10, 11,12]
                #data = [data[i] for i in range(len(data)) if i not in indices_to_remove]
                #data=data[0:12]
                #data[11]='1'
               # data[10]='1'
                #data[9]='1'
                #data.append(1)
                print(data)
                #print(data[1]+' '+data[2]+' '+data[3]+' '+data[4])
                #del data[1:4]
                print(len(data))
                #modifieddata=modifydata(data)
                #print(data)
                cur.execute(
                sqlInsert,
                data
                )

try:
    cur = conn.cursor()
    sql_insert_candidate = "INSERT INTO candidate (CAND_ID, CAND_NAME, CAND_PTY_AFFILIATION, CAND_ELECTION_YR, CAND_OFFICE_ST, CAND_OFFICE, CAND_OFFICE_DISTRICT, CAND_ICI, CAND_STATUS, CAND_PCC, CAND_ST1, CAND_ST2, CAND_CITY, CAND_ST, CAND_ZIP) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    sql_insert_comittee = "INSERT INTO committee (CMTE_ID, CMTE_NM, TRES_NM, CMTE_ST1, CMTE_ST2, CMTE_CITY, CMTE_ST, CMTE_ZIP, CMTE_DSGN, CMTE_TP, CMTE_PTY_AFFILIATION, CMTE_FILING_FREQ, ORG_TP, CONNECTED_ORG_NM, CAND_ID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    sql_insert_candidate_committees = "INSERT INTO candidate_committee (CAND_ID,CAND_ELECTION_YR, FEC_ELECTION_YR , CMTE_ID, CMTE_TP, CMTE_DSGN, LINKAGE_ID) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    sql_insert_contributor="INSERT INTO contributor(CONTRIBUTOR_ID,NAME,CITY ,STATE , ZIP_CODE ,EMPLOYER ,OCCUPATION ) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    sql_insert_pacpartysummary="INSERT INTO pacandpartysummary(CMTE_ID,TTL_RECEIPTS, TRANS_FROM_AFF, INDV_CONTRIB, OTHER_POL_CMTE_CONTRIB , CAND_CONTRIB , CAND_LOANS , TTL_LOANS_RECEIVED , TTL_DISB, TRANF_TO_AFF, INDV_REFUNDS , OTHER_POL_CMTE_REFUNDS , CAND_LOAN_REPAY , LOAN_REPAY , COH_BOP , COH_COP , DEBTS_OWED_BY , NONFED_TRANS_RECEIVED , CONTRIB_TO_OTHER_CMTE , IND_EXP , PTY_COORD_EXP , NONFED_SHARE_EXP , CVG_END_DT) VALUES (%s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s,%s,%s)"
    sql_insert_houseandsenate="INSERT INTO currentcampaignforhouseandsenate(CAND_ID,PTY_CD, TTL_RECEIPTS ,TRANS_FROM_AUTH , TTL_DISB , TRANS_TO_AUTH , COH_BOP , COH_COP , CAND_CONTRIB , CAND_LOANS , OTHER_LOANS, CAND_LOAN_REPAY , OTHER_LOAN_REPAY , DEBTS_OWED_BY , TTL_INDIV_CONTRIB,SPEC_ELECTION , PRIM_ELECTION , RUN_ELECTION , GEN_ELECTION , GEN_ELECTION_PRECENT , OTHER_POL_CMTE_CONTRIB, POL_PTY_CONTRIB , CVG_END_DT , INDIV_REFUNDS , CMTE_REFUNDS) VALUES (%s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s,%s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s)"
    sql_insert_independentexpenditures="INSERT INTO independentexpenditures(CMTE_ID, AMNDT_IND , RPT_TP , TRANSACTION_PGI , TRANSACTION_TP, ENTITY_TP , CONTRIBUTOR_ID, TRANSACTION_DT , TRANSACTION_AMT, OTHER_ID , TRAN_ID , MEMO_CD ) VALUES (%s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s)"
    load_text_file_into_db('data/cn.txt', sql_insert_candidate, cur)
    load_text_file_into_db('data/cm.txt', sql_insert_comittee, cur)
    load_text_file_into_db('data/ccl.txt', sql_insert_candidate_committees, cur)
    #load_text_file_into_db('contributor.txt', sql_insert_contributor,cur)
    #load_text_file_into_db('newpac.txt', sql_insert_pacpartysummary,cur)
    #load_text_file_into_db('houseandsenate.txt', sql_insert_houseandsenate,cur)
    # load_text_file_into_db('independentexpenditures.txt',sql_insert_independentexpenditures,cur)
    # Commit the changes and close the connection
    conn.commit()
    
except Exception as err:
    print(err)
finally:
    cur.close()
    conn.close()
