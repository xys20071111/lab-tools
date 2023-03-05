from tqdm import tqdm
import whisper
import opencc
import os,sys,argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser(prog='whisper-transcribe', description='Transcribe text by OpenAI Whisper')
    parser.add_argument('--audio_dir')
    parser.add_argument('--out_dir')
    args = parser.parse_args()

    path = args.audio_dir
    file_list = os.listdir(path)

    model = whisper.load_model('medium')
    options = whisper.DecodingOptions()
    cc = opencc.OpenCC('t2s')

    for item in tqdm(file_list):
        if(item.endswith('wav')):
            audio = whisper.load_audio(f'{path}/{item}')
            audio = whisper.pad_or_trim(audio)
            mel = whisper.log_mel_spectrogram(audio).to(model.device)
            _, probs = model.detect_language(mel)
            if max(probs, key=probs.get) == 'zh':
                result = whisper.decode(model, mel, options)
                result_text = result.text.replace(' ', '').replace('?', '').replace(',', '').replace("!", '').replace('。', '').replace('《', '').replace('》', '')
                with open(f"{args.out_dir}/{item.replace('wav', 'txt')}", mode='w', encoding='utf8') as f:
                    print(cc.convert(result_text), file=f)
