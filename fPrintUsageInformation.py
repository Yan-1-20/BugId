from oConsole import oConsole;
from dxConfig import dxConfig;
from mColors import *;

def fPrintUsageInformation(asApplicationKeywords):
  oConsole.fLock();
  try:
    oConsole.fPrint(HILITE,"Usage:");
    oConsole.fPrint();
    oConsole.fPrint(INFO,"  BugId.py [options] <target> [options] [-- argument [argument [...]]]");
    oConsole.fPrint();
    oConsole.fPrint(HILITE, "Targets:");
    oConsole.fPrint(INFO, "  \"path\\to\\binary.exe\"");
    oConsole.fPrint("    Start the given binary in the debugger with the given arguments.");
    oConsole.fPrint(INFO,"  --pids=pid[,pid[...]]");
    oConsole.fPrint("    Attach debugger to the process(es) provided in the list. The processes ", HILITE, "must");
    oConsole.fPrint("    all have been suspended, as they will be resumed by the debugger.");
    oConsole.fPrint("    Arguments cannot be provided for obvious reasons.");
    oConsole.fPrint(INFO,"  --uwp-app=<package name>!<application id>");
    oConsole.fPrint("    Start and debug a Universal Windows Platform App identified by the given");
    oConsole.fPrint("    package name and application id. Note that only one argument can be");
    oConsole.fPrint("    passed to a UWP App; additional arguments will be ignored.");
    oConsole.fPrint(INFO,"  <known application keyword>");
    oConsole.fPrint("    BugId has a list of known targets that are identified by a keyword. You can");
    oConsole.fPrint("    use such a keyword to have BugId try to automatically find the binary or");
    oConsole.fPrint("    determine the package name and id for that application, optionally apply");
    oConsole.fPrint("    application specific settings and provide default arguments. This makes it");
    oConsole.fPrint("    easier to run these applications without having to manually provide these.");
    oConsole.fPrint("    You can optioanlly override any default settings by providing them *after*");
    oConsole.fPrint("    the keyword. You can also provide the path to the application binary after");
    oConsole.fPrint("    the keyword to use a different binary than the one BugId automatically");
    oConsole.fPrint("    detects, or if BugId is unable to detect the binary on your system.");
    oConsole.fPrint();
    oConsole.fPrint(HILITE, "Options:");
    oConsole.fPrint(INFO, "  -h, --help");
    oConsole.fPrint("    This cruft.");
    oConsole.fPrint(INFO,"  --version");
    oConsole.fPrint("    Show version information and check for updates.");
    oConsole.fPrint(INFO, "  -q, --quiet");
    oConsole.fPrint("    Output only essential information.");
    oConsole.fPrint(INFO, "  -v, --verbose");
    oConsole.fPrint("    Output all commands send to cdb.exe and everything it outputs in return.");
    oConsole.fPrint("    Note that -q and -v are not mutually exclusive.");
    oConsole.fPrint(INFO,"  --isa=x86|x64");
    oConsole.fPrint("    Use the x86 or x64 version of cdb to debug the application. The default is");
    oConsole.fPrint("    to use the ISA* of the OS. Applications build to run on x86 systems can be");
    oConsole.fPrint("    debugged using the x64 version of cdb, and you are strongly encouraged to ");
    oConsole.fPrint("    do so. But you can use the x86 debugger to debug x86 application if you");
    oConsole.fPrint("    want to. (ISA = Instruction Set Architecture)");
    oConsole.fPrint(INFO,"  --symbols=path/to/symbols/folder");
    oConsole.fPrint("    Use the given path as a local symbol folder in addition to the symbol paths");
    oConsole.fPrint("    specified in dxConfig. You can provide this option multiple times to add");
    oConsole.fPrint("    as many additional local symbol paths as needed.");
    oConsole.fPrint(INFO, "  -c, --collateral[=number of bugs]");
    oConsole.fPrint("    When the specified number of bugs is larger than 1 (default 5), BugId will");
    oConsole.fPrint("    go into \"collateral bug handling\" mode. This means that after certain");
    oConsole.fPrint("    access violation bugs are reported, it will attempt to \"fake\" that the");
    oConsole.fPrint("    instruction that caused the exception succeeded without triggering an");
    oConsole.fPrint("    exception. For read operations, it will set the destination register to a");
    oConsole.fPrint("    tainted value (0x41414141...). For write operations, it will simply step");
    oConsole.fPrint("    over the instruction. It will do this for up to the specified number of");
    oConsole.fPrint("    bugs.");
    oConsole.fPrint("    The upshot of this is that you can get an idea of what would happen if");
    oConsole.fPrint("    you were able to control the bad read/write operation. This can be usedful");
    oConsole.fPrint("    when determining if a particular vulnerability is theoretically exploitable");
    oConsole.fPrint("    or not. E.g. it might show that nothing else happens, that the application");
    oConsole.fPrint("    crashes unavoidably and immediately, both of which indicate that the issue");
    oConsole.fPrint("    is not exploitable. It might also show that reading from or writing to");
    oConsole.fPrint("    otherwise inaccessible parts of memory or controlling execution flow is");
    oConsole.fPrint("    potentially possible, indicating it is exploitable.");
    oConsole.fPrint(INFO, "  -f, --fast");
    oConsole.fPrint("    Create no HTML report, do not use symbols. This is an alias for:");
    oConsole.fPrint("        ", INFO, "--bGenerateReportHTML=false");
    oConsole.fPrint("        ", INFO, "--cBugId.asSymbolServerURLs=[]");
    oConsole.fPrint("        ", INFO, "--cBugId.bUse_NT_SYMBOL_PATH=false");
    oConsole.fPrint(INFO, "  -r, --repeat[=number of loops]");
    oConsole.fPrint("    Restart the application to run another test as soon as the application is");
    oConsole.fPrint("    terminated. Useful when testing the reliability of a repro, detecting the");
    oConsole.fPrint("    various crashes a non-deterministic repro can cause or while making ");
    oConsole.fPrint("    modifications to the repro in order to test how they affect the crash.");
    oConsole.fPrint("    A statistics file is created or updated after each run that contains the");
    oConsole.fPrint("    number of occurances of each Bug Id that was detected. If a number is");
    oConsole.fPrint("    provided, the application will be run that many times. Otherwise the");
    oConsole.fPrint("    application will be run indefinitely.");
    oConsole.fPrint();
    oConsole.fPrint("  Options also include any of the settings in dxConfig.py; you can specify them");
    oConsole.fPrint("  using ", INFO, "--[name]=[JSON value]", NORMAL, ". Here are some examples:");
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
    oConsole.fPrint("  The remaining dxConfig settings are:");
    for sSettingName in sorted(dxConfig.keys()):
      if sSettingName not in ["bGenerateReportHTML", "sReportFolderPath", "cBugId"]:
        xSettingValue = dxConfig[sSettingName];
        oConsole.fPrint("  ", INFO, "--", sSettingName, NORMAL, " (default value: ", INFO, str(xSettingValue), NORMAL, ")");
    oConsole.fPrint("  See ", INFO, "dxConfig.py", NORMAL, " for details on each setting.");
    oConsole.fPrint();
    oConsole.fPrint("  You can also adjust cBugId specific settings, such as:");
    oConsole.fPrint(INFO,"  --cBugId.bSaveDump=true");
    oConsole.fPrint("    Save a debug dump file when a crash is detected.");
    oConsole.fPrint(INFO,"  --cBugId.asSymbolServerURLs=[\"http://msdl.microsoft.com/download/symbols\"]");
    oConsole.fPrint("    Use http://msdl.microsoft.com/download/symbols as a symbol server.");
    oConsole.fPrint(INFO,"  --cBugId.asSymbolCachePaths=[\"C:\\Symbols\"]");
    oConsole.fPrint("    Use C:\\Symbols to cache symbol files.");
    oConsole.fPrint("  See ", INFO, "cBugId\\dxConfig.py", NORMAL, " for details on all available settings.");
    oConsole.fPrint("  All values must be valid JSON of the appropriate type. No checks are made to");
    oConsole.fPrint("  ensure this! Providing illegal values may result in exceptions at any time");
    oConsole.fPrint("  during execution. You have been warned!");
    oConsole.fPrint();
    oConsole.fPrint("  Note that you may need to do a bit of \"quote-juggling\" because Windows likes");
    oConsole.fPrint("  to eat quotes for no obvious reason. So, if you want to specify --a=\"b\", you");
    oConsole.fPrint("  will need to use \"--a=\\\"b\\\"\", or BugId will see --a=b and `b` is not valid");
    oConsole.fPrint("  JSON.");
    oConsole.fPrint();
    oConsole.fPrint(HILITE, "Known application keywords:");
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
    oConsole.fPrint("  Run ", INFO, "BugId.py application?", NORMAL, " for an overview of the application specific command");
    oConsole.fPrint("  line arguments and settings.");
    oConsole.fPrint();
    oConsole.fPrint(HILITE, "Exit codes:");
    oConsole.fPrint("  ", INFO, "0", NORMAL," = BugId successfully ran the application ", UNDERLINE, "without detecting a bug", NORMAL, ".");
    oConsole.fPrint("  ", INFO, "1", NORMAL," = BugId successfully ran the application and ", UNDERLINE, "detected a bug", NORMAL, ".");
    oConsole.fPrint("  ", ERROR_INFO, "2", NORMAL, " = BugId was unable to parse the command-line arguments provided.");
    oConsole.fPrint("  ", ERROR_INFO, "3", NORMAL, " = BugId ran into an internal error: please report the details!");
    oConsole.fPrint("  ", ERROR_INFO, "4", NORMAL, " = BugId was unable to start or attach to the application.");
    oConsole.fPrint("  ", ERROR_INFO, "5", NORMAL, " = You do not have a valid license.");
  finally:
    oConsole.fUnlock();