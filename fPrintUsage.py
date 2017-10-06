from oConsole import oConsole;
from dxConfig import dxConfig;
NORMAL =  0x0F07;  # Console default color
INFO =    0x0F0A;  # Light green (foreground only)
HILITE =  0x0F0F;  # White (foreground only)
ERROR =   0x0F0C;  # Light red (foreground only)

def fPrintUsage(asApplicationKeywords):
  oConsole.fPrint(HILITE,"Usage:");
  oConsole.fPrint();
  oConsole.fPrint(INFO,"  BugId.py [options] \"path\\to\\binary.exe\" [-- argument [argument [...]]]");
  oConsole.fPrint("    Start the binary in the debugger with the provided arguments.");
  oConsole.fPrint();
  oConsole.fPrint(INFO,"  BugId.py [options] --pids=pid[,pid[...]]");
  oConsole.fPrint("    Attach debugger to the process(es) provided in the list. The processes must");
  oConsole.fPrint("    all have been suspended, as they will be resumed by the debugger.");
  oConsole.fPrint();
  oConsole.fPrint(INFO,"  BugId.py [options] --package=[full package name] [-- argument]");
  oConsole.fPrint("    Start and debug the Universal Windows App specified through its package");
  oConsole.fPrint("    name with the provided argument.");
  oConsole.fPrint();
  oConsole.fPrint(INFO,"  BugId.py [options] application [options] [-- argument [argument [...]]]");
  oConsole.fPrint("    (Where \"application\" is a known application keyword, see below)");
  oConsole.fPrint("    BugId has a list of known applications for which it has specific settings,");
  oConsole.fPrint("    can automatically find the binary on your system, or knows the package name,");
  oConsole.fPrint("    and knows what arguments you will probably want to supply. This makes it a");
  oConsole.fPrint("    lot easier to start an application and apply common settings.");
  oConsole.fPrint("    You may be able to overwrite some of these settings by providing different");
  oConsole.fPrint("    values after the keyword. You can also provide a binary path after the");
  oConsole.fPrint("    keyword to use a different binary than BugId detects, or if BugId is unable.");
  oConsole.fPrint("    to detect the binary on your system.");
  oConsole.fPrint();
  oConsole.fPrint(HILITE, "Options:");
  oConsole.fPrint(INFO, "  -h, --help");
  oConsole.fPrint("    This cruft.");
  oConsole.fPrint(INFO, "  -q, --quiet");
  oConsole.fPrint("    Output only essential information.");
  oConsole.fPrint(INFO, "  -v, --verbose");
  oConsole.fPrint("    Output all commands send to cdb.exe and everything it outputs in return.");
  oConsole.fPrint("    Note that -q and -v are not mutually exclusive.");
  oConsole.fPrint(INFO, "  -f, --fast");
  oConsole.fPrint("    Create no HTML report, do not use symbols. This is an alias for:");
  oConsole.fPrint("        ", HILITE, "--bGenerateReportHTML=false");
  oConsole.fPrint("        ", HILITE, "--cBugId.asSymbolServerURLs=[]");
  oConsole.fPrint("        ", HILITE, "--cBugId.bUse_NT_SYMBOL_PATH=false");
  oConsole.fPrint(INFO, "  -r, --repeat");
  oConsole.fPrint("    Restart the application to run another test as soon as the application is");
  oConsole.fPrint("    terminated. Useful when testing the reliability of a repro, detecting the");
  oConsole.fPrint("    various crashes a non-deterministic repro can cause or while making ");
  oConsole.fPrint("    modifications to the repro in order to test how they affect the crash.");
  oConsole.fPrint("    A statistics file is created or updated after each run that contains the");
  oConsole.fPrint("    number of occurances of each Bug Id that was detected.");
  oConsole.fPrint(INFO,"  --isa=x86|x64");
  oConsole.fPrint("    Use the x86 or x64 version of cdb to debug the application. The default is");
  oConsole.fPrint("    to use the ISA* of the OS. Applications build to run on x86 systems can be");
  oConsole.fPrint("    debugged using the x64 version of cdb, and you are strongly encouraged to ");
  oConsole.fPrint("    do so. But you can use the x86 debugger to debug x86 application if you");
  oConsole.fPrint("    want to. (ISA = Instruction Set Architecture)");
  oConsole.fPrint(INFO,"  --version");
  oConsole.fPrint("    Show cBugId version and that of its sub-modules and check for updates.");
  oConsole.fPrint();
  oConsole.fPrint("Options also include any of the settings in dxConfig.py; you can specify them");
  oConsole.fPrint("using ", HILITE, "--[name]=[JSON value]", NORMAL, ". Here are some examples:");
  oConsole.fPrint(INFO,"  --bGenerateReportHTML=false");
  oConsole.fPrint("    Do not save a HTML formatted crash report. This should make BugId run");
  oConsole.fPrint("    faster and use less RAM, as it does not need to gather and process the");
  oConsole.fPrint("    information needed for the HTML report.");
  oConsole.fPrint("    If you only need to confirm a crash can be reproduced, you may want to use");
  oConsole.fPrint("    this: it can make the process of analyzing a crash a lot faster. But if");
  oConsole.fPrint("    no local or cached symbols are available, you'll get less information");
  oConsole.fPrint(INFO,"  \"--sReportFolderPath=\\\"BugId\\\"\"");
  oConsole.fPrint("    Save report to the specified folder, in this case \"BugId\". The quotes");
  oConsole.fPrint("    mess is needed because of the Windows quirck explained below.");
  oConsole.fPrint("The remaining dxConfig settings are:");
  for sSettingName in sorted(dxConfig.keys()):
    if sSettingName not in ["bGenerateReportHTML", "sReportFolderPath", "cBugId", "Kill"]:
      xSettingValue = dxConfig[sSettingName];
      oConsole.fPrint("  ", INFO, "--", sSettingName, NORMAL, " (default value: ", HILITE, str(xSettingValue), NORMAL, ")");
  oConsole.fPrint("See ", HILITE, "dxConfig.py", NORMAL, " for details on each setting.");
  oConsole.fPrint();
  oConsole.fPrint("You can also adjust cBugId specific settings, such as:");
  oConsole.fPrint(INFO,"  --cBugId.bSaveDump=true");
  oConsole.fPrint("    Save a debug dump file when a crash is detected.");
  oConsole.fPrint(INFO,"  --cBugId.asSymbolServerURLs=[\"http://msdl.microsoft.com/download/symbols\"]");
  oConsole.fPrint("    Use http://msdl.microsoft.com/download/symbols as a symbol server.");
  oConsole.fPrint(INFO,"  --cBugId.asSymbolCachePaths=[\"C:\\Symbols\"]");
  oConsole.fPrint("    Use C:\\Symbols to cache symbol files.");
  oConsole.fPrint();
  oConsole.fPrint("See ", HILITE, "cBugId\\dxConfig.py", NORMAL, " for details on all available settings.");
  oConsole.fPrint("All values must be valid JSON of the appropriate type. No checks are made to");
  oConsole.fPrint("ensure this! Providing illegal values may result in exceptions at any time");
  oConsole.fPrint("during execution. You have been warned!");
  oConsole.fPrint();
  oConsole.fPrint("Note that you may need to do a bit of \"quote-juggling\" because Windows likes");
  oConsole.fPrint("to eat quotes for no obvious reason. So, if you want to specify --a=\"b\", you");
  oConsole.fPrint("will need to use \"--a=\\\"b\\\"\", or BugId will see --a=b and `b` is not valid");
  oConsole.fPrint("JSON.");
  oConsole.fPrint();
  oConsole.fPrint("Known application keywords:");
  asLine = ["  "];
  uLineLength = 2;
  for sApplicationKeyword in asApplicationKeywords:
    if uLineLength > 2:
      if uLineLength + 2 + len(sApplicationKeyword) + 2 > 80:
        asLine += [NORMAL, ","];
        oConsole.fPrint(*asLine);
        asLine = ["  "];
        uLineLength = 2;
      else:
        asLine += [NORMAL, ", "];
        uLineLength += 2;
    asLine += [INFO, sApplicationKeyword];
    uLineLength += len(sApplicationKeyword);
  asLine += [NORMAL, "."];
  oConsole.fPrint(*asLine);
  oConsole.fPrint();
  oConsole.fPrint("Run ", HILITE, "BugId.py application?", NORMAL, " for an overview of the application specific command");
  oConsole.fPrint("line arguments and settings.");
  oConsole.fPrint();
  oConsole.fPrint("BugId will set it errorlevel/exit code to one of the following values:");
  oConsole.fPrint("  ", INFO, "0", NORMAL," = BugId successfully ran the application ", HILITE, "without detecting a bug", NORMAL, ".");
  oConsole.fPrint("  ", INFO, "1", NORMAL," = BugId successfully ran the application and ", HILITE, "detected a bug", NORMAL, ".");
  oConsole.fPrint("  ", INFO, "2", NORMAL," = BugId was unable to parse the command-line arguments provided.");
  oConsole.fPrint("  ", INFO, "3", NORMAL," = BugId ran into an internal error: pleace report the details!");
  oConsole.fPrint("  ", INFO, "4", NORMAL," = BugId was unable to start or attach to the application.");
