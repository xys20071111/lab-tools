from pypinyin import lazy_pinyin
from tqdm import tqdm
import argparse
import shutil
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser('text2lab', description='Convert txt file to lab')
    parser.add_argument('--txt_dir')
    parser.add_argument('--audio_dir')
    parser.add_argument('--output')

    args = parser.parse_args()

    txt_files_list = os.listdir(args.txt_dir)
    for item in tqdm(txt_files_list):
        if not item.endswith('.txt'):
            continue
        with open(f'{args.txt_dir}/{item}', mode='r', encoding='utf8') as input:
            pinyin_string = ' '.join(lazy_pinyin(input.readline()))
            with open(f'{args.output}/{item.replace(".txt", ".lab")}', mode='w', encoding='utf8') as f:
                f.write(pinyin_string)
            shutil.copyfile(f'{args.audio_dir}/{item.replace(".txt", ".wav")}', f'{args.output}/{item.replace(".txt", ".wav")}')
