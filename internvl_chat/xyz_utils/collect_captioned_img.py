import json

if __name__ == "__main__":
    lan="ru"
    caption_json = f"/nas/shared/ADLab_Oasim/gaoyufei/InternVL/internvl_chat/xyz_data/{lan}/trans_{lan}.json"
    outfile = f"/nas/shared/ADLab_Oasim/gaoyufei/InternVL/internvl_chat/xyz_data/{lan}/captioned_img.txt"

    with open(caption_json, "r") as f:
        captions = json.load(f)

    with open(outfile, "a") as f:
        for item in captions:
            f.write(f"{item.get('img_id')}\n")