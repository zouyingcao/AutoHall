"""
owner:
data: 2023-07-27
description:
"""
import json


num=183
x=0
y=[]
with open('detections_17.jsonl') as file:
    for line in file:
        data = json.loads(line)
        answer = data[1]['choices'][0]['message']['content']
        question = data[0]['messages'][0]['content']
        p1 = question.split('P1: ')[1].split('P2: ')[0]
        if "here are no conflicting parts" in answer:
            x+=1
        else:
            y.append(p1)
print(x,num,(num-x)/num)

from typing import Optional

import fire
import json
from llama import Llama


def main(
        dataset_filepath: str,
        save_filepath: str,
        ckpt_dir: str,
        tokenizer_path: str,
        temperature: float = 0.9,
        top_p: float = 0.9,
        max_seq_len: int = 512,
        max_batch_size: int = 4,
        max_gen_len: Optional[int] = None,
):
    generator = Llama.build(
        ckpt_dir=ckpt_dir,
        tokenizer_path=tokenizer_path,
        max_seq_len=max_seq_len,
        max_batch_size=max_batch_size,
    )
    i = 0
    with open(save_filepath, 'w') as outfile:
        with open(dataset_filepath) as file:
            for line in file:
                # data = json.loads(line)
                claim = line.split("\"\"> Assistant: ")[0].split("Claim: ")[1]
                reference = line.split("\"\"> Assistant: ")[-1][0:-1]
                dialogs = [
                    [
                        {"role": "system", "content": "Always answer true or false."},
                        {"role": "user", "content": "Given the claim and the reference, " +
                                                    "you should answer whether the claim is true or false. Claim: " + claim + " Reference: " + reference},
                    ],
                ]
                results = generator.chat_completion(
                    dialogs,  # type: ignores
                    max_gen_len=max_gen_len,
                    temperature=temperature,
                    top_p=top_p,
                )

            for dialog, result in zip(dialogs, results):
                for msg in dialog:
                    print(f"{msg['role'].capitalize()}: {msg['content']}\n")
                    question = "{}: {}".format(msg['role'].capitalize(), msg['content'])
                    outfile.write(json.dumps(question))
                print(f"> {result['generation']['role'].capitalize()}: {result['generation']['content']}")
                answer = "> {}: {}".format(result['generation']['role'].capitalize(), result['generation']['content'])
                outfile.write(json.dumps(answer) + "\n")
                print("\n==================================\n")


if __name__ == "__main__":
    fire.Fire(main)
