import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'dart:io';
import 'dart:convert';
import 'dart:async';
import 'package:bottom_navy_bar/bottom_navy_bar.dart';
import 'home_app.dart';
import 'grades_app.dart';
import 'extra_app.dart';
import 'settings_app.dart';
import 'package:flutter/services.dart';
import 'package:flare_splash_screen/flare_splash_screen.dart';
import 'package:flutter_spinkit/flutter_spinkit.dart';
import 'package:shared_preferences/shared_preferences.dart';

void main() {
  runApp(new MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    SystemChrome.setPreferredOrientations([
      DeviceOrientation.portraitUp,
    ]);

    return MaterialApp(
      builder: (context, child) {
        return ScrollConfiguration(
          behavior: MyBehavior(),
          child: child,
        );
      },
      title: 'Grade Genius',
      theme: ThemeData(
        primaryColor: Colors.cyan,
      ),
      home: SplashScreen(
        'assets/splashIntro.flr',
        MyLoginPage(),
        startAnimation: 'Untitled',
        backgroundColor: Colors.black,
      ),
    );
  }
}

class MyBehavior extends ScrollBehavior {
  @override
  Widget buildViewportChrome(
      BuildContext context, Widget child, AxisDirection axisDirection) {
    return child;
  }
}

class MyLoginPage extends StatefulWidget {
  @override
  _LoginPage createState() => _LoginPage();
}

class DataInfo {
  List dateList;
  String user;
  String studentGrade;
  String studentName;
  String studentID;
  String studentSchool;
  String reportRun;
  Map classAverages;
  Map classAssignments;
  List myCookies;
  List newAssignments;
  List newScores;
  List newClasses;
  DataInfo({
    this.dateList,
    this.user,
    this.studentGrade,
    this.studentID,
    this.studentName,
    this.studentSchool,
    this.reportRun,
    this.classAverages,
    this.classAssignments,
    this.myCookies,
    this.newAssignments,
    this.newScores,
    this.newClasses,
  });
}

class _LoginPage extends State<MyLoginPage> {
  String loginUrl = '';
  var infoList = '';
  var username = TextEditingController();
  var password = TextEditingController();
  List<Cookie> myCookies = [];

  // local Android host url = 'http://10.0.2.2:5000/'
  // app url = 'https://gradegenius.org/'
  String host = 'http://10.0.2.2:5000/';
  bool isLoggedIn = false;
  bool gotInfo = false;
  var client = HttpClient();
  bool textVisible = false;
  bool isLoading = false;
  String errorMessage = '';
  String user = '';
  String pass = '';
  bool isError = false;
  bool gradeError = false;
  String userPassError;
  bool _obscureText = true;
  bool displayLoad = false;
  var loginButton;
  var dataLoginPage;
  bool error = false;
  String oldClassString = "";
  String currentClassString = "";
  Map oldMap;
  Map currentMap;
  String oldC = "";
  String currentC = "";
  Map oldClassesMap;
  Map currentClassesMap;
  List diffAssignments = [];
  List diffScores = [];
  List diffClasses = [];
  String oldReportRun = "";

  Future<HttpClientResponse> makeRequest(
      Uri uri, List<Cookie> requestCookies) async {
    var request = await client.getUrl(uri);
    print(uri);
    request.cookies.addAll(requestCookies);
    request.followRedirects = false;
    return await request.close();
  }

  Future mainInfo(loginUrl) async {
    var response = await makeRequest(
      Uri.parse(loginUrl),
      [Cookie('user', user), (Cookie('pass', pass))],
    );
    if (response.statusCode == 401) {
      setState(() {
        isLoggedIn = false;
      });
    } else {
      setState(() {
        isLoading = true;
        textVisible = false;
      });
      Uri location = Uri.parse(response.headers[HttpHeaders.locationHeader][0]);
      setState(() {
        myCookies = response.cookies;
      });
      setState(() {
        isLoggedIn = true;
      });
      response = await makeRequest(location, response.cookies);
      if (response.statusCode == 404 || response.statusCode == 500) {
        setState(() {
          isLoading = false;
          gradeError = true;
          gotInfo = true;
          errorMessage =
              'HAC Servers are probably down. Please try again later.';
        });
      }
      final completer = Completer<String>();
      final contents = StringBuffer();
      response.transform(utf8.decoder).listen((data) {
        contents.write(data);
      }, onDone: () => completer.complete(contents.toString()));
      return await completer.future;
    }
  }

  Future<bool> _willPopCallback() async {
    return false;
  }

  addStringToSF(oldString, name) async {
    SharedPreferences prefs = await SharedPreferences.getInstance();
    prefs.setString(name + ' oldClassString', oldString);
  }

  getStringValuesSF(name) async {
    SharedPreferences prefs = await SharedPreferences.getInstance();
    String stringValue = prefs.get(name + ' oldClassString');
    return (stringValue.toString());
  }

  checkAvailable(name) async {
    SharedPreferences prefs = await SharedPreferences.getInstance();
    bool checkVal = prefs.containsKey(name + ' oldClassString');
    return checkVal;
  }

  addStringToSF2(oldString, name) async {
    SharedPreferences prefs = await SharedPreferences.getInstance();
    prefs.setString(name + ' oldClasses', oldString);
  }

  getStringValuesSF2(name) async {
    SharedPreferences prefs = await SharedPreferences.getInstance();
    String stringValue = prefs.get(name + ' oldClasses');
    return (stringValue.toString());
  }

  checkAvailable2(name) async {
    SharedPreferences prefs = await SharedPreferences.getInstance();
    bool checkVal = prefs.containsKey(name + ' oldClasses');
    return checkVal;
  }

  addRun(oldRun, name) async {
    SharedPreferences prefs = await SharedPreferences.getInstance();
    prefs.setString(name + ' run', oldRun);
  }

  getRun(name) async {
    SharedPreferences prefs = await SharedPreferences.getInstance();
    String stringValue = prefs.get(name + ' run');
    return (stringValue.toString());
  }

  checkAvailableRun(name) async {
    SharedPreferences prefs = await SharedPreferences.getInstance();
    bool checkVal = prefs.containsKey(name + ' run');
    return checkVal;
  }

  @override
  Widget build(BuildContext context) {
    void _toggle() {
      setState(() {
        _obscureText = !_obscureText;
      });
    }

    void differenceMethod() async {
      String studentName = dataLoginPage.studentName;
      String currentReportRun = dataLoginPage.reportRun;
      try {
        if (checkAvailableRun(studentName) == false) {
          await addRun(currentReportRun, studentName);
        }
        if (checkAvailable(studentName) == false &&
            checkAvailable2(studentName) == false) {
          await addStringToSF(
              (json.encode(dataLoginPage.classAssignments).toString()),
              studentName);
          await addStringToSF2(
              (json.encode(dataLoginPage.classAverages).toString()),
              studentName);
        } else {
          currentClassString =
              json.encode(dataLoginPage.classAssignments).toString();
          oldClassString = await getStringValuesSF(studentName);
          currentC = json.encode(dataLoginPage.classAverages).toString();
          oldC = await getStringValuesSF2(studentName);
          oldReportRun = await getRun(studentName);
          await addRun(currentReportRun, studentName);
          await addStringToSF2(
              (json.encode(dataLoginPage.classAverages).toString()),
              studentName);
          await addStringToSF(
              (json.encode(dataLoginPage.classAssignments).toString()),
              studentName);
        }

        if (currentReportRun == oldReportRun) {
          oldMap = await json.decode(oldClassString);
          currentMap = await json.decode(currentClassString);
          oldClassesMap = await json.decode(oldC);
          currentClassesMap = await json.decode(currentC);

          List oldAssignments = [];
          List oldScores = [];
          List oldClasses = [];
          List currAssignments = [];
          List currScores = [];
          List currClasses = [];
          for (int index = 0;
              index < currentClassesMap['Class Name'].length;
              index++) {
            String indexName = "Class " + (index + 1).toString();
            oldAssignments.add(oldMap[indexName]['Assignments']);
            oldScores.add(oldMap[indexName]['Score']);
            oldClasses.add(oldClassesMap['Class Name'][index]);
            currAssignments.add(currentMap[indexName]['Assignments']);
            currScores.add(currentMap[indexName]['Score']);
            currClasses.add(currentClassesMap['Class Name'][index]);
          }

          int value = 0;
          for (int index = 0; index < currAssignments.length; index++) {
            value = 0;
            currAssignments[index].forEach((element) {
              if (!oldAssignments[index].contains(element)) {
                diffAssignments.add(element);
                diffScores.add(currScores[index][value]);
                diffClasses.add(currClasses[index]);
              }
              value++;
            });
          }
        } else {
          diffAssignments = [];
          diffScores = [];
          diffClasses = [];
        }
      } on RangeError {
        setState(() {
          error = true;
        });
      } on NoSuchMethodError {
        setState(() {
          error = true;
        });
      } on FormatException {
        setState(() {
          error = true;
        });
      } on Error {
        setState(() {
          error = true;
        });
      }
    }

    if (displayLoad == false) {
      loginButton = Container(
        child: InkWell(
          child: Container(
            width: 300,
            height: 50,
            alignment: Alignment.center,
            decoration: ShapeDecoration(
              shape: RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(30.0),
              ),
              gradient: LinearGradient(
                colors: [
                  Colors.amber,
                  Colors.orangeAccent[700],
                  Colors.redAccent[400],
                ],
                begin: Alignment.topLeft,
                end: Alignment.bottomRight,
              ),
            ),
            child: Text(
              'LOGIN',
              style: GoogleFonts.quicksand(
                textStyle: TextStyle(
                  fontWeight: FontWeight.bold,
                  fontSize: 21.5,
                  color: Colors.white,
                ),
              ),
            ),
          ),
          onTap: () async {
            try {
              setState(() {
                errorMessage = '';
                gotInfo = false;
                _obscureText = true;
                displayLoad = true;
              });
              FocusScope.of(context).unfocus();
              var gradesList = '';
              if (loginUrl == '' || user == '' || pass == '') {
                setState(() {
                  isError = true;
                });
              }
              if (isError == false) {
                gradesList = await mainInfo(loginUrl);
              }
              if (isLoggedIn == true && gradeError == false) {
                setState(() {
                  gotInfo = true;
                });
                Map infoMap;
                Map averagesMap;
                Map assignmentsMap;
                List dates;
                var currMap;
                String reportRun;
                setState(
                  () {
                    currMap = json.decode(gradesList);
                    infoMap = currMap['Info'];
                    averagesMap = currMap['Averages'];
                    dates = currMap["Date List"];
                    assignmentsMap = currMap['Grades'];
                    reportRun = currMap['Report Run'];
                  },
                );
                dataLoginPage = DataInfo(
                  dateList: dates,
                  user: user,
                  studentGrade: (infoMap['Grade']),
                  studentName: (infoMap['Name']),
                  studentID: (infoMap['ID']),
                  studentSchool: (infoMap['Home Campus']),
                  reportRun: (reportRun),
                  classAverages: averagesMap,
                  classAssignments: assignmentsMap,
                  myCookies: myCookies,
                );
                differenceMethod();
                final dataLoginPage2 = DataInfo(
                  dateList: dates,
                  user: user,
                  studentGrade: (infoMap['Grade']),
                  studentName: (infoMap['Name']),
                  studentID: (infoMap['ID']),
                  studentSchool: (infoMap['Home Campus']),
                  reportRun: (reportRun),
                  classAverages: averagesMap,
                  classAssignments: assignmentsMap,
                  myCookies: myCookies,
                  newAssignments: diffAssignments,
                  newScores: diffScores,
                  newClasses: diffClasses,
                );
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (context) => MyWelcomePage(
                      dataHomePage: dataLoginPage2,
                    ),
                  ),
                );
              }
              if (gotInfo == false) {
                setState(() {
                  displayLoad = false;
                  textVisible = true;
                  password.clear();
                  errorMessage =
                      'Username and/or password is incorrect. Please try again.';
                  isError = false;
                });
              }
            } on NoSuchMethodError {
              gradeError = true;
              isLoading = false;
            } on HttpException {
              gradeError = true;
              isLoading = false;
            } on Error {
              gradeError = true;
              isLoading = false;
            }
          },
        ),
      );
    } else {
      loginButton = Center(
        child: SizedBox(
          height: 20.0,
          child: SpinKitWave(
            color: Colors.grey,
          ),
        ),
      );
    }

    var loadingIndicator = isLoading
        ? new WillPopScope(
            onWillPop: _willPopCallback,
            child: Container(
              child: Stack(
                children: <Widget>[
                  Container(
                    alignment: AlignmentDirectional.center,
                    decoration: BoxDecoration(
                      color: Colors.grey[100],
                    ),
                    child: Container(
                      decoration: BoxDecoration(
                          borderRadius: BorderRadius.circular(10.0)),
                      width: 300.0,
                      height: 200.0,
                      alignment: AlignmentDirectional.center,
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.center,
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: <Widget>[
                          Center(
                            child: SizedBox(
                              height: 50.0,
                              width: 50.0,
                              child: SpinKitFadingCircle(
                                color: Colors.grey[600],
                              ),
                            ),
                          ),
                          Container(
                            margin: const EdgeInsets.only(top: 25.0),
                            child: Center(
                              child: Text(
                                'Loading Grades...',
                                style: GoogleFonts.patrickHand(
                                  fontSize: 25,
                                  color: Colors.grey[700],
                                ),
                              ),
                            ),
                          ),
                        ],
                      ),
                    ),
                  ),
                ],
              ),
            ),
          )
        : new Container();

    var serverDown = gradeError
        ? new WillPopScope(
            onWillPop: _willPopCallback,
            child: Container(
              alignment: AlignmentDirectional.center,
              decoration: BoxDecoration(
                color: Colors.white70,
              ),
              child: AlertDialog(
                title: Text(
                  '404 Data Error',
                  style: GoogleFonts.roboto(
                    fontSize: 21,
                    fontWeight: FontWeight.bold,
                  ),
                ),
                content: Text(
                  'Grade Genius could not load the data. The HAC servers are probably down. Please try again later.',
                  style: GoogleFonts.roboto(
                    fontSize: 16,
                  ),
                ),
                actions: <Widget>[
                  FlatButton(
                    child: Text(
                      'OK',
                      style: GoogleFonts.roboto(
                        fontSize: 19.5,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                    onPressed: () {
                      setState(() {
                        gradeError = false;
                      });
                    },
                  ),
                ],
              ),
            ),
          )
        : new Container();

    Shader linearGradient1 = LinearGradient(
      colors: <Color>[
        Colors.red[900],
        Colors.orangeAccent[700],
        Colors.amber,
        Colors.green[400],
      ],
    ).createShader(
      Rect.fromLTWH(0.0, 0.0, 275.0, 0),
    );

    Shader linearGradient2 = LinearGradient(
      colors: <Color>[
        Colors.greenAccent[400],
        Colors.teal[300],
        Colors.cyan[400],
        Colors.purple[400],
        Colors.pinkAccent,
      ],
    ).createShader(
      Rect.fromLTWH(0.0, 0.0, 300.0, 0),
    );

    return WillPopScope(
      onWillPop: _willPopCallback,
      child: Scaffold(
        backgroundColor: Colors.white,
        resizeToAvoidBottomInset: false,
        body: Stack(
          children: <Widget>[
            Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: <Widget>[
                Container(
                  alignment: Alignment.center,
                  child: Text(
                    'GRADE',
                    style: GoogleFonts.galindo(
                      textStyle: TextStyle(
                        shadows: <Shadow>[
                          Shadow(
                            offset: Offset(7, 5),
                            blurRadius: 3.0,
                            color: Colors.grey[300],
                          ),
                        ],
                        foreground: Paint()..shader = linearGradient1,
                        fontSize: 40.0,
                        height: .7,
                        letterSpacing: 2,
                      ),
                    ),
                  ),
                ),
                Image.asset(
                  'assets/AtomImage.JPG',
                  width: 165,
                  height: 165,
                ),
                Container(
                  alignment: Alignment.center,
                  child: Text(
                    'GENIUS',
                    style: GoogleFonts.galindo(
                      textStyle: TextStyle(
                        shadows: <Shadow>[
                          Shadow(
                            offset: Offset(7, 5),
                            blurRadius: 3.0,
                            color: Colors.grey[300],
                          ),
                        ],
                        foreground: Paint()..shader = linearGradient2,
                        fontSize: 40.0,
                        height: 1,
                        letterSpacing: 2,
                      ),
                    ),
                  ),
                ),
                Padding(
                  padding: EdgeInsets.only(top: 25),
                ),
                Padding(
                  padding: EdgeInsets.all(16.0),
                  child: Align(
                    alignment: Alignment.center,
                    child: Column(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: <Widget>[
                        Material(
                          elevation: 20,
                          shape: RoundedRectangleBorder(
                            borderRadius: BorderRadius.only(
                              topRight: Radius.circular(30.0),
                              bottomLeft: Radius.circular(30.0),
                            ),
                          ),
                          child: Container(
                            child: TextField(
                              maxLines: 1,
                              controller: username,
                              decoration: new InputDecoration(
                                border: InputBorder.none,
                                hintText: 'Username',
                                contentPadding: EdgeInsets.all(30.0),
                              ),
                              style: GoogleFonts.scada(
                                textStyle: TextStyle(
                                  letterSpacing: 1.4,
                                  fontSize: 22.0,
                                  color: Colors.black,
                                ),
                              ),
                            ),
                          ),
                        ),
                        Padding(
                          padding: EdgeInsets.all(10.0),
                        ),
                        Material(
                          elevation: 25,
                          shape: RoundedRectangleBorder(
                            borderRadius: BorderRadius.only(
                              topRight: Radius.circular(30.0),
                              bottomLeft: Radius.circular(30.0),
                            ),
                          ),
                          child: Row(
                            children: [
                              Expanded(
                                child: TextField(
                                  maxLines: 1,
                                  controller: password,
                                  onChanged: (x) {
                                    user = username.text;
                                    user = user.trim();
                                    pass = password.text;
                                    pass = pass.trim();
                                    loginUrl = host + 'login';
                                  },
                                  decoration: InputDecoration(
                                    border: InputBorder.none,
                                    hintText: 'Password',
                                    contentPadding: EdgeInsets.all(30.0),
                                  ),
                                  obscureText: _obscureText,
                                  style: GoogleFonts.scada(
                                    textStyle: TextStyle(
                                      letterSpacing: 1.4,
                                      fontSize: 22.0,
                                      color: Colors.black,
                                    ),
                                  ),
                                  textInputAction: TextInputAction.go,
                                ),
                              ),
                              IconButton(
                                onPressed: _toggle,
                                icon: Icon(Icons.remove_red_eye),
                                iconSize: 27,
                                color: Colors.grey,
                              ),
                              Padding(
                                padding: EdgeInsets.only(left: 10),
                              ),
                            ],
                          ),
                        ),
                      ],
                    ),
                  ),
                ),
                Container(
                  child: Text(
                    errorMessage,
                    textAlign: TextAlign.center,
                    style: GoogleFonts.heebo(
                      textStyle: TextStyle(
                        fontSize: 19.0,
                        color: Colors.red[600],
                      ),
                    ),
                  ),
                ),
                Padding(
                  padding: EdgeInsets.all(20),
                ),
                loginButton,
                Padding(
                  padding: EdgeInsets.all(10),
                ),
                InkWell(
                  child: Container(
                    width: 300,
                    height: 50,
                    alignment: Alignment.center,
                    decoration: ShapeDecoration(
                      shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(30.0),
                      ),
                      gradient: LinearGradient(
                        colors: [
                          Colors.greenAccent[400],
                          Colors.teal[300],
                          Colors.cyan[400],
                        ],
                        begin: Alignment.topLeft,
                        end: Alignment.bottomRight,
                      ),
                    ),
                    child: Text(
                      'Terms of Service',
                      style: GoogleFonts.oxygen(
                        textStyle: TextStyle(
                          fontWeight: FontWeight.bold,
                          fontSize: 21.5,
                          color: Colors.white,
                        ),
                      ),
                    ),
                  ),
                  onTap: () {},
                ),
              ],
            ),
            Align(
              child: loadingIndicator,
              alignment: FractionalOffset.center,
            ),
            Align(
              child: serverDown,
              alignment: FractionalOffset.center,
            ),
          ],
        ),
      ),
    );
  }
}

class MyWelcomePage extends StatefulWidget {
  final DataInfo dataHomePage;
  MyWelcomePage({this.dataHomePage});

  @override
  WelcomePage createState() => WelcomePage();
}

class WelcomePage extends State<MyWelcomePage> {
  Future<bool> _willPopCallback() async {
    return false;
  }

  int _selectedTabIndex = 0;

  Widget callPage(_selectedTabIndex) {
    switch (_selectedTabIndex) {
      case 0:
        return MyHomeApp(
          dataHomePage2: widget.dataHomePage,
        );
      case 1:
        return MyGradePage(
          dataGrades: widget.dataHomePage,
        );
      case 2:
        return MyExtrasPage(
          dataExtras: widget.dataHomePage,
        );
      case 3:
        return SettingsApp();

        break;
      default:
        return MyHomeApp();
    }
  }

  @override
  Widget build(BuildContext context) {
    return WillPopScope(
      onWillPop: _willPopCallback,
      child: Scaffold(
        body: callPage(_selectedTabIndex),
        bottomNavigationBar: BottomNavyBar(
          selectedIndex: _selectedTabIndex,
          showElevation: true,
          containerHeight: 63.0,
          onItemSelected: (index) => setState(() {
            _selectedTabIndex = index;
          }),
          items: [
            BottomNavyBarItem(
              icon: Icon(Icons.apps),
              title: Text(
                'Home',
                style: GoogleFonts.oswald(
                  textStyle: TextStyle(
                      fontSize: 20.0,
                      height: 1.2,
                      color: Colors.cyanAccent[700]),
                ),
              ),
              activeColor: Colors.cyanAccent[700],
              textAlign: TextAlign.center,
            ),
            BottomNavyBarItem(
              icon: Icon(Icons.assignment),
              title: Text(
                'Grades',
                style: GoogleFonts.oswald(
                  textStyle: TextStyle(
                      fontSize: 20.0, height: 1.2, color: Colors.red[400]),
                ),
              ),
              activeColor: Colors.red[400],
              textAlign: TextAlign.center,
            ),
            BottomNavyBarItem(
              icon: Icon(Icons.school),
              title: Text(
                'Extra',
                style: GoogleFonts.oswald(
                  textStyle: TextStyle(
                      fontSize: 20.0, height: 1.2, color: Colors.amber),
                ),
              ),
              activeColor: Colors.amber,
              textAlign: TextAlign.center,
            ),
            BottomNavyBarItem(
              icon: Icon(Icons.settings),
              title: Text(
                'Settings',
                style: GoogleFonts.oswald(
                  textStyle: TextStyle(
                      fontSize: 20.0, height: 1.2, color: Colors.blueGrey[800]),
                ),
              ),
              activeColor: Colors.blueGrey[800],
              textAlign: TextAlign.center,
            ),
          ],
        ),
      ),
    );
  }
}
