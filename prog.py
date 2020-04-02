validation_source_samples = open("validation_source_samples.txt", encoding="utf-8").read()
validation_source_labels = open("validation_source_labels.txt").read()
validation_target_samples = open("validation_source_labels.txt", encoding="utf-8").read()
validation_target_labels = open("validation_source_labels.txt").read()

def get_freq_dic(text):
    ap_dic = {}

    for ch in text:
        if ch in ap_dic:
            ap_dic[ch] += 1
        else:
            ap_dic[ch] = 1

    freq_dic = ap_dic

    for key, val in freq_dic.items():
        val2 = val / len(text)
        freq_dic[key] = val2

    #print(freq_dic)
    return freq_dic


def merge_dict(new_dict, big_dict):
    return (big_dict.update(new_dict))


def filter_text(text, labels, rdi):
    text2 = []
    text = text.splitlines()
    labels = labels.splitlines()
    i = 0
    for line in text:
        if labels[i][7:] == rdi:
            text2.append(line)
        i += 1

    return text2


def get_med_freq(text, labels, rdi):
    if rdi == "RO":
        text = filter_text(text,labels,'1')
    elif rdi == "MD":
        text = filter_text(text,labels,'0')
    else:
        raise Exception('Wrong RDI!')

    ch_dic = {}
    dict_list = []
    size = 0
    for line in text:
        text = (line[7:])
        freq_dic = get_freq_dic(text)
        merge_dict(freq_dic, ch_dic)
        size += 1
        dict_list.append(freq_dic)

    for ch, fr in ch_dic.items():
        ch_dic[ch] = 0

    for dic in dict_list:
        for ch, fr in dic.items():
            ch_dic[ch] += dic[ch]

    for ch, fr in ch_dic.items():
        fr_med = fr/size
        ch_dic[ch] = fr_med

    return ch_dic

med_freq_source_0 = get_med_freq(validation_source_samples, validation_source_labels, "RO")
med_freq_source_1 = get_med_freq(validation_source_samples, validation_source_labels, "MD")

med_freq_target_0 = get_med_freq(validation_target_samples, validation_target_labels, "RO")
med_freq_target_1 = get_med_freq(validation_target_samples, validation_target_labels, "MD")


print("\n-------------------------\n")

#chars_dic = get_chars_dic(text)