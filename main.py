file = open("example_input.txt" , "r")
line = file.readline()
lines = []
while line :
    lines.append(line)
    line = file.readline()
file.close()

output_list = []
for i in range(len(lines)):
    if(lines == " "):
        output_list.append("\n")
    else:
        word = lines[i]
        word = word.rstrip()
        words = word.split(" ")
        flag = True
        while flag:
            try:
                if(words.__contains__("%")):
                    index = words.index("%")
                    words[index - 1] = float(words[index - 1]) % float(words[index + 1])
                    words.remove(words[index])
                    words.remove(words[index])
                elif(words.__contains__("**")):
                    index = words.index("**")
                    words[index - 1] = float(words[index - 1]) ** float(words[index + 1])
                    words.remove(words[index])
                    words.remove(words[index])
                elif(words.__contains__("*") or words.__contains__("/") or words.__contains__("//")):
                    if(words.__contains__("*") and words.__contains__("/") and words.__contains__("//")):
                        if (words.index("*") < words.index("/") and words.index("x") < words.index("//")):
                            index = words.index("*")
                            words[index - 1] = float(words[index - 1]) * float(words[index + 1])
                            words.remove(words[index])
                            words.remove(words[index])
                        elif (words.index("/") < words.index("*") and words.index("/") < words.index("//")):
                            index = words.index("/")
                            words[index - 1] = float(words[index - 1]) / float(words[index + 1])
                            words.remove(words[index])
                            words.remove(words[index])
                        elif (words.index("//") < words.index("*") and words.index("//") < words.index("/")):
                            index = words.index("//")
                            words[index - 1] = float(words[index - 1]) // float(words[index + 1])
                            words.remove(words[index])
                            words.remove(words[index])
                    elif(words.__contains__("*") and words.__contains__("/")):
                        if (words.index("*") < words.index("/")):
                            index = words.index("*")
                            words[index - 1] = float(words[index - 1]) * float(words[index + 1])
                            words.remove(words[index])
                            words.remove(words[index])
                        else:
                            index = words.index("/")
                            words[index - 1] = float(words[index - 1]) / float(words[index + 1])
                            words.remove(words[index])
                            words.remove(words[index])
                    elif(words.__contains__("*") and words.__contains__("//")):
                        if (words.index("*") < words.index("//")):
                            index = words.index("*")
                            words[index - 1] = float(words[index - 1]) * float(words[index + 1])
                            words.remove(words[index])
                            words.remove(words[index])
                        else:
                            index = words.index("//")
                            words[index - 1] = float(words[index - 1]) // float(words[index + 1])
                            words.remove(words[index])
                            words.remove(words[index])
                    elif(words.__contains__("/") and words.__contains__("//")):
                        if (words.index("/") < words.index("//")):
                            index = words.index("/")
                            words[index - 1] = float(words[index - 1]) / float(words[index + 1])
                            words.remove(words[index])
                            words.remove(words[index])
                        else:
                            index = words.index("//")
                            words[index - 1] = float(words[index - 1]) // float(words[index + 1])
                            words.remove(words[index])
                            words.remove(words[index])
                    else:
                        if(words.__contains__("*")):
                            index = words.index("*")
                            words[index - 1] = float(words[index - 1]) * float(words[index + 1])
                            words.remove(words[index])
                            words.remove(words[index])
                        elif(words.__contains__("/")):
                            index = words.index("/")
                            words[index - 1] = float(words[index - 1]) / float(words[index + 1])
                            words.remove(words[index])
                            words.remove(words[index])
                        else:
                            index = words.index("//")
                            words[index - 1] = float(words[index - 1]) // float(words[index + 1])
                            words.remove(words[index])
                            words.remove(words[index])

                elif(words.__contains__("+") or words.__contains__("-")):
                    if(words.__contains__("+")):
                        index = words.index("+")
                        words[index - 1] = float(words[index - 1]) + float(words[index + 1])
                        words.remove(words[index])
                        words.remove(words[index])
                    else:
                        index = words.index("-")
                        words[index - 1] = float(words[index - 1]) - float(words[index + 1])
                        words.remove(words[index])
                        words.remove(words[index])
                elif(words.__contains__(">") or words.__contains__("<") or words.__contains__("==") or words.__contains__(">=") or words.__contains__("<=") or
                         words.__contains__("!=")):
                    if(words.__contains__(">")):
                        index = words.index(">")
                        words[index - 1] = float(words[index - 1]) > float(words[index + 1])
                        words.remove(words[index])
                        words.remove(words[index])
                    elif(words.__contains__("<")):
                        index = words.index("<")
                        words[index - 1] = float(words[index - 1]) < float(words[index + 1])
                        words.remove(words[index])
                        words.remove(words[index])
                    elif(words.__contains__("==")):
                        if(type(words[index - 1] or words[index + 1]) == bool):
                            output_list.append("ERORE")
                            break
                        index = words.index("==")
                        words[index - 1] = float(words[index - 1]) == float(words[index + 1])
                        words.remove(words[index])
                        words.remove(words[index])
                    elif(words.__contains__(">=")):
                        index = words.index(">=")
                        words[index - 1] = float(words[index - 1]) >= float(words[index + 1])
                        words.remove(words[index])
                        words.remove(words[index])
                    elif(words.__contains__("<=")):
                        index = words.index("<=")
                        words[index - 1] = float(words[index - 1]) <= float(words[index + 1])
                        words.remove(words[index])
                        words.remove(words[index])
                    else:
                        index = words.index("!=")
                        words[index - 1] = float(words[index - 1]) != float(words[index + 1])
                        words.remove(words[index])
                        words.remove(words[index])
                if(len(words) == 1):
                    output_list.append(words[0])
                    break
                elif(len(words) == 2):
                    output_list.append("ERORE")
                    break

            except:
                output_list.append("ERORE")
                break

for i in range(len(output_list)):
    if(output_list[i] == "ERORE" or output_list[i] == True or output_list[i] == False or output_list[i] == '' or type(output_list[i]) == float):
        output_list[i] = str(output_list[i]) + "\n"
    else:
        output_list[i] = "ERORE" + "\n"

print(output_list)

filename = ('output.txt')
outfile = open(filename, 'w')
outfile.writelines(output_list)
outfile.close()