import os
import csv
# DATA_PATH = "../TestData/"
DATA_PATH = "../Data/"
BLACK_PATH = os.path.join(DATA_PATH, "black_count")
WHITE_PATH = os.path.join(DATA_PATH, "white_count")
API_NAME_LIST = ['HttpOpenRequestA', 'InternetCrackUrlA', 'NtSetContextThread', 'AnalyzeStart', 'KeBugCheck2', 'NtWriteVirtualMemory', 'NtWriteFile', 'DeleteFileW', 'gethostbyname', 'Fake_SetFileCreationTime', 'FindFirstFileExW', 'NtCreateThreadEx', 'NtShutdownSystem', 'GetComputerNameExW', 'NtCreateMutant', 'connect', 'NtReadVirtualMemory', 'Thread32First', 'Process32FirstW', 'listen', 'CreateServiceW', 'CryptExportKey', 'WSARecv', 'KiTrap0D', 'NtDeleteKey', 'WSAConnect', 'AnalyzeStop', 'NtTerminateProcess', 'CreateProcessInternalW', 'URLDownloadToFileW', 'MoveFileWithProgressW', 'WMICreateInstanceEnum', 'Fake_BeInjected', 'InternetCrackUrlW', 'WSARecvFrom', 'GetComputerNameW', 'AutoLogin', 'GetForegroundWindow', 'GetAdaptersAddresses', 'StrangeBehavior', 'CryptGenKey', 'NtSuspendThread', 'OpenSCManagerW', 'WMIExecQuery', 'sendto', 'NtUnloadDriver', 'NtLoadDriver',
                 'Module32FirstW', 'Fake_TerminateRemoteProcess', 'NtReadFile', 'WSASocketW', 'recv', 'NtSetValueKey', 'NtTerminateThread', 'Fake_DetectDebugger', 'EnumServicesStatusExW', 'InternetReadFile', 'Login', 'NtSetSystemInformation', 'StartServiceW', 'GetProcessAffinityMask', 'UnpackSelf', 'EnumServicesStatusA', 'OpenServiceW', 'KiGeneralProtectionFault', 'NtQueryAttributesFile', 'LoadLibraryExW', 'NtDeleteValueKey', 'SetWindowsHookExW', 'CopyFileExW', 'NtSetSystemTime', 'NtCreateFile', 'NtCreateThread', 'EnumServicesStatusW', 'NtQueryDirectoryFile', 'PowerOn', 'VMDetect', 'WMIConnectServer', 'SendARP', 'WSASendTo', 'DeleteService', 'send', 'NtAdjustPrivilegesToken', 'Fake_SetFileHiddenOrReadOnly', 'NtQueryFullAttributesFile', 'Fake_BeCreatedEx', 'NtSuspendProcess', 'recvfrom', 'WSASend', 'TryToAnalyze', 'TooManyBehavior', 'Fake_WritePEFile', 'NtDeleteFile']


def make_api_name_table(csv_file_name, path, label):
    # init csv file
    # 1:black,0:white
    csv_file = open(csv_file_name, "w")
    csv_head = API_NAME_LIST + ["label", "api_name"]
    csv.writer(csv_file).writerow(csv_head)

    folders = os.listdir(path)
    for folder in folders:
        if os.path.isdir(os.path.join(path, folder)):
            files = os.listdir(os.path.join(path, folder))
            f = open(os.path.join(os.path.join(path, folder),
                                  "api_name"), "r")  # read api_name file
            add_row(csv_file, label, folder, f.readlines())
            f.close()
    csv_file.close()


def add_row(csv_file, label, api_name, lines):
    row = [0]*len(API_NAME_LIST) + [label, api_name]  # init all to 0
    for line in lines:
        api_name = line.split(" ")[0]
        api_count = line.split(" ")[1]
        row[API_NAME_LIST.index(api_name)] = api_count
    csv.writer(csv_file).writerow(row)


if __name__ == "__main__":
    make_api_name_table("black_usage.csv", BLACK_PATH, 1)
    make_api_name_table("white_usage.csv", WHITE_PATH, 0)
