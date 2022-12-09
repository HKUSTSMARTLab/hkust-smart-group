import csv
test = "ap chest reviewed in the absence of prior chest radiographs: tip of the right pic line ends at the level 2.5 cm below the carina in the low svc. lung volumes are quite low, reflected in moderately severe bibasilar atelectasis. upper lungs are clear. the heart is normal size. slight displacement of the trachea to the right at the thoracic inlet could be due to an enlarged left thyroid lobe. clinical correlation advised. heart size is normal. there is no pulmonary edema and the upper lungs are clear. pleural effusions are small if any."
print(len(test))

##with open('test.csv', newline='') as csvfile:
 # reader = csv.DictReader(csvfile)
 # total_paper = 0
 # for row in reader:
 #   total_paper += 1
 #   print('''<small><a href="'''+row['URL']+'''">'''+ row['Title'] + "</a></small><i><small><small><br>"+row['Authors']+'.'+row['Source']+'</br></small></small></i>\n')

# line = line.replace('\n','')
# content = line.split('\t')
if 'findings:' in row[1]:
  text = row[1].split('findings:')[1].strip()
  text = text.split('impression:')[0].strip()
elif 'impression:' in row[1]:
  text = row[1].split('impression:')[1].strip()
else:
  text = ''
# text = row[1].split('findings:')
# if len(text)==2:
#    row[1] = text[1]
sentence = text.split('.')
new_sentence = []
current_length = 0
#    for i in sentences:
#        if ('___' not in i) or ('impression' in i):
#            new_sentence.append(i)
#            current_length += len(i#)
#        if current_length>880:
#            break
for i in sentence:
  if len(i) > 0 and ('__' not in i) or ('impression' in i):
    if len(i) < 4 and 'dr' in i:
      continue
    new_sentence.append(i)
    current_length += len(i)
  if current_length > 512:
    break
# row[1] = '.'.join(new_sentence)
# row[1] = row[1].split('impression:')[0]
if new_sentence != []:
  line = '.'.join(new_sentence)
  if line[-1] != '.':
    line = line + '.'
  line = line.strip()

