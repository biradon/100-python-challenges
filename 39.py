def compare_versions(version1, version2):
    str_version1 = str(version1)
    str_version2 = str(version2)
    if len(str_version1) >= len(str_version2):
        for i in range(len(str_version1)):
            if i > len(str_version2)-1:
                return ">"
            if str_version1[i] != "." and str_version2[i] != ".":
                if int(str_version1[i]) > int(str_version2[i]):
                    return ">"
                elif int(str_version1[i]) < int(str_version2[i]):
                    return "<"
    if len(str_version1) <= len(str_version2):
        for i in range(len(str_version2)):
            if i > len(str_version1)-1:
                return "<"
            if str_version1[i] != "." and str_version2[i] != ".":
                if int(str_version1[i]) > int(str_version2[i]):
                    return ">"
                elif int(str_version1[i]) < int(str_version2[i]):
                    return "<"
    return "="



print(compare_versions("1.11.17","2.3.5"))
print(compare_versions("2.1","2.1.3"))
print(compare_versions("2.3.5","2.4"))
print(compare_versions("3.1","2.4"))
print(compare_versions("3.3","3.2.9"))
print(compare_versions("7.2.71","7.2.71"))
