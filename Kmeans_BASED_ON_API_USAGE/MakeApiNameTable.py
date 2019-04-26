import os
import csv
# DATA_PATH = "../TestData/"
DATA_PATH = "../Data/"
COUNT_PATH = os.path.join(DATA_PATH, "count")
API_NAME_LIST = ['NtWriteVirtualMemory', 'WSASocketW', 'InternetOpenUrlA', 'OpenSCManagerW', 'MoveFileWithProgressW', 'CopyFileExW', 'AnalyzeStop', 'NtCreateMutant', 'WSASend', 'StartServiceW', 'NtCreateThreadEx', 'NtQueryAttributesFile', 'WMICreateInstanceEnum', 'WSARecv', 'TooManyBehavior', 'Fake_SetFileCreationTime', 'StrangeBehavior', 'DeleteFileW', 'NtCreateThread', 'WMIExecQuery', 'NtAdjustPrivilegesToken', 'NtLoadDriver', 'NtQueryDirectoryFile', 'DeleteService', 'WSAConnect', 'TryToAnalyze', 'NtSuspendThread', 'KeBugCheck2', 'InternetConnectA', 'HttpOpenRequestA', 'InternetCrackUrlA', 'NtDeleteKey', 'Login', 'URLDownloadToFileW', 'Process32FirstW', 'LoadLibraryExW', 'NtSetSystemTime', 'CreateServiceW', 'SendARP', 'RemoveDirectoryW', 'VMDetect', 'InternetReadFile', 'GetComputerNameExW', 'NtWriteFile', 'Fake_SetFileHiddenOrReadOnly', 'KiTrap0D', 'NtSetSystemInformation', 'NtDeleteFile', 'CryptExportKey', 'send',
                 'KiGeneralProtectionFault', 'Fake_BeCreatedEx', 'AnalyzeStart', 'recv', 'EnumServicesStatusExW', 'NtCreateFile', 'FindFirstFileExW', 'Thread32First', 'Fake_WritePEFile', 'AutoLogin', 'PowerOn', 'WSASendTo', 'CreateDirectoryW', 'CoCreateInstanceEx', 'NtUnloadDriver', 'InternetCrackUrlW', 'NtTerminateProcess', 'GetForegroundWindow', 'listen', 'NtDeleteValueKey', 'Fake_DetectDebugger', 'Module32FirstW', 'gethostbyname', 'NtShutdownSystem', 'WSARecvFrom', 'connect', 'GetComputerNameW', 'WMIConnectServer', 'EnumServicesStatusW', 'sendto', 'NtSetContextThread', 'DnsQuery_A', 'recvfrom', 'CoGetClassObject', 'Fake_TerminateRemoteProcess', 'DnsQuery_W', 'SetWindowsHookExW', 'NtQueryFullAttributesFile', 'NtSetValueKey', 'CreateDirectoryExW', 'EnumServicesStatusA', 'NtReadVirtualMemory', 'NtReadFile', 'NtTerminateThread', 'OpenServiceW', 'CryptGenKey', 'UnpackSelf', 'Fake_BeInjected', 'CreateProcessInternalW', 'GetAdaptersAddresses']


def make_api_name_table(csv_file_name, path, label):
    # init csv file
    # 1:black,0:white,-1:test
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
    make_api_name_table("api_usage.csv", COUNT_PATH, -1)
