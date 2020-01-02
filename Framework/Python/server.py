from nltk.corpus import wordnet as wn
from flask import Flask
from flask import jsonify
from flask import request

import json

app = Flask(__name__)

from nltk.corpus import wordnet as wn
import json


class synset(object):
    def __init__(self, word, definition, pos, lemmas):
        self.word = word
        self.definition = definition
        self.pos = pos
        
        self.lemmas = []
        for i in range(len(lemmas)):
            self.lemmas.append(lemmas[i].name())
    
    def synset_to_dict(self, synset):
        dict_ret = dict(word = synset.word, definition = synset.definition, pos = synset.pos, lemmas = synset.lemmas)

        return dict_ret

    def synset_to_json(self):
        json_string = json.dumps(self, default = self.synset_to_dict)
        return json_string

class synsets(object):
    def __init__(self, synsets_list):
        self.synsets_list = []
        for i in range(len(synsets_list)):
            syn = synset(synsets_list[i].name(), synsets_list[i].definition(), synsets_list[i].pos(), synsets_list[i].lemmas())
            print(syn.lemmas)
            self.synsets_list.append(syn)

    def synsets_to_json(self):
        json_str = "[ "
        
        for i in range(len(self.synsets_list)):
            syn = self.synsets_list[i]
            json_str += syn.synset_to_json()
            if (i < len(self.synsets_list) - 1):
                json_str += ","

        json_str += " ]"
        return json_str

    def synsets_to_json_short(self):
        json_str = "[ "
        
        for i in range(len(self.synsets_list)):
            syn = self.synsets_list[i]
            json_str += syn.word
            if (i < len(self.synsets_list) - 1):
                json_str += ","

        json_str += " ]"
        return json_str


@app.route('/wordnet/<word>',methods=['GET'])
def getSynset(word):
    result = wn.synsets(word, pos='n')
    resultObj = synsets(result)
    json_str = resultObj.synsets_to_json()
    return json_str

#-1 - left is hypernym (parent)
#1 - rigth is hypernym
#0 - lack of relation
@app.route('/wordnet/<left>,<right>',methods=['GET'])
def isHypernym(left, right):
    res_list = wn.synset(left).lowest_common_hypernyms(wn.synset(right))
    for member in res_list:
        if member.name() == left:
            return "-1"
        elif member.name() == right:
            return "1"
        else:
            return "0"

@app.route('/wordnet/path/<word>,<entity>',methods=['GET'])
def getPath(word, entity):
    w1 = wn.synset(word)
    w2 = wn.synset(entity)

    paths = w1.hypernym_paths()
    reduced = []
    for l in paths:
        mappedList = list(map(lambda syn: syn.name(), l))
        if entity in mappedList:
            reduced.append(mappedList)

    res = min(reduced, key=len)

    res2 = subPath(res, word, entity)
    my_json_string = json.dumps(res2)
    return my_json_string

def subPath(l, word, entity):
    skip = 1
    res = []
    for e in l:
        if (skip==0):
             res.append(e)
        else:
            if (e == entity):
                skip = 0
                res.append(e)
    return res

@app.route('/wordnet/path/<word>',methods=['GET'])
def getPathShort(word):
    return getPath(word, 'entity.n.01')


@app.route('/wordnet/children/<word>',methods=['GET'])
def getChildren(word):
    w1 = wn.synset(word)
    result = w1.hyponyms()
    resultObj = synsets(result)
    json_str = resultObj.synsets_to_json_short()
    print(json_str) 
    return json_str

if __name__ == "__main__":
    app.run()
    
