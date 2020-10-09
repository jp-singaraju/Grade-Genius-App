from flask import *

# ALL FUNCTIONS HAVE TO RUN IN THE ORDER AS IN BELOW

# defines the flask app
app = Flask(__name__)

# creates a secret key for the app
secret_key = b'\xad7\xe7\x04\xb6^\x9a\x95\xb97k\xdd\x06w\x00\xc7BlX\xc0\x88JBM\x07\x8c\xf8k\xf5\x17\xb5\xf0\xed\x81EU' \
             b'\x01\xbc\x85\xcc '

# update the keys
app.config['SECRET_KEY'] = secret_key
app.config['SESSION_TYPE'] = 'filesystem'
app.config['FLASK_ENV'] = 'production'


# defines the app route for login
@app.route('/login', methods=['GET'])
# function in order to get login
def login():
    return redirect(url_for("grades"))


# defines the app route for grades
@app.route('/grades')
# function in order to get grades
def grades():
    try:
        # create an overall dictionary for all values
        dict_main_assignments = {"Averages": {
            "Class Average": ["100.00%", "100.00%", "100.00%", "100.00%", "100.00%", "100.00%", "100.00%", "100.00%"],
            "Class Name": ["PLTW-Intr Engr Des S2@CTEC", "GT HumanitiesI/PAP Eng S2", "PAP Spanish II - S2",
                           "PAP Pre Calculus - S2", "Found of Pers Fitness - Sem", "PAP Biology - S2",
                           "AP Human Geog- Grade 9 S2", "PAP Computer Science - S2"]}, "Grades": {"Class 1": {
            "Assignments": ["Chair Portfolio Part 1", "Chair Description Step 10", "Chair Mock-up Construction",
                            "3D Model", "Top 3 ISO Sketches", "15 Brainstorming Sketches", "Chair Research",
                            "Design Brief", "CFA"],
            "Category": ["eLearning", "eLearning", "eLearning", "eLearning", "eLearning", "eLearning", "eLearning",
                         "eLearning", "eLearning"],
            "Due Date": ["05/11/2020", "05/04/2020", "04/28/2020", "04/28/2020", "04/14/2020", "04/06/2020",
                         "03/26/2020", "03/25/2020", "03/25/2020"],
            "Percentage": ["100.000%", "100.000%", "100.000%", "100.000%", "100.000%", "100.000%", "100.000%",
                           "100.000%", "100.000%"],
            "Score": ["100.0", "100.0", "100.0", "100.0", "100.0", "100.0", "100.0", "100.0", "100.0"],
            "Weight": ["1.00", "1.00", "1.00", "1.00", "1.00", "1.00", "1.00", "1.00", "1.00"],
            "Weighted Score": ["100.00", "100.00", "100.00", "100.00", "100.00", "100.00", "100.00", "100.00",
                               "100.00"],
            "Weighted Total Points": ["100.00", "100.00", "100.00", "100.00", "100.00", "100.00", "100.00", "100.00",
                                      "100.00"]}, "Class 2": {
            "Assignments": ["Anthem Review Project", "Symbolism FlipGrid", "Anthem Response Questions",
                            "Soviet Artful Thinking", "FlipGrid Response", "TKaM Intro Journal",
                            "Early Modern Labor Tweets"],
            "Category": ["eLearning", "eLearning", "eLearning", "eLearning", "eLearning", "eLearning", "eLearning"],
            "Due Date": ["05/11/2020", "05/04/2020", "04/28/2020", "04/20/2020", "04/13/2020", "04/06/2020",
                         "03/24/2020"],
            "Percentage": ["100.000%", "100.000%", "100.000%", "100.000%", "100.000%", "100.000%", "100.000%"],
            "Score": ["100.0", "100.0", "100.0", "100.0", "100.0", "100.0", "100.0"],
            "Weight": ["1.00", "1.00", "1.00", "1.00", "1.00", "1.00", "1.00"],
            "Weighted Score": ["100.00", "100.00", "100.00", "100.00", "100.00", "100.00", "100.00"],
            "Weighted Total Points": ["100.00", "100.00", "100.00", "100.00", "100.00", "100.00", "100.00"]},
            "Class 3": {
                "Assignments": [
                    "Week # 7 Edpuzzle",
                    "Week # 6 Int. Writing Elaboration",
                    "Week # 5 Edpuzzle",
                    "Week # 4 Presentational Speaking",
                    "Week # 3 Writing - TS",
                    "Week # 2 EdPuzzle"],
                "Category": [
                    "eLearning",
                    "eLearning",
                    "eLearning",
                    "eLearning",
                    "eLearning",
                    "eLearning"],
                "Due Date": [
                    "05/11/2020",
                    "04/28/2020",
                    "04/20/2020",
                    "04/13/2020",
                    "04/06/2020",
                    "03/27/2020"],
                "Percentage": [
                    "100.00%",
                    "100.000%",
                    "100.00%",
                    "100.000%",
                    "100.00%",
                    "100.00%"],
                "Score": ["CWS",
                          "100.0",
                          "CWS",
                          "100.0",
                          "CWS",
                          "CWS"],
                "Weight": ["1.00",
                           "1.00",
                           "1.00",
                           "1.00",
                           "1.00",
                           "1.00"],
                "Weighted Score": [
                    "100.00",
                    "100.00",
                    "100.00",
                    "100.00",
                    "100.00",
                    "100.00"],
                "Weighted Total Points": [
                    "100.00",
                    "100.00",
                    "100.00",
                    "100.00",
                    "100.00",
                    "100.00"]},
            "Class 4": {
                "Assignments": [
                    "5/11 - 5/15 Assignment",
                    "5/4 - 5/8 Assignment",
                    "4/27 - 5/1 Assignment",
                    "4/20 - 4/24 Assignment",
                    "4/13 - 4/17 Assignment",
                    "4/6 - 4/10 Assignment",
                    "3/30 - 4/3 Assignment",
                    "3/23 - 3/27 Assignment"],
                "Category": [
                    "eLearning",
                    "eLearning",
                    "eLearning",
                    "eLearning",
                    "eLearning",
                    "eLearning",
                    "eLearning",
                    "eLearning"],
                "Due Date": [
                    "05/15/2020",
                    "05/08/2020",
                    "05/01/2020",
                    "04/24/2020",
                    "04/17/2020",
                    "04/09/2020",
                    "04/02/2020",
                    "03/27/2020"],
                "Percentage": [
                    "100.000%",
                    "100.000%",
                    "100.000%",
                    "100.000%",
                    "100.000%",
                    "100.000%",
                    "100.000%",
                    "100.000%"],
                "Score": ["100.0",
                          "100.0",
                          "100.0",
                          "100.0",
                          "100.0",
                          "100.0",
                          "100.0",
                          "100.0"],
                "Weight": ["1.00",
                           "1.00",
                           "1.00",
                           "1.00",
                           "1.00",
                           "1.00",
                           "1.00",
                           "1.00"],
                "Weighted Score": [
                    "100.00",
                    "100.00",
                    "100.00",
                    "100.00",
                    "100.00",
                    "100.00",
                    "100.00",
                    "100.00"],
                "Weighted Total Points": [
                    "100.00",
                    "100.00",
                    "100.00",
                    "100.00",
                    "100.00",
                    "100.00",
                    "100.00",
                    "100.00"]},
            "Class 5": {
                "Assignments": [
                    "Week 7 April 27th",
                    "Week 6 April 20",
                    "Week 5 April 13th",
                    "Week 4 April 6th",
                    "Week 3 March 30th",
                    "Week 2 March 23rd"],
                "Category": [
                    "eLearning",
                    "eLearning",
                    "eLearning",
                    "eLearning",
                    "eLearning",
                    "eLearning"],
                "Due Date": [
                    "05/04/2020",
                    "04/28/2020",
                    "04/20/2020",
                    "04/13/2020",
                    "04/06/2020",
                    "03/30/2020"],
                "Percentage": [
                    "100.000%",
                    "100.000%",
                    "100.000%",
                    "100.000%",
                    "100.000%",
                    "100.000%"],
                "Score": ["100.0",
                          "100.0",
                          "100.0",
                          "100.0",
                          "100.0",
                          "100.0"],
                "Weight": ["1.00",
                           "1.00",
                           "1.00",
                           "1.00",
                           "1.00",
                           "1.00"],
                "Weighted Score": [
                    "100.00",
                    "100.00",
                    "100.00",
                    "100.00",
                    "100.00",
                    "100.00"],
                "Weighted Total Points": [
                    "100.00",
                    "100.00",
                    "100.00",
                    "100.00",
                    "100.00",
                    "100.00"]},
            "Class 6": {
                "Assignments": [
                    "e-Learning Week 7: Endocrine & Nervous Systems",
                    "e-Learning Week 6: Skeletal & Muscular Systems",
                    "e-Learning Week 5: Digestive System Flowchart",
                    "e-Learning Week 4: Excretory System Poster",
                    "e-Learning Week 3: Immune System Menu",
                    "e-Learning Week 2: Respiratory System Case Study",
                    "e-Learning Week 1: Tic-Tac-Toe"],
                "Category": [
                    "eLearning",
                    "eLearning",
                    "eLearning",
                    "eLearning",
                    "eLearning",
                    "eLearning",
                    "eLearning"],
                "Due Date": [
                    "05/08/2020",
                    "05/01/2020",
                    "04/24/2020",
                    "04/17/2020",
                    "04/09/2020",
                    "04/03/2020",
                    "03/27/2020"],
                "Percentage": [
                    "100.000%",
                    "100.000%",
                    "100.000%",
                    "100.000%",
                    "100.000%",
                    "100.000%",
                    "100.000%"],
                "Score": ["100.0",
                          "100.0",
                          "100.0",
                          "100.0",
                          "100.0",
                          "100.0",
                          "100.0"],
                "Weight": ["1.00",
                           "1.00",
                           "1.00",
                           "1.00",
                           "1.00",
                           "1.00",
                           "1.00"],
                "Weighted Score": [
                    "100.00",
                    "100.00",
                    "100.00",
                    "100.00",
                    "100.00",
                    "100.00",
                    "100.00"],
                "Weighted Total Points": [
                    "100.00",
                    "100.00",
                    "100.00",
                    "100.00",
                    "100.00",
                    "100.00",
                    "100.00"]},
            "Class 7": {
                "Assignments": [
                    "Week 8: Unit 5, FRQ #3",
                    "Week 8: Unit 5, FRQ #2",
                    "Unit 5, FRQ #1",
                    "Week 8: Unit 4, FRQ #2",
                    "Week 8: Unit 4, FRQ #1",
                    "Week 7: Unit 5, Topic 4 Review Packet",
                    "Week 7: Unit 5, Topic 3 Review Packet",
                    "Week 7: Unit 5, Topic 2 Review Packet",
                    "Week 7: Unit 5, Topic 1 Review Packet",
                    "Week 6: Unit 4, Topic 3 Review Packet",
                    "Week 6: Unit 4, Topic 2 Review Packet",
                    "Week 6: Unit 4, Topic 1 Review Packet",
                    "Week 5: Unit 3, FRQ 4",
                    "Week 5: Unit 3, FRQ 3",
                    "Week 5: Unit 3, FRQ 2",
                    "Week 5: Unit 3, FRQ #1",
                    "Week 4: Unit 3, Topic 3 Review Packet",
                    "Week 4: Unit 3, Topic 2 Review Packet",
                    "Week 4: Unit 3, Topic 1 Review Packet",
                    "Week 3: Unit 2, Topic 3 Review",
                    "Week 3: Unit 2, Topic 2 Review",
                    "Week 3: Unit 2, Topic 1 Review",
                    "Week 2- Unit 2 Vocab (CNS)",
                    "Week 2- FRQ #2",
                    "Week 2- FRQ #1",
                    "Week 2- Exit Ticket #3 (CNS)",
                    "Week 2- Exit Ticket #2 (CNS)",
                    "Week 2: Exit Ticket #1 (CNS)"],
                "Category": [
                    "eLearning",
                    "eLearning",
                    "eLearning",
                    "eLearning",
                    "eLearning",
                    "eLearning",
                    "eLearning",
                    "eLearning",
                    "eLearning",
                    "eLearning",
                    "eLearning",
                    "eLearning",
                    "eLearning",
                    "eLearning",
                    "eLearning",
                    "eLearning",
                    "eLearning",
                    "eLearning",
                    "eLearning",
                    "eLearning",
                    "eLearning",
                    "eLearning",
                    "eLearning",
                    "eLearning",
                    "eLearning",
                    "eLearning",
                    "eLearning",
                    "eLearning"],
                "Due Date": [
                    "05/11/2020",
                    "05/11/2020",
                    "05/11/2020",
                    "05/11/2020",
                    "05/11/2020",
                    "05/04/2020",
                    "05/04/2020",
                    "05/04/2020",
                    "05/04/2020",
                    "04/28/2020",
                    "04/28/2020",
                    "04/28/2020",
                    "04/20/2020",
                    "04/20/2020",
                    "04/20/2020",
                    "04/20/2020",
                    "04/13/2020",
                    "04/13/2020",
                    "04/13/2020",
                    "04/06/2020",
                    "04/06/2020",
                    "04/06/2020",
                    "03/30/2020",
                    "03/30/2020",
                    "03/30/2020",
                    "03/30/2020",
                    "03/30/2020",
                    "03/30/2020"],
                "Percentage": [
                    "100.00%",
                    "100.00%",
                    "100.00%",
                    "100.00%",
                    "100.00%",
                    "100.000%",
                    "100.000%",
                    "100.000%",
                    "100.000%",
                    "100.000%",
                    "100.000%",
                    "100.000%",
                    "100.00%",
                    "100.00%",
                    "100.00%",
                    "100.00%",
                    "100.000%",
                    "100.000%",
                    "100.000%",
                    "100.000%",
                    "100.000%",
                    "100.000%",
                    "0.00%",
                    "100.000%",
                    "100.000%",
                    "0.00%",
                    "0.00%",
                    "0.00%"],
                "Score": ["CWS",
                          "CWS",
                          "CWS",
                          "CWS",
                          "CWS",
                          "25.00",
                          "25.00",
                          "25.00",
                          "25.00",
                          "30.00",
                          "30.00",
                          "40.00",
                          "CWS",
                          "CWS",
                          "CWS",
                          "CWS",
                          "30.00",
                          "30.00",
                          "40.00",
                          "30.00",
                          "40.00",
                          "30.00",
                          "CNS",
                          "50.00",
                          "50.00",
                          "CNS",
                          "CNS",
                          "CNS"],
                "Weight": ["1.00",
                           "1.00",
                           "1.00",
                           "1.00",
                           "1.00",
                           "1.00",
                           "1.00",
                           "1.00",
                           "1.00",
                           "1.00",
                           "1.00",
                           "1.00",
                           "1.00",
                           "1.00",
                           "1.00",
                           "1.00",
                           "1.00",
                           "1.00",
                           "1.00",
                           "1.00",
                           "1.00",
                           "1.00",
                           "1.00",
                           "1.00",
                           "1.00",
                           "1.00",
                           "1.00",
                           "1.00"],
                "Weighted Score": [
                    "20.00",
                    "20.00",
                    "20.00",
                    "20.00",
                    "20.00",
                    "25.00",
                    "25.00",
                    "25.00",
                    "25.00",
                    "30.00",
                    "30.00",
                    "40.00",
                    "25.00",
                    "25.00",
                    "25.00",
                    "25.00",
                    "30.00",
                    "30.00",
                    "40.00",
                    "30.00",
                    "40.00",
                    "30.00",
                    "0.00",
                    "50.00",
                    "50.00",
                    "0.00",
                    "0.00",
                    "0.00"],
                "Weighted Total Points": [
                    "20.00",
                    "20.00",
                    "20.00",
                    "20.00",
                    "20.00",
                    "25.00",
                    "25.00",
                    "25.00",
                    "25.00",
                    "30.00",
                    "30.00",
                    "40.00",
                    "25.00",
                    "25.00",
                    "25.00",
                    "25.00",
                    "30.00",
                    "30.00",
                    "40.00",
                    "30.00",
                    "40.00",
                    "30.00",
                    "100.00",
                    "50.00",
                    "50.00",
                    "100.00",
                    "100.00",
                    "100.00"]},
            "Class 8": {
                "Assignments": [
                    "Lab 29",
                    "Lab 28 - CS - 4V",
                    "Lab 26 - CS - 6R",
                    "Lab 25 - CS - 6H/6I",
                    "Lab 24 - CS - 6H/6I"],
                "Category": [
                    "eLearning",
                    "eLearning",
                    "eLearning",
                    "eLearning",
                    "eLearning"],
                "Due Date": [
                    "05/01/2020",
                    "04/17/2020",
                    "04/09/2020",
                    "04/03/2020",
                    "03/30/2020"],
                "Percentage": [
                    "100.000%",
                    "100.000%",
                    "100.000%",
                    "100.000%",
                    "100.000%"],
                "Score": ["100.0",
                          "100.0",
                          "100.0",
                          "100.0",
                          "100.0"],
                "Weight": ["1.00",
                           "1.00",
                           "1.00",
                           "1.00",
                           "1.00"],
                "Weighted Score": [
                    "100.00",
                    "100.00",
                    "100.00",
                    "100.00",
                    "100.00"],
                "Weighted Total Points": [
                    "100.00",
                    "100.00",
                    "100.00",
                    "100.00",
                    "100.00"]}},
            "Info": {"Grade": "09", "Home Campus": "Independence High School", "ID": "228751",
                     "Name": "Jathin Singaraju"}, "Report Run": "4"}

        # return the json object mentioned
        print(dict_main_assignments)
        return jsonify(dict_main_assignments)
    except (AttributeError, KeyError, TypeError):
        return jsonify({"status": "error", "msg": "unable to receive info now, please retry"}), 404


@app.route('/schedule')
# function in order to get schedule
def schedule():
    try:
        schedule_dict = {
            "Building": ["Independence High School", "Independence High School", "Independence High School",
                         "Independence High School", "Independence High School", "Independence High School",
                         "Independence High School", "Independence High School", "Independence High School",
                         "Independence High School", "Independence High School", "Independence High School", "CTE",
                         "Independence High School", "CTE", "Independence High School", "Independence High School"],
            "Class": ["PAP Pre Calculus - S1", "AP Human Geog- Grade 9 S1", "PAP Pre Calculus - S2",
                      "AP Human Geog- Grade 9 S2", "PAP Spanish II - S1", "PAP Biology - S1", "PAP Spanish II - S2",
                      "PAP Biology - S2", "GT HumanitiesI/PAP Eng S1", "Individual/Team Sports-Sem",
                      "GT HumanitiesI/PAP Eng S2", "Found of Pers Fitness - Sem", "PLTW-Intr Engr Des S1@CTEC",
                      "PAP Computer Science - S1", "PLTW-Intr Engr Des S2@CTEC", "PAP Computer Science - S2",
                      "9th Grade Advisory Period"],
            "Course": ["MTH34200A - 1", "SST11500A - 3", "MTH34200B - 1", "SST11500B - 3", "FLG22200A - 1",
                       "SCI11200A - 9", "FLG22200B - 1", "SCI11200B - 9", "ELA11500A - 1", "PEI01001S - 5",
                       "ELA11500B - 1", "PEF01001S - 5", "CATE03742A - 17", "TEC21200A - 4", "CATE03742B - 17",
                       "TEC21200B - 4", "MSC15133M - 19"],
            "Days": ["A", "B", "A", "B", "A", "B", "A", "B", "A", "B", "A", "B", "A", "B", "A", "B", "A, B"],
            "Marking Period": ["Q1, Q2", "Q1, Q2", "Q3, Q4", "Q3, Q4", "Q1, Q2", "Q1, Q2", "Q3, Q4", "Q3, Q4", "Q1, Q2",
                               "Q1, Q2", "Q3, Q4", "Q3, Q4", "Q1, Q2", "Q1, Q2", "Q3, Q4", "Q3, Q4", "Q1, Q2, Q3, Q4"],
            "Period": ["1", "1", "1", "1", "2", "2", "2", "2", "3", "3", "3", "3", "4", "4", "4", "4", "ADV"],
            "Room": ["C223", "B206", "C223", "B206", "C119", "B213", "C119", "B213", "A200", "G100", "A200", "G100",
                     "XF119", "B108", "XF119", "B108", "C202"],
            "Teacher": ["TODD, MICHAEL", "DIAMOND, MEGAN", "TODD, MICHAEL", "DIAMOND, MEGAN", "PHILLIPS, PAOLA",
                        "BARNES, LEIGH", "PHILLIPS, PAOLA", "BARNES, LEIGH", "RILEY, LINDA", "MATLOCK, AMY",
                        "RILEY, LINDA", "MATLOCK, AMY", "DELUCA, DAVID", "MORRIS, ROBERT", "DELUCA, DAVID",
                        "MORRIS, ROBERT", "MONTGOMERY, CHRISTY"]}
        return jsonify(schedule_dict)
    except (AttributeError, KeyError, TypeError):
        return jsonify({"status": "error", "msg": "unable to receive info now, please retry"}), 404


# defines the app route for ipr
@app.route('/ipr')
# function in order to get ipr
def ipr():
    try:
        ipr_run_dict = {"Run": "Interim Progress Report For Monday, May 11, 2020", "Schedule": {
            "Class": ["PAP Pre Calculus - S2", "AP Human Geog- Grade 9 S2", "PAP Spanish II - S2", "PAP Biology - S2",
                      "Found of Pers Fitness - Sem", "GT HumanitiesI/PAP Eng S2", "PAP Computer Science - S2",
                      "PLTW-Intr Engr Des S2@CTEC"],
            "Course": ["MTH34200B - 1", "SST11500B - 3", "FLG22200B - 1", "SCI11200B - 9", "PEF01001S - 5",
                       "ELA11500B - 1", "TEC21200B - 4", "CATE03742B - 17"],
            "Grade": ["100", "100", "100", "100", "100", "100", "100", "100"],
            "Period": ["1", "1", "2", "2", "3", "3", "4", "4"],
            "Room": ["C223", "B206", "C119", "B213", "G100", "A200", "B108", "XF119"],
            "Teacher": ["TODD, MICHAEL", "DIAMOND, MEGAN", "PHILLIPS, PAOLA", "BARNES, LEIGH", "MATLOCK, AMY",
                        "RILEY, LINDA", "MORRIS, ROBERT", "DELUCA, DAVID"]}}
        return jsonify(ipr_run_dict)
    except (AttributeError, KeyError, TypeError):
        return jsonify({"status": "error", "msg": "unable to receive info now, please retry"}), 404


# defines the app route for rc
@app.route('/reportcard')
# function in order to get rc
def report_card():
    try:
        final_dict = {
            "Att.Credit": {"1": "0.5000", "2": "0.5000", "3": "0.5000", "4": "0.5000", "5": "0.5000", "6": "0.5000",
                           "7": "0.5000", "8": "0.5000", "9": "0.5000", "10": "0.5000", "11": "0.5000", "12": "0.5000",
                           "13": "0.5000", "14": "0.5000", "15": "0.5000", "16": "0.5000", "17": "0.5000",
                           "18": "0.5000", "19": "0.5000", "20": "0.5000", "21": "0.5000", "22": "0.5000",
                           "23": "0.5000", "24": "0.5000"},
            "CIT": {"1": "", "2": "", "3": "", "4": "", "5": "", "6": "", "7": "", "8": "", "9": "", "10": "", "11": "",
                    "12": "", "13": "", "14": "", "15": "", "16": "", "17": "", "18": "", "19": "", "20": "", "21": "",
                    "22": "", "23": "", "24": ""},
            "CM1": {"1": "", "2": "", "3": "", "4": "", "5": "", "6": "", "7": "", "8": "", "9": "", "10": "901",
                    "11": "", "12": "901", "13": "", "14": "901", "15": "", "16": "901", "17": "", "18": "", "19": "",
                    "20": "", "21": "", "22": "901", "23": "", "24": "901"},
            "CM2": {"1": "", "2": "", "3": "", "4": "", "5": "", "6": "", "7": "", "8": "", "9": "", "10": "", "11": "",
                    "12": "", "13": "", "14": "", "15": "", "16": "", "17": "", "18": "", "19": "", "20": "", "21": "",
                    "22": "", "23": "", "24": ""},
            "Course": {"1": "EAWL180A - 2", "2": "EAWL180B - 2", "3": "EAWL280A - 1", "4": "EAWL280B - 1",
                       "5": "EAWL380A - 1", "6": "EAWL380B - 1", "7": "EAWL480A - 1", "8": "EAWL480B - 1",
                       "9": "MTH34200A - 1", "10": "MTH34200B - 1", "11": "SST11500A - 3", "12": "SST11500B - 3",
                       "13": "FLG22200A - 1", "14": "FLG22200B - 1", "15": "SCI11200A - 9", "16": "SCI11200B - 9",
                       "17": "ELA11500A - 1", "18": "ELA11500B - 1", "19": "PEF01001S - 5", "20": "PEI01001S - 5",
                       "21": "CATE03742A - 17", "22": "CATE03742B - 17", "23": "TEC21200A - 4", "24": "TEC21200B - 4"},
            "Description": {"1": "EA Spanish I - S1", "2": "EA Spanish I - S2", "3": "EA Spanish II - S1",
                            "4": "EA Spanish II - S2", "5": "EA Spanish III - S1", "6": "EA Spanish III - S2",
                            "7": "EA Spanish IV - S1", "8": "EA Spanish IV - S2", "9": "PAP Pre Calculus - S1",
                            "10": "PAP Pre Calculus - S2", "11": "AP Human Geog- Grade 9 S1",
                            "12": "AP Human Geog- Grade 9 S2", "13": "PAP Spanish II - S1", "14": "PAP Spanish II - S2",
                            "15": "PAP Biology - S1", "16": "PAP Biology - S2", "17": "GT HumanitiesI/PAP Eng S1",
                            "18": "GT HumanitiesI/PAP Eng S2", "19": "Found of Pers Fitness - Sem",
                            "20": "Individual/Team Sports-Sem", "21": "PLTW-Intr Engr Des S1@CTEC",
                            "22": "PLTW-Intr Engr Des S2@CTEC", "23": "PAP Computer Science - S1",
                            "24": "PAP Computer Science - S2"},
            "Ern.Credit": {"1": "0.5000", "2": "0.5000", "3": "0.5000", "4": "0.5000", "5": "0.5000", "6": "0.5000",
                           "7": "0.5000", "8": "0.5000", "9": "0.5000", "10": "0.5000", "11": "0.5000", "12": "0.5000",
                           "13": "0.5000", "14": "0.5000", "15": "0.5000", "16": "0.5000", "17": "0.5000",
                           "18": "0.5000", "19": "0.5000", "20": "0.5000", "21": "0.5000", "22": "0.5000",
                           "23": "0.5000", "24": "0.5000"},
            "FIN": {"1": "", "2": "", "3": "", "4": "", "5": "", "6": "", "7": "", "8": "", "9": "", "10": "", "11": "",
                    "12": "", "13": "", "14": "", "15": "", "16": "", "17": "", "18": "", "19": "", "20": "", "21": "",
                    "22": "", "23": "", "24": ""},
            "Period": {"1": "0", "2": "0", "3": "0", "4": "0", "5": "0", "6": "0", "7": "0", "8": "0", "9": "1",
                       "10": "1", "11": "1", "12": "1", "13": "2", "14": "2", "15": "2", "16": "2", "17": "3",
                       "18": "3", "19": "3", "20": "3", "21": "4", "22": "4", "23": "4", "24": "4"},
            "Q1": {"1": "", "2": "", "3": "", "4": "", "5": "", "6": "", "7": "", "8": "", "9": "100", "10": "",
                   "11": "98", "12": "", "13": "97", "14": "", "15": "98", "16": "", "17": "90", "18": "", "19": "",
                   "20": "100", "21": "98", "22": "", "23": "96", "24": ""},
            "Q2": {"1": "", "2": "", "3": "", "4": "", "5": "", "6": "", "7": "", "8": "", "9": "100", "10": "",
                   "11": "94", "12": "", "13": "100", "14": "", "15": "98", "16": "", "17": "90", "18": "", "19": "",
                   "20": "100", "21": "99", "22": "", "23": "99", "24": ""},
            "Q3": {"1": "", "2": "", "3": "", "4": "", "5": "", "6": "", "7": "", "8": "", "9": "", "10": "98",
                   "11": "", "12": "94", "13": "", "14": "99", "15": "", "16": "99", "17": "", "18": "96", "19": "100",
                   "20": "", "21": "", "22": "99", "23": "", "24": "100"},
            "Q4": {"1": "", "2": "", "3": "", "4": "", "5": "", "6": "", "7": "", "8": "", "9": "", "10": "100",
                   "11": "", "12": "100", "13": "", "14": "100", "15": "", "16": "100", "17": "", "18": "100",
                   "19": "100", "20": "", "21": "", "22": "100", "23": "", "24": "100"},
            "Room": {"1": "", "2": "", "3": "", "4": "", "5": "", "6": "", "7": "", "8": "", "9": "C223", "10": "C223",
                     "11": "B206", "12": "B206", "13": "C119", "14": "C119", "15": "B213", "16": "B213", "17": "A200",
                     "18": "A200", "19": "G100", "20": "G100", "21": "XF119", "22": "XF119", "23": "B108",
                     "24": "B108"},
            "SEM1": {"1": "P", "2": "", "3": "P", "4": "", "5": "P", "6": "", "7": "P", "8": "", "9": "100", "10": "",
                     "11": "96", "12": "", "13": "99", "14": "", "15": "98", "16": "", "17": "90", "18": "", "19": "",
                     "20": "100", "21": "99", "22": "", "23": "98", "24": ""},
            "SEM2": {"1": "", "2": "P", "3": "", "4": "P", "5": "", "6": "P", "7": "", "8": "82", "9": "", "10": "99",
                     "11": "", "12": "97", "13": "", "14": "100", "15": "", "16": "100", "17": "", "18": "98",
                     "19": "100", "20": "", "21": "", "22": "100", "23": "", "24": "100"},
            "Teacher": {"1": "STAFF", "2": "STAFF", "3": "STAFF", "4": "STAFF", "5": "STAFF", "6": "STAFF",
                        "7": "STAFF", "8": "STAFF", "9": "TODD, MICHAEL", "10": "TODD, MICHAEL", "11": "DIAMOND, MEGAN",
                        "12": "DIAMOND, MEGAN", "13": "PHILLIPS, PAOLA", "14": "PHILLIPS, PAOLA", "15": "BARNES, LEIGH",
                        "16": "BARNES, LEIGH", "17": "RILEY, LINDA", "18": "RILEY, LINDA", "19": "MATLOCK, AMY",
                        "20": "MATLOCK, AMY", "21": "DELUCA, DAVID", "22": "DELUCA, DAVID", "23": "MORRIS, ROBERT",
                        "24": "MORRIS, ROBERT"},
            "YTDA": {"1": "", "2": "", "3": "", "4": "", "5": "", "6": "", "7": "", "8": "", "9": "0", "10": "0",
                     "11": "0", "12": "0", "13": "0", "14": "0", "15": "0", "16": "0", "17": "0", "18": "0", "19": "0",
                     "20": "0", "21": "", "22": "", "23": "0", "24": "0"},
            "YTDT": {"1": "", "2": "", "3": "", "4": "", "5": "", "6": "", "7": "", "8": "", "9": "0", "10": "1",
                     "11": "0", "12": "0", "13": "0", "14": "0", "15": "0", "16": "0", "17": "0", "18": "0", "19": "0",
                     "20": "0", "21": "", "22": "", "23": "0", "24": "0"}}
        return jsonify(final_dict)
    except (AttributeError, KeyError, TypeError):
        return jsonify({"status": "error", "msg": "unable to receive info now, please retry"}), 404


# defines the app route for gpa
@app.route('/gpa')
# function in order to get gpa
def gpa():
    try:
        gpa_dict = {"Unweighted GPA": "4.0000/4.0000", "Weighted GPA": "5.2480/6.0000"}
        return jsonify(gpa_dict)
    except (AttributeError, KeyError, TypeError):
        return jsonify({"status": "error", "msg": "unable to receive info now, please retry"}), 404


# runs the python flask apps
if __name__ == '__main__':
    app.run()
