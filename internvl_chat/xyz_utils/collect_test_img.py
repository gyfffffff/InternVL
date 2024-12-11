# {"id": 16, "image": "/nas/shared/ADLab_Oasim/gaoyufei/xyz_v2_data/hu/image_pure/d30d6d3ef080d73760aaad053a48447774fd6eff7a9ad13fd7d17d359e4f2d20", "width": 426, "height": 640, "conversations": [{"from": "human", "value": "<image>\nÖn az előadó, kérlek, magyarázza el ezt a képet a nézőknek", "prompt_sample_id": 14}, {"from": "gpt", "value": "A képen egy férfi látható, aki egy megbeszélésen vagy megbeszélésen ül. Hivatalos öltönyt visel, és koncentráltnak és komolynak tűnik. Haja rövidre van vágva, világosabb arcbőre van, szemei pedig komoly arckifejezéssel egyenesen előre néznek. A háttérben több más résztvevő is látható, de arcuk nincs teljesen a képben, így részletes leírás nem adható. A háttér elmosódott, de feltételezhető, hogy egy beltéri környezetről van szó, valószínűleg egy konferenciateremről vagy irodáról. A képből formális és komoly hangulatot érzékelhetünk, valószínűleg egy fontos megbeszélés vagy értekezlet zajlik. A férfi testtartása és arckifejezése koncentrációt és komolyságot sugall, ami azt jelentheti, hogy egy fontos párbeszédben vagy döntéshozatali folyamatban vesz részt. A kulturális jellemzők részletes leírása nem lehetséges, mivel a képek nem nyújtanak elegendő információt az adott kulturális környezet vagy ország azonosításához. A képeken látható érzelmi légkör komoly és professzionális, ami sok hivatalos megbeszélés vagy megbeszélés helyszínének felel meg. A képek fényhatásai és színtextúrái viszonylag egyszerűek, nincsenek különösebben kiemelkedő művészi stílusú vagy kézműves elemek. Összességében a kép formális és professzionális hangulatot közvetít."}]}

import os
import json

question = {
    "en": "Describe this picture.",
    "hu": "Írd le ezt a képet.",
    "ar": "وصف هذه الصورة.",
    "vi": "Hãy mô tả bức tranh này.",
    "ko": "이 그림을 설명하세요.",
    "sr": "Опишите ову слику.",
    "cs": "Popište tento obrázek.",
    "th": "อธิบายภาพนี้",
    "ru": "Опишите эту картину."

}

if __name__ == "__main__":
    language = "hu"
    training_data_path = f"xyz_data/{language}/{language}_caption_90k.jsonl"
    all_img_path = f"/nas/shared/ADLab_Oasim/gaoyufei/xyz_v2_data/{language}/image_pure" 
    ouput_jsonl_path = f"data/SLVQA/{language.upper()}/NLG/caption_test.jsonl"
    trans_file = f"xyz_data/{language}/trans_{language}.json"

    with open(training_data_path, "r") as f:
        data_l = f.readlines()
        data = []
        for d in data_l:  
            try:
                data.append(json.loads(d))
            except:
                print(30, d)
        trained_img_set = set([d["image"].split('/')[-1] for d in data])

    img_we_have = set(os.listdir(all_img_path))

    caption_dict = {}
    with open(trans_file, "r") as f:
        trans_data = json.load(f)
    for td in trans_data:
        if td["img_id"] not in trained_img_set and td["img_id"] in img_we_have:
            caption_dict[td["img_id"]] = td["caption"]    

    print(40, len(caption_dict.keys()))
    # import pdb; pdb.set_trace()

    with open(ouput_jsonl_path, "w") as f:
        # {"id": 5, "image": "data/SLVQA/AR/images/5.jpg", "question_eng": "Describe this picture in Arabic, about 10 words.", "answer_eng": "Argentina was defeated and Messi was very frustrated.", "question": "وصف هذه الصورة باللغة العربية، حوالي 10 كلمة.", "answer": "لقد هُزمت الأرجنتين وكان ميسي محبطًا للغاية."}
        for i, img in enumerate(caption_dict.keys()):
            img_path = f"/nas/shared/ADLab_Oasim/gaoyufei/InternVL/internvl_chat/data/SLVQA/{language.upper()}/images/{i}.jpg"
            os.system(f"cp {all_img_path}/{img} {img_path}")
            data = {"id":i, 
                    "image": img_path, 
                    "question": question[language],
                    "answer": caption_dict[img]}
            f.write(json.dumps(data, ensure_ascii=False) + "\n")
            if i == 150:
                break
            