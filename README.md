# AutoHall: Automated Hallucination Dataset Generation for Large Language Models
该仓库开源了论文"AutoHall: Automated Hallucination Dataset Generation for Large Language Models"中的代码和收集到的数据。<br>
This repository provides the source code and collected data from paper "AutoHall: Automated Hallucination Dataset Generation for Large Language Models".<br>
https://arxiv.org/abs/2310.00259

## 引用 Citation
```
@article{cao2023autohall,
  title={Autohall: Automated hallucination dataset generation for large language models},
  author={Cao, Zouying and Yang, Yifei and Zhao, Hai},
  journal={arXiv preprint arXiv:2310.00259},
  year={2023}
}
```


## 代码 Code
**1. code/ChatGPT dir: code for collecting hallucination generated by ChatGPT**<br>
```
-- api_request_parallel_processor.py: API file for calling gpt-3.5-trubo
-- Climate_hallucination.ipynb: analyse hallucination generated based on Climate-fever dataset
-- Pubhealth_hallucination.ipynb: analyse hallucination generated based on Pubhealth dataset
-- WICE_hallucination.ipynb: analyse hallucination generated based on WICE dataset
```

**2. code/Llama2-Chat dir: code for collecting hallucination generated by Llama2-Chat series**<br>
```
-- main.py: main file for using Llama2-Chat series
-- llama_hallucination.ipynb: analyse hallucination generated by Llama2-7B-Chat
-- llama2_hallucination.ipynb: analyse hallucination generated based by Llama2-13B-Chat
```

**3. code/analyse.py: some codes for testing**<br>

**4. code/baselines.ipynb: analyse the baseline models' experimental results**<br>

**5. code/cal_result.py: analyse the proportion of hallucination**<br>

**6. code/content_analysis.py: analyse the content/topic of hallucination**<br>

**7. code/dataset_construct.py: for hallucination detection dataset creation**<br>

**8. code/multi_ref_construct.py: for multiple sampled references collection**<br>

## 收集到的数据 - Datasets
**1. dataset/fact-checking datasets dir: existing fact-checking datasets used for reference generation in AutoHall***
**2. other dirs in dataset/ dir: collected hallucination datasets**

## 论文总结 - Summary of this paper
### Automated Hallucination Dataset Generation Pipeline
![datasets](https://github.com/user-attachments/assets/525be22c-a395-424f-8f86-653aad5c996c)

### Hallucination Detection Method
![detection](https://github.com/user-attachments/assets/bb0d6a7a-9c2d-4d70-a369-ab5f6df6c5ad)


