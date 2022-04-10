def NLP_main(user_input):
       import numpy as np
       import nltk
       from nltk.stem.porter import PorterStemmer
       stemmer = PorterStemmer()

       def tokenize(sentence):
              return nltk.word_tokenize(
                     sentence.lower())  # the sentence would be tokenized and converted into lower case

       # def stem(word):
       #   return stemmer.stem(word.lower())

       def bag_of_words(tokenized_sentence, words):
              # stem each word
              sentence_words = [tokenize(sentence) for sentence in tokenized_sentence]
              # initialize bag with 0 for each word
              bag = np.zeros(len(words), dtype=np.float32)
              for idx, w in enumerate(words):
                     if w in sentence_words:
                            bag[idx] = 1

              return bag

              #   return bag of words array:
              #   example:
              #   sentence = ["hello", "how", "are", "you"]
              #   words = ["hi", "hello", "I", "you", "bye", "thank", "cool"]
              #   bog   = [  0 ,    1 ,    0 ,   1 ,    0 ,    0 ,      0]

              # tokenization
              #   a="How much Wheat was produced in Maharashtra in 2019?"
              #   print(a)
              #   a=tokenize(a)
              #   print(a)

       district = ['24 paraganas north', '24 paraganas south', 'adilabad',
                   'agar malwa', 'agra', 'ahmadabad', 'ahmednagar', 'aizawl', 'ajmer',
                   'akola', 'alappuzha', 'aligarh', 'alirajpur', 'allahabad',
                   'almora', 'alwar', 'ambala', 'ambedkar nagar', 'amethi',
                   'amravati', 'amreli', 'amritsar', 'amroha', 'anand', 'anantapur',
                   'anantnag', 'anjaw', 'anugul', 'anuppur', 'araria', 'ariyalur',
                   'arwal', 'ashoknagar', 'auraiya', 'aurangabad', 'azamgarh',
                   'badgam', 'bagalkot', 'bageshwar', 'baghpat', 'bahraich', 'baksa',
                   'balaghat', 'balangir', 'baleshwar', 'ballia', 'balod',
                   'baloda bazar', 'balrampur', 'banas kantha', 'banda', 'bandipora',
                   'bangalore rural', 'banka', 'bankura', 'banswara', 'barabanki',
                   'baramulla', 'baran', 'bardhaman', 'bareilly', 'bargarh', 'barmer',
                   'barnala', 'barpeta', 'barwani', 'bastar', 'basti', 'bathinda',
                   'beed', 'begusarai', 'belgaum', 'bellary', 'bemetara',
                   'bengaluru urban', 'betul', 'bhadrak', 'bhagalpur', 'bhandara',
                   'bharatpur', 'bharuch', 'bhavnagar', 'bhilwara', 'bhind',
                   'bhiwani', 'bhojpur', 'bhopal', 'bidar', 'bijapur', 'bijnor',
                   'bikaner', 'bilaspur', 'birbhum', 'bishnupur', 'bokaro',
                   'bongaigaon', 'boudh', 'budaun', 'bulandshahr', 'buldhana',
                   'bundi', 'burhanpur', 'buxar', 'cachar', 'chamarajanagar',
                   'chamba', 'chamoli', 'champawat', 'champhai', 'chandauli',
                   'chandel', 'chandigarh', 'chandrapur', 'changlang', 'chatra',
                   'chhatarpur', 'chhindwara', 'chikballapur', 'chikmagalur',
                   'chirang', 'chitradurga', 'chitrakoot', 'chittoor', 'chittorgarh',
                   'churachandpur', 'churu', 'coimbatore', 'coochbehar', 'cuddalore',
                   'cuttack', 'dadra and nagar haveli', 'dakshin kannad', 'damoh',
                   'dang', 'dantewada', 'darbhanga', 'darjeeling', 'darrang', 'datia',
                   'dausa', 'davangere', 'dehradun', 'deogarh', 'deoghar', 'deoria',
                   'dewas', 'dhalai', 'dhamtari', 'dhanbad', 'dhar', 'dharmapuri',
                   'dharwad', 'dhemaji', 'dhenkanal', 'dholpur', 'dhubri', 'dhule',
                   'dibang valley', 'dibrugarh', 'dima hasao', 'dimapur',
                   'dinajpur dakshin', 'dinajpur uttar', 'dindigul', 'dindori',
                   'doda', 'dohad', 'dumka', 'dungarpur', 'durg', 'east district',
                   'east garo hills', 'east godavari', 'east jaintia hills',
                   'east kameng', 'east khasi hills', 'east siang', 'east singhbum',
                   'ernakulam', 'erode', 'etah', 'etawah', 'faizabad', 'faridabad',
                   'faridkot', 'farrukhabad', 'fatehabad', 'fatehgarh sahib',
                   'fatehpur', 'fazilka', 'firozabad', 'firozepur', 'gadag',
                   'gadchiroli', 'gajapati', 'ganderbal', 'gandhinagar', 'ganganagar',
                   'ganjam', 'garhwa', 'gariyaband', 'gautam buddha nagar', 'gaya',
                   'ghaziabad', 'ghazipur', 'giridih', 'goalpara', 'godda',
                   'golaghat', 'gomati', 'gonda', 'gondia', 'gopalganj', 'gorakhpur',
                   'gulbarga', 'gumla', 'guna', 'guntur', 'gurdaspur', 'gurgaon',
                   'gwalior', 'hailakandi', 'hamirpur', 'hanumangarh', 'hapur',
                   'harda', 'hardoi', 'haridwar', 'hassan', 'hathras', 'haveri',
                   'hazaribagh', 'hingoli', 'hisar', 'hooghly', 'hoshangabad',
                   'hoshiarpur', 'howrah', 'hyderabad', 'idukki', 'imphal east',
                   'imphal west', 'indore', 'jabalpur', 'jagatsinghapur', 'jaipur',
                   'jaisalmer', 'jajapur', 'jalandhar', 'jalaun', 'jalgaon', 'jalna',
                   'jalore', 'jalpaiguri', 'jammu', 'jamnagar', 'jamtara', 'jamui',
                   'janjgir-champa', 'jashpur', 'jaunpur', 'jehanabad', 'jhabua',
                   'jhajjar', 'jhalawar', 'jhansi', 'jharsuguda', 'jhunjhunu', 'jind',
                   'jodhpur', 'jorhat', 'junagadh', 'kabirdham', 'kachchh', 'kadapa',
                   'kaimur (bhabua)', 'kaithal', 'kalahandi', 'kamrup',
                   'kamrup metro', 'kanchipuram', 'kandhamal', 'kangra', 'kanker',
                   'kannauj', 'kanniyakumari', 'kannur', 'kanpur dehat',
                   'kanpur nagar', 'kapurthala', 'karaikal', 'karauli',
                   'karbi anglong', 'kargil', 'karimganj', 'karimnagar', 'karnal',
                   'karur', 'kasaragod', 'kasganj', 'kathua', 'katihar', 'katni',
                   'kaushambi', 'kendrapara', 'kendujhar', 'khagaria', 'khammam',
                   'khandwa', 'khargone', 'kheda', 'kheri', 'khordha', 'khowai',
                   'khunti', 'kinnaur', 'kiphire', 'kishanganj', 'kishtwar', 'kodagu',
                   'koderma', 'kohima', 'kokrajhar', 'kolar', 'kolasib', 'kolhapur',
                   'kollam', 'kondagaon', 'koppal', 'koraput', 'korba', 'korea',
                   'kota', 'kottayam', 'kozhikode', 'krishna', 'krishnagiri',
                   'kulgam', 'kullu', 'kupwara', 'kurnool', 'kurukshetra',
                   'kurung kumey', 'kushi nagar', 'lahul and spiti', 'lakhimpur',
                   'lakhisarai', 'lalitpur', 'latehar', 'latur', 'lawngtlai',
                   'leh ladakh', 'lohardaga', 'lohit', 'longding', 'longleng',
                   'lower dibang valley', 'lower subansiri', 'lucknow', 'ludhiana',
                   'lunglei', 'madhepura', 'madhubani', 'madurai', 'maharajganj',
                   'mahasamund', 'mahbubnagar', 'mahe', 'mahendragarh', 'mahesana',
                   'mahoba', 'mainpuri', 'malappuram', 'maldah', 'malkangiri',
                   'mamit', 'mandi', 'mandla', 'mandsaur', 'mandya', 'mansa',
                   'marigaon', 'mathura', 'mau', 'mayurbhanj', 'medak',
                   'medinipur east', 'medinipur west', 'meerut', 'mewat', 'mirzapur',
                   'moga', 'mokokchung', 'mon', 'moradabad', 'morena', 'muktsar',
                   'mumbai', 'mungeli', 'munger', 'murshidabad', 'muzaffarnagar',
                   'muzaffarpur', 'mysore', 'nabarangpur', 'nadia', 'nagaon',
                   'nagapattinam', 'nagaur', 'nagpur', 'nainital', 'nalanda',
                   'nalbari', 'nalgonda', 'namakkal', 'namsai', 'nanded', 'nandurbar',
                   'narayanpur', 'narmada', 'narsinghpur', 'nashik', 'navsari',
                   'nawada', 'nawanshahr', 'nayagarh', 'neemuch', 'nicobars',
                   'nizamabad', 'north and middle andaman', 'north district',
                   'north garo hills', 'north goa', 'north tripura', 'nuapada',
                   'osmanabad', 'pakur', 'palakkad', 'palamu', 'palghar', 'pali',
                   'palwal', 'panch mahals', 'panchkula', 'panipat', 'panna',
                   'papum pare', 'parbhani', 'pashchim champaran', 'patan',
                   'pathanamthitta', 'pathankot', 'patiala', 'patna', 'pauri garhwal',
                   'perambalur', 'peren', 'phek', 'pilibhit', 'pithoragarh',
                   'pondicherry', 'poonch', 'porbandar', 'prakasam', 'pratapgarh',
                   'pudukkottai', 'pulwama', 'pune', 'purbi champaran', 'puri',
                   'purnia', 'purulia', 'rae bareli', 'raichur', 'raigad', 'raigarh',
                   'raipur', 'raisen', 'rajauri', 'rajgarh', 'rajkot', 'rajnandgaon',
                   'rajsamand', 'ramanagara', 'ramanathapuram', 'ramban', 'ramgarh',
                   'rampur', 'ranchi', 'rangareddi', 'ratlam', 'ratnagiri',
                   'rayagada', 'reasi', 'rewa', 'rewari', 'ri bhoi', 'rohtak',
                   'rohtas', 'rudra prayag', 'rupnagar', 's.a.s nagar',
                   'sabar kantha', 'sagar', 'saharanpur', 'saharsa', 'sahebganj',
                   'saiha', 'salem', 'samastipur', 'samba', 'sambalpur', 'sambhal',
                   'sangli', 'sangrur', 'sant kabeer nagar', 'sant ravidas nagar',
                   'saraikela kharsawan', 'saran', 'satara', 'satna',
                   'sawai madhopur', 'sehore', 'senapati', 'seoni', 'sepahijala',
                   'serchhip', 'shahdol', 'shahjahanpur', 'shajapur', 'shamli',
                   'sheikhpura', 'sheohar', 'sheopur', 'shimla', 'shimoga',
                   'shivpuri', 'shopian', 'shravasti', 'siddharth nagar', 'sidhi',
                   'sikar', 'simdega', 'sindhudurg', 'singrauli', 'sirmaur', 'sirohi',
                   'sirsa', 'sitamarhi', 'sitapur', 'sivaganga', 'sivasagar', 'siwan',
                   'solan', 'solapur', 'sonbhadra', 'sonepur', 'sonipat', 'sonitpur',
                   'south andamans', 'south district', 'south garo hills',
                   'south goa', 'south tripura', 'south west garo hills',
                   'south west khasi hills', 'spsr nellore', 'srikakulam', 'srinagar',
                   'sukma', 'sultanpur', 'sundargarh', 'supaul', 'surajpur', 'surat',
                   'surendranagar', 'surguja', 'tamenglong', 'tapi', 'tarn taran',
                   'tawang', 'tehri garhwal', 'thane', 'thanjavur', 'the nilgiris',
                   'theni', 'thiruvallur', 'thiruvananthapuram', 'thiruvarur',
                   'thoubal', 'thrissur', 'tikamgarh', 'tinsukia', 'tirap',
                   'tiruchirappalli', 'tirunelveli', 'tiruppur', 'tiruvannamalai',
                   'tonk', 'tuensang', 'tumkur', 'tuticorin', 'udaipur', 'udalguri',
                   'udam singh nagar', 'udhampur', 'udupi', 'ujjain', 'ukhrul',
                   'umaria', 'una', 'unakoti', 'unnao', 'upper siang',
                   'upper subansiri', 'uttar kannad', 'uttar kashi', 'vadodara',
                   'vaishali', 'valsad', 'varanasi', 'vellore', 'vidisha',
                   'villupuram', 'virudhunagar', 'visakhapatanam', 'vizianagaram',
                   'warangal', 'wardha', 'washim', 'wayanad', 'west district',
                   'west garo hills', 'west godavari', 'west jaintia hills',
                   'west kameng', 'west khasi hills', 'west siang', 'west singhbhum',
                   'west tripura', 'wokha', 'yadgir', 'yamunanagar', 'yanam',
                   'yavatmal', 'zunheboto']

       state = ['andaman and nicobar islands', 'andhra pradesh',
                'arunachal pradesh', 'assam', 'bihar', 'chandigarh',
                'chhattisgarh', 'dadra and nagar haveli', 'goa', 'gujarat',
                'haryana', 'himachal pradesh', 'jammu and kashmir ', 'jharkhand',
                'karnataka', 'kerala', 'madhya pradesh', 'maharashtra', 'manipur',
                'meghalaya', 'mizoram', 'nagaland', 'odisha', 'puducherry',
                'punjab', 'rajasthan', 'sikkim', 'tamil nadu', 'telangana ',
                'tripura', 'uttar pradesh', 'uttarakhand', 'west bengal']

       subDivision = ['andaman & nicobar islands', 'arunachal pradesh',
                      'assam & meghalaya', 'bihar', 'chhattisgarh',
                      'coastal andhra pradesh', 'coastal karnataka',
                      'east madhya pradesh', 'eastrajasthan', 'east uttar pradesh',
                      'gangetic west bengal', 'gujarat region',
                      'haryana delhi & chandigarh', 'himachal pradesh',
                      'jammu & kashmir', 'jharkhand', 'kerala', 'konkan & goa',
                      'lakshadweep', 'madhya maharashtra', 'marathwada',
                      'naga mani mizo tripura', 'north interior karnataka', 'orissa',
                      'punjab', 'rayalseema', 'saurashtra & kutch',
                      'south interior karnataka', 'sub himalayan west bengal & sikkim',
                      'tamil nadu', 'telangana', 'uttarakhand', 'vidarbha',
                      'west madhya pradesh', 'west rajasthan', 'west uttar pradesh']

       crops = ['apple', 'arcanut (processed)', 'arecanut', 'arhar/tur',
                'ash gourd', 'atcanut (raw)', 'bajra', 'banana', 'barley', 'bean',
                'beans & mutter(vegetable)', 'beet root', 'ber', 'bhindi',
                'bitter gourd', 'black pepper', 'blackgram', 'bottle gourd',
                'brinjal', 'cabbage', 'cardamom', 'carrot', 'cashewnut',
                'cashewnut processed', 'cashewnut raw', 'castor seed',
                'cauliflower', 'citrus fruit', 'coconut ', 'coffee', 'colocosia',
                'cond-spcs other', 'coriander', 'cotton(lint)', 'cowpea(lobia)',
                'cucumber', 'drum stick', 'dry chillies', 'dry ginger', 'garlic',
                'ginger', 'gram', 'grapes', 'groundnut', 'guar seed', 'horse-gram',
                'jack fruit', 'jobster', 'jowar', 'jute', 'jute & mesta', 'kapas',
                'khesari', 'korra', 'lab-lab', 'lemon', 'lentil', 'linseed',
                'litchi', 'maize', 'mango', 'masoor', 'mesta', 'moong(green gram)',
                'moth', 'niger seed', 'oilseeds total', 'onion', 'orange',
                'other  rabi pulses', 'other cereals & millets',
                'other citrus fruit', 'other dry fruit', 'other fibres',
                'other fresh fruits', 'other kharif pulses', 'other misc. pulses',
                'other oilseeds', 'other vegetables', 'paddy', 'papaya', 'peach',
                'pear', 'peas  (vegetable)', 'peas & beans (pulses)', 'perilla',
                'pineapple', 'plums', 'pome fruit', 'pome granet', 'potato',
                'pulses total', 'pump kin', 'ragi', 'rajmash kholar',
                'rapeseed &mustard', 'redish', 'ribed guard', 'rice',
                'ricebean (nagadal)', 'rubber', 'safflower', 'samai', 'sannhamp',
                'sapota', 'sesamum', 'small millets', 'snak guard', 'soyabean',
                'sugarcane', 'sunflower', 'sweet potato', 'tapioca', 'tea',
                'tobacco', 'tomato', 'total foodgrain', 'turmeric', 'turnip',
                'urad', 'varagu', 'water melon', 'wheat', 'yam']

       months = [
           'january','february','march','april','may','june','july','august','september','october'
           ,'november','december','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec'
       ]

       rainfall = [
           'rainfall','rain'
       ]
       cr = [
           'crop','CROP','crops','CuROPS'
       ]

       def intersection_s(sent):  # prints the state from the given input
              for value in sent:
                     if value in state:
                            #print("State : ", value)
                            return value

       def intersection_d(sent):  # prints the district from the given input
              for value in sent:
                     if value in district:
                            # print("District : ", value)
                            return value

       def intersection_sd(sent):  # prints the subdivision from the given input
              for value in sent:
                     if value in subDivision:
                            #print("SubDivision : ", value)
                            return value

       def intersection_crop(sent):  # prints the crops from the given input
              for value in sent:
                     if value in crops:
                            # print("Crop : ", value)
                            return value

       def checkNum(sent):  # prints the Year from the given input
              number = []
              for value in sent:
                     for subitem in value:
                            if (subitem.isdigit()):
                                   number.append(subitem)
                                   join_num = ''.join(number)
                                   if (len(join_num) == 4):
                                          # print("Year : ", join_num)
                                          return join_num

       def intersection_month(sent):
           for value in sent:
               if value in months:
                   # print("Crop : ", value)
                   return value

       def rainfall_word(sent):
           for value in sent:
               if value in rainfall:
                   # print("Crop : ", value)
                   return value

       def crp_word(sent):
           for value in sent:
               if value in cr:
                   # print("Crop : ", value)
                   return value
       # sent= "How much Wheat was produced in Tiruvannamalai and Maharashtra in 2019?"
       # a=tokenize(sent)
       # print(a)
       # print(intersection(a,state,district,subDivision))
       # print(checkNum(a))

       # user_input=str(input("You - "))



              # sentence = "do you use credit cards?"
       #user_input = input("You- ")

       sentence = tokenize(user_input)
       st = intersection_s(sentence)
       ds = intersection_d(sentence)
       subD = intersection_sd(sentence)
       crop = intersection_crop(sentence)
       year = checkNum(sentence)
       month = intersection_month(sentence)
       rainf = rainfall_word(sentence)
       crp = crp_word(sentence)
       return st,ds,subD,crop,year,month,rainf,crp


