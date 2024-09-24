# Copyright (c) Meta Platforms, Inc. and affiliates.
# This software may be used and distributed according to the terms of the Llama 2 Community License Agreement.

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
    i=0
    p2 = None
    with open(save_filepath,'a') as outfile:
        with open(dataset_filepath) as file:
            for line in file:
                # step1: hallu_data
                #data = json.loads(line)
                #claim = data['claim']
                #dialogs = [
                #    [
                #        {"role": "system", "content": "Always answer one reference with complete sentence."},
                #        {"role": "user", "content": "Given one claim whose authenticity is unknown, "+
                #        "you should provide one reference about it and summarize the reference in a paragraph. Claim: "+claim},
                #    ],
                #]
                
                # step2: cls
                #claim = line.split("\"\"> Assistant: ")[0].split("Claim: ")[1]
                #reference = line.split("\"\"> Assistant: ")[-1][0:-1]  
                #dialogs = [
                #                  [
                #                      {"role": "system", "content": "Always answer true or false."},
                #                      {"role": "user", "content": "Given the claim and the reference, "+
                #                     "you should answer whether the claim is true or false. Claim: "+claim+" Reference: "+reference},
                #                 ],
                #]
                
                # step3: multi-reference
                #claim = line.split(" Reference: ")[0].split("Claim: ")[1]
                #dialogs = [
                #       [
                #             {"role": "system", "content": "Always answer one reference with complete sentence."},
                #             {"role": "user", "content": "Given one claim whose truthfulness is uncertain, you should provide one reference about it. This reference should be summarized as one paragraph. Claim: "+claim},
                #       ],
                #]
                
                # step4: detection
                p1 = p2
                p2 = line
                print(p2)
                i+=1
                if i%2==0:
                    dialogs = [
                       [
                             {"role": "user", "content": "Are there any conflicting parts in these paragraphs P1,P2? "+
                            "P1: "+p1+" P2: "+p2},
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
                                question="{}: {}".format(msg['role'].capitalize(),msg['content'])
                                outfile.write(json.dumps(question))
                            print(f"> {result['generation']['role'].capitalize()}: {result['generation']['content']}")
                            answer="> {}: {}".format(result['generation']['role'].capitalize(),result['generation']['content'])
                            outfile.write(json.dumps(answer)+"\n")
                            print("\n==================================\n")


if __name__ == "__main__":
    fire.Fire(main)